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

from baler_operator.kube.core import operate_on_resource
from baler_operator.utils.core import get_path_in_assets_directory, validate_annotations

logger = logging.getLogger(__name__)

# Lookup for DocumentStores
documentstore_object_lookup = {"ElasticsearchDocumentStore": {}}


# A function that is capable of parsing the send CRD spec for they haystack pipeline
# it checks the components sections if there is a match in the type field for
# any of the document_store_lookup keys and it will receive the appropriate
# function.
def identify_documentstore(spec):
    """
    Identify the DocumentStore component in the pipeline spec

    :param spec: The haystack pipeline spec

    :return: The type of the DocumentStore and the function to be used
    """
    for component in spec["components"]:
        if component["type"] in documentstore_object_lookup:
            logger.info(f"Identified DocumentStore: {component['type']}")
            return component["type"], documentstore_object_lookup[component["type"]]
    return None, None


# Function that comissions the documentstore component of the haystack pipeline
def comission_haystack_datasource(owner, spec, name, namespace, meta, **kwargs):
    """
    Comission the DocumentStore component in the pipeline spec

    :param owner: The owner of the DocumentStore used for labelling the
    underlying resources with the owner label (pipelines.baler.gatecastle.com/owned-by: <owner>)
    :param spec: The haystack pipeline spec
    :param name: The name of the haystack pipeline
    :param namespace: The namespace of the haystack pipeline
    :param meta: The metadata of the haystack pipeline
    :param kwargs: Additional arguments
    """

    annotations = meta.get("annotations", {})
    # Validate the initial annotations given by the user
    annotations = validate_annotations(annotations)

    documentstore, value = identify_documentstore(spec)
    if documentstore is None:
        logger.info("No DocumentStore found in the pipeline spec.")
        return

    if (
        annotations.get(
            "auto-provision-documentstore.pipelines.baler.gatecastle.com/enabled", "false"
        )
        == "false"
    ):
        logger.info(
            "Auto-provision documentstore is disabled, skipping comissioning of DocumentStore"
        )
        return

    # Create the DocumentStore
    service_yaml_path = get_path_in_assets_directory(
        f"documentstores/{documentstore}/service.yaml"
    )
    deployment_yaml_path = get_path_in_assets_directory(
        f"documentstores/{documentstore}/deployment.yaml"
    )

    operate_on_resource(owner, service_yaml_path, "create", {"owner": owner}, namespace)
    operate_on_resource(
        owner, deployment_yaml_path, "create", {"owner": owner}, namespace
    )

    logger.info(f"Creating DocumentStore: {documentstore} in namespace {namespace}")


# Function that decomissions the haystack pipeline including
# the documentstore and pipeline components
def decomission_haystack_datasource(owner, spec, name, namespace, meta, **kwargs):
    """
    Decomission the DocumentStore component in the pipeline spec

    :param owner: The owner of the DocumentStore used for labelling the
    underlying resources with the owner label (pipelines.baler.gatecastle.com/owned-by: <owner>)
    :param spec: The haystack pipeline spec
    :param name: The name of the haystack pipeline
    :param namespace: The namespace of the haystack pipeline
    :param meta: The metadata of the haystack pipeline
    :param kwargs: Additional arguments
    """

    annotations = meta.get("annotations", {})
    # Validate the initial annotations given by the user
    annotations = validate_annotations(annotations)

    if (
        annotations.get(
            "preserve-documentstore.pipelines.baler.gatecastle.com/enabled", "false"
        )
        == "true"
    ):
        logger.info(
            "Preserve documentstore is enabled, skipping decomissioning of DocumentStore"
        )
        return

    documentstore, value = identify_documentstore(spec)
    if documentstore is None:
        logger.error("No DocumentStore found in the pipeline spec.")
        return

    # Delete the DocumentStore
    service_yaml_path = get_path_in_assets_directory(
        f"documentstores/{documentstore}/service.yaml"
    )
    deployment_yaml_path = get_path_in_assets_directory(
        f"documentstores/{documentstore}/deployment.yaml"
    )

    operate_on_resource(owner, service_yaml_path, "delete", {}, namespace)
    operate_on_resource(owner, deployment_yaml_path, "delete", {}, namespace)

    logger.info(
        f"Decomissioning DocumentStore: {documentstore} in namespace {namespace}"
    )
