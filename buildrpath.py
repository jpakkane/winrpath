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
    cwdlen = len(os.getcwd())
    base = 'a'*(cwdlen+20)
    libname = base + '.dll'
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
    return base

def create_builddir(dirname, basename):
    subdir = os.path.join(dirname, 'sub')
    os.mkdir(dirname)
    os.mkdir(subdir)
    exe_outname = os.path.join(dirname, 'prog.exe')
    dll_outname = os.path.join(subdir, 'helper.dll')
    abs_dll_outname = os.path.join(os.getcwd(), dll_outname)
    placeholder_name = basename + '.dll'
    print(len(abs_dll_outname))
    print(len(placeholder_name))
    assert(len(abs_dll_outname) == len(placeholder_name))
    dll = open(basename + '.dll', 'rb').read()
    exe = open('prog.exe', 'rb').read()
    exe = exe.replace(placeholder_name.encode(encoding='ascii'),
                      abs_dll_outname.encode(encoding='ascii'))
    open(dll_outname, 'wb').write(dll)
    open(exe_outname, 'wb').write(exe)

if __name__ == '__main__':
    if os.path.exists('builddir'):
        shutil.rmtree('builddir')
    if os.path.exists('installdir'):
        shutil.rmtree('installdir')
    basename = build_binaries()
    create_builddir('builddir', basename)

