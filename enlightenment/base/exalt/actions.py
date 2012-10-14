#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "exalt"

def setup():
    shelltools.system("./autogen.sh \
                        --disable-static \
                        --prefix=/usr \
                        --with-wpa_supplicant=/sbin/wpa_supplicant \
                        --with-dhcp=/usr/sbin/dhclient")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
