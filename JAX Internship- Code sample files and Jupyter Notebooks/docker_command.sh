#!/bin/sh
# start beakerx with this directory mounted in the container as ckb_beakerx
docker run -p 8888:8888 --mount type=bind,source="$PWD",target=/home/beakerx/ckb_beakerx beakerx/beakerx
