#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
#    shelltools.system('xdt-autogen')
    autotools.configure("--disable-static \
                         --enable-gio-unix \
                         --enable-dbus \
                         --enable-gudev \
                         --enable-notifications \
                         --enable-startup-notification \
                         --enable-exif \
                         --enable-pcre \
                         --enable-wallpaper-plugin \
                         --enable-uca-plugin \
                         --enable-tpa-plugin \
                         --enable-apr-plugin \
                        ")

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "FAQ", "HACKING", "NEWS", "README", "THANKS", "TODO")
