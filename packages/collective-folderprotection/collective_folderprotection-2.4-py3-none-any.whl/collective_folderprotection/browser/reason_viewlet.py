# -*- coding: utf-8 -*-
from Acquisition import aq_parent
from collective_folderprotection.behaviors.interfaces import IPasswordProtected
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.contenttypes.interfaces import IFolder
from plone.app.textfield.interfaces import IRichTextValue
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot


class ReasonViewlet(ViewletBase):
    """Displays alert messages with the reason on why this content is pw protected"""

    context_pw_protected = False
    reason = ""

    def update(self):
        super(ReasonViewlet, self).update()
        if self.request.response.getStatus() == 401:
            return
        context = self.context
        if not IPloneSiteRoot.providedBy(context):
            if not IFolder.providedBy(self.context):
                context = aq_parent(self.context)

        passw_behavior = IPasswordProtected(context, None)
        if passw_behavior:
            self.context_pw_protected = passw_behavior.is_password_protected()

            if self.context_pw_protected:
                reason = passw_behavior.passw_reason
                if reason:
                    if IRichTextValue.providedBy(reason):
                        self.reason = reason.output_relative_to(context)
                    else:
                        self.reason = reason
