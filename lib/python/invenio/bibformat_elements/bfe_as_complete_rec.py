# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011 CERN.
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
"""BibFormat element - Prints whole AS record
"""

__revision__ = "$Id$"

import cgi
from urllib import quote
from invenio.config import CFG_SITE_URL


def format_element(bfo, separator="; ", print_link="yes"):
    """
    to be supplied
    """

    out = ""
    temp1 = []
    temp2 = []
    temp3 = []


    #190
    fields = bfo.fields('190%%', repeatable_subfields_p=True)
    for field in fields:
        out += "<h3 class='preview'>Záhlaví – osobní jméno</h3>"
        sf_b = field.get('1',[])
        sf_3 = field.get('3',[])
        sf_4 = field.get('4',[])
        sf_a = field.get('a',[])
        sf_c = field.get('c',[])
        sf_y = field.get('y',[])
        sf_x = field.get('x',[])
        sf_v = field.get('v',[])
        sf_l = field.get('l',[])
        temp1[:] = []
        for val in sf_b:
            temp1.append(val)
        for val in sf_3:
            temp1.append(val)
        for val in sf_4:
            temp1.append(val)
        out += " ".join(temp1)
        temp2[:] = []
        for val in sf_a:
            temp2.append(val)
        for val in sf_c:
            temp2.append(val)
        if len(temp1)>0 and len(temp2)>0:
            out += ", "
        out += ", ".join(temp2)
        temp3[:] = []
        for val in sf_y:
            temp3.append(val)
        for val in sf_x:
            temp3.append(val)
        for val in sf_v:
            temp3.append(val)
        for val in sf_l:
            temp3.append(val)
        if (len(temp1)>0 or len(temp2)>0) and len(temp3)>0:
            out += "<br/>"
        out += "<br/>".join(temp3)

    #400, 500
    titul = {"400%%":"Variantní jméno", "500%%":"Alternativní jméno"}
    for tag in ["400%%","500%%"]:
        fields = bfo.fields(tag, repeatable_subfields_p=True)
        for field in fields:
            out += "<h3 class='preview'>%s</h3>" % titul[tag]
            sf_b = field.get('1',[])
            sf_3 = field.get('3',[])
            sf_4 = field.get('4',[])
            sf_a = field.get('a',[])
            sf_c = field.get('c',[])
            sf_y = field.get('y',[])
            sf_w = field.get('w',[])
            sf_x = field.get('x',[])
            sf_v = field.get('v',[])
            temp1[:] = []
            for val in sf_b:
                temp1.append(val)
            for val in sf_3:
                temp1.append(val)
            for val in sf_4:
                temp1.append(val)
            out += " ".join(temp1)
            temp2[:] = []
            for val in sf_a:
                temp2.append(val)
            for val in sf_c:
                temp2.append(val)
            if len(temp1)>0 and len(temp2)>0:
                out += ", "
            out += ", ".join(temp2)
            temp3[:] = []
            for val in sf_y:
                temp3.append(val)
            for val in sf_w:
                temp3.append(val)
            for val in sf_x:
                temp3.append(val)
            for val in sf_v:
                temp3.append(val)
            if (len(temp1)>0 or len(temp2)>0) and len(temp3)>0:
                out += "<br/>"
            out += "<br/>".join(temp3)

    #690
    fields = bfo.fields('690%%', repeatable_subfields_p=True)
    for field in fields:
        out += "<h3 class='preview'>Heraldické údaje</h3>"
        sf_g = field.get('g',[])
        sf_a = field.get('a',[])
        temp1[:] = []
        for val in sf_g:
            temp1.append(val)
        for val in sf_a:
            temp1.append(val)
        out += "<br/>".join(temp1)

    #670
    fields = bfo.fields('670%%', repeatable_subfields_p=True)
    i = 0
    for field in fields:
        i = i + 1
        if i == 1:
            out += "<h3 class='preview'>Literatura</h3><ul>"
        out += "<li>"
        sf_a = field.get('a',[])
        sf_z = field.get('z',[])
        sf_y = field.get('y',[])
        sf_x = field.get('x',[])
        sf_5 = field.get('5',[])
        temp1[:] = []
        for val in sf_a:
            temp1.append(val)
        for val in sf_z:
            temp1.append(val)
        for val in sf_y:
            temp1.append(val)
        out += " ".join(temp1)+". "
        temp2[:] = []
        for val in sf_x:
            temp2.append(val)
        out += " ".join(temp2)
        temp3[:] = []
        for val in sf_5:
            temp3.append(val)
        if len(temp3)>0:
            out += " (" + " ".join(temp3) + ")"
        out += "</li>"
    out += "</ul>"

    #678
    fields = bfo.fields('678%%', repeatable_subfields_p=True)
    i = 0
    for field in fields:
        i = i + 1
        if i == 1:
            out += "<h3 class='preview'>Biografie</h3><ul>"
        out += "<li>"
        sf_a = field.get('a',[])
        temp1[:] = []
        for val in sf_a:
            temp1.append(val)
        out += "<br/>".join(temp1)
        out += "</li>"
    out += "</ul>"

    #680
    fields = bfo.fields('680%%', repeatable_subfields_p=True)
    i = 0
    for field in fields:
        i = i + 1
        if i == 1:
            out += "<h3 class='preview'>Poznámky</h3><ul>"
        out += "<li>"
        sf_i = field.get('i',[])
        temp1[:] = []
        for val in sf_i:
            temp1.append(val)
        out += "<br/>".join(temp1)
        out += "</li>"
    out += "</ul>"

    #700
    fields = bfo.fields('700%%', repeatable_subfields_p=True)
    i = 0
    for field in fields:
        i = i + 1
        if i == 1:
            out += "<h3 class='preview'>Osobní jméno - propojení</h3><ul>"
        out += "<li>"
        sf_b = field.get('1',[])
        sf_3 = field.get('3',[])
        sf_4 = field.get('4',[])
        sf_a = field.get('a',[])
        sf_c = field.get('c',[])
        sf_y = field.get('y',[])
        sf_w = field.get('w',[])
        sf_x = field.get('x',[])
        sf_v = field.get('v',[])
        temp1[:] = []
        for val in sf_b:
            temp1.append(val)
        for val in sf_3:
            temp1.append(val)
        for val in sf_4:
            temp1.append(val)
        out += " ".join(temp1)
        temp2[:] = []
        for val in sf_a:
            temp2.append(val)
        for val in sf_c:
            temp2.append(val)
        if len(temp1)>0 and len(temp2)>0:
            out += ", "
        out += ", ".join(temp2)
        temp3[:] = []
        for val in sf_y:
            temp3.append(val)
        for val in sf_w:
            temp3.append(val)
        for val in sf_x:
            temp3.append(val)
        for val in sf_v:
            temp3.append(val)
        if (len(temp1)>0 or len(temp2)>0) and len(temp3)>0:
            out += "<br/>"
        out += "<br/>".join(temp3)
        out += "</li>"
    out += "</ul>"

    #751
    titul2 = {"751%%":"Místní název – propojení", "451%%":"Variantní místní název", "711%%":"Událost – propojení"}
    for tag in ["751%%","451%%","711%%"]:
        fields = bfo.fields(tag, repeatable_subfields_p=True)
        i = 0
        for field in fields:
            i = i + 1
            if i == 1:
                out += "<h3 class='preview'>%s</h3><ul>" % titul2[tag]
            out += "<li>"
            sf_a = field.get('a',[])
            sf_y = field.get('y',[])
            sf_x = field.get('x',[])
            temp1[:] = []
            for val in sf_a:
                temp1.append(val)
            out += " ".join(temp1)
            temp2[:] = []
            for val in sf_y:
                temp2.append(val)
            if len(temp1)>0 and len(temp2)>0:
                out += "<br/>"
            out += " ".join(temp2)
            temp3[:] = []
            for val in sf_x:
                temp3.append(val)
            if (len(temp1)>0 or len(temp2)>0) and len(temp3)>0:
                out += "<br/>"
            out += " ".join(temp3)
            out += "</li>"
        out += "</ul>"

    #950
    fields = bfo.fields('950%%', repeatable_subfields_p=True)
    for field in fields:
        out += "<h3 class='preview'>Status</h3>"
        sf_s = field.get('s',[])
        sf_p = field.get('p',[])
        temp1[:] = []
        for val in sf_s:
            temp1.append("<span class='cardStatusPreview cardStatus"+val+"'>"+val+"</span>")
        for val in sf_p:
            temp1.append(val)
        out += "<br/>".join(temp1)

    return out

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0

