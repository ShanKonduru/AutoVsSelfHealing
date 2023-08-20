@echo off

echo pull ux image from docker hub
docker pull shankonduru/autovsselfhealing-ux

echo chnage ux image scale
docker service scale shankonduru/autovsselfhealing-ux=2 

echo pull db image from docker hub
docker pull shankonduru/autovsselfhealing-db

echo chnage db image scale
docker service scale shankonduru/autovsselfhealing-db=2 

echo pull api image from docker hub
docker pull shankonduru/autovsselfhealing-api

echo chnage api image scale
docker service scale shankonduru/autovsselfhealing-api=2
