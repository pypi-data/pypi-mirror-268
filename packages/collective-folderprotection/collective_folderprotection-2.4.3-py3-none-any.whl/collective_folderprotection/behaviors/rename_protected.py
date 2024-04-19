# -*- coding: utf-8 -*-


class RenameProtected(object):
    def __init__(self, context):
        self.context = context

    def _get_rename_protection(self):
        result = False
        if self.context.rename_protection:
            result = True
        return result

    def _set_rename_protection(self, value):
        self.context.rename_protection = value

    rename_protection = property(_get_rename_protection, _set_rename_protection)
