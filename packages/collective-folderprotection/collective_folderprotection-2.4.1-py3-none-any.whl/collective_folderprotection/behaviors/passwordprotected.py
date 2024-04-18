# -*- coding: utf-8 -*-
import six
from datetime import datetime
from hashlib import md5

from zope.annotation import IAnnotations

from collective_folderprotection.config import HASHES_ANNOTATION_KEY
from collective_folderprotection.config import HASH_COOKIE_KEY


class PasswordProtected(object):
    def __init__(self, context):
        self.context = context

    def is_password_protected(self):
        return getattr(self.context, "passw_hash", False)

    def allowed_to_access(self):
        allowed = False
        request = self.context.REQUEST
        ann = IAnnotations(self.context)
        hashes = ann.get(HASHES_ANNOTATION_KEY, {})
        user_hash = request.cookies.get(HASH_COOKIE_KEY, None)

        if user_hash and user_hash in hashes:
            now = datetime.now()
            valid_until = hashes[user_hash]
            allowed = valid_until > now

        return allowed

    def _assign_password(self, passw=None):
        ann = IAnnotations(self.context)

        if passw:
            # If there's a password, assign it
            if six.PY3:
                passw_hash = md5(passw.encode()).hexdigest()
            else:
                passw_hash = md5(passw).hexdigest()
            if HASHES_ANNOTATION_KEY in ann:
                # Remove old stored hashes
                del ann[HASHES_ANNOTATION_KEY]

            self.context.passw_hash = passw_hash
        else:
            # If no password was provided, just remove everything
            if HASHES_ANNOTATION_KEY in ann:
                # Remove old storde hashes
                del ann[HASHES_ANNOTATION_KEY]

            self.context.passw_hash = None

    def assign_password(self, passw):
        self._assign_password(passw)

    def remove_password(self):
        self._assign_password(None)

    def _get_password(self):
        return self.context.passw_hash

    def _set_password(self, value):
        if value:
            self.assign_password(value)

    def _get_passw_reason(self):
        return self.context.passw_reason

    def _set_passw_reason(self, value):
        self.context.passw_reason = value

    passw_hash = property(_get_password, _set_password)
    passw_reason = property(_get_passw_reason, _set_passw_reason)
