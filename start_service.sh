#!/bin/bash
# Script to start the service
PORT=8000
DOCKER_IMAGE=qa_service_0
CONTAINER_NAME=qa_service_test_0
# CFG_PATH=/home/shreyas/code/siterx-docker-builds/patient_consent_service

# docker command to build and run container
docker build -t $DOCKER_IMAGE ./
docker run --rm -it -p $PORT:8000  --name $CONTAINER_NAME  $DOCKER_IMAGE
# docker run --rm -it -p $PORT:80  -v $CFG_PATH/cfg:/cfg --name $CONTAINER_NAME  $DOCKER_IMAGE