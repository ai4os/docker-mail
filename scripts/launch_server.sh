#!/bin/bash
# ------------------------------------------------------------------
# [sftobias] Launch server
#            Launch a docker container with the server part
# ------------------------------------------------------------------

script_dir="$(dirname "$0")"
cd "$script_dir/../server/"

docker kill mail-server
docker remove mail-server
docker build -t mail-server_image .
docker run --name mail-server --env-file vars.env --network mailing_net --ip 192.168.1.3 -p 0.0.0.0:8082:8082 -d mail-server_image:latest
docker container logs mail-server