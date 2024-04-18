# -*- coding: utf-8 -*-
import unittest

from collective_folderprotection.exceptions import DeleteProtectionException
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from collective_folderprotection.behaviors.interfaces import IDeleteProtected
from collective_folderprotection.testing import INTEGRATION_TESTING


class TestDelProtect(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]

        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        # Create a folderish protected
        self.portal.invokeFactory("folderish_protected", "protected")
        self.protected = self.portal["protected"]
        adapter = IDeleteProtected(self.protected)
        adapter.delete_protection = True
        self.protected.invokeFactory("Document", "internal")

        # Create another folderish protected, with protection disabled
        self.portal.invokeFactory("folderish_protected", "protected-disabled")
        self.protected_disabled = self.portal["protected-disabled"]
        adapter = IDeleteProtected(self.protected_disabled)
        adapter.delete_protection = False
        self.protected_disabled.invokeFactory("Document", "internal")

        # And a folderish unprotected
        self.portal.invokeFactory("folderish_not_protected", "not-protected")
        self.not_protected = self.portal["not-protected"]
        self.not_protected.invokeFactory("Document", "internal")

    def test_unable_to_remove_protected(self):
        self.assertRaises(DeleteProtectionException, self.protected.manage_delObjects, "internal")
        self.assertIn("internal", self.protected)
        self.assertRaises(DeleteProtectionException, self.portal.manage_delObjects, "protected")
        self.assertIn("protected", self.portal)

    def test_able_to_remove_unprotected(self):
        self.not_protected.manage_delObjects("internal")
        self.assertNotIn("internal", self.not_protected)
        self.portal.manage_delObjects("not-protected")
        self.assertNotIn("not-protected", self.portal)

    def test_able_to_remove_disabled(self):
        self.protected_disabled.manage_delObjects("internal")
        self.assertNotIn("internal", self.protected_disabled)
        self.portal.manage_delObjects("protected-disabled")
        self.assertNotIn("protected-disabled", self.portal)
