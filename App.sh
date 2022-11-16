#!/bin/sh

python3 /home/long/RaspDHT/Programs/FlaskWeb.py &
python3 /home/long/RaspDHT/Programs/SQLALC.py &

(trap 'kill -9 python3' SIGINT)
