#!/bin/sh
start_path=$PWD/startup.sh

chmod +x $start_path

sudo echo $start_path >> /etc/xdg/lxsession/LXDE-pi/autostart