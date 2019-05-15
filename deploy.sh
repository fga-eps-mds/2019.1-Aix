#!/bin/bash
if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
  echo "Logging in to Dockerhub..."
  docker login --username=$DOCKERHUB_ID --password=$DOCKERHUB_PASSWORD
  echo "Pushing images..."
  docker push $DOCKERHUB_ID/$SERVICE_NAME:latest
fi
