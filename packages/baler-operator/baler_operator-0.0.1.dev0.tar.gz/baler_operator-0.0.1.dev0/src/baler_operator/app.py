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
import sys

import kopf

import baler_operator.errors.core as errors
from baler_operator.config.core import (
    __OPERATOR_API_PIPELINE__,
    __OPERATOR_API_VERSION__,
    __OPERATOR_KIND_HAYSTACK_SINGULAR__,
)
from baler_operator.documentstore.core import (
    comission_haystack_datasource,
    decomission_haystack_datasource,
)
from baler_operator.kube.core import manage_kubernetes_object
from baler_operator.pipelines.core import (
    comission_haystack_pipeline,
    decomission_haystack_pipeline,
)
from baler_operator.utils.core import kubernetes_object_lookup

# Basic logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def is_not_running(body, spec, status, **_) -> bool:
    # Stop polling if the pipeline is in error or running state
    if (
        status.get("phase", "NotRunning") == "Error"
        or status.get("phase", "NotRunning") == "Running"
    ):
        return False
    return True


@kopf.on.timer(
    __OPERATOR_API_PIPELINE__,
    __OPERATOR_API_VERSION__,
    __OPERATOR_KIND_HAYSTACK_SINGULAR__,
    interval=5,
    when=is_not_running,
)
def poll_pipeline_stasus(spec, status, patch, meta, body, namespace, **kwargs):
    """
    This function is called periodically to poll the status of the Haystack pipeline's underlying Kubernetes objects
    it checks the status of these objects and updates the status of the Haystack pipeline CRD accordingly.

    :param spec: The spec of the Haystack pipeline CRD
    :param patch: The patch of the Haystack pipeline CRD
    :param meta: The metadata of the Haystack pipeline CR
    :param body: The body of the Haystack pipeline CRD
    :param namespace: The namespace of the Haystack pipeline CRD
    :param kwargs: Additional keyword arguments

    For more details, see `see this GitHub issue <https://github.com/nolar/kopf/issues/514>`
    For documentation, see `documentation <https://github.com/nolar/kopf/blob/main/docs/configuration.rst>`
    """

    # If any of the handlers set error ignore
    # This should be added to the termination condition of the timer
    try:
        if status["handler"] == "Error":
            patch.status["phase"] = "Error"
            return
    except KeyError:
        patch.status["phase"] = "Pending"
        return

    states = []
    for kind, config in kubernetes_object_lookup.items():
        label_selector = f"pipelines.baler.gatecastle.com/owned-by={meta['name']}"
        objects = manage_kubernetes_object(
            "list",
            kind,
            body=body,
            namespace=namespace,
            label_selector=label_selector,
            **kwargs,
        )
        for obj in objects.items:
            logger.info(
                f"Polling {kind} {obj.metadata.name} for pipeline {meta['name']} in namespace {meta['namespace']}"
            )
            healtz = config["healthz"](obj)
            states.append(healtz)

    if len(states) == 0:
        patch.status["phase"] = "Failed"
    elif all(states):
        patch.status["phase"] = "Running"
    else:
        patch.status["phase"] = "Pending"


@kopf.on.delete(
    __OPERATOR_API_PIPELINE__,
    __OPERATOR_API_VERSION__,
    __OPERATOR_KIND_HAYSTACK_SINGULAR__,
)
def delete_pipeline_haystack(body, spec, patch, name, namespace, meta, **kwargs):
    """
    This function is called when a Haystack pipeline CRD is deleted

    :param spec: The spec of the Haystack pipeline CRD
    :param name: The name of the Haystack pipeline CRD
    :param namespace: The namespace of the Haystack pipeline CRD
    :param meta: The metadata of the Haystack pipeline CRD
    :param kwargs: Additional keyword arguments

    For more details, see `documentation <https://kopf.readthedocs.io/en/stable/events/>`
    """

    patch.status["handler"] = "Pending"

    try:

        spec_pipelines = spec.get("pipelines", [])
        for subpipeline in spec_pipelines:
            decomission_haystack_pipeline(
                name, spec, subpipeline["name"], namespace, meta, **kwargs
            )

        decomission_haystack_datasource(name, spec, name, namespace, meta, **kwargs)

    except (errors.ProviderFailure, errors.UserFailure, errors.OperatorFailure) as e:
        patch.status["handler"] = "Error"
        msg = f"Error deleting Haystack pipeline: {name} in namespace {namespace}. {e}"
        raise kopf.PermanentError(msg) from e


@kopf.on.create(
    __OPERATOR_API_PIPELINE__,
    __OPERATOR_API_VERSION__,
    __OPERATOR_KIND_HAYSTACK_SINGULAR__,
)
def create_pipeline_haystack(body, spec, patch, name, namespace, meta, **kwargs):
    """
    This function is called when a new Haystack pipeline CRD is created

    :param spec: The spec of the Haystack pipeline CRD
    :param name: The name of the Haystack pipeline CRD
    :param namespace: The namespace of the Haystack pipeline CRD
    :param meta: The metadata of the Haystack pipeline CRD
    :param kwargs: Additional keyword arguments

    For more details, see `documentation <https://kopf.readthedocs.io/en/stable/events/>`
    """

    patch.status["handler"] = "Pending"

    try:

        spec_pipelines = spec.get("pipelines", [])
        for subpipeline in spec_pipelines:
            comission_haystack_pipeline(
                name, spec, subpipeline["name"], namespace, meta, **kwargs
            )

        comission_haystack_datasource(name, spec, name, namespace, meta, **kwargs)
    except (errors.ProviderFailure, errors.UserFailure, errors.OperatorFailure) as e:
        patch.status["handler"] = "Error"
        msg = f"Error creating Haystack pipeline: {name} in namespace {namespace}. {e}"
        raise kopf.PermanentError(msg) from e


@kopf.on.update(
    __OPERATOR_API_PIPELINE__,
    __OPERATOR_API_VERSION__,
    __OPERATOR_KIND_HAYSTACK_SINGULAR__,
)
def update_pipeline_haystack(body, spec, name, patch, namespace, meta, **kwargs):
    """
    This function is called when a Haystack pipeline CRD is updated

    :param spec: The spec of the Haystack pipeline CRD
    :param name: The name of the Haystack pipeline CRD
    :param namespace: The namespace of the Haystack pipeline CRD
    :param meta: The metadata of the Haystack pipeline CRD
    :param kwargs: Additional keyword arguments

    For more details, see `documentation <https://kopf.readthedocs.io/en/stable/events/>`
    """

    patch.status["handler"] = "Pending"

    try:
        spec_pipelines = spec.get("pipelines", [])
        for subpipeline in spec_pipelines:

            # Simply decomission and recomission the subpipeline
            # Note that the documentstore is not recomissioned here, there is no point
            decomission_haystack_pipeline(
                name, spec, subpipeline["name"], namespace, meta, **kwargs
            )
            comission_haystack_pipeline(
                name, spec, subpipeline["name"], namespace, meta, **kwargs
            )
    except (errors.ProviderFailure, errors.UserFailure, errors.OperatorFailure) as e:
        patch.status["handler"] = "Error"
        msg = f"Error updating Haystack pipeline: {name} in namespace {namespace}. {e}"
        raise kopf.PermanentError(msg) from e


# Place any cleanup tasks here in the future
# Right now we don't have any cleanup tasks
@kopf.on.cleanup()
async def cleanup(logger, **kwargs):
    """This function is called when the operator is shutting down
    :param logger: The logger of the operator
    :param kwargs: Additional keyword arguments

    For more details, see `documentation <https://kopf.readthedocs.io/en/stable/shutdown/>`
    """
    pass


# Place any startup configuration tasks here in the future
# Right now we don't have any startup configuration tasks
@kopf.on.startup()
def configure(settings: kopf.OperatorSettings, **_):
    """
    This function is called when the operator starts up

    :param settings: The settings of the operator
    :param _: Additional keyword arguments

    For more details, see `documentation <https://kopf.readthedocs.io/en/stable/configuration/>`
    """
    pass
