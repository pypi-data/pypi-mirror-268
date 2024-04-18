from typing import overload
import System
import System.Configuration.Assemblies


class AssemblyHashAlgorithm(System.Enum):
    """This class has no documentation."""

    NONE = 0

    MD5 = ...

    SHA1 = ...

    SHA256 = ...

    SHA384 = ...

    SHA512 = ...


class AssemblyVersionCompatibility(System.Enum):
    """This class has no documentation."""

    SAME_MACHINE = 1

    SAME_PROCESS = 2

    SAME_DOMAIN = 3


