@echo off

set NETWORK_NAME=my-pycalc-network

docker run -itd  --network %NETWORK_NAME% -p 5000:5000 my-api-app
