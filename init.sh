#!/bin/sh
start_path=$PWD/startup.sh

chmod +x $start_path

echo @lxterminal -e $start_path >> /etc/xdg/lxsession/LXDE-pi/autostart