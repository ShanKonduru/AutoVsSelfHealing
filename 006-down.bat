@echo off
REM docker-compose down -v
REM docker image prune --force

docker-compose down -v 

docker image prune --force

echo Removing all Docker images...
for /f %%i in ('docker images -aq') do (
    docker rmi -f %%i
)
echo All Docker images removed.
