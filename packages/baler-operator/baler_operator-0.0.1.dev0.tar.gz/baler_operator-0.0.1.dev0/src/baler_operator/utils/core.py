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

import base64
import json
import logging
import os
import time
from pathlib import Path

import jinja2
import kubernetes
import yaml
from jinja2 import Environment, FileSystemLoader
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import baler_operator.errors.core as errors

logger = logging.getLogger(__name__)


def get_current_directory():
    """
    Get the current directory using os and pathlib.

    :return: Tuple of current directory paths using os and pathlib
    """
    # Using os
    current_directory_os = os.path.abspath(os.path.dirname(__file__))

    # Using pathlib
    current_directory_pathlib = (Path(__file__).parent).resolve()

    return current_directory_os, current_directory_pathlib


def get_assets_directory():
    """
    Get the assets directory using os and pathlib.

    :return: Tuple of assets directory paths using os and pathlib
    """
    # Using os
    assets_directory_os = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "../assets/"
    )

    # Using pathlib
    assets_directory_pathlib = (Path(__file__).parent / Path("../assets/")).resolve()

    return assets_directory_os, assets_directory_pathlib


def get_path_in_assets_directory(path):
    """
    Get the path in the assets directory using os and pathlib.

    :param path: Path to the file or directory in the assets directory

    :return: Tuple of paths to the file or directory in the assets directory using os and pathlib
    """
    return get_assets_directory()[1] / Path(path)


def load_schema_from_file(schema_file_path):
    """
    Load JSON schema from a file.

    :param schema_file_path: Path to the schema file

    :return: JSON schema

    :raises SystemFailure: If the file is not found, invalid, or an unknown error occurs
    """

    try:
        with open(schema_file_path) as file:
            schema = json.load(file)
    except FileNotFoundError as e:
        msg = f"Schema file not found: {e}"
        raise errors.SystemFailure(msg) from e
    except json.JSONDecodeError as e:
        msg = f"Invalid schema file: {e}"
        raise errors.SystemFailure(msg) from e
    except Exception as e:
        msg = f"Unknown error: {e}"
        raise errors.SystemFailure(msg) from e

    return schema


def load_supported_versions(filename):
    """
    Load supported versions from a file, stripping 'v' and considering only major.minor.

    :param filename: Path to the file containing supported versions

    :return: List of supported versions in major.minor format, without 'v'

    :raises SystemFailure: If the file is not found or an unknown error occurs
    """

    try:
        with open(filename) as file:
            # Strip 'v', then extract major and minor components
            supported_versions = [
                ".".join(line.strip()[1:].split(".")[:2]) for line in file
            ]
    except FileNotFoundError as e:
        msg = f"Supported versions file not found: {e}"
        raise errors.SystemFailure(msg) from e
    except Exception as e:
        msg = f"Unknown error: {e}"
        raise errors.SystemFailure(msg) from e

    return supported_versions


# Function for checking if the version is supported
# ignoring the patch version
def is_version_supported(version, supported_versions):
    """
    Check if the version is supported based only on major.minor.

    :param version: Version string in the format {major}.{minor} or {major}.{minor}.{patch}
    :param supported_versions: List of version strings in major.minor format, without 'v'

    :return: True if supported, False otherwise

    :raises SystemFailure: If an unknown error occurs
    """
    try:
        major_minor = ".".join(version.split(".")[:2])
    except Exception as e:
        msg = f"Unknown error: {e}"
        raise errors.SystemFailure(msg) from e

    return major_minor in supported_versions


# Write a function that validates the annotations and validates them
# against the annotations schema
# It is important that the annotations are validated before the pipeline
# and no other annotations are validated only the ones that are relevant
# to the pipeline and the pipeline components
def validate_annotations(annotations):
    """
    Validate the annotations against the annotations schema.

    :param annotations: Annotations to validate

    :return: Annotations JSON spec

    :raises UserFailure: If the annotations are invalid
    """

    try:
        schema = load_schema_from_file(
            get_assets_directory()[1] / Path("annotations_schema.json")
        )
        annotations = dict(annotations)
        validate(instance=annotations, schema=schema)
    except ValidationError as e:
        msg = f"Annotations validation failed: {e}"
        raise errors.UserFailure(msg) from e

    # Returning annotations JSON spec
    return annotations


# Write a function that validates the haystack pipeline spec and creates the appropriate
# document store and pipeline components via rendering the appropriate jinja templates
# and calling the appropriate kubernetes API methods.
def validate_haystack_pipeline(spec):
    """
    Validate the haystack pipeline spec against the pipeline schema.

    :param spec: Haystack pipeline spec to validate

    :return: Haystack pipeline JSON spec

    :raises UserFailure: If the pipeline spec is invalid
    """

    # Validate the pipeline spec
    try:
        # This casting is needed so validate function can handle
        # it can only handle python dicts and what is returned
        # from kopf is a special kopf specific structure
        schema = load_schema_from_file(
            get_assets_directory()[1] / Path("pipeline_schema.json")
        )
        spec = dict(spec)
        validate(instance=spec, schema=schema)
    except ValidationError as e:
        msg = f"Pipeline spec validation failed: {e}"
        raise errors.UserFailure(msg) from e

    # Returning haystack pipeline JSON spec
    return spec


def render_jinja_template_to_yaml(file_path, context=None):
    """
    Render a Jinja template to YAML.

    :param file_path: Path to the Jinja template file
    :param context: Context to render the template with

    :return: List of YAML documents

    :raises SystemFailure: If the template is not found, has syntax errors, or an unknown error occurs
    :raises SystemFailure: If the rendered YAML is invalid

    """

    rendered_template = None
    # Assuming the template is in the same directory as the script or provide the correct path
    try:

        template_dir, template_file = os.path.split(file_path)
        env = Environment(
            loader=FileSystemLoader(searchpath=template_dir or "./"), autoescape=True
        )
        env.filters["to_yaml"] = to_yaml
        template = env.get_template(template_file)
        # Render the template with the provided context or an empty context if none provided
        rendered_template = template.render(context or {})
        # Parse the rendered template as YAML
        documents = yaml.safe_load_all(rendered_template)
        manifests = list(documents)  # Convert generator to list for multiple uses
        return manifests

    except jinja2.TemplateNotFound as e:
        msg = f"Jinja template '{template_file}' was not found in directory '{template_dir}'."
        raise errors.SystemFailure(msg) from e
    except jinja2.TemplateSyntaxError as e:
        msg = f"Jinja template syntax error: {e}"
        raise errors.SystemFailure(msg) from e
    except Exception as e:
        msg = f"Unknown error: {e}"
        raise errors.SystemFailure(msg) from e
    except yaml.YAMLError as e:
        msg = f"Error parsing the rendered YAML: {e}"
        raise errors.SystemFailure(msg) from e


# This lookup table holds the valid kinds in Kubernetes
# that are allowed to be managed by the operator
# The `api_client` key holds the API client class for the object
# The `methods` key holds the methods for the object
# The methods are dynamically called based on the action
# The `action` parameter is used to determine which method to call
kubernetes_object_lookup = {
    "Deployment": {
        "api_client": kubernetes.client.AppsV1Api,
        "methods": {
            "create": "create_namespaced_deployment",
            "update": "patch_namespaced_deployment",
            "delete": "delete_namespaced_deployment",
            "list": "list_namespaced_deployment",
            "get": "read_namespaced_deployment",
        },
        "healthz": lambda deployment: (
            deployment.status.ready_replicas >= deployment.spec.replicas
            if deployment.status.ready_replicas is not None
            and deployment.spec.replicas is not None
            else False
        ),
    },
    "Service": {
        "api_client": kubernetes.client.CoreV1Api,
        "methods": {
            "create": "create_namespaced_service",
            "update": "patch_namespaced_service",
            "delete": "delete_namespaced_service",
            "list": "list_namespaced_service",
            "get": "read_namespaced_service",
        },
        "healthz": lambda obj: True,
    },
    "Pod": {
        "api_client": kubernetes.client.CoreV1Api,
        "methods": {
            "create": "create_namespaced_pod",
            "update": "patch_namespaced_pod",
            "delete": "delete_namespaced_pod",
            "list": "list_namespaced_pod",
            "get": "read_namespaced_pod",
        },
        "healthz": lambda obj: True,
    },
    "ConfigMap": {
        "api_client": kubernetes.client.CoreV1Api,
        "methods": {
            "create": "create_namespaced_config_map",
            "update": "patch_namespaced_config_map",
            "delete": "delete_namespaced_config_map",
            "list": "list_namespaced_config_map",
            "get": "read_namespaced_config_map",
        },
        "healthz": lambda obj: True,
    },
    "Secret": {
        "api_client": kubernetes.client.CoreV1Api,
        "methods": {
            "create": "create_namespaced_secret",
            "update": "patch_namespaced_secret",
            "delete": "delete_namespaced_secret",
            "list": "list_namespaced_secret",
            "get": "read_namespaced_secret",
        },
    },
    # Add more Kubernetes objects as needed
}


# Lookup function
# This function is used to lookup the Kubernetes object
# based on the kind of the object
# The kind is the type of the Kubernetes object
# The function returns the API client and methods
# for the specified Kubernetes object
def lookup_kubernetes_object(object_type):
    """
    Lookup the Kubernetes object based on the kind of the object.

    :param object_type: Kind of the Kubernetes object

    :return: API client and methods for the specified Kubernetes object, healthz function to check the health of the object

    :raises SystemFailure: If no entry is found for the Kubernetes object type
    """
    if object_type in kubernetes_object_lookup:
        return kubernetes_object_lookup[object_type]
    else:
        msg = f"No entry found for Kubernetes object type: {object_type}"
        raise errors.SystemFailure(msg)


def exponential_retry(
    func, max_attempts=3, initial_delay=1.0, backoff_factor=2, *args, **kwargs
):
    """
    Attempts to execute the specified function up to max_attempts times,
    waiting an exponentially increasing amount of time between each retry.

    :param func: The function to execute.
    :param max_attempts: The maximum number of attempts to execute the function.
    :param initial_delay: The initial delay between attempts, in seconds.
    :param backoff_factor: The factor by which the delay is exponentially increased.
    :param *args, **kwargs: Arguments and keyword arguments to pass to the function.

    :return: The result of the function if successful, or raises the last exception on failure.

    :raises Exception: If all attempts fail

    """
    attempts = 0
    delay = initial_delay
    while attempts < max_attempts:
        try:
            # Try executing the function with arguments
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, errors.SystemFailure):  # Unrecoverable error
                raise e
            attempts += 1
            if attempts < max_attempts:
                # Wait for an exponentially increasing time
                wait_time = delay * (backoff_factor ** (attempts - 1))
                time.sleep(wait_time)
            else:
                # All attempts failed; re-raise the last exception
                raise


def nodeselector_parse_annotation_string_to_dict(input_string):
    """
    Parse the node selector annotation string into a dictionary.

    :param input_string: Node selector annotation string in the format "key1=value1;key2=value2,..."

    :return: Node selector dictionary
    """
    split_parts = 2

    # Split the string into key-value pairs based on the semicolon
    pairs = input_string.split(";")
    # Initialize an empty dictionary
    result_dict = {}
    # Iterate over each pair
    for pair in pairs:
        if pair:  # Check if the pair is not empty
            # Split the pair into key and value based on the colon
            parts = pair.split(":")
            # Check if the split operation resulted in exactly 2 items
            if len(parts) == split_parts:
                key, value = parts
                # Add the key-value pair to the dictionary
                result_dict[key] = value
            else:
                # Handle the error or log a warning
                msg = "Invalid annotation value list format. Expected 'key1=value1;key2=value2;...'"
                raise errors.UserFailure(msg) from None
    return result_dict


def parse_annotation_string_to_list(input_string):
    """
    Parse the annotation string into a list of strings.

    :param input_string: Annotation string in the format "value1;value2,..."

    :return: List of strings
    """
    # Split the string into values based on the semicolon
    values = input_string.split(";")
    # Filter out empty values
    values = [value for value in values if value]
    return values


def tolerations_parse_annotation_string_to_list(tolerations_str):
    """
    Parse the tolerations annotation string into a list of dictionaries.

    :param tolerations_str: Tolerations annotation string in the format "key:operator

    :return: List of tolerations dictionaries
    """
    split_parts = 4

    tolerations_list = tolerations_str.split(";")
    tolerations_dicts = []
    for tol in tolerations_list:
        parts = tol.split(":")
        if (
            len(parts) == split_parts
        ):  # Ensure we have exactly four parts: key, operator, value, effect
            tolerations_dicts.append(
                {
                    "key": parts[0],
                    "operator": parts[1],
                    "value": parts[2],  # Note: This can be an empty string
                    "effect": parts[3],
                }
            )
        else:
            logger.warning(f"Warning: Skipping invalid toleration format '{tol}'")
    return tolerations_dicts


def to_yaml(obj):
    """
    Convert an object to a YAML string.

    :param obj: Object to convert to YAML

    :return: YAML string
    """
    return yaml.dump(obj, default_flow_style=False)


def resolve_refs_in_kube_in_namespace(filename, namespace):

    with open(filename) as file:
        data = yaml.safe_load(file)

    # Check if `.components` exists and is an array
    if "components" in data and isinstance(data["components"], list):
        for component in data["components"]:
            # Check if the component has a `params` field
            if "params" in component and isinstance(component["params"], dict):
                for key, value in component["params"].items():
                    # Check if the value is a dictionary and contains `valueFrom`
                    if isinstance(value, dict) and "valueFrom" in value:
                        if "secretKeyRef" in value["valueFrom"]:
                            logger.info(
                                f"Component '{component.get('name', 'Unknown')}' has a param '{key}' with 'value from secretKeyRef'."
                            )
                            secret = (
                                kubernetes.client.CoreV1Api().read_namespaced_secret(
                                    value["valueFrom"]["secretKeyRef"]["name"],
                                    namespace,
                                )
                            )
                            secret_data_encoded = secret.data[
                                value["valueFrom"]["secretKeyRef"]["key"]
                            ]
                            secret_data_decoded = base64.b64decode(
                                secret_data_encoded
                            ).decode("utf-8")
                            component["params"][key] = secret_data_decoded
                        if "configMapKeyRef" in value["valueFrom"]:
                            logger.info(
                                f"Component '{component.get('name', 'Unknown')}' has a param '{key}' with 'value from configMapKeyRef'."
                            )
    else:
        error_message = "No `.components` array found or the structure is incorrect."
        raise errors.UserFailure(error_message)

    with open("/mnt/" + filename, "w") as file:
        yaml.dump(data, file)
