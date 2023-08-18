@echo off

set NETWORK_NAME=my-pycalc-network

docker run -itd  --network %NETWORK_NAME% -p 8888:8888 my-ux-app
