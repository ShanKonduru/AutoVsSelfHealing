@echo off

set NETWORK_NAME=my-pycalc-network

REM Check if the network exists
docker network inspect %NETWORK_NAME% >nul 2>&1
if %errorlevel% equ 0 (
    echo Removing network %NETWORK_NAME%
    docker network rm --force %NETWORK_NAME%
) else (
    echo Network %NETWORK_NAME% does not exist
)

docker network create %NETWORK_NAME%

docker build -t my-api-app -f Dockerfile.api .
