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

.PHONY: build docs

# Define variables
VERSION=$(shell grep 'VERSION =' VERSION | sed 's/VERSION = "\(.*\)"/\1/')
CRD_PATH=./crds/*
HELM_CHART_PATH=./charts/baler-operator
NAMESPACE=baler
DOCKER_CONFIG_JSON_PATH=$(HOME)/.docker/config.json
DOCKER_DIR=./docker

# Build the Docker image
docker-build-local:
	VERSION=${VERSION} docker buildx bake -f docker/docker-bake.hcl local


# Push the Docker image
docker-push-local:
	VERSION=${VERSION} docker buildx bake -f docker/docker-bake.hcl --push local

# Build the Docker image
docker-build-release:
	VERSION=${VERSION} docker buildx bake -f docker/docker-bake.hcl release


# Push the Docker image
docker-push-release:
	VERSION=${VERSION} docker buildx bake -f docker/docker-bake.hcl --push release


# Create Docker pull secret for Kubernetes
create-pull-secret:
	kubectl create secret generic dockerhub \
	-n $(NAMESPACE) \
    --from-file=.dockerconfigjson=$(DOCKER_CONFIG_JSON_PATH) \
    --type=kubernetes.io/dockerconfigjson

# Create namespace if it does not exist
create-namespace:
	@kubectl get namespace $(NAMESPACE) || kubectl create namespace $(NAMESPACE)

# Deploy the Operator
deploy-operator:
	helm install baler -n $(NAMESPACE) $(HELM_CHART_PATH)

# Undeploy the Operator
undeploy-operator:
	helm uninstall -n $(NAMESPACE) baler

# Build documentation using sphinx makefile
docs:
	hatch run docs:build

# Coverage report
coverage:
	hatch run cov

# Lint checks
lint:
	hatch run lint:fmt

pip-build:
	hatch build

pip-publish: pip-build
	hatch publish -u __token__ -p $(PYPI_TOKEN)

# Help
help:
	@echo "Makefile commands:"
	@echo "TODO: Add commands here"
