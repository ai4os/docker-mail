#!/bin/bash
# ------------------------------------------------------------------
# [sftobias] Update docker image
#            Automated process for uploading a docker image
# ------------------------------------------------------------------
ls
docker remove mail-client
docker build -t mail-client-image -f Dockerfile_Client .
docker run --name mail-client -d mail-client-image:latest
docker container logs mail-client