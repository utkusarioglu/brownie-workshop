for c in $(docker -c u-Boulanger container ls -a --format json | jq -r '.Names | select(startswith("brownie"))'); do docker container rm $c; done
for volume in $(docker volume ls --format json | jq -r '.Name | select(startswith("brownie"))'); do docker volume rm $volume; done

# docker compose -f .docker/docker-compose.dev.yml up brownie-workshop-mongodb-community-server
