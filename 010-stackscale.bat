@echo off

docker pull shankonduru/autovsselfhealing-ux
docker service scale shankonduru/autovsselfhealing-ux=2 

docker pull shankonduru/autovsselfhealing-db
docker service scale shankonduru/autovsselfhealing-db=2 

docker pull shankonduru/autovsselfhealing-api
docker service scale shankonduru/autovsselfhealing-api=2