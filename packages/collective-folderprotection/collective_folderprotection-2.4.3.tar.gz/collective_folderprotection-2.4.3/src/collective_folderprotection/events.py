# -*- coding: utf-8 -*-

from Acquisition import aq_parent
from collective_folderprotection import _
from collective_folderprotection.behaviors.interfaces import IDeleteProtected
from collective_folderprotection.behaviors.interfaces import IPasswordProtected
from collective_folderprotection.behaviors.interfaces import IRenameProtected
from collective_folderprotection.exceptions import (
    PasswordProtectedUnauthorized,
    DeleteProtectionException,
    RenameProtectionException,
)

from OFS.event import ObjectWillBeMovedEvent
from Products.statusmessages.interfaces import IStatusMessage
from plone import api


def checkPassword(portal, request):
    portal_path = "/".join(portal.getPhysicalPath())
    # We get the full path
    if "VIRTUAL_URL_PARTS" in request:
        full_path = request.get("VIRTUAL_URL_PARTS")[1]
    else:
        full_path = request.get("PATH_INFO")

    if full_path.startswith(portal_path):
        # just strip the portal_path from the full_path and the '/'
        full_path = full_path[len(portal_path) + 1 :]
    ob = portal
    # Now iterate over each one
    for name in full_path.split("/"):
        authorized = False
        obj_is_protected = False
        try:
            ob = ob.unrestrictedTraverse(name)
        except Exception:
            # This path is not traversable or doesn't exist, just ignore
            break
        try:
            passwordprotected = IPasswordProtected(ob)
            obj_is_protected = True

        except TypeError:
            pass

        if obj_is_protected:
            # We are at a content type that is password protected, first check
            # if the password is actually set for this content, and then
            # see if we are not actually at the passwordprompt view
            if (
                passwordprotected.is_password_protected()
                and "passwordprompt" not in full_path
            ):
                # We are not at the passwordprotected prompt, so we now check
                # if the current user is not Manager or the Owner
                pm = portal.portal_membership
                roles = pm.getAuthenticatedMember().getRolesInContext(ob)
                if "Manager" in roles or "Owner" in roles:
                    # This user is the Owner or a Manager, so we just authorize
                    # it
                    authorized = True

                if not (authorized or passwordprotected.allowed_to_access()):
                    # User is not authorized to access this resource
                    raise PasswordProtectedUnauthorized(name=name)

    return None


def insertCheckPasswordHook(portal, event):
    """Add this hook to the post_traversal so we can check if some object
    during the traversal needs a password
    """
    try:
        event.request.post_traverse(checkPassword, (portal, event.request))
    except RuntimeError:
        pass


def preventRemove(object, event):
    # First check if the object itself is protected
    adapter = IDeleteProtected(object, None)
    request = api.env.getRequest()
    if adapter:
        if adapter.delete_protection:
            if request:
                messages = IStatusMessage(request)
                messages.add(
                    _("Item cannot be deleted because it is protected."), type="error"
                )
            raise DeleteProtectionException()
    else:
        # Check with the parent
        parent = aq_parent(object)
        adapter = IDeleteProtected(parent, None)
        if adapter:
            if adapter.delete_protection:
                if request:
                    messages = IStatusMessage(request)
                    messages.add(
                        _("Item cannot be deleted because its parent folder is protected."),
                        type="error",
                    )
                raise DeleteProtectionException()


def preventRename(object, event):
    # ObjectWillBeMovedEvent is a base class of ObjectWillBeAddedEvent, so we
    # use type() to be sure we only check ObjectWillBeMovedEvent
    if type(event) is not ObjectWillBeMovedEvent:
        return
    # Only check for items that remain in the same folder, with different
    # name (ie. renamed)
    request = api.env.getRequest()
    if event.oldParent is event.newParent and event.oldName != event.newName:
        # First check if the object itself is protected
        adapter = IRenameProtected(object, None)
        if adapter:
            if adapter.rename_protection:
                if request:
                    messages = IStatusMessage(request)
                    messages.add(
                        _("This item is protected against being renamed"), type="error"
                    )
                raise RenameProtectionException()
        else:
            # Check with the parent
            parent = aq_parent(object)
            adapter = IRenameProtected(parent, None)
            if adapter:
                if adapter.rename_protection:
                    if request:
                        messages = IStatusMessage(request)
                        messages.add(
                            _(
                                "This folder is protected against renaming "
                                "items inside of it."
                            ),
                            type="error",
                        )
                    raise RenameProtectionException()
