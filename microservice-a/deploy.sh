#!/bin/sh
set -eux pipefail

BASEDIR=$(dirname "$0")

eval $(minikube docker-env)
docker build $BASEDIR/app --tag microservice-a:1.0.0
helm upgrade --install microservice-a $BASEDIR/chart
