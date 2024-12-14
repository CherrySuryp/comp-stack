#!/bin/bash

image="cherrysuryp/comp-stack"

echo "Enter the version of the build for $image:"
read -r version

echo "Should this build be tagged as 'latest'? (y/n)"
read -r is_latest


if [ "$is_latest" = "y" ] || [ "$is_latest" = "yes" ]; then
  docker buildx build --platform linux/amd64,linux/arm64 -t "$image":"$version" -t "$image":latest . --push
else
  docker buildx build --platform linux/amd64,linux/arm64 -t "$image":"$version" . --push --no-cache
fi