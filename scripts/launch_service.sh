#!/bin/bash
# ------------------------------------------------------------------
# [sftobias] Update docker image
#            Automated process for uploading a docker image
# ------------------------------------------------------------------

docker kill mail-service
docker remove mail-service
docker build -t mail-service_image -f Dockerfile_Service .
docker run --name mail-service -p 127.0.0.1:8082:8082 -d mail-service_image:latest
docker container logs mail-service