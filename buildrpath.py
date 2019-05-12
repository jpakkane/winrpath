#!/usr/bin/env python3

#  Copyright (C) 2019 Jussi Pakkanen.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 3, or (at your option) any later
# version, of the GNU General Public License as published by the Free
# Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import shutil, subprocess, sys, os

def build_binaries():
    libname = 'somelib.dll'
    libimport = libname[:-3] + 'lib'
    subprocess.check_call(['cl',
                           '/MDd',
                           '/nologo',
                           '/c',
                           '/Folibfile.obj',
                           'libfile.c'])
    subprocess.check_call(['link',
                           '/nologo',
                           '/DLL',
                           '/OUT:' + libname,
                           'libfile.obj'])
    subprocess.check_call(['cl',
                           '/nologo',
                           'prog.c',
                           '/link',
                           libimport])

if __name__ == '__main__':
    build_binaries()

