# -*- coding: utf-8 -*-


class DeleteProtected(object):
    def __init__(self, context):
        self.context = context

    def _get_delete_protection(self):
        result = False
        if self.context.delete_protection:
            result = True
        return result

    def _set_delete_protection(self, value):
        self.context.delete_protection = value

    delete_protection = property(_get_delete_protection, _set_delete_protection)
