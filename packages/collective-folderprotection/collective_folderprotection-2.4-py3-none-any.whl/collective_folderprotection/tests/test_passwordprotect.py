# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import unittest

from zope.annotation import IAnnotations

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from plone.dexterity.utils import createContentInContainer

from collective_folderprotection.behaviors.interfaces import IPasswordProtected

from collective_folderprotection.config import HASHES_ANNOTATION_KEY
from collective_folderprotection.config import HASH_COOKIE_KEY

from collective_folderprotection.testing import INTEGRATION_TESTING


class TestPasswordProtect(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]

        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        # Create a folderish protected
        self.folder = createContentInContainer(
            self.portal, "folderish_protected", title="Protected"
        )

    def test_not_enabled_by_default(self):
        passwordprotect = IPasswordProtected(self.folder)
        self.assertFalse(passwordprotect.is_password_protected())

    def test_not_allowed_if_cookie_not_present(self):
        passwordprotect = IPasswordProtected(self.folder)
        self.assertFalse(passwordprotect.allowed_to_access())

    def test_not_allowed_if_expired_hash(self):
        # Let's create a hash and put it in the cookie and the annotation
        pw_hash = "this-is-the-hash"
        ann = IAnnotations(self.folder)
        hashes = ann.get(HASHES_ANNOTATION_KEY, {})

        # We will put the time 1 day in the past, so it would be expired
        hashes[pw_hash] = datetime.now() - timedelta(days=1)

        ann[HASHES_ANNOTATION_KEY] = hashes

        self.request.response.setCookie(HASH_COOKIE_KEY, pw_hash)

        passwordprotect = IPasswordProtected(self.folder)
        self.assertFalse(passwordprotect.allowed_to_access())

    def test_allowed_if_valid_hash(self):
        # Let's create a hash and put it in the cookie and the annotation
        pw_hash = "this-is-the-hash"
        ann = IAnnotations(self.folder)
        hashes = ann.get(HASHES_ANNOTATION_KEY, {})

        # We will put the time 10 days in the future, so it would be valid
        hashes[pw_hash] = datetime.now() + timedelta(days=10)

        ann[HASHES_ANNOTATION_KEY] = hashes

        self.request.cookies[HASH_COOKIE_KEY] = pw_hash

        passwordprotect = IPasswordProtected(self.folder)
        self.assertTrue(passwordprotect.allowed_to_access())

    def test_assign_password(self):
        pw = "this-is-the-pw"
        passwordprotect = IPasswordProtected(self.folder)
        self.assertFalse(passwordprotect.is_password_protected())
        passwordprotect.assign_password(pw)
        self.assertTrue(passwordprotect.is_password_protected())

    def test_remove_password(self):
        pw = "this-is-the-pw"
        passwordprotect = IPasswordProtected(self.folder)
        passwordprotect.assign_password(pw)
        self.assertTrue(passwordprotect.is_password_protected())
        passwordprotect.remove_password()
        self.assertFalse(passwordprotect.is_password_protected())

    def test_set_password_on_creation(self):
        pw = "this-is-the-pw"

        protected = createContentInContainer(
            self.portal,
            "folderish_protected",
            title="Protected",
            passw_hash=pw,
        )

        passwordprotect = IPasswordProtected(protected)
        self.assertTrue(passwordprotect.is_password_protected())
