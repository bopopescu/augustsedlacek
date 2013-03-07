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

"""BibEdit Configuration."""

__revision__ = "$Id$"

from invenio.config import CFG_ETCDIR

import os

## CFG_BIBEDIT_FILENAME - default filename for BibEdit files.
CFG_BIBEDIT_FILENAME = "bibedit_record"

## The CFG_BIBEDIT_JS_* constants are passed on and used by the BibEdit
## Javascript engine.

## CFG_BIBEDIT_JS_HASH_CHECK_INTERVAL - interval (in ms) between checking if
## hash has changed.
CFG_BIBEDIT_JS_HASH_CHECK_INTERVAL = 250

## CFG_BIBEDIT_JS_CHECK_SCROLL_INTERVAL - interval (in ms) between menu
## repositioning.
CFG_BIBEDIT_JS_CHECK_SCROLL_INTERVAL = 250

## CFG_BIBEDIT_JS_STATUS_INFO_TIME - display status info messages for how long
## (in ms).
CFG_BIBEDIT_JS_STATUS_INFO_TIME = 1000

## CFG_BIBEDIT_JS_STATUS_ERROR_TIME - display status error messages for how long
## (in ms).
CFG_BIBEDIT_JS_STATUS_ERROR_TIME = 2000

## CFG_BIBEDIT_JS_CLONED_RECORD_COLOR - Color of cloned record ID highlighting.
CFG_BIBEDIT_JS_CLONED_RECORD_COLOR = 'yellow'

## CFG_BIBEDIT_JS_CLONED_RECORD_COLOR_FADE_DURATION - Duration (in ms) for the
## fading of cloned record ID highlighting.
CFG_BIBEDIT_JS_CLONED_RECORD_COLOR_FADE_DURATION = 5000

## CFG_BIBEDIT_JS_NEW_ADD_FIELD_FORM_COLOR - Color of new field forms'
## highlighting.
CFG_BIBEDIT_JS_NEW_ADD_FIELD_FORM_COLOR = 'lightblue'

## CFG_BIBEDIT_JS_NEW_ADD_FIELD_FORM_COLOR_FADE_DURATION - Duration (in ms) for
## the fading of new field forms' highlighting.
CFG_BIBEDIT_JS_NEW_ADD_FIELD_FORM_COLOR_FADE_DURATION = 2000

## CFG_BIBEDIT_JS_NEW_FIELDS_COLOR - Color of new fields' highlighting
CFG_BIBEDIT_JS_NEW_FIELDS_COLOR = 'lightgreen'

## CFG_BIBEDIT_JS_NEW_FIELDS_COLOR_FADE_DURATION - Duration (in ms) for the
## fading of new fields' highlighting.
CFG_BIBEDIT_JS_NEW_FIELDS_COLOR_FADE_DURATION = 2000

## CFG_BIBEDIT_JS_NEW_CONTENT_HIGHLIGHT_DELAY - Duration (in ms) before
## highlighting newly modified content.
## WARNING: If set to low, the Jeditable plugin won't have time to update the
## cell with the new content (recommended: >50).
CFG_BIBEDIT_JS_NEW_CONTENT_HIGHLIGHT_DELAY = 50

## CFG_BIBEDIT_JS_NEW_FIELDS_COLOR - Color of new fields' highlighting
CFG_BIBEDIT_JS_NEW_CONTENT_COLOR = 'lightgreen'

## CFG_BIBEDIT_JS_NEW_FIELDS_COLOR_FADE_DURATION - Duration (in ms) for the
## fading of new fields' highlighting.
CFG_BIBEDIT_JS_NEW_CONTENT_COLOR_FADE_DURATION = 2000

## CFG_BIBEDIT_JS_TICKET_REFRESH_DELAY - Duration (in ms) before refreshing
## a record's tickets after the user clicks on the link to create a new one.
## WARNING: If set to low, the request for RT to generate the ticket won't have
## time to finish (recommended: >2000).
CFG_BIBEDIT_JS_TICKET_REFRESH_DELAY = 5000

## CFG_BIBEDIT_AJAX_RESULT_CODES - dictionary of result codes and messages used
## by the Ajax engine.

CFG_BIBEDIT_AJAX_RESULT_CODES_REV = {
#TODO: all the result codes should be accessible through the constants rather than
#      a direct number ! some parts of the bibedit_engine.py are not readable because
#      of using the numbers
#      The dictionary is convenient at this place because it can be imported with one command
#      unlike a number of constants
    'editor_modifications_changed': 33,
    'disabled_hp_changeset' : 34,
    'added_positioned_subfields' : 35,
    'autosuggestion_scanned' : 36,
    'error_rec_locked_by_user' : 104,
    'error_rec_locked_by_queue' : 105,
    'error_wrong_cache_file_format' : 111,
    'error_physical_copies_exist': 112
}

CFG_BIBEDIT_AJAX_RESULT_CODES = {
    0: '',
    1: 'Search completed',
    2: 'Tag format changed',
    3: 'Record loaded',
    4: 'Record submitted',
    5: 'Cancelled',
    6: 'Record created (new)',
    7: 'Record created (from template)',
    8: 'Record created (from existing)',
    9: 'Record cloned',
    10: 'Record deleted',
    11: 'Cache deleted',
    12: 'Record ready for merge',
    20: 'Added controlfield',
    21: 'Added field',
    22: 'Added subfield',
    23: 'Added subfields',
    24: 'Content modified',
    25: 'Subfield moved',
    26: 'Field deleted',
    27: 'Fields deleted',
    28: 'Subfield deleted',
    29: 'Subfields deleted',
    30: 'Selection deleted',
    31: 'Tickets retrieved',
    32: 'Field moved',
    33: 'Modifications updates',
    34: 'Disabled a changeset',
    35: 'Added fields/subfields',
    36: 'Autosuggestion scanned',
    100: 'Error: Not logged in',
    101: 'Error: Permission denied',
    102: 'Error: Non-existent record',
    103: 'Error: Deleted record',
    104: 'Error: Record locked by user',
    105: 'Error: Record locked by queue',
    106: 'Error: Cache file missing',
    107: 'Error: Cache file changed',
    108: 'Error: Template file missing',
    109: 'Error: Invalid template file',
    110: 'Error: Invalid content in record',
    111: 'Error: Wrong cache file format',
    112: 'Error: Physical copies of this record exist',
    113: 'Error: Upload simulation found some errors'
}

CFG_BIBEDIT_MSG = {
    "not_authorised" : "You are not authorised to submit a record into the given \
                        collection. Please, review the collection tags."
}
## CFG_BIBEDIT_MAX_SEARCH_RESULTS
CFG_BIBEDIT_MAX_SEARCH_RESULTS = 99

## CFG_BIBEDIT_TAG_FORMAT - default format to use when displaying MARC tags.
CFG_BIBEDIT_TAG_FORMAT = 'MARC'

## CFG_BIBEDIT_TO_MERGE_SUFFIX - default filename suffix for XML file to be
## merged. Filename will then be constructed like this:
## <CFG_BIBEDIT_FILENAME>_<RECID>_<UID>_<CFG_BIBEDIT_TO_MERGE_SUFFIX>.xml
CFG_BIBEDIT_TO_MERGE_SUFFIX = 'merge'

# CFG_BIBEDIT_RECORD_TEMPLATES_PATH - path to record template directory

CFG_BIBEDIT_RECORD_TEMPLATES_PATH = "%s%sbibedit%srecord_templates" % (CFG_ETCDIR, os.sep, os.sep)
CFG_BIBEDIT_FIELD_TEMPLATES_PATH = "%s%sbibedit%sfield_templates" % (CFG_ETCDIR, os.sep, os.sep)

# CFG_BIBEDIT_AUTOSUGGEST_TAGS - for which tags the editor should try to autosuggest values
# This is "safe" to have configured since it does not rely to a particular existing KB
CFG_BIBEDIT_AUTOSUGGEST_TAGS = ['100__a','190__a','19000a','19001a','19010a','19011a','190__1','190001','190011','190101','190111','190__3','190003','190013','190103','190113','190__4','190004','190014','190104','190114','400__a','40000a','40001a','40010a','40011a','400__1','400001','400011','400101','400111','400__3','400003','400013','400103','400113','400__4','400004','400014','400104','400114','500__a','50000a','50001a','50010a','50011a','500__1','500001','500011','500101','500111','500__3','500003','500013','500103','500113','500__4','500004','500014','500104','500114','700__a','70000a','70001a','70010a','70011a','700__1','700001','700011','700101','700111','700__3','700003','700013','700103','700113','700__4','700004','700014','700104','700114','7112_c','7112_x','751__a','751__x','451__a','451__x','670__a']
# CFG_BIBEDIT_AUTOCOMPLETE_TAGS_KBS - a dictionary whose keys are tags and values kb names
# This is better left empty when in doubt
CFG_BIBEDIT_AUTOCOMPLETE_TAGS_KBS = {} # { '65017a': 'SISC-65017a---65017a' }
# CFG_BIBEDIT_KEYWORD_TAXONOMY - the name of the taxonomy DB that holds the taxonomy file used
# for getting the keywords. Use only if you have a taxonomy KB.
CFG_BIBEDIT_KEYWORD_TAXONOMY = "" #'HEP.RDF'
#what tag is used for keywords
CFG_BIBEDIT_KEYWORD_TAG = "" # '6531_a'
#what label inside the RDF file contains the term
CFG_BIBEDIT_KEYWORD_RDFLABEL = "" #'prefLabel'
