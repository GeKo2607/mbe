#!/bin/sh
path=$(dirname "$(realpath $0)")

chmod +x $path/startup.sh

echo "@lxterminal -e $path/startup.sh" >> /etc/xdg/lxsession/LXDE-pi/autostart

./startup.sh