@echo off

REM Push api Image to Docker Hub
docker push vedicmetaverses/my-pycalc-api:latest

REM Push ux Image to Docker Hub
docker push vedicmetaverses/my-pycalc-ux:latest
