#!/usr/bin/env bash
#
# Start the webserver for local applications at port 8080. Intended to be run inside or outside of docker.
# If you do run this in docker, ensure to designate that <host>:<container> port mapping appropriately
# in your docker or docker-comose set up. The project template will have it set to 57xxx:8080 by default.

# shellcheck disable=SC2086
uvicorn --log-level debug --reload --reload-dir src --factory 'src.api.app:create_app' --host 0.0.0.0 --port 8080 $1
