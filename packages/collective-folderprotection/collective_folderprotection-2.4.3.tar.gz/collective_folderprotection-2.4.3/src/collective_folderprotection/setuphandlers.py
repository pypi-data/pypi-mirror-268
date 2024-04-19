# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective_folderprotection:uninstall",
        ]


def post_install(context):
    new_val = list()
    to_add = [
        "DeleteProtectionException",
        "PasswordProtectedUnauthorized",
        "RenameProtectionException",
    ]
    err_log = context.error_log
    for exc in err_log._ignored_exceptions:
        new_val.append(exc)

    for exc in to_add:
        if exc not in new_val:
            new_val.append(exc)

    err_log._ignored_exceptions = tuple(new_val)


def post_uninstall(context):
    new_val = list()
    to_remove = (
        "DeleteProtectionException",
        "PasswordProtectedUnauthorized",
        "RenameProtectionException",
    )
    err_log = context.error_log
    for exc in err_log._ignored_exceptions:
        if exc not in to_remove:
            new_val.append(exc)

    err_log._ignored_exceptions = tuple(new_val)
