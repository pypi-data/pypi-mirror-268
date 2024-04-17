# Copyright 2024 Gergo Nagy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
import os

import yaml

import baler_operator.errors.core as errors
from baler_operator.kube.core import operate_on_resource
from baler_operator.utils.core import (
    get_path_in_assets_directory,
    is_version_supported,
    load_supported_versions,
    nodeselector_parse_annotation_string_to_dict,
    parse_annotation_string_to_list,
    tolerations_parse_annotation_string_to_list,
    validate_annotations,
    validate_haystack_pipeline,
)

logger = logging.getLogger(__name__)


# Function that decomissions the haystack pipeline
def decomission_haystack_pipeline(owner, spec, name, namespace, meta, **kwargs):
    """
    Decomissions a haystack pipeline

    :param owner: The owner of the pipeline, this will be used to put label on the resources
    to prove ownership (pipelines.baler.gatecastle.com/owned-by: <owner>)
    :param spec: The specification of the pipeline
    :param name: The name of the pipeline
    :param namespace: The namespace where the pipeline is running
    :param meta: The metadata of the pipeline
    :param kwargs: Additional arguments that are not used in this function
    """

    configmap_yaml = get_path_in_assets_directory("configmap.yaml")
    service_yaml = get_path_in_assets_directory("service.yaml")
    deployment_yaml = get_path_in_assets_directory("deployment.yaml")

    operate_on_resource(owner, configmap_yaml, "delete", {"name": name}, namespace)
    operate_on_resource(owner, service_yaml, "delete", {"name": name}, namespace)
    operate_on_resource(owner, deployment_yaml, "delete", {"name": name}, namespace)

    logger.info(f"Decomissioning Haystack pipeline: {name} in namespace {namespace}")


# Function that comissions the haystack pipeline
def comission_haystack_pipeline(owner, spec, name, namespace, meta, **kwargs):
    """
    Comissions a haystack pipeline

    :param owner: The owner of the pipeline, this will be used to put label on the resources
    to prove ownership (pipelines.baler.gatecastle.com/owned-by: <owner>)
    :param spec: The specification of the pipeline
    :param name: The name of the pipeline
    :param namespace: The namespace where the pipeline is running
    :param meta: The metadata of the pipeline
    :param kwargs: Additional arguments that are not used in this function

    :raises UserFailure: If the pipeline version is not supported
    """

    # Validate the version of the pipeline and check if it is supported
    supported_versions_file = get_path_in_assets_directory(
        "haystack_supported_versions.txt"
    )
    supported_versions = load_supported_versions(supported_versions_file)

    if not is_version_supported(spec.get("version", "v0.0"), supported_versions):
        msg = f"❌ Haystack pipeline version {spec.get('version', '0.0')} is not supported or missing from pipeline specification. Supported versions: {supported_versions}"
        raise errors.UserFailure(msg)

    # Validate the annotations first that are given by the user
    annotations = validate_annotations(meta.get("annotations", {}))
    # Validate the pipeline spec
    pipeline_json = validate_haystack_pipeline(spec)
    pipeline_yaml = yaml.dump(pipeline_json)

    # Constructing haystack image URL
    # The default compute type is CPU
    # TODO: It would be nicer if this comes from the annotations defaults from the JSON schema
    compute_type = annotations.get("compute.pipelines.baler.gatecastle.com/type", "cpu")
    # TODO: compute.pipeline.baler.gatecastle.com annotations should be validated strictly
    # so for example typos
    compute_cpu = annotations.get(
        "compute.pipelines.baler.gatecastle.com/request-cpu", "500m"
    )
    compute_memory = annotations.get(
        "compute.pipelines.baler.gatecastle.com/request-memory", "1Gi"
    )
    # This is a bit tricky, since GPU's can't be shared on overcommitting here we ask for a request
    # but in reality what we set is a limit, since the GPU is not shared
    # Why we picked request over limit, because it would be more intuitive for the user
    compute_gpu = annotations.get(
        "compute.pipelines.baler.gatecastle.com/request-gpu", "0"
    )
    # Get the compute gpu class that will be used to overwrite the nvidia.com/gpu definition in the limits
    # this is required because in most cases users will use MIG and reference the GPU class in the limit
    compute_gpu_class = annotations.get(
        "compute.pipelines.baler.gatecastle.com/gpu-class", "gpu"
    )
    # Get the node-selector annotation and transform it to a dictionary
    # so it can be embedded in the deployment
    node_selector = annotations.get(
        "compute.pipelines.baler.gatecastle.com/node-selector", ""
    )
    node_selector_dict = nodeselector_parse_annotation_string_to_dict(node_selector)
    # Get tolerations from the annotations and transform it to a list of dictionaries
    tolerations = annotations.get(
        "compute.pipelines.baler.gatecastle.com/tolerations", ""
    )
    tolerations_list = tolerations_parse_annotation_string_to_list(tolerations)
    # Get the image pull secrets from the annotations
    image_pull_secrets = annotations.get(
        "compute.pipelines.baler.gatecastle.com/image-pull-secrets", ""
    )
    image_pull_secrets_list = parse_annotation_string_to_list(image_pull_secrets)
    logger.error(f"Image pull secrets: {image_pull_secrets_list}")
    # Get the service account from the annotations that will be applied to the deployment
    service_account = annotations.get(
        "compute.pipelines.baler.gatecastle.com/service-account", ""
    )

    # If the number of requested GPUs is not 0, then the compute type is GPU
    if compute_gpu != "0" and compute_type == "cpu":
        msg = f"""❌ Haystack pipeline {name} requests 0+ GPU, but the compute type is set/defaults to CPU.
                                 Please set the compute type to GPU explicitly in the annotations: compute.pipelines.baler.gatecastle.com/type: gpu
                                 """
        raise errors.UserFailure(msg)

    haystack_version = spec.get("version", "v1.x")
    # Final haystack image constructed from compute_type and the pipeline version
    haystack_image = f"deepset/haystack:{compute_type}-v{haystack_version}"

    # Create the ConfigMap, Service and Deployment from the assets directory manifest files
    configmap_yaml = get_path_in_assets_directory("configmap.yaml")
    service_yaml = get_path_in_assets_directory("service.yaml")
    deployment_yaml = get_path_in_assets_directory("deployment.yaml")

    configmap_context = {"name": name, "pipeline_definition": pipeline_yaml}
    service_context = {"name": name}
    deployment_context = {
        "name": name,
        "namespace": namespace,
        "haystack_image": haystack_image,
        "owner": owner,
        "cpu": compute_cpu,
        "memory": compute_memory,
        "gpu": compute_gpu if compute_type == "gpu" else None,
        "node_selector": node_selector_dict if node_selector_dict else {},
        "tolerations": tolerations_list if tolerations_list else [],
        "env": spec.get("env", ""),
        "service_account": service_account,
        "init_image": os.getenv("OPERATOR_REPOSITORY", "gatecastle/baler-operator")
        + ":"
        + os.getenv("OPERATOR_TAG", "latest"),
        "image_pull_secrets": image_pull_secrets_list,
        "gpu_class": compute_gpu_class,
    }

    operate_on_resource(owner, configmap_yaml, "create", configmap_context, namespace)
    operate_on_resource(owner, service_yaml, "create", service_context, namespace)
    operate_on_resource(owner, deployment_yaml, "create", deployment_context, namespace)

    logger.info(f"Comissioning Haystack pipeline: {name} in namespace {namespace}")
