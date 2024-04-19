from typing import overload
import abc

import System
import System.Runtime.InteropServices.ComTypes


class IConnectionPoint(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ITypeInfo(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ITypeInfo2(System.Runtime.InteropServices.ComTypes.ITypeInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ITypeLib(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ITypeLib2(System.Runtime.InteropServices.ComTypes.ITypeLib, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class BIND_OPTS:
    """This class has no documentation."""

    @property
    def cb_struct(self) -> int:
        ...

    @property
    def grf_flags(self) -> int:
        ...

    @property
    def grf_mode(self) -> int:
        ...

    @property
    def dw_tick_count_deadline(self) -> int:
        ...


class IBindCtx(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IRunningObjectTable(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IEnumString(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class TYPEKIND(System.Enum):
    """This class has no documentation."""

    TKIND_ENUM = 0

    TKIND_RECORD = ...

    TKIND_MODULE = ...

    TKIND_INTERFACE = ...

    TKIND_DISPATCH = ...

    TKIND_COCLASS = ...

    TKIND_ALIAS = ...

    TKIND_UNION = ...

    TKIND_MAX = ...


class TYPEFLAGS(System.Enum):
    """This class has no documentation."""

    TYPEFLAG_FAPPOBJECT = ...

    TYPEFLAG_FCANCREATE = ...

    TYPEFLAG_FLICENSED = ...

    TYPEFLAG_FPREDECLID = ...

    TYPEFLAG_FHIDDEN = ...

    TYPEFLAG_FCONTROL = ...

    TYPEFLAG_FDUAL = ...

    TYPEFLAG_FNONEXTENSIBLE = ...

    TYPEFLAG_FOLEAUTOMATION = ...

    TYPEFLAG_FRESTRICTED = ...

    TYPEFLAG_FAGGREGATABLE = ...

    TYPEFLAG_FREPLACEABLE = ...

    TYPEFLAG_FDISPATCHABLE = ...

    TYPEFLAG_FREVERSEBIND = ...

    TYPEFLAG_FPROXY = ...


class IMPLTYPEFLAGS(System.Enum):
    """This class has no documentation."""

    IMPLTYPEFLAG_FDEFAULT = ...

    IMPLTYPEFLAG_FSOURCE = ...

    IMPLTYPEFLAG_FRESTRICTED = ...

    IMPLTYPEFLAG_FDEFAULTVTABLE = ...


class TYPEDESC:
    """This class has no documentation."""

    @property
    def lp_value(self) -> System.IntPtr:
        ...

    @property
    def vt(self) -> int:
        ...


class IDLFLAG(System.Enum):
    """This class has no documentation."""

    IDLFLAG_NONE = ...

    IDLFLAG_FIN = ...

    IDLFLAG_FOUT = ...

    IDLFLAG_FLCID = ...

    IDLFLAG_FRETVAL = ...


class IDLDESC:
    """This class has no documentation."""

    @property
    def dw_reserved(self) -> System.IntPtr:
        ...

    @property
    def w_idl_flags(self) -> System.Runtime.InteropServices.ComTypes.IDLFLAG:
        ...


class TYPEATTR:
    """This class has no documentation."""

    MEMBER_ID_NIL: int = ...

    @property
    def guid(self) -> System.Guid:
        ...

    @property
    def lcid(self) -> int:
        ...

    @property
    def dw_reserved(self) -> int:
        ...

    @property
    def memid_constructor(self) -> int:
        ...

    @property
    def memid_destructor(self) -> int:
        ...

    @property
    def lpstr_schema(self) -> System.IntPtr:
        ...

    @property
    def cb_size_instance(self) -> int:
        ...

    @property
    def typekind(self) -> System.Runtime.InteropServices.ComTypes.TYPEKIND:
        ...

    @property
    def c_funcs(self) -> int:
        ...

    @property
    def c_vars(self) -> int:
        ...

    @property
    def c_impl_types(self) -> int:
        ...

    @property
    def cb_size_vft(self) -> int:
        ...

    @property
    def cb_alignment(self) -> int:
        ...

    @property
    def w_type_flags(self) -> System.Runtime.InteropServices.ComTypes.TYPEFLAGS:
        ...

    @property
    def w_major_ver_num(self) -> int:
        ...

    @property
    def w_minor_ver_num(self) -> int:
        ...

    @property
    def tdesc_alias(self) -> System.Runtime.InteropServices.ComTypes.TYPEDESC:
        ...

    @property
    def idldesc_type(self) -> System.Runtime.InteropServices.ComTypes.IDLDESC:
        ...


class FUNCKIND(System.Enum):
    """This class has no documentation."""

    FUNC_VIRTUAL = 0

    FUNC_PUREVIRTUAL = 1

    FUNC_NONVIRTUAL = 2

    FUNC_STATIC = 3

    FUNC_DISPATCH = 4


class INVOKEKIND(System.Enum):
    """This class has no documentation."""

    INVOKE_FUNC = ...

    INVOKE_PROPERTYGET = ...

    INVOKE_PROPERTYPUT = ...

    INVOKE_PROPERTYPUTREF = ...


class CALLCONV(System.Enum):
    """This class has no documentation."""

    CC_CDECL = 1

    CC_MSCPASCAL = 2

    CC_PASCAL = ...

    CC_MACPASCAL = 3

    CC_STDCALL = 4

    CC_RESERVED = 5

    CC_SYSCALL = 6

    CC_MPWCDECL = 7

    CC_MPWPASCAL = 8

    CC_MAX = 9


class PARAMFLAG(System.Enum):
    """This class has no documentation."""

    PARAMFLAG_NONE = 0

    PARAMFLAG_FIN = ...

    PARAMFLAG_FOUT = ...

    PARAMFLAG_FLCID = ...

    PARAMFLAG_FRETVAL = ...

    PARAMFLAG_FOPT = ...

    PARAMFLAG_FHASDEFAULT = ...

    PARAMFLAG_FHASCUSTDATA = ...


class PARAMDESC:
    """This class has no documentation."""

    @property
    def lp_var_value(self) -> System.IntPtr:
        ...

    @property
    def w_param_flags(self) -> System.Runtime.InteropServices.ComTypes.PARAMFLAG:
        ...


class ELEMDESC:
    """This class has no documentation."""

    class DESCUNION:
        """This class has no documentation."""

        @property
        def idldesc(self) -> System.Runtime.InteropServices.ComTypes.IDLDESC:
            ...

        @property
        def paramdesc(self) -> System.Runtime.InteropServices.ComTypes.PARAMDESC:
            ...

    @property
    def tdesc(self) -> System.Runtime.InteropServices.ComTypes.TYPEDESC:
        ...

    @property
    def desc(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC.DESCUNION:
        ...


class FUNCDESC:
    """This class has no documentation."""

    @property
    def memid(self) -> int:
        ...

    @property
    def lprgscode(self) -> System.IntPtr:
        ...

    @property
    def lprgelemdesc_param(self) -> System.IntPtr:
        ...

    @property
    def funckind(self) -> System.Runtime.InteropServices.ComTypes.FUNCKIND:
        ...

    @property
    def invkind(self) -> System.Runtime.InteropServices.ComTypes.INVOKEKIND:
        ...

    @property
    def callconv(self) -> System.Runtime.InteropServices.ComTypes.CALLCONV:
        ...

    @property
    def c_params(self) -> int:
        ...

    @property
    def c_params_opt(self) -> int:
        ...

    @property
    def o_vft(self) -> int:
        ...

    @property
    def c_scodes(self) -> int:
        ...

    @property
    def elemdesc_func(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC:
        ...

    @property
    def w_func_flags(self) -> int:
        ...


class VARKIND(System.Enum):
    """This class has no documentation."""

    VAR_PERINSTANCE = ...

    VAR_STATIC = ...

    VAR_CONST = ...

    VAR_DISPATCH = ...


class VARDESC:
    """This class has no documentation."""

    class DESCUNION:
        """This class has no documentation."""

        @property
        def o_inst(self) -> int:
            ...

        @property
        def lpvar_value(self) -> System.IntPtr:
            ...

    @property
    def memid(self) -> int:
        ...

    @property
    def lpstr_schema(self) -> str:
        ...

    @property
    def desc(self) -> System.Runtime.InteropServices.ComTypes.VARDESC.DESCUNION:
        ...

    @property
    def elemdesc_var(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC:
        ...

    @property
    def w_var_flags(self) -> int:
        ...

    @property
    def varkind(self) -> System.Runtime.InteropServices.ComTypes.VARKIND:
        ...


class DISPPARAMS:
    """This class has no documentation."""

    @property
    def rgvarg(self) -> System.IntPtr:
        ...

    @property
    def rgdispid_named_args(self) -> System.IntPtr:
        ...

    @property
    def c_args(self) -> int:
        ...

    @property
    def c_named_args(self) -> int:
        ...


class EXCEPINFO:
    """This class has no documentation."""

    @property
    def w_code(self) -> int:
        ...

    @property
    def w_reserved(self) -> int:
        ...

    @property
    def bstr_source(self) -> str:
        ...

    @property
    def bstr_description(self) -> str:
        ...

    @property
    def bstr_help_file(self) -> str:
        ...

    @property
    def dw_help_context(self) -> int:
        ...

    @property
    def pv_reserved(self) -> System.IntPtr:
        ...

    @property
    def pfn_deferred_fill_in(self) -> System.IntPtr:
        ...

    @property
    def scode(self) -> int:
        ...


class FUNCFLAGS(System.Enum):
    """This class has no documentation."""

    FUNCFLAG_FRESTRICTED = ...

    FUNCFLAG_FSOURCE = ...

    FUNCFLAG_FBINDABLE = ...

    FUNCFLAG_FREQUESTEDIT = ...

    FUNCFLAG_FDISPLAYBIND = ...

    FUNCFLAG_FDEFAULTBIND = ...

    FUNCFLAG_FHIDDEN = ...

    FUNCFLAG_FUSESGETLASTERROR = ...

    FUNCFLAG_FDEFAULTCOLLELEM = ...

    FUNCFLAG_FUIDEFAULT = ...

    FUNCFLAG_FNONBROWSABLE = ...

    FUNCFLAG_FREPLACEABLE = ...

    FUNCFLAG_FIMMEDIATEBIND = ...


class VARFLAGS(System.Enum):
    """This class has no documentation."""

    VARFLAG_FREADONLY = ...

    VARFLAG_FSOURCE = ...

    VARFLAG_FBINDABLE = ...

    VARFLAG_FREQUESTEDIT = ...

    VARFLAG_FDISPLAYBIND = ...

    VARFLAG_FDEFAULTBIND = ...

    VARFLAG_FHIDDEN = ...

    VARFLAG_FRESTRICTED = ...

    VARFLAG_FDEFAULTCOLLELEM = ...

    VARFLAG_FUIDEFAULT = ...

    VARFLAG_FNONBROWSABLE = ...

    VARFLAG_FREPLACEABLE = ...

    VARFLAG_FIMMEDIATEBIND = ...


class FILETIME:
    """This class has no documentation."""

    @property
    def dw_low_date_time(self) -> int:
        ...

    @property
    def dw_high_date_time(self) -> int:
        ...


class STATSTG:
    """This class has no documentation."""

    @property
    def pwcs_name(self) -> str:
        ...

    @property
    def type(self) -> int:
        ...

    @property
    def cb_size(self) -> int:
        ...

    @property
    def mtime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @property
    def ctime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @property
    def atime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @property
    def grf_mode(self) -> int:
        ...

    @property
    def grf_locks_supported(self) -> int:
        ...

    @property
    def clsid(self) -> System.Guid:
        ...

    @property
    def grf_state_bits(self) -> int:
        ...

    @property
    def reserved(self) -> int:
        ...


class IStream(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IEnumVARIANT(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IEnumMoniker(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IPersistFile(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class SYSKIND(System.Enum):
    """This class has no documentation."""

    SYS_WIN16 = 0

    SYS_WIN32 = ...

    SYS_MAC = ...

    SYS_WIN64 = ...


class LIBFLAGS(System.Enum):
    """This class has no documentation."""

    LIBFLAG_FRESTRICTED = ...

    LIBFLAG_FCONTROL = ...

    LIBFLAG_FHIDDEN = ...

    LIBFLAG_FHASDISKIMAGE = ...


class TYPELIBATTR:
    """This class has no documentation."""

    @property
    def guid(self) -> System.Guid:
        ...

    @property
    def lcid(self) -> int:
        ...

    @property
    def syskind(self) -> System.Runtime.InteropServices.ComTypes.SYSKIND:
        ...

    @property
    def w_major_ver_num(self) -> int:
        ...

    @property
    def w_minor_ver_num(self) -> int:
        ...

    @property
    def w_lib_flags(self) -> System.Runtime.InteropServices.ComTypes.LIBFLAGS:
        ...


class IMoniker(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class DESCKIND(System.Enum):
    """This class has no documentation."""

    DESCKIND_NONE = 0

    DESCKIND_FUNCDESC = ...

    DESCKIND_VARDESC = ...

    DESCKIND_TYPECOMP = ...

    DESCKIND_IMPLICITAPPOBJ = ...

    DESCKIND_MAX = ...


class BINDPTR:
    """This class has no documentation."""

    @property
    def lpfuncdesc(self) -> System.IntPtr:
        ...

    @property
    def lpvardesc(self) -> System.IntPtr:
        ...

    @property
    def lptcomp(self) -> System.IntPtr:
        ...


class ITypeComp(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IEnumConnectionPoints(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class CONNECTDATA:
    """This class has no documentation."""

    @property
    def p_unk(self) -> System.Object:
        ...

    @property
    def dw_cookie(self) -> int:
        ...


class IEnumConnections(metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IConnectionPointContainer(metaclass=abc.ABCMeta):
    """This class has no documentation."""


