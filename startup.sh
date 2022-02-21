#!/bin/sh

path=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

python3 -m venv $path/.venv
. $path/.venv/bin/activate
pip install -r $path/requirements.txt
python3 $path/main.py