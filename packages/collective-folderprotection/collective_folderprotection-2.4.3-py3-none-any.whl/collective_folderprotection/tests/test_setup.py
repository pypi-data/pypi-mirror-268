# -*- coding: utf-8 -*-
import unittest

from plone.browserlayer.utils import registered_layers

from collective_folderprotection.testing import INTEGRATION_TESTING


class TestSetup(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]

    def test_addon_layer(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue(
            "IFolderProtectLayer" in layers, "add-on layer was not installed"
        )
