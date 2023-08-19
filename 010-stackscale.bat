@echo off

REM Push api Image to Docker Hub
docker push vedicmetaverses/my-pycalc-api:latest

REM docker build -t my-pycalc-api:latest .
docker build -t my-pycalc-api:latest ./app/api


REM Push ux Image to Docker Hub
docker push vedicmetaverses/my-pycalc-ux:latest

REM docker build -t my-pycalc-ux:latest .
docker build -t my-pycalc-ux:latest ./app/ux


docker service scale my-pycalc-stack_api=1 my-pycalc-stack_ux=1
