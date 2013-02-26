# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2008, 2010, 2011 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Invenio WebStat Configuration."""

__revision__ = "$Id$"

from invenio.config import CFG_ETCDIR

CFG_WEBSTAT_CONFIG_PATH = CFG_ETCDIR + "/webstat/webstat.cfg"

## TP: nastaveni prislusnosti uyivatelu k supervizorum
## Simunek: 9
## Dolezalova: 10
## invenio.autor: 12
cfg_supervisors_groups = {
	9: [18,15,9],
	10: [14,20],
	22: [13,21,26],
	23: [16,25,27],
	12: [24,29]
}

CFG_SUPERVISORS_APPROX_GOAL = 200000;
