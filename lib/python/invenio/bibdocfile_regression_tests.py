# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2009, 2010, 2011, 2012 CERN.
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

"""BibDocFile Regression Test Suite."""

__revision__ = "$Id$"

import os
import unittest
from invenio.testutils import make_test_suite, run_test_suite
from invenio.bibdocfile import BibRecDocs, check_bibdoc_authorization, bibdocfile_url_p, guess_format_from_url, CFG_HAS_MAGIC
from invenio.dbquery import run_sql
from invenio.access_control_config import CFG_WEBACCESS_WARNING_MSGS
from invenio.config import \
        CFG_SITE_URL, \
        CFG_PREFIX, \
        CFG_BIBDOCFILE_FILEDIR, \
        CFG_SITE_RECORD, \
        CFG_WEBDIR, \
        CFG_TMPDIR

from datetime import datetime
import time

class BibDocFsInfoTest(unittest.TestCase):
    """Regression tests about the table bibdocfsinfo"""
    def setUp(self):
        self.my_bibrecdoc = BibRecDocs(2)
        self.unique_name = self.my_bibrecdoc.propose_unique_docname('file')
        self.my_bibdoc = self.my_bibrecdoc.add_new_file(CFG_PREFIX + '/lib/webtest/invenio/test.jpg', docname=self.unique_name)
        self.my_bibdoc_id = self.my_bibdoc.id

    def tearDown(self):
        self.my_bibdoc.expunge()

    def test_hard_delete(self):
        """bibdocfile - test correct update of bibdocfsinfo when hard-deleting"""
        self.assertEqual(run_sql("SELECT MAX(version) FROM bibdocfsinfo WHERE id_bibdoc=%s", (self.my_bibdoc_id, ))[0][0], 1)
        self.assertEqual(run_sql("SELECT last_version FROM bibdocfsinfo WHERE id_bibdoc=%s AND version=1 AND format='.jpg'", (self.my_bibdoc_id, ))[0][0], True)
        self.my_bibdoc.add_file_new_version(CFG_PREFIX + '/lib/webtest/invenio/test.gif')
        self.assertEqual(run_sql("SELECT MAX(version) FROM bibdocfsinfo WHERE id_bibdoc=%s", (self.my_bibdoc_id, ))[0][0], 2)
        self.assertEqual(run_sql("SELECT last_version FROM bibdocfsinfo WHERE id_bibdoc=%s AND version=2 AND format='.gif'", (self.my_bibdoc_id, ))[0][0], True)
        self.assertEqual(run_sql("SELECT last_version FROM bibdocfsinfo WHERE id_bibdoc=%s AND version=1 AND format='.jpg'", (self.my_bibdoc_id, ))[0][0], False)
        self.my_bibdoc.delete_file('.gif', 2)
        self.assertEqual(run_sql("SELECT MAX(version) FROM bibdocfsinfo WHERE id_bibdoc=%s", (self.my_bibdoc_id, ))[0][0], 1)
        self.assertEqual(run_sql("SELECT last_version FROM bibdocfsinfo WHERE id_bibdoc=%s AND version=1 AND format='.jpg'", (self.my_bibdoc_id, ))[0][0], True)

class BibDocFileGuessFormat(unittest.TestCase):
    """Regression tests for guess_format_from_url"""

    def test_guess_format_from_url_local_no_ext(self):
        """bibdocfile - guess_format_from_url(), local URL, no extension"""
        self.assertEqual(guess_format_from_url(os.path.join(CFG_WEBDIR, 'img', 'test')), '.bin')

    if CFG_HAS_MAGIC:
        def test_guess_format_from_url_local_no_ext_with_magic(self):
            """bibdocfile - guess_format_from_url(), local URL, no extension, with magic"""
            self.assertEqual(guess_format_from_url(os.path.join(CFG_WEBDIR, 'img', 'testgif')), '.gif')
    else:
        def test_guess_format_from_url_local_no_ext_with_magic(self):
            """bibdocfile - guess_format_from_url(), local URL, no extension, no magic"""
            self.assertEqual(guess_format_from_url(os.path.join(CFG_WEBDIR, 'img', 'testgif')), '.bin')

    def test_guess_format_from_url_local_unknown_ext(self):
        """bibdocfile - guess_format_from_url(), local URL, unknown extension"""
        self.assertEqual(guess_format_from_url(os.path.join(CFG_WEBDIR, 'img', 'test.foo')), '.foo')

    def test_guess_format_from_url_local_known_ext(self):
        """bibdocfile - guess_format_from_url(), local URL, unknown extension"""
        self.assertEqual(guess_format_from_url(os.path.join(CFG_WEBDIR, 'img', 'test.gif')), '.gif')

    def test_guess_format_from_url_remote_no_ext(self):
        """bibdocfile - guess_format_from_url(), remote URL, no extension"""
        self.assertEqual(guess_format_from_url(CFG_SITE_URL + '/img/test'), '.bin')

    if CFG_HAS_MAGIC:
        def test_guess_format_from_url_remote_no_ext_with_magic(self):
            """bibdocfile - guess_format_from_url(), remote URL, no extension, with magic"""
            self.assertEqual(guess_format_from_url(CFG_SITE_URL + '/img/testgif'), '.gif')
    else:
        def test_guess_format_from_url_remote_no_ext_with_magic(self):
            """bibdocfile - guess_format_from_url(), remote URL, no extension, no magic"""
            self.failUnless(guess_format_from_url(CFG_SITE_URL + '/img/testgif') in ('.bin', '.gif'))

    if CFG_HAS_MAGIC:
        def test_guess_format_from_url_remote_unknown_ext(self):
            """bibdocfile - guess_format_from_url(), remote URL, unknown extension, with magic"""
            self.assertEqual(guess_format_from_url(CFG_SITE_URL + '/img/test.foo'), '.gif')
    else:
        def test_guess_format_from_url_remote_unknown_ext(self):
            """bibdocfile - guess_format_from_url(), remote URL, unknown extension, no magic"""
            self.failUnless(guess_format_from_url(CFG_SITE_URL + '/img/test.foo') in ('.bin', '.gif'))

    def test_guess_format_from_url_remote_known_ext(self):
        """bibdocfile - guess_format_from_url(), remote URL, known extension"""
        self.assertEqual(guess_format_from_url(CFG_SITE_URL + '/img/test.gif'), '.gif')

    def test_guess_format_from_url_local_gpl_license(self):
        local_path = os.path.join(CFG_TMPDIR, 'LICENSE')
        print >> open(local_path, 'w'), """
            GNU GENERAL PUBLIC LICENSE
               Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
                       59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Library General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.
[...]
"""
        try:
            if CFG_HAS_MAGIC:
                self.assertEqual(guess_format_from_url(local_path), '.txt')
            else:
                self.assertEqual(guess_format_from_url(local_path), '.bin')
        finally:
            os.remove(local_path)


class BibRecDocsTest(unittest.TestCase):
    """regression tests about BibRecDocs"""

    def test_BibRecDocs(self):
        """bibdocfile - BibRecDocs functions"""
        my_bibrecdoc = BibRecDocs(2)
        #add bibdoc
        my_bibrecdoc.add_new_file(CFG_PREFIX + '/lib/webtest/invenio/test.jpg', 'Main', 'img_test', False, 'test add new file', 'test', '.jpg')
        my_bibrecdoc.add_bibdoc(doctype='Main', docname='file', never_fail=False)
        self.assertEqual(len(my_bibrecdoc.list_bibdocs()), 3)
        my_added_bibdoc = my_bibrecdoc.get_bibdoc('file')
        #add bibdocfile in empty bibdoc
        my_added_bibdoc.add_file_new_version(CFG_PREFIX + '/lib/webtest/invenio/test.gif', \
        description= 'added in empty bibdoc', comment=None, format=None, flags=['PERFORM_HIDE_PREVIOUS'])
        #propose unique docname
        self.assertEqual(my_bibrecdoc.propose_unique_docname('file'), 'file_2')
        #has docname
        self.assertEqual(my_bibrecdoc.has_docname_p('file'), True)
        #merge 2 bibdocs
        my_bibrecdoc.merge_bibdocs('img_test', 'file')
        self.assertEqual(len(my_bibrecdoc.get_bibdoc("img_test").list_all_files()), 2)
        #check file exists
        self.assertEqual(my_bibrecdoc.check_file_exists(CFG_PREFIX + '/lib/webtest/invenio/test.jpg', '.jpg'), True)
        #get bibdoc names
        self.assertEqual(my_bibrecdoc.get_bibdoc_names('Main')[0], '0104007_02')
        self.assertEqual(my_bibrecdoc.get_bibdoc_names('Main')[1],'img_test')
        #get total size
        self.assertEqual(my_bibrecdoc.get_total_size(), 1647591)
        #get total size latest version
        self.assertEqual(my_bibrecdoc.get_total_size_latest_version(), 1647591)
        #display
        value = my_bibrecdoc.display(docname='img_test', version='', doctype='', ln='en', verbose=0, display_hidden=True)
        self.assert_("<small><b>Main</b>" in value)
        #get xml 8564
        value = my_bibrecdoc.get_xml_8564()
        self.assert_('/'+ CFG_SITE_RECORD +'/2/files/img_test.jpg</subfield>' in value)
        #check duplicate docnames
        self.assertEqual(my_bibrecdoc.check_duplicate_docnames(), True)

    def tearDown(self):
        my_bibrecdoc = BibRecDocs(2)
        #delete
        my_bibrecdoc.delete_bibdoc('img_test')
        my_bibrecdoc.delete_bibdoc('file')

class BibDocsTest(unittest.TestCase):
    """regression tests about BibDocs"""

    def test_BibDocs(self):
        """bibdocfile - BibDocs functions"""
        #add file
        my_bibrecdoc = BibRecDocs(2)
        timestamp1 = datetime(*(time.strptime("2011-10-09 08:07:06", "%Y-%m-%d %H:%M:%S")[:6]))
        my_bibrecdoc.add_new_file(CFG_PREFIX + '/lib/webtest/invenio/test.jpg', 'Main', 'img_test', False, 'test add new file', 'test', '.jpg', modification_date=timestamp1)
        my_new_bibdoc = my_bibrecdoc.get_bibdoc("img_test")
        value = my_bibrecdoc.list_bibdocs()
        self.assertEqual(len(value), 2)
        #get total file (bibdoc)
        self.assertEqual(my_new_bibdoc.get_total_size(), 91750)
        #get recid
        self.assertEqual(my_new_bibdoc.get_recid(), 2)
        #change name
        my_new_bibdoc.change_name('new_name')
        #get docname
        self.assertEqual(my_new_bibdoc.get_docname(), 'new_name')
        #get type
        self.assertEqual(my_new_bibdoc.get_type(), 'Main')
        #get id
        self.assert_(my_new_bibdoc.get_id() > 80)
        #set status
        my_new_bibdoc.set_status('new status')
        #get status
        self.assertEqual(my_new_bibdoc.get_status(), 'new status')
        #get base directory
        self.assert_(my_new_bibdoc.get_base_dir().startswith(CFG_BIBDOCFILE_FILEDIR))
        #get file number
        self.assertEqual(my_new_bibdoc.get_file_number(), 1)
        #add file new version
        timestamp2 = datetime(*(time.strptime("2010-09-08 07:06:05", "%Y-%m-%d %H:%M:%S")[:6]))
        my_new_bibdoc.add_file_new_version(CFG_PREFIX + '/lib/webtest/invenio/test.jpg', description= 'the new version', comment=None, format=None, flags=["PERFORM_HIDE_PREVIOUS"], modification_date=timestamp2)
        self.assertEqual(my_new_bibdoc.list_versions(), [1, 2])
        #revert
        timestamp3 = datetime.now()
        time.sleep(2) # so we can see a difference between now() and the time of the revert
        my_new_bibdoc.revert(1)
        self.assertEqual(my_new_bibdoc.list_versions(), [1, 2, 3])
        self.assertEqual(my_new_bibdoc.get_description('.jpg', version=3), 'test add new file')
        #get total size latest version
        self.assertEqual(my_new_bibdoc.get_total_size_latest_version(), 91750)
        #get latest version
        self.assertEqual(my_new_bibdoc.get_latest_version(), 3)
        #list latest files
        self.assertEqual(len(my_new_bibdoc.list_latest_files()), 1)
        self.assertEqual(my_new_bibdoc.list_latest_files()[0].get_version(), 3)
        #list version files
        self.assertEqual(len(my_new_bibdoc.list_version_files(1, list_hidden=True)), 1)
        #display
        value = my_new_bibdoc.display(version='', ln='en', display_hidden=True)
        self.assert_('>test add new file<' in value)
        #format already exist
        self.assertEqual(my_new_bibdoc.format_already_exists_p('.jpg'), True)
        #get file
        self.assertEqual(my_new_bibdoc.get_file('.jpg', version='1').get_version(), 1)
        #set description
        my_new_bibdoc.set_description('new description', '.jpg', version=1)
        #get description
        self.assertEqual(my_new_bibdoc.get_description('.jpg', version=1), 'new description')
        #set comment
        my_new_bibdoc.set_description('new comment', '.jpg', version=1)
        #get comment
        self.assertEqual(my_new_bibdoc.get_description('.jpg', version=1), 'new comment')
        #get history
        assert len(my_new_bibdoc.get_history()) > 0
        #check modification date
        self.assertEqual(my_new_bibdoc.get_file('.jpg', version=1).md, timestamp1)
        self.assertEqual(my_new_bibdoc.get_file('.jpg', version=2).md, timestamp2)
        assert my_new_bibdoc.get_file('.jpg', version=3).md > timestamp3
        #delete file
        my_new_bibdoc.delete_file('.jpg', 2)
        #list all files
        self.assertEqual(len(my_new_bibdoc.list_all_files()), 2)
        #delete file
        my_new_bibdoc.delete_file('.jpg', 3)
        #add new format
        timestamp4 = datetime(*(time.strptime("2012-11-10 09:08:07", "%Y-%m-%d %H:%M:%S")[:6]))
        my_new_bibdoc.add_file_new_format(CFG_PREFIX + '/lib/webtest/invenio/test.gif', version=None, description=None, comment=None, format=None, modification_date=timestamp4)
        self.assertEqual(len(my_new_bibdoc.list_all_files()), 2)
        #check modification time
        self.assertEqual(my_new_bibdoc.get_file('.jpg', version=1).md, timestamp1)
        self.assertEqual(my_new_bibdoc.get_file('.gif', version=1).md, timestamp4)
        #delete file
        my_new_bibdoc.delete_file('.jpg', 1)
        #delete file
        my_new_bibdoc.delete_file('.gif', 1)
        #empty bibdoc
        self.assertEqual(my_new_bibdoc.empty_p(), True)
        #hidden?
        self.assertEqual(my_new_bibdoc.hidden_p('.jpg', version=1), False)
        #hide
        my_new_bibdoc.set_flag('HIDDEN', '.jpg', version=1)
        #hidden?
        self.assertEqual(my_new_bibdoc.hidden_p('.jpg', version=1), True)
        #add and get icon
        my_new_bibdoc.add_icon( CFG_PREFIX + '/lib/webtest/invenio/icon-test.gif', modification_date=timestamp4)
        value =  my_bibrecdoc.list_bibdocs()[1]
        self.assertEqual(value.get_icon(), my_new_bibdoc.get_icon())
        #check modification time
        self.assertEqual(my_new_bibdoc.get_icon().md, timestamp4)
        #delete icon
        my_new_bibdoc.delete_icon()
        #get icon
        self.assertEqual(my_new_bibdoc.get_icon(), None)
        #delete
        my_new_bibdoc.delete()
        self.assertEqual(my_new_bibdoc.deleted_p(), True)
        #undelete
        my_new_bibdoc.undelete(previous_status='')
        #expunging
        my_new_bibdoc.expunge()
        my_bibrecdoc.build_bibdoc_list()
        self.failIf('new_name' in my_bibrecdoc.get_bibdoc_names())
        self.failUnless(my_bibrecdoc.get_bibdoc_names())

    def tearDown(self):
        my_bibrecdoc = BibRecDocs(2)
        #delete
        my_bibrecdoc.delete_bibdoc('img_test')
        my_bibrecdoc.delete_bibdoc('new_name')


class BibDocFilesTest(unittest.TestCase):
    """regression tests about BibDocFiles"""

    def test_BibDocFiles(self):
        """bibdocfile - BibDocFile functions """
        #add bibdoc
        my_bibrecdoc = BibRecDocs(2)
        timestamp = datetime(*(time.strptime("2010-09-08 07:06:05", "%Y-%m-%d %H:%M:%S")[:6]))
        my_bibrecdoc.add_new_file(CFG_PREFIX + '/lib/webtest/invenio/test.jpg', 'Main', 'img_test', False, 'test add new file', 'test', '.jpg', modification_date=timestamp)
        my_new_bibdoc = my_bibrecdoc.get_bibdoc("img_test")
        my_new_bibdocfile = my_new_bibdoc.list_all_files()[0]
        #get url
        self.assertEqual(my_new_bibdocfile.get_url(), CFG_SITE_URL + '/%s/2/files/img_test.jpg' % CFG_SITE_RECORD)
        #get type
        self.assertEqual(my_new_bibdocfile.get_type(), 'Main')
        #get path
        self.assert_(my_new_bibdocfile.get_path().startswith(CFG_BIBDOCFILE_FILEDIR))
        self.assert_(my_new_bibdocfile.get_path().endswith('/img_test.jpg;1'))
        #get bibdocid
        self.assertEqual(my_new_bibdocfile.get_bibdocid(), my_new_bibdoc.get_id())
        #get name
        self.assertEqual(my_new_bibdocfile.get_name() , 'img_test')
        #get full name
        self.assertEqual(my_new_bibdocfile.get_full_name() , 'img_test.jpg')
        #get full path
        self.assert_(my_new_bibdocfile.get_full_path().startswith(CFG_BIBDOCFILE_FILEDIR))
        self.assert_(my_new_bibdocfile.get_full_path().endswith('/img_test.jpg;1'))
        #get format
        self.assertEqual(my_new_bibdocfile.get_format(), '.jpg')
        #get version
        self.assertEqual(my_new_bibdocfile.get_version(), 1)
        #get description
        self.assertEqual(my_new_bibdocfile.get_description(), my_new_bibdoc.get_description('.jpg', version=1))
        #get comment
        self.assertEqual(my_new_bibdocfile.get_comment(), my_new_bibdoc.get_comment('.jpg', version=1))
        #get recid
        self.assertEqual(my_new_bibdocfile.get_recid(), 2)
        #get status
        self.assertEqual(my_new_bibdocfile.get_status(), '')
        #get size
        self.assertEqual(my_new_bibdocfile.get_size(), 91750)
        #get checksum
        self.assertEqual(my_new_bibdocfile.get_checksum(), '28ec893f9da735ad65de544f71d4ad76')
        #check
        self.assertEqual(my_new_bibdocfile.check(), True)
        #display
        value = my_new_bibdocfile.display(ln='en')
        assert 'files/img_test.jpg?version=1">' in value
        #hidden?
        self.assertEqual(my_new_bibdocfile.hidden_p(), False)
        #check modification date
        self.assertEqual(my_new_bibdocfile.md, timestamp)
        #delete
        my_new_bibdoc.delete()
        self.assertEqual(my_new_bibdoc.deleted_p(), True)

class CheckBibDocAuthorizationTest(unittest.TestCase):
    """Regression tests for check_bibdoc_authorization function."""
    def test_check_bibdoc_authorization(self):
        """bibdocfile - check_bibdoc_authorization function"""
        from invenio.webuser import collect_user_info, get_uid_from_email
        jekyll = collect_user_info(get_uid_from_email('jekyll@cds.cern.ch'))
        self.assertEqual(check_bibdoc_authorization(jekyll, 'role:thesesviewer'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))
        self.assertEqual(check_bibdoc_authorization(jekyll, 'role: thesesviewer'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))
        self.assertEqual(check_bibdoc_authorization(jekyll, 'role:  thesesviewer'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))
        self.assertEqual(check_bibdoc_authorization(jekyll, 'Role:  thesesviewer'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))
        self.assertEqual(check_bibdoc_authorization(jekyll, 'email: jekyll@cds.cern.ch'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))
        self.assertEqual(check_bibdoc_authorization(jekyll, 'email: jekyll@cds.cern.ch'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))

        juliet = collect_user_info(get_uid_from_email('juliet.capulet@cds.cern.ch'))
        self.assertEqual(check_bibdoc_authorization(juliet, 'restricted_picture'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))
        self.assertEqual(check_bibdoc_authorization(juliet, 'status: restricted_picture'), (0, CFG_WEBACCESS_WARNING_MSGS[0]))
        self.assertNotEqual(check_bibdoc_authorization(juliet, 'restricted_video')[0], 0)
        self.assertNotEqual(check_bibdoc_authorization(juliet, 'status: restricted_video')[0], 0)

class BibDocFileURLTest(unittest.TestCase):
    """Regression tests for bibdocfile_url_p function."""
    def test_bibdocfile_url_p(self):
        self.failUnless(bibdocfile_url_p(CFG_SITE_URL + '/%s/98/files/9709037.pdf' % CFG_SITE_RECORD))
        self.failUnless(bibdocfile_url_p(CFG_SITE_URL + '/%s/098/files/9709037.pdf' % CFG_SITE_RECORD))

TEST_SUITE = make_test_suite(BibRecDocsTest,
                             BibDocsTest,
                             BibDocFilesTest,
                             CheckBibDocAuthorizationTest,
                             BibDocFileURLTest,
                             BibDocFsInfoTest,
                             BibDocFileGuessFormat)
if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
