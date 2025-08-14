#!/bin/bash

# Exit immediately if a command fails
set -e

# Environment variables
IMAGE_NAME="ghcr.io/phylip28/task-manager:main"

echo "Init deployment with Docker Compose"

echo 1. Download the latest image from GitHub Container Registry
docker pull $IMAGE_NAME

echo 2. Update services with new image
docker-compose up -d

echo 3. Remove dangling images
docker image prune -f

echo 4. Deployment completed successfully!