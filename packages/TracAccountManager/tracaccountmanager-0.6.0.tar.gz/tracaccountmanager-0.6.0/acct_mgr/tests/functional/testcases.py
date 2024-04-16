# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 Matthew Good <trac@matt-good.net>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: Pedro Algarvio <ufs@ufsoft.org>

import email
import re
import unittest

from . import FunctionalTestSuite, FunctionalTestCaseSetup, tc


def parse_smtp_message(data):
    assert data is not None
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    message = email.message_from_string(data)
    headers = dict(message.items())
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                break
        else:
            return headers, u''
    else:
        part = message
    payload = part.get_payload(decode=True)
    encoding = part.get_content_charset()
    body = payload.decode(encoding)
    return headers, body


class TestInitialSetup(FunctionalTestCaseSetup):
    def runTest(self):
        """initial Trac authentication setup"""
        tc.find('Login')
        tc.follow('Login')
        tc.find(r'logged in as <span[^>]+>setup</span>')
        # step 1
        tc.find(r'>\s*Step 1: Authentication Options\s*</legend>')
        tc.formvalue('cfg_wiz', 'acctmgr_login', '1')
        tc.formvalue('cfg_wiz', 'next', '1')
        tc.submit()
        # step 2
        tc.find(r'>\s*Step 2: Password Store\s*</legend>')
        tc.formvalue('cfg_wiz', 'init_store', 'file')
        tc.formvalue('cfg_wiz', 'init_store_file', 'htpasswd')
        tc.formvalue('cfg_wiz', 'next', '1')
        tc.submit()
        # step 3
        tc.find(r'>\s*Step 3: Password Policy\s*</legend>')
        tc.formvalue('cfg_wiz', 'next', '1')
        tc.submit()
        # step 4
        tc.find(r'>\s*Step 4: Account Policy\s*</legend>')
        tc.formvalue('cfg_wiz', 'acctmgr_register', 'true')
        tc.formvalue('cfg_wiz', 'BasicCheck', '1')
        tc.formvalue('cfg_wiz', 'EmailCheck', '2')
        tc.formvalue('cfg_wiz', 'RegExpCheck', '3')
        tc.formvalue('cfg_wiz', 'RegExpCheck.username_regexp',
                     '^[-A-Za-z0-9._]{3,}$')
        tc.formvalue('cfg_wiz', 'UsernamePermCheck', '4')
        tc.formvalue('cfg_wiz', 'next', '1')
        tc.submit()
        # step 5
        tc.find(r'>\s*Step 5: Account Guard\s*</legend>')
        tc.formvalue('cfg_wiz', 'next', '1')
        tc.submit()
        # step 6 - admin
        tc.find(r'>\s*Step 6: Initialization\s*</legend>')
        tc.find(r'>\s*Add Admin Account:\s*</legend>')
        tc.formvalue('cfg_wiz', 'username', 'admin')
        tc.formvalue('cfg_wiz', 'password', 'admin')
        tc.formvalue('cfg_wiz', 'password_confirm', 'admin')
        tc.formvalue('cfg_wiz', 'add', '1')
        tc.submit()
        # step 6 - admin created
        tc.find(r'\bAccount <[a-z]+>admin</[a-z]+> created\.')
        tc.find(r'>\s*Step 6: Initialization\s*</legend>')
        #tc.notfind(r'>\s*Add Admin Account:\s*</legend>')
        tc.formvalue('cfg_wiz', 'save', '1')
        tc.submit()
        # wizard finished
        tc.url(re.escape(self._tester.url))
        tc.find(r'>WikiStart</a>')
        tc.find(r'logged in as <span[^>]+>setup</span>')
        self._tester.logout()


class TestFormLoginAdmin(FunctionalTestCaseSetup):
    def runTest(self):
        """Login with test user 'admin'"""
        self._tester.login('admin')
        self._tester.logout()


class TestAdminFormAddUser(FunctionalTestCaseSetup):
    def runTest(self):
        self._tester.login('admin')
        tc.find('Admin')
        tc.follow('Admin')
        tc.find('Users')
        tc.follow('Users')
        tc.find(r'<legend>\s*Add New Account:\s*</legend>')
        form = 'account-editor'
        tc.formvalue(form, 'username', 'user')
        tc.formvalue(form, 'password', 'user')
        tc.formvalue(form, 'password_confirm', 'user')
        tc.formvalue(form, 'email', 'user@trac.example.org')
        tc.formvalue(form, 'email_approved', [])
        tc.submit()
        tc.find(r'\bAccount <[a-z]+>user</[a-z]+> created\.')
        tc.find('Users')
        tc.follow('Users')
        tc.find(r'<a\s*[^>]*>user</a>')
        self._tester.logout()


class TestFormLoginUser(FunctionalTestCaseSetup):
    def runTest(self):
        """Login with test user 'user'"""
        self._tester.login('user')
        self._tester.logout()


class TestRegisterNewUser(FunctionalTestCaseSetup):
    def runTest(self):
        """Register 'testuser'"""
        self._tester.register('testuser', 'testuser@trac.example.org')


class TestLoginNewUser(FunctionalTestCaseSetup):
    def runTest(self):
        """Login just registered 'testuser'"""
        self._tester.login('testuser')
        self._tester.logout()


class TestFailRegisterPasswdConfirmNotPassed(FunctionalTestCaseSetup):
    def runTest(self):
        """Fail if no password confirmation is passed"""
        reg_form_name = 'acctmgr_registerform'
        username = 'testuser1'
        tc.find("Register")
        tc.follow("Register")
        tc.formvalue(reg_form_name, 'user', username)
        tc.formvalue(reg_form_name, 'password', username)
        tc.submit()
        tc.find(r'The passwords must match\.')


class TestFailRegisterDuplicateUsername(FunctionalTestCaseSetup):
    def runTest(self):
        """Fail if username exists"""
        reg_form_name = 'acctmgr_registerform'
        username = 'testuser'
        tc.find("Register")
        tc.follow("Register")
        tc.formvalue(reg_form_name, 'user', username)
        tc.formvalue(reg_form_name, 'password', username)
        tc.formvalue(reg_form_name, 'password_confirm', username)
        tc.submit()
        tc.find("Another account or group already exists")


class TestNewAccountNotification(FunctionalTestCaseSetup):
    def runTest(self):
        """Send out notification on new account registrations"""
        tc.notfind('Logout')
        address_to_notify = 'admin@testenv%s.tld' % self._testenv.port
        new_username = 'foo'
        new_username_email = "foo@%s" % address_to_notify.split('@')[1]

        env = self._testenv.get_trac_environment()
        env.config.set('account-manager', 'account_changes_notify_addresses',
                       address_to_notify)
        env.config.set('account-manager', 'notify_actions', 'new,change,delete')
        env.config.set('account-manager', 'force_passwd_change', 'true')
        env.config.save()
        self._tester.register(new_username, new_username_email)

        headers, body = parse_smtp_message(self._smtpd.get_message())

        self.assertEqual(self._smtpd.get_recipients(), [address_to_notify])
        self.assertEqual(headers['Subject'],
                         '[testenv%d] Account created: %s' %
                         (self._testenv.port, new_username))
        self.assertEqual(headers['X-URL'], self._testenv.url)


class TestNewAccountEmailVerification(FunctionalTestCaseSetup):
    def runTest(self):
        """User is shown info that he needs to verify his address"""
        user_email = "foo@testenv%s.tld" % self._testenv.port
        self._tester.login("foo")

        tc.find(r'An email has been sent to &lt;%s&gt; with a token to '
                r'<a href="/trac/verify_email">verify your new email address'
                r'</a>' % re.escape(user_email))
        self._tester.go_to_front()
        tc.find(r'<strong>Warning:</strong>\s*'
                r'Your permissions have been limited until you '
                r'<a href="/trac/verify_email">verify your email address</a>')


class VerifyNewAccountEmailAddress(FunctionalTestCaseSetup):
    def runTest(self):
        """User confirms his address with mailed token"""
        headers, body = parse_smtp_message(self._smtpd.get_message())
        blines = body.splitlines()
        token = [l.split() for l in blines if 'Verification Token' in l][0][-1]
        warning = (r'<strong>Warning:</strong>\s*'
                   r'Your permissions have been limited until you <a '
                   r'href="/trac/verify_email">verify your email address</a>')

        tc.find('Logout') # User is logged in from previous test
        self._tester.go_to_front()
        tc.find(warning)
        tc.go(self._testenv.url + '/verify_email')

        reg_form_name = 'acctmgr_verify_email'
        tc.formvalue(reg_form_name, 'token', token)
        tc.submit('verify')

        tc.notfind(warning)
        tc.find('Thank you for verifying your email address')
        self._tester.go_to_front()


class PasswdResetsNotifiesAdmin(FunctionalTestCaseSetup):
    def runTest(self):
        """User password resets notifies admin by mail"""
        self._tester.logout()
        self._smtpd.full_reset() # Clean all previous sent emails
        tc.notfind('Logout')
        # Goto Login
        tc.find("Login")
        tc.follow("Login")
        # Do we have the Forgot passwd link
        tc.find('Forgot your password?')
        tc.follow('Forgot your password?')

        username = "foo"
        email_addr = "foo@testenv%s.tld" % self._testenv.port

        reset_form_name = 'acctmgr_passwd_reset'
        tc.formvalue(reset_form_name, 'username', username)
        tc.formvalue(reset_form_name, 'email', email_addr)
        tc.submit()

        headers, body = parse_smtp_message(
            self._smtpd.get_message('admin@testenv%s.tld' % self._testenv.port))
        self.assertEqual(headers['Subject'],
                         '[testenv%s] Account password reset: %s' %
                         (self._testenv.port, username))
        self.assertEqual(headers['X-URL'], self._testenv.url)


class PasswdResetsNotifiesUser(FunctionalTestCaseSetup):
    def runTest(self):
        """Password reset sends new password to user by mail"""
        username = "foo"
        email_addr = "foo@testenv%s.tld" % self._testenv.port
        headers, self.body = parse_smtp_message(self._smtpd.get_message(email_addr))
        self.assertEqual(headers['Subject'],
                         '[testenv%d] Account password reset: %s' %
                         (self._testenv.port, username))


class UserLoginWithMailedPassword(PasswdResetsNotifiesUser):
    def runTest(self):
        """User is able to login with the new password"""
        PasswdResetsNotifiesUser.runTest(self)
        # Does it include a new password
        body = self.body
        username = 'foo'
        self.assertTrue('Username: %s' % username in body)
        self.assertTrue('Password:' in body)

        passwd = [l.split(':')[1].strip() for l in
                  body.splitlines() if 'Password:' in l][0]

        self._tester.login(username, passwd)


class UserIsForcedToChangePassword(FunctionalTestCaseSetup):
    def runTest(self):
        """User is forced to change password after resets"""
        tc.find('Logout')
        tc.find(r'You are required to change password because of a recent '
                r'password change request\.')


class UserCantBrowseUntilPasswdChange(PasswdResetsNotifiesUser):
    def runTest(self):
        """User can't navigate out of '/prefs/account' before password change"""
        PasswdResetsNotifiesUser.runTest(self)
        tc.find('Logout')
        forced_passwd_change_url = '^%s/prefs/account$' % self._tester.url
        tc.follow('Roadmap')
        tc.url(forced_passwd_change_url)
        tc.follow('View Tickets')
        tc.url(forced_passwd_change_url)
        tc.follow('New Ticket')
        tc.url(forced_passwd_change_url)

        # Now, let's change his password
        body = self.body
        passwd = [l.split(':')[1].strip() for l in
                  body.splitlines() if 'Password:' in l][0]
        username = 'foo'
        change_passwd_form = 'userprefs'
        tc.formvalue(change_passwd_form, 'old_password', passwd)
        tc.formvalue(change_passwd_form, 'password', username)
        tc.formvalue(change_passwd_form, 'password_confirm', username)
        tc.submit()

        tc.notfind("You are required to change password because of a recent "
                   "password change request")
        tc.find(r'Thank you for taking the time to update your password\.')

        # We can now browse away from /prefs/accounts
        tc.follow('Roadmap')
        tc.url(self._tester.url + '/roadmap')
        # Clear the mailstore
        self._smtpd.full_reset()


class DeleteAccountNotifiesAdmin(FunctionalTestCaseSetup):
    def runTest(self):
        """Delete account notifies admin"""
        tc.find("Logout") # We're logged-in from previous post
        tc.follow("Preferences")
        tc.follow("Account")
        tc.url(self._testenv.url + '/prefs/account')

        delete_account_form_name = 'acctmgr_delete_account'
        tc.formvalue(delete_account_form_name, 'password', 'foo')
        tc.submit()
        tc.find("Login") # We're logged out when we delete our account
        headers, _ = parse_smtp_message(self._smtpd.get_message())
        self.assertEqual(headers['Subject'],
                         '[testenv%d] Account deleted: %s' %
                         (self._testenv.port, 'foo'))


class UserNoLongerLogins(FunctionalTestCaseSetup):
    def runTest(self):
        """Deleted user can't login"""
        tc.follow('Login')
        login_form_name = 'acctmgr_loginform'
        tc.formvalue(login_form_name, 'user', 'foo')
        tc.formvalue(login_form_name, 'password', 'foo')
        tc.submit()
        tc.find("Invalid username or password")
        tc.notfind('Logout')


class UserIsAbleToRegisterWithSameUserName(FunctionalTestCaseSetup):
    def runTest(self):
        """Register with deleted username (session and session_attributes clean)"""
        self._tester.register('foo', 'foo@trac.example.org')
        self._tester.login('foo')
        self._tester.logout()
        self._smtpd.full_reset()


class NoEmailVerificationForAnonymousUsers(FunctionalTestCaseSetup):
    def runTest(self):
        """Anonymous users don't get their email address verified"""
        tc.find("Login")
        tc.follow("Preferences")
        form_name = 'userprefs'
        email_address = 'anonyous.user@fakedomain.tld'
        tc.formvalue(form_name, 'email', email_address)
        tc.submit()
        tc.notfind(r'<strong>Notice:</strong>\s*<span>An email has been sent '
                   r'to {0} with a token to <a href="/verify_email">verify '
                   r'your new email address</a></span>'
                   .format(re.escape(email_address)))
        self._tester.go_to_front()
        tc.notfind(r'<strong>Warning:</strong>\s*<span>Your permissions have '
                   r'been limited until you <a href="/verify_email">verify '
                   r'your email address</a></span>')


def test_suite():
    suite = FunctionalTestSuite()
    suite.addTest(TestInitialSetup())
    suite.addTest(TestFormLoginAdmin())
    suite.addTest(TestAdminFormAddUser())
    suite.addTest(TestFormLoginUser())
    suite.addTest(TestRegisterNewUser())
    suite.addTest(TestLoginNewUser())
    suite.addTest(TestFailRegisterPasswdConfirmNotPassed())
    suite.addTest(TestFailRegisterDuplicateUsername())
    suite.addTest(TestNewAccountNotification())
    suite.addTest(TestNewAccountEmailVerification())
    suite.addTest(VerifyNewAccountEmailAddress())
    suite.addTest(PasswdResetsNotifiesAdmin())
    suite.addTest(PasswdResetsNotifiesUser())
    suite.addTest(UserLoginWithMailedPassword())
    suite.addTest(UserIsForcedToChangePassword())
    suite.addTest(UserCantBrowseUntilPasswdChange())
    suite.addTest(DeleteAccountNotifiesAdmin())
    suite.addTest(UserNoLongerLogins())
    suite.addTest(UserIsAbleToRegisterWithSameUserName())
    suite.addTest(NoEmailVerificationForAnonymousUsers())
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
