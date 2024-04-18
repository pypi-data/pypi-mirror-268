# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Acquisition import aq_parent
from collective_folderprotection.behaviors.interfaces import IPasswordProtected
from plone.app.layout.viewlets.common import ViewletBase
try:
    from plone.base.interfaces.siteroot import IPloneSiteRoot
except:
    from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot

class AlertViewlet(ViewletBase):
    """Displays alert messages when content is pw protected"""

    context_pw_protected = False
    folder_pw_protected = False
    parent_pw_protected = None

    def update(self):
        super(AlertViewlet, self).update()
        if self.request.response.getStatus() == 401:
            return
        is_default_page = False
        parent = None
        context = aq_inner(self.context)

        passw_behavior = IPasswordProtected(context, None)
        if passw_behavior:
            self.context_pw_protected = passw_behavior.is_password_protected()

        if not IPloneSiteRoot.providedBy(context):
            parent = aq_parent(context)
            if context.id == parent.getDefaultPage():
                is_default_page = True

        if is_default_page and not self.context_pw_protected:
            passw_behavior = IPasswordProtected(parent, None)
            if passw_behavior:
                self.context_pw_protected = passw_behavior.is_password_protected()

            if not IPloneSiteRoot.providedBy(parent):
                parent = aq_parent(parent)

        if parent:
            passw_behavior = IPasswordProtected(parent, None)
            if passw_behavior:
                self.folder_pw_protected = passw_behavior.is_password_protected()

            while not IPloneSiteRoot.providedBy(parent):
                parent = aq_parent(parent)
                passw_behavior = IPasswordProtected(parent, None)
                if passw_behavior and passw_behavior.is_password_protected():
                    self.parent_pw_protected = parent
                    break
