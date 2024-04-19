# -*- coding: utf-8 -*-
from collective_folderprotection.behaviors.interfaces import IPasswordProtected
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IPasswordWidget
from z3c.form.util import getSpecification
from z3c.form.widget import FieldWidget
from z3c.form.browser.password import PasswordWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementer_only


class IPasswordNoAutocompleteWidget(IPasswordWidget):
    """ """


@implementer_only(IPasswordNoAutocompleteWidget)
class PasswordNoAutocompleteWidget(PasswordWidget):
    """Input type password widget implementation with no autocomplete."""


@adapter(getSpecification(IPasswordProtected["passw_hash"]), IFormLayer)
@implementer(IFieldWidget)
def PasswordNoAutocompleteFieldWidget(field, request):
    return FieldWidget(field, PasswordNoAutocompleteWidget(request))
