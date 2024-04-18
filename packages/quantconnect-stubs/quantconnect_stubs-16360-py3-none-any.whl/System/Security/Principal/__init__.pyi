from typing import overload
import abc

import System
import System.Security.Principal


class IPrincipal(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class PrincipalPolicy(System.Enum):
    """This class has no documentation."""

    UNAUTHENTICATED_PRINCIPAL = 0

    NO_PRINCIPAL = 1

    WINDOWS_PRINCIPAL = 2


class IIdentity(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class TokenImpersonationLevel(System.Enum):
    """This class has no documentation."""

    NONE = 0

    ANONYMOUS = 1

    IDENTIFICATION = 2

    IMPERSONATION = 3

    DELEGATION = 4


