#!/bin/bash
# ------------------------------------------------------------------
# [sftobias] Launch client
#            Launch a docker container with the client part
# ------------------------------------------------------------------
script_dir="$(dirname "$0")"
cd "$script_dir/../client/"

docker kill mail-client
docker remove mail-client
docker build -t mail-client-image .
docker run --name mail-client --env-file vars.env --network mailing_net --ip 192.168.1.2 -d mail-client-image:latest 
docker container logs mail-client