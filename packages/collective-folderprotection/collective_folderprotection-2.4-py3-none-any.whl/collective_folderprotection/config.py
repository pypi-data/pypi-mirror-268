# -*- coding: utf-8 -*-
from datetime import timedelta

PROJECTNAME = "collective_folderprotection"

HASHES_ANNOTATION_KEY = "collective_folderprotection_valid_hashes"
HASH_COOKIE_KEY = "collective_folderprotection_hash"

# How much time the password should be remembered.
# XXX: Should this be configurable ?
TIME_TO_LIVE = timedelta(days=2)
