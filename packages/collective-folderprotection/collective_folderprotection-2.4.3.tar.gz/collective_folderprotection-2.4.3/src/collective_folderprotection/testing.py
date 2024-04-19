# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

try:
    from plone.testing.zope import WSGI_SERVER_FIXTURE
except ImportError:
    from plone.testing.z2 import ZSERVER_FIXTURE as WSGI_SERVER_FIXTURE

class CollectivefolderprotectionLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective_folderprotection

        self.loadZCML(package=collective_folderprotection)
        self.loadZCML(package=collective_folderprotection, name="overrides.zcml")

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, "collective_folderprotection:test_fixture")

        # Create a manager user
        pas = portal["acl_users"]
        pas.source_users.addUser("manager", "manager", "manager")
        pas.portal_role_manager.doAssignRoleToPrincipal("manager", "Manager")

        # Create a contributor user
        pas = portal["acl_users"]
        pas.source_users.addUser("contributor", "contributor", "contributor")
        pas.portal_role_manager.doAssignRoleToPrincipal("contributor", "Contributor")


FIXTURE = CollectivefolderprotectionLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="collective_folderprotection:Integration"
)
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="collective_folderprotection:Functional"
)
ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, WSGI_SERVER_FIXTURE),
    name="collective_folderprotection:Acceptance",
)