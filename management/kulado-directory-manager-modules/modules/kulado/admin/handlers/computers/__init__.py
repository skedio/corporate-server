#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Univention Admin Modules
#  import all computer modules
#
# Copyright 2004-2019 Univention GmbH
#
# https://www.univention.de/
#
# All rights reserved.
#
# The source code of this program is made available
# under the terms of the GNU Affero General Public License version 3
# (GNU AGPL V3) as published by the Free Software Foundation.
#
# Binary versions of this program provided by Univention to you as
# well as other copyrighted, protected or trademarked materials like
# Logos, graphics, fonts, specific documentations and configurations,
# cryptographic keys etc. are subject to a license agreement between
# you and Univention and not subject to the GNU AGPL V3.
#
# In the case you use this program under the terms of the GNU AGPL V3,
# the program is provided in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License with the Debian GNU/Linux or Univention distribution in file
# /usr/share/common-licenses/AGPL-3; if not, see
# <https://www.gnu.org/licenses/>.

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import os.path

computers = []


def __walk(root, dir, files):
	for file_ in files:
		if file_.endswith('.py') and not file_.startswith('__') and file_ not in ('computer.py',):
			computers.append(__import__(file_[: -3], globals(), locals(), ['']))


path = os.path.abspath(os.path.dirname(__file__))
os.path.walk(path, __walk, path)