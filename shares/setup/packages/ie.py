#!/usr/bin/python
# Cuckoo Sandbox - Automated Malware Analysis
# Copyright (C) 2010-2011  Claudio "nex" Guarnieri (nex@cuckoobox.org)
# http://www.cuckoobox.org
#
# This file is part of Cuckoo.
#
# Cuckoo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cuckoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

import os
import sys
import ConfigParser

sys.path.append("\\\\VBOXSVR\\setup\\lib\\")

from cuckoo.execute import *
from cuckoo.monitor import *

def cuckoo_run(target_path):
    config = ConfigParser.ConfigParser()
    config.read(target_path)
    url = config.get("InternetShortcut", "URL")

    pids = []

    internet_explorer = "C:\\Program Files\\Internet Explorer\\iexplore.exe"

    suspended = True
    (pid, h_thread) = cuckoo_execute(internet_explorer, "%s" % url, suspended)
    cuckoo_monitor(pid, h_thread, suspended)

    pids.append(pid)
    return pids

def cuckoo_check():
    return True

def cuckoo_finish():
    return True
