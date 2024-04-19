import six
from zope.interface import implementer
from zope.interface.common.interfaces import IException


class IPasswordProtectedUnauthorized(IException):
    """ """


class IDeleteProtectionException(IException):
    """
    an exception raised when a delete protected folder is attempted to be deleted
    """


class IRenameProtectionException(IException):
    """
    an exception raised when a rename protected folder is attempted to be renamed
    """


@implementer(IPasswordProtectedUnauthorized)
class PasswordProtectedUnauthorized(Exception):
    def _get_message(self):
        return self._message

    message = property(_get_message)

    def __init__(self, message=None, name=None):
        """Possible signatures:

        PasswordProtectedUnauthorized()
        PasswordProtectedUnauthorized(message)
        PasswordProtectedUnauthorized(name)
        PasswordProtectedUnauthorized(message, name)

        """

        self.name = name
        self._message = message

    def __str__(self):
        if self.message is not None:
            return self.message
        if self.name is not None:
            return "You need a password to access '%s'" % self.name
        return repr(self)

    if six.PY2:

        def __unicode__(self):
            result = self.__str__()
            if isinstance(result, unicode):  # noqa: F821
                return result
            return unicode(  # noqa: F821
                result, "ascii"
            )  # override sys.getdefaultencoding()


@implementer(IDeleteProtectionException)
class DeleteProtectionException(Exception):
    """ """


@implementer(IRenameProtectionException)
class RenameProtectionException(Exception):
    """ """
