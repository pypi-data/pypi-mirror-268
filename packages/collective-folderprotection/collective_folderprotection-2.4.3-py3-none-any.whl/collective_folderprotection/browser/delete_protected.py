# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from collective_folderprotection import _
from collective_folderprotection.behaviors.interfaces import IDeleteProtected
from plone.app.content.browser.contents.delete import (
    DeleteActionView as BaseDeleteActionView,
)
from plone.app.uuid.utils import uuidToCatalogBrain
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory
from Products.Five import BrowserView
from zope.component import getMultiAdapter
from zope.component.hooks import getSite

import json


FOLDER_PROTECTED_TEMPLATE = """
<h2>This folder is protected</h2>
<div id="content-core">
<p>Items inside this folder are protected against being deleted.</p>
</div>
"""


class DeleteActionView(BaseDeleteActionView):
    def __call__(self, keep_selection_order=False):
        self.protect()
        self.errors = list()
        if self.request.form.get("render") == "yes":
            confirm_view = getMultiAdapter(
                (getSite(), self.request), name="delete_confirmation_info"
            )
            selection = self.get_selection()
            self.request.response.setHeader(
                "Content-Type", "application/json; charset=utf-8"
            )
            # Check the current folder allows to remove items
            adapter = IDeleteProtected(self.context, None)
            if adapter:
                if adapter.delete_protection:
                    self.errors.append(
                        _(
                            "This folder is protected against deleting "
                            "items inside of it."
                        )
                    )
                    return json.dumps({"html": FOLDER_PROTECTED_TEMPLATE})

            catalog = getToolByName(self.context, "portal_catalog")
            brains = catalog(UID=selection, show_inactive=True)
            items = [i.getObject() for i in brains]
            self.request.response.setHeader(
                "Content-Type", "application/json; charset=utf-8"
            )
            return json.dumps({"html": confirm_view(items)})
        else:
            context = aq_inner(self.context)
            selection = self.get_selection()

            parts = str(self.request.form.get("folder", "").lstrip("/")).split("/")
            if parts:
                parent = self.site.unrestrictedTraverse("/".join(parts[:-1]))
                self.dest = parent.restrictedTraverse(parts[-1])

            # Check the current folder allows to remove items
            adapter = IDeleteProtected(self.context, None)
            if adapter:
                if adapter.delete_protection:
                    self.errors.append(
                        _(
                            "This folder is protected against deleting "
                            "items inside of it."
                        )
                    )
                    return self.message(list())

            self.catalog = getToolByName(context, "portal_catalog")
            self.mtool = getToolByName(self.context, "portal_membership")

            brains = []
            if keep_selection_order:
                brains = [uuidToCatalogBrain(uid) for uid in selection]
            else:
                brains = self.catalog(UID=selection, show_inactive=True)

            for brain in brains:
                if not brain:
                    continue

                # remove everyone so we know if we missed any
                selection.remove(brain.UID)
                obj = brain.getObject()

                # Check if item is allowed to be removed
                adapter = IDeleteProtected(obj, None)
                if adapter:
                    if adapter.delete_protection:
                        msgid = _(
                            "protected_item_delete",
                            default=(
                                "Item ${title} is protected against " "being deleted"
                            ),
                            mapping={"title": obj.Title()},
                        )
                        self.errors.append(msgid)
                        return self.message(list())

                if self.required_obj_permission and not self.mtool.checkPermission(
                    self.required_obj_permission, obj
                ):
                    self.errors.append(
                        PloneMessageFactory(
                            'Permission denied for "${title}"',
                            mapping={"title": self.objectTitle(obj)},
                        )
                    )
                    continue
                self.action(obj)

            self.finish()
            return self.message(selection)


class DeleteProtectedView(BrowserView):

    def __call__(self):
        # XXX: We cannot simply redirect from here
        # See more: ZPublisher/WSGIPublisher.py(141)_exc_view_created_response()
        self.request.response.setStatus(200)
        return self.__parent__()
