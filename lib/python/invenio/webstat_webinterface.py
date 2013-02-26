## This file is part of Invenio.
## Copyright (C) 2007, 2008, 2009, 2010, 2011 CERN.
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

__revision__ = "$Id$"
__lastupdated__ = "$Date$"

import os, sys
from urllib import unquote
from invenio import webinterface_handler_config as apache

from invenio.config import \
     CFG_TMPDIR, \
     CFG_SITE_URL, \
     CFG_SITE_LANG
from invenio.bibindex_engine import CFG_JOURNAL_TAG
from invenio.webinterface_handler import wash_urlargd, WebInterfaceDirectory
from invenio.webpage import page
from invenio.access_control_engine import acc_authorize_action
from invenio.access_control_config import VIEWRESTRCOLL
from invenio.search_engine import collection_restricted_p
from invenio.webuser import collect_user_info, page_not_authorized
from invenio.urlutils import redirect_to_url

from invenio.webstat import perform_request_index, \
    perform_display_keyevent, \
    perform_display_customevent, \
    perform_display_customevent_help, \
    perform_display_error_log_analyzer, \
    register_customevent, \
    perform_display_custom_summary, \
    perform_display_stats_per_coll, \
    perform_display_current_system_health, \
    perform_display_coll_list


def detect_suitable_graph_format():
    """
    Return suitable graph format default argument. It is always flot (when there wasn't plot, gnuplot if it is
    present, otherwise asciiart).
    """
    return "flot"
#    try:
#        import Gnuplot
#        suitable_graph_format = "gnuplot"
#    except ImportError:
#        suitable_graph_format = "asciiart"
#    return suitable_graph_format

SUITABLE_GRAPH_FORMAT = detect_suitable_graph_format()


class WebInterfaceStatsPages(WebInterfaceDirectory):
    """Defines the set of stats pages."""

    _exports = ['', 'system_health',
                 'collection_population', 'new_records', 'search_frequency', 'search_type_distribution',
                 'download_frequency', 'comments_frequency', 'number_of_loans', 'web_submissions',
                 'loans_stats', 'loans_lists', 'renewals_lists', 'returns_table', 'returns_graph',
                 'ill_requests_stats', 'ill_requests_lists', 'ill_requests_graph', 'items_stats',
                 'items_list', 'loans_requests', 'loans_request_lists', 'user_stats',
                 'user_lists', 'error_log', 'customevent', 'customevent_help',
                 'customevent_register', 'custom_summary', 'collections' , 'collection_stats',
                 'export']

    navtrail = """<a class="navtrail" href="%s/stats/%%(ln_link)s">Statistics</a>""" % CFG_SITE_URL

    def __call__(self, req, form):
        """Index page."""
        argd = wash_urlargd(form, {'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='index',
                ln=ln)

        return page(title="Statistics",
                    body=perform_request_index(ln=ln),
                    description="CDS, Statistics",
                    keywords="CDS, statistics",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='stats',
                    language=ln)

    # CURRENT SYSTEM HEALTH
    def system_health(self, req, form):
        argd = wash_urlargd(form, {'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='current system health',
                ln=ln)

        return page(title="Current system health",
                    body=perform_display_current_system_health(ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Current system health",
                    keywords="CDS, statistics, current system health",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='current system health',
                    language=ln)

    # KEY EVENT SECTION
    def collection_population(self, req, form):
        """Collection population statistics page."""
        argd = wash_urlargd(form, {'collection': (str, "All"),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='collection population',
                ln=ln)

        return page(title="Collection population",
                    body=perform_display_keyevent('collection population', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Collection population",
                    keywords="CDS, statistics, collection population",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='collection population',
                    language=ln)

    def new_records(self, req, form):
        """Collection population statistics page."""
        argd = wash_urlargd(form, {'collection': (str, "All"),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='new records',
                ln=ln)

        return page(title="New records",
                    body=perform_display_keyevent('new records', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, New records",
                    keywords="CDS, statistics, new records",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='new records',
                    language=ln)


    def search_frequency(self, req, form):
        """Search frequency statistics page."""
        argd = wash_urlargd(form, {'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='search frequency',
                ln=ln)

        return page(title="Search frequency",
                    body=perform_display_keyevent('search frequency', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Search frequency",
                    keywords="CDS, statistics, search frequency",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='search frequency',
                    language=ln)

    def comments_frequency(self, req, form):
        """Comments frequency statistics page."""
        argd = wash_urlargd(form, {'collection': (str, "All"),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='comments frequency',
                ln=ln)

        return page(title="Comments frequency",
                    body=perform_display_keyevent('comments frequency', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Comments frequency",
                    keywords="CDS, statistics, Comments frequency",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='comments frequency',
                    language=ln)

    def search_type_distribution(self, req, form):
        """Search type distribution statistics page."""
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        argd = wash_urlargd(form, {'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='search type distribution',
                ln=ln)

        return page(title="Search type distribution",
                    body=perform_display_keyevent('search type distribution', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Search type distribution",
                    keywords="CDS, statistics, search type distribution",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='search type distribution',
                    language=ln)

    def download_frequency(self, req, form):
        """Download frequency statistics page."""
        argd = wash_urlargd(form, {'collection': (str, "All"),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='download frequency',
                ln=ln)

        return page(title="Download frequency",
                    body=perform_display_keyevent('download frequency', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Download frequency",
                    keywords="CDS, statistics, download frequency",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='download frequency',
                    language=ln)

    def number_of_loans(self, req, form):
        """Number of loans statistics page."""
        argd = wash_urlargd(form, {'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='number of circulation loans',
                ln=ln)

        return page(title="Number of circulation loans",
                    body=perform_display_keyevent('number of loans', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Number of circulation loans",
                    keywords="CDS, statistics, Number of circulation loans",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='number of circulation loans',
                    language=ln)

    def web_submissions(self, req, form):
        """Web submissions statistics page."""
        argd = wash_urlargd(form, {'doctype': (str, "all"),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='web submissions',
                ln=ln)

        return page(title="Web submissions",
                    body=perform_display_keyevent('web submissions', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Web submissions",
                    keywords="CDS, statistics, websubmissions",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='web submissions',
                    language=ln)

    def loans_stats(self, req, form):
        """Number of loans statistics page."""
        argd = wash_urlargd(form, {'udc': (str, ""),
                                   'item_status': (str, ""),
                                   'publication_date': (str, ""),
                                   'creation_date': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation loans statistics',
                ln=ln)

        return page(title="Circulation loans statistics",
                    body=perform_display_keyevent('loans statistics', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation loans statistics",
                    keywords="CDS, statistics, Circulation loans statistics",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation loans statistics',
                    language=ln)

    def loans_lists(self, req, form):
        """Number of loans lists page."""
        argd = wash_urlargd(form, {'udc': (str, ""),
                                   'loan_period': (str, ""),
                                   'min_loans': (int, 0),
                                   'max_loans': (int, sys.maxint),
                                   'publication_date': (str, ""),
                                   'creation_date': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        argd['min_loans'] = str(argd['min_loans'])
        argd['max_loans'] = str(argd['max_loans'])
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation loans lists',
                ln=ln)

        return page(title="Circulation loans lists",
                    body=perform_display_keyevent('loans lists', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation oans lists",
                    keywords="CDS, statistics, Circulation loans lists",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation loans lists',
                    language=ln)

    def renewals_lists(self, req, form):
        """Renewed items lists page."""
        argd = wash_urlargd(form, {'udc': (str, ""),
                                   'collection': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation renewals lists',
                ln=ln)

        return page(title="Circulation renewals lists",
                    body=perform_display_keyevent('renewals', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation renewals lists",
                    keywords="CDS, statistics, Circulation renewals lists",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation renewals lists',
                    language=ln)

    def returns_table(self, req, form):
        """Number of returns table page."""
        argd = wash_urlargd(form, {'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='Circulation returns table',
                ln=ln)

        return page(title="Circulation returns table",
                    body=perform_display_keyevent('number returns', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation returns table",
                    keywords="CDS, statistics, Circulation returns table",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation returns table',
                    language=ln)

    def returns_graph(self, req, form):
        """Percentage of returns graph page."""
        argd = wash_urlargd(form, {'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation returns graph',
                ln=ln)

        return page(title="Circulation returns graph",
                    body=perform_display_keyevent('percentage returns', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation returns graph",
                    keywords="CDS, statistics, Circulation returns graph",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation returns graph',
                    language=ln)

    def ill_requests_stats(self, req, form):
        """ILL Requests statistics page."""
        argd = wash_urlargd(form, {'doctype': (str, ""),
                                   'status': (str, ""),
                                   'supplier': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation ill requests statistics',
                ln=ln)

        return page(title="Circulation ILL Requests statistics",
                    body=perform_display_keyevent('ill requests statistics', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation ILL Requests statistics",
                    keywords="CDS, statistics, Circulation ILL Requests statistics",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation ill requests statistics',
                    language=ln)

    def ill_requests_lists(self, req, form):
        """Number of loans lists page."""
        argd = wash_urlargd(form, {'doctype': (str, ""),
                                   'supplier': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation ill requests list',
                ln=ln)

        return page(title="Circulation ILL Requests list",
                    body=perform_display_keyevent('ill requests list', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation ILL Requests list",
                    keywords="CDS, statistics, Circulation ILL Requests list",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation ill requests list',
                    language=ln)

    def ill_requests_graph(self, req, form):
        """Percentage of satisfied ILL requests graph page."""
        argd = wash_urlargd(form, {'doctype': (str, ""),
                                   'status': (str, ""),
                                   'supplier': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='percentage circulation satisfied ill requests',
                ln=ln)

        return page(title="Percentage of circulation satisfied ILL requests",
                    body=perform_display_keyevent('percentage satisfied ill requests',
                                                  argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Percentage of circulation satisfied ILL requests",
                    keywords="CDS, statistics, Percentage of circulation satisfied ILL requests",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='percentage circulation satisfied ill requests',
                    language=ln)

    def items_stats(self, req, form):
        """ILL Requests statistics page."""
        argd = wash_urlargd(form, {'udc': (str, ""),
                                   'collection': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation items stats',
                ln=ln)

        return page(title="Circulation items statistics",
                    body=perform_display_keyevent('items stats', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation items statistics",
                    keywords="CDS, statistics, Circulation items statistics",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation items stats',
                    language=ln)

    def items_list(self, req, form):
        """Number of loans lists page."""
        argd = wash_urlargd(form, {'library': (str, ""),
                                   'status': (str, ""),
                                   'format': (str, ""),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation items list',
                ln=ln)

        return page(title="Circulation items list",
                    body=perform_display_keyevent('items list', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation items list",
                    keywords="CDS, statistics, Circulation items list",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation items list',
                    language=ln)

    def loans_requests(self, req, form):
        """Number of loans statistics page."""
        argd = wash_urlargd(form, {'item_status': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation loan request statistics',
                ln=ln)

        return page(title="Circulation hold requests statistics",
                    body=perform_display_keyevent('loan request statistics', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation hold requests statistics",
                    keywords="CDS, statistics, Circulation hold requests statistics",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation loan request statistics',
                    language=ln)

    def loans_request_lists(self, req, form):
        """Number of loans request lists page."""
        argd = wash_urlargd(form, {'udc': (str, ""),
                                   'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation hold request lists',
                ln=ln)

        return page(title="Circulation loans request lists",
                    body=perform_display_keyevent('loan request lists', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation hold request lists",
                    keywords="CDS, statistics, Circulation hold request lists",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation hold request lists',
                    language=ln)

    def user_stats(self, req, form):
        """Number of loans statistics page."""
        argd = wash_urlargd(form, {'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation user statistics',
                ln=ln)

        return page(title="Circulation users statistics",
                    body=perform_display_keyevent('user statistics', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation users statistics",
                    keywords="CDS, statistics, Circulation users statistics",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation user statistics',
                    language=ln)

    def user_lists(self, req, form):
        """Number of loans lists page."""
        argd = wash_urlargd(form, {'timespan': (str, "today"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, SUITABLE_GRAPH_FORMAT),
                                   'sql': (int, 0),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='circulation users lists',
                ln=ln)

        return page(title="Circulation users lists",
                    body=perform_display_keyevent('user lists', argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Circulation users lists",
                    keywords="CDS, statistics, Circulation users lists",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='circulation users lists',
                    language=ln)

    # CUSTOM EVENT SECTION
    def customevent(self, req, form):
        """Custom event statistics page"""
        arg_format = {'ids': (list, []),
                     'timespan': (str, "today"),
                     's_date': (str, ""),
                     'f_date': (str, ""),
                     'format': (str, SUITABLE_GRAPH_FORMAT),
                     'ln': (str, CFG_SITE_LANG)}
        for key in form.keys():
            if key[:4] == 'cols':
                i = key[4:]
                arg_format['cols' + i] = (list, [])
                arg_format['col_value' + i] = (list, [])
                arg_format['bool' + i] = (list, [])
        argd = wash_urlargd(form, arg_format)

        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='custom event',
                ln=ln)

        body = perform_display_customevent(argd['ids'], argd, req=req, ln=ln)
        return page(title="Custom event",
                    body=body,
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS Personalize, Statistics, Custom event",
                    keywords="CDS, statistics, custom event",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='custom event',
                    language=ln)

    def error_log(self, req, form):
        """Number of loans request lists page."""
        argd = wash_urlargd(form, {'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='error log analyzer',
                ln=ln)

        return page(title="Error log analyzer",
                    body=perform_display_error_log_analyzer(ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Error log analyzer",
                    keywords="CDS, statistics, Error log analyzer",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='error log analyzer',
                    language=ln)

    def customevent_help(self, req, form):
        """Custom event help page"""
        argd = wash_urlargd(form, {'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='custom event help',
                ln=ln)

        return page(title="Custom event help",
                    body=perform_display_customevent_help(ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS Personalize, Statistics, Custom event help",
                    keywords="CDS, statistics, custom event help",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='custom event help',
                    language=ln)

    def customevent_register(self, req, form):
        """Register a customevent and reload to it defined url"""
        argd = wash_urlargd(form, {'event_id': (str, ""),
                                   'arg': (str, ""),
                                   'url': (str, ""),
                                   'ln': (str, CFG_SITE_LANG)})
        params = argd['arg'].split(',')
        if "WEBSTAT_IP" in params:
            index = params.index("WEBSTAT_IP")
            params[index] = str(req.remote_ip)
        register_customevent(argd['event_id'], params)
        return redirect_to_url(req, unquote(argd['url']), apache.HTTP_MOVED_PERMANENTLY)

    # CUSTOM REPORT SECTION
    def custom_summary(self, req, form):
        """Custom report page"""
        argd = wash_urlargd(form, {'query': (str, ""),
                                   'tag': (str, CFG_JOURNAL_TAG.replace("%", "p")),
                                   'title': (str, "Publications"),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='custom query summary',
                ln=ln)

        return page(title="Custom query summary",
                    body=perform_display_custom_summary(argd, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Custom Query Summary",
                    keywords="CDS, statistics, custom query summary",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='custom query summary',
                    language=ln)

    # COLLECTIONS SECTION
    def collection_stats(self, req, form):
        """Collection statistics list page"""
        argd = wash_urlargd(form, {'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                navmenuid='collections list',
                text=auth_msg,
                ln=ln)

        return page(title="Collection statistics",
                    body=perform_display_coll_list(req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Collection statistics",
                    keywords="CDS, statistics",
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='collections list',
                    language=ln)


    def collections(self, req, form):
        """Collections statistics page"""
        argd = wash_urlargd(form, {'collection': (str, "All"),
                                   'timespan': (str, "this month"),
                                   's_date': (str, ""),
                                   'f_date': (str, ""),
                                   'format': (str, "flot"),
                                   'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                navmenuid='collections',
                text=auth_msg,
                ln=ln)

        if collection_restricted_p(argd['collection']):
            (auth_code_coll, auth_msg_coll) = acc_authorize_action(user_info, VIEWRESTRCOLL, collection=argd['collection'])
            if auth_code_coll:
                return page_not_authorized(req,
                                           navmenuid='collections',
                                           text=auth_msg_coll,
                                           ln=ln)
        return page(title="Statistics of %s" % argd['collection'],
                    body=perform_display_stats_per_coll(argd, req, ln=ln),
                    navtrail="""<a class="navtrail" href="%s/stats/%s">Statistics</a>""" % \
                    (CFG_SITE_URL, (ln != CFG_SITE_LANG and '?ln=' + ln) or ''),
                    description="CDS, Statistics, Collection %s" % argd['collection'],
                    keywords="CDS, statistics, %s" % argd['collection'],
                    req=req,
                    lastupdated=__lastupdated__,
                    navmenuid='collections',
                    language=ln)

    # EXPORT SECTION
    def export(self, req, form):
        """Exports data"""
        argd = wash_urlargd(form, {'ln': (str, CFG_SITE_LANG)})
        ln = argd['ln']
        user_info = collect_user_info(req)
        (auth_code, auth_msg) = acc_authorize_action(user_info, 'runwebstatadmin')
        if auth_code:
            return page_not_authorized(req,
                navtrail=self.navtrail % {'ln_link': (ln != CFG_SITE_LANG and '?ln=' + ln) or ''},
                text=auth_msg,
                navmenuid='export',
                ln=ln)

        argd = wash_urlargd(form, {"filename": (str, ""),
                                   "mime": (str, "")})

        # Check that the particular file exists and that it's OK to export
        webstat_files = [x for x in os.listdir(CFG_TMPDIR) if x.startswith("webstat")]
        if argd["filename"] not in webstat_files:
            return "Bad file."

        # Set correct header type
        req.content_type = argd["mime"]
        req.send_http_header()

        # Rebuild path, send it to the user, and clean up.
        filename = CFG_TMPDIR + '/' + argd["filename"]
        req.sendfile(filename)
        os.remove(filename)

    index = __call__
