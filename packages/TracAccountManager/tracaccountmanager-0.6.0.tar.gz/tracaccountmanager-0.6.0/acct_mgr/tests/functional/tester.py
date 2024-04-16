# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 Matthew Good <trac@matt-good.net>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: Pedro Algarvio <ufs@ufsoft.org>

import re

from . import tc


internal_error = 'Trac detected an internal error:'


class FunctionalTester(object):

    url = None

    def __init__(self, url):
        self.url = url
        self.go_to_front()

    def go_to_url(self, url):
        tc.go(url)
        tc.url(re.escape(url))
        tc.notfind(internal_error)

    def go_to_front(self):
        """Go to the Trac front page"""
        self.go_to_url(self.url)

    def login(self, username, passwd=None):
        """Override FunctionalTester.login, we're not using Basic
        Authentication."""
        if not passwd:
            passwd = username
        login_form_name = 'acctmgr_loginform'
        self.go_to_front()
        tc.find('Login')
        tc.follow('Login')
        tc.formvalue(login_form_name, 'user', username)
        tc.formvalue(login_form_name, 'password', passwd)
        tc.submit()
        tc.find("logged in as <span[^>]+>%s</span>" % username)
        tc.find("Logout")
        tc.url(self.url)
        tc.notfind(internal_error)

    def logout(self):
        tc.formvalue('logout', 'logout', 'Logout')
        tc.submit()
        tc.notfind(internal_error)
        tc.notfind('logged in as')

    def register(self, username, email='', passwd=None):
        """Allow user registration."""
        if not passwd:
            passwd = username
        reg_form_name = 'acctmgr_registerform'
        tc.find("Register")
        tc.follow("Register")
        tc.formvalue(reg_form_name, 'user', username)
        tc.formvalue(reg_form_name, 'password', passwd)
        tc.formvalue(reg_form_name, 'password_confirm', passwd)
        tc.formvalue(reg_form_name, 'email', email)
        tc.submit()
        tc.notfind("The passwords must match.")
        tc.notfind(internal_error)
        tc.find(r'Your username has been successfully registered but your '
                r'account still requires activation\. Please login as user '
                r'<strong>{0}</strong>, and follow the instructions\.'
                .format(re.escape(username)))
        tc.url('/login$')
