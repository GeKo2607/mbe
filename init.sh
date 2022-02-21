#!/bin/sh
path=$PWD

chmod +x $path/startup.sh

echo @lxterminal -e cd $path && ./startup.sh >> /etc/xdg/lxsession/LXDE-pi/autostart

./startup.sh