@echo off
REM docker-compose down -v
REM docker image prune --force

docker-compose down -v && docker image prune --force
