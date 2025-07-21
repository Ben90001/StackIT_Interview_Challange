#!/bin/bash

# Build the Docker image
docker build -t siren .

# Run the Docker container
docker run -d -p 8000:8000 --name siren_container siren

# List running containers
docker ps

# Show logs from the container
docker logs -f siren_container
