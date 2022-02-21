#!/bin/sh

path=$PWD

python3 -m venv $path/.venv
. $path/.venv/bin/activate
pip install -r requirements.txt
python3 $path/main.py