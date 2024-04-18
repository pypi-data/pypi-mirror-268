# -*- coding: utf-8 -*-

from .. import _
from ..behaviors.interfaces import IRenameProtected
from Acquisition import aq_inner
from Acquisition import aq_parent
from plone.app.content.browser.actions import RenameForm as BaseRenameForm
from plone.app.content.browser.contents.rename import (
    RenameActionView as BaseRenameActionView,
)
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
try:
    from plone.base import PloneMessageFactory
except:
    from Products.CMFPlone import PloneMessageFactory


class RenameForm(BaseRenameForm):
    @button.buttonAndHandler(PloneMessageFactory("Rename"), name="Rename")
    def handle_rename(self, action):
        # First check if the object itself is protected
        protected = False
        adapter = IRenameProtected(self.context, None)
        if adapter:
            if adapter.rename_protection:
                IStatusMessage(self.request).add(
                    _("This item is protected against being renamed"),
                    type="error",
                )
                protected = True
        else:
            # Check with the parent
            parent = aq_parent(aq_inner(self.context))
            adapter = IRenameProtected(parent, None)
            if adapter:
                if adapter.rename_protection:
                    IStatusMessage(self.request).add(
                        _(
                            "This folder is protected against renaming "
                            "items inside of it."
                        ),
                        type="error",
                    )
                    protected = True
        if protected:
            self.request.response.redirect(self.context.absolute_url())
        else:
            return super(RenameForm, self).handle_rename(self, action)

    @button.buttonAndHandler(
        PloneMessageFactory("label_cancel", default="Cancel"), name="Cancel"
    )
    def handle_cancel(self, action):
        self.request.response.redirect(self.view_url())


class RenameActionView(BaseRenameActionView):
    def __call__(self):
        self.errors = list()
        context = aq_inner(self.context)
        catalog = getToolByName(context, "portal_catalog")

        for key in self.request.form.keys():
            if not key.startswith("UID_"):
                continue
            uid = self.request.form[key]
            brains = catalog.searchResults(UID=uid, show_inactive=True)
            if len(brains) == 0:
                continue
            obj = brains[0].getObject()

            # First check if the object itself is protected
            adapter = IRenameProtected(obj, None)
            if adapter:
                if adapter.rename_protection:
                    msgid = _(
                        "protected_item_rename",
                        default=("Item ${title} is protected against " "being renamed"),
                        mapping={"title": obj.Title()},
                    )
                    self.errors.append(msgid)
                    return self.message(list())
            else:
                # Check with the parent
                parent = aq_parent(aq_inner(obj))
                adapter = IRenameProtected(parent, None)
                if adapter:
                    if adapter.rename_protection:
                        self.errors.append(
                            _(
                                "This folder is protected against renaming "
                                "items inside of it."
                            )
                        )
                        return self.message(list())

        return super(RenameActionView, self).__call__()


class RenameProtectedView(BrowserView):

    def __call__(self):
        # XXX: We cannot simply redirect from here
        # See more: ZPublisher/WSGIPublisher.py(141)_exc_view_created_response()
        self.request.response.setStatus(200)
        return self.__parent__()
