#!/bin/bash
docker run \
    --restart always \
    --publish 2241:22/tcp \
    --publish 8841:80/tcp \
    --name Re_ID_GRPC_Base \
    --detach \
    reid_grpc:v1
