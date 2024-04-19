# -*- coding: utf-8 -*-
import unittest

from collective_folderprotection.exceptions import RenameProtectionException
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from collective_folderprotection.behaviors.interfaces import IRenameProtected
from collective_folderprotection.testing import INTEGRATION_TESTING


class TestRenameProtect(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]

        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        # Create a folderish protected
        self.portal.invokeFactory("folderish_protected", "protected")
        self.protected = self.portal["protected"]
        adapter = IRenameProtected(self.protected)
        adapter.rename_protection = True
        self.protected.invokeFactory("Document", "internal")

        # Create another folderish protected, with protection disabled
        self.portal.invokeFactory("folderish_protected", "protected-disabled")
        self.protected_disabled = self.portal["protected-disabled"]
        adapter = IRenameProtected(self.protected_disabled)
        adapter.rename_protection = False
        self.protected_disabled.invokeFactory("Document", "internal")

        # And a folderish unprotected
        self.portal.invokeFactory("folderish_not_protected", "not-protected")
        self.not_protected = self.portal["not-protected"]
        self.not_protected.invokeFactory("Document", "internal")

    def test_unable_to_rename_protected(self):
        self.assertRaises(
            RenameProtectionException,
            self.protected.manage_renameObjects,
            ["internal"],
            ["new-internal"],
        )
        self.assertIn("internal", self.protected)
        self.assertNotIn("new-internal", self.protected)
        self.assertRaises(
            RenameProtectionException,
            self.portal.manage_renameObjects,
            ["protected"],
            ["new-protected"],
        )
        self.assertIn("protected", self.portal)
        self.assertNotIn("new-protected", self.portal)

    def test_able_to_rename_unprotected(self):
        self.not_protected.manage_renameObjects(["internal"], ["new-internal"])
        self.assertNotIn("internal", self.not_protected)
        self.assertIn("new-internal", self.not_protected)
        self.portal.manage_renameObjects(["not-protected"], ["new-not-protected"])
        self.assertNotIn("not-protected", self.portal)
        self.assertIn("new-not-protected", self.portal)

    def test_able_to_rename_disabled(self):
        self.protected_disabled.manage_renameObjects(["internal"], ["new-internal"])
        self.assertNotIn("internal", self.protected_disabled)
        self.assertIn("new-internal", self.protected_disabled)
        self.portal.manage_renameObjects(
            ["protected-disabled"], ["new-protected-disabled"]
        )
        self.assertNotIn("protected-disabled", self.portal)
        self.assertIn("new-protected-disabled", self.portal)
