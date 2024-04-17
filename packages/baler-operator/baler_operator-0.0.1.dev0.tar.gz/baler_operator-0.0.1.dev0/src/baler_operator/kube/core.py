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

from kubernetes.client.exceptions import ApiException

import baler_operator.errors.core as errors
from baler_operator.utils.core import (
    exponential_retry,
    lookup_kubernetes_object,
    render_jinja_template_to_yaml,
)

logger = logging.getLogger(__name__)


def manage_kubernetes_object(action, object_type, namespace, body, **kwargs):
    """
    Manage a Kubernetes object (create, update, delete, list)
    see list of supported object types and actions in lookup_kubernetes_object in utils/core.py

    :param action: str: The action to perform on the object (create, update, delete, list)
    :param object_type: str: The type of the Kubernetes object to manage
    :param namespace: str: The namespace in which to manage the object
    :param body: dict: The Kubernetes object manifest
    :param kwargs: dict: Additional keyword arguments to pass to the Kubernetes API method

    :return: dict: The response from the Kubernetes API method

    :raises: ProviderFailure: If the Kubernetes API call fails
    :raises: SystemFailure: If the API client or method cannot be initialized
    """
    # Lookup the Kubernetes object to get the API client and methods
    object_info = lookup_kubernetes_object(object_type)

    # Initialize variables
    api_client_instance = None
    method = None
    response = None

    try:
        # Initialize the appropriate API client
        api_client_instance = object_info["api_client"]()
        # Get the method name for the specified action (create, update, delete)
        method_name = object_info["methods"][action]
        # Get the method itself
        method = getattr(api_client_instance, method_name)
    except Exception as e:
        msg = f"Failed to initialize API client or method for {object_type}: {e}"
        raise errors.SystemFailure(msg) from e

    try:
        # Call the method with exponential backoff
        # Dynamically call the method
        if action == "delete":
            # Deletion might require additional arguments like body=V1DeleteOptions()
            response = exponential_retry(
                method, namespace=namespace, name=body["metadata"]["name"]
            )
        elif action == "list":
            response = exponential_retry(
                method, namespace=namespace, label_selector=kwargs["label_selector"]
            )
        else:
            response = exponential_retry(method, body=body, namespace=namespace)
    except ApiException as e:
        # TODO: implement error code handling from kubernetes.client.exceptions.ApiException
        # Would be more elegant to make it a lookup table grouped by recoverable and non-recoverable errors
        if e.status == 404:
            logger.warning(
                f"Resource {object_type} '{body['metadata']['name']}' not found in namespace '{namespace}'"
            )
        elif e.status == 409:
            logger.warning(
                f"Resource {object_type} '{body['metadata']['name']}' already exists in namespace '{namespace}'"
            )
        elif e.status == 422:
            msg = f"Kubernetes cannot provide the resources requested for {object_type} '{body['metadata']['name']}': {e}"
            raise errors.ProviderFailure(msg) from e
        else:
            # If we get an error code that we don't know how to handle, raise it
            msg = f"Kubernetes API call failed for {object_type} '{body['metadata']['name']}': {e}"
            raise errors.ProviderFailure(msg) from e

    return response


def inject_owner_label(manifest, owner_name):
    """
    Injects the owner label into the manifest

    :param manifest: dict: The Kubernetes object manifest
    :param owner_name: str: The name of the owner

    return: dict: The Kubernetes object manifest with the owner label injected
    """
    if "metadata" not in manifest:
        manifest["metadata"] = {}
    if "labels" not in manifest["metadata"]:
        manifest["metadata"]["labels"] = {}
    manifest["metadata"]["labels"][
        "pipelines.baler.gatecastle.com/owned-by"
    ] = owner_name
    return manifest


def operate_on_resource(
    owner_name, file_path, action, context=None, namespace="default"
):
    """
    Operate on a Kubernetes resource, loading the manifest from a file and performing the specified action

    :param owner_name: str: The name of the owner of the resource, used to inject the owner label (pipelines.baler.gatecastle.com/owned-by)
    :param file_path: str: The path to the file containing the Kubernetes object manifest
    :param action: str: The action to perform on the resource (create, update, delete)
    :param context: dict: The context to render the Jinja template with
    :param namespace: str: The namespace in which to manage the resource

    :raises: ProviderFailure: If the Kubernetes API call fails
    """

    manifests = render_jinja_template_to_yaml(file_path, context)

    for manifest in manifests:

        kind = manifest.get("kind")
        if kind is None:
            msg = f"Kind not found in manifest: {manifest}"
            raise errors.SystemFailure(msg)

        lookup_kubernetes_object(kind)

        target_namespace = manifest.get("metadata", {}).get("namespace", namespace)
        injected_manifest = inject_owner_label(manifest, owner_name)

        try:
            manage_kubernetes_object(action, kind, target_namespace, injected_manifest)
        except errors.ProviderFailure as e:
            logger.error(
                f"Kubernetes API call failed for {kind} '{manifest['metadata']['name']}': {e}"
            )
            raise e
