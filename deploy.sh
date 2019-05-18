#!/bin/bash
if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
  echo "Logging in to Dockerhub..."
  docker login --username=$DOCKERHUB_ID --password=$DOCKERHUB_PASSWORD
  echo "Pushing images..."
  docker push $DOCKERHUB_ID/$SERVICE_NAME:latest
  if [ "$SERVICE_NAME" = "aix-bot" ]; then
    echo "Upgrading aix-bot"
     docker run cdrx/rancher-gitlab-deploy upgrade --rancher-url $RANCHER_URL --rancher-key $RANCHER_ACCESS_KEY --rancher-secret $RANCHER_SECRET_KEY --environment Default --stack bot --service $SERVICE_NAME --finish-upgrade
     docker run cdrx/rancher-gitlab-deploy upgrade --rancher-url $RANCHER_URL --rancher-key $RANCHER_ACCESS_KEY --rancher-secret $RANCHER_SECRET_KEY --environment Default --stack bot --service $SERVICE_NAME"-telegram" --finish-upgrade
  else
    docker run cdrx/rancher-gitlab-deploy upgrade --rancher-url $RANCHER_URL --rancher-key $RANCHER_ACCESS_KEY --rancher-secret $RANCHER_SECRET_KEY --environment Default --stack bot --service $SERVICE_NAME --finish-upgrade
  fi

  echo "Restarting Nginx..."
  curl -u "${RANCHER_ACCESS_KEY}:${RANCHER_SECRET_KEY}" \
    -X POST \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
      "rollingRestartStrategy": {
  		"batchSize": 1,
  		"intervalMillis": 2000
  	  }
    }' "${RANCHER_URL}/v2-beta/${PROJECT_AND_CONTAINER_URI}/?action=restart"
fi
