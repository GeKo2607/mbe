#!/bin/sh
path=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

chmod +x $path/startup.sh

echo "@lxterminal -e $path/startup.sh" >> /etc/xdg/lxsession/LXDE-pi/autostart

./startup.sh