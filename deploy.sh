#!/bin/bash

# Exit immediately if a command fails
set -e

# Environment variables
IMAGE_NAME="ghcr.io/phylip28/task-manager:main"
CONTAINER_NAME="fastapi_container"

echo "Init deployment process of api: $CONTAINER_NAME"

echo 1. Download the latest image from GitHub Container Registry
docker pull $IMAGE_NAME

echo 2. Stop and remove the existing container if it exists
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
  docker stop $CONTAINER_NAME
  docker rm $CONTAINER_NAME
fi

echo 3. Build and run the new container
docker run -d --name $CONTAINER_NAME \
    -p 127.0.0.1:8000:8000 \
    $IMAGE_NAME

echo 4. Remove dangling images
docke image prune -f

echo 5. Deployment completed successfully!