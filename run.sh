#!/bin/bash

# Define your Docker image name
DOCKER_IMAGE="mittalprashant/bhagvad-gita-gpt:latest"

# Check if the Docker image exists
if [[ "$(docker images -q $DOCKER_IMAGE 2> /dev/null)" == "" ]]; then
  echo "Docker image $DOCKER_IMAGE not found locally. Pulling from Docker Hub..."
  
  # Pull the Docker image from Docker Hub
  docker pull $DOCKER_IMAGE || {
    echo "Error: Failed to pull the Docker image from Docker Hub."
    exit 1
  }
fi

# Run the Docker container
docker run -p 5000:5000 --name bhagvad-gita-gpt $DOCKER_IMAGE

echo "Container started successfully. Access it at http://localhost:5000"
