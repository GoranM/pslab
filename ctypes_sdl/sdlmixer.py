'''Wrapper for SDL_mixer.h

Generated with:
/usr/bin/ctypesgen -lSDL_mixer /usr/include/SDL/SDL_mixer.h -o sdlmixer.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, str):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return int(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, str):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, str):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, str):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, str):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["SDL_mixer"] = load_library("SDL_mixer")

# 1 libraries
# End libraries

# No modules

# /usr/include/bits/types.h: 61
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    '__val',
]
struct_anon_1._fields_ = [
    ('__val', c_long * 2),
]

__quad_t = struct_anon_1 # /usr/include/bits/types.h: 61

__off_t = c_long # /usr/include/bits/types.h: 140

__off64_t = __quad_t # /usr/include/bits/types.h: 141

# /usr/include/libio.h: 253
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE # /usr/include/stdio.h: 48

_IO_lock_t = None # /usr/include/libio.h: 162

# /usr/include/libio.h: 168
class struct__IO_marker(Structure):
    pass

struct__IO_marker.__slots__ = [
    '_next',
    '_sbuf',
    '_pos',
]
struct__IO_marker._fields_ = [
    ('_next', POINTER(struct__IO_marker)),
    ('_sbuf', POINTER(struct__IO_FILE)),
    ('_pos', c_int),
]

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '__pad1',
    '__pad2',
    '__pad3',
    '__pad4',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', POINTER(None)),
    ('__pad2', POINTER(None)),
    ('__pad3', POINTER(None)),
    ('__pad4', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
]

Uint8 = c_uint8 # /usr/include/SDL/SDL_stdinc.h: 99

Sint16 = c_int16 # /usr/include/SDL/SDL_stdinc.h: 100

Uint16 = c_uint16 # /usr/include/SDL/SDL_stdinc.h: 101

Uint32 = c_uint32 # /usr/include/SDL/SDL_stdinc.h: 103

# /usr/include/SDL/SDL_error.h: 43
if hasattr(_libs['SDL_mixer'], 'SDL_SetError'):
    _func = _libs['SDL_mixer'].SDL_SetError
    _restype = None
    _argtypes = [String]
    SDL_SetError = _variadic_function(_func,_restype,_argtypes)

# /usr/include/SDL/SDL_error.h: 44
if hasattr(_libs['SDL_mixer'], 'SDL_GetError'):
    SDL_GetError = _libs['SDL_mixer'].SDL_GetError
    SDL_GetError.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_GetError.restype = ReturnString
    else:
        SDL_GetError.restype = String
        SDL_GetError.errcheck = ReturnString

# /usr/include/SDL/SDL_rwops.h: 42
class struct_SDL_RWops(Structure):
    pass

# /usr/include/SDL/SDL_rwops.h: 78
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'autoclose',
    'fp',
]
struct_anon_30._fields_ = [
    ('autoclose', c_int),
    ('fp', POINTER(FILE)),
]

# /usr/include/SDL/SDL_rwops.h: 83
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'base',
    'here',
    'stop',
]
struct_anon_31._fields_ = [
    ('base', POINTER(Uint8)),
    ('here', POINTER(Uint8)),
    ('stop', POINTER(Uint8)),
]

# /usr/include/SDL/SDL_rwops.h: 88
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'data1',
]
struct_anon_32._fields_ = [
    ('data1', POINTER(None)),
]

# /usr/include/SDL/SDL_rwops.h: 65
class union_anon_33(Union):
    pass

union_anon_33.__slots__ = [
    'stdio',
    'mem',
    'unknown',
]
union_anon_33._fields_ = [
    ('stdio', struct_anon_30),
    ('mem', struct_anon_31),
    ('unknown', struct_anon_32),
]

struct_SDL_RWops.__slots__ = [
    'seek',
    'read',
    'write',
    'close',
    'type',
    'hidden',
]
struct_SDL_RWops._fields_ = [
    ('seek', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops), c_int, c_int)),
    ('read', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops), POINTER(None), c_int, c_int)),
    ('write', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops), POINTER(None), c_int, c_int)),
    ('close', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops))),
    ('type', Uint32),
    ('hidden', union_anon_33),
]

SDL_RWops = struct_SDL_RWops # /usr/include/SDL/SDL_rwops.h: 93

# /usr/include/SDL/SDL_rwops.h: 99
if hasattr(_libs['SDL_mixer'], 'SDL_RWFromFile'):
    SDL_RWFromFile = _libs['SDL_mixer'].SDL_RWFromFile
    SDL_RWFromFile.argtypes = [String, String]
    SDL_RWFromFile.restype = POINTER(SDL_RWops)

# /usr/include/SDL/SDL_version.h: 51
class struct_SDL_version(Structure):
    pass

struct_SDL_version.__slots__ = [
    'major',
    'minor',
    'patch',
]
struct_SDL_version._fields_ = [
    ('major', Uint8),
    ('minor', Uint8),
    ('patch', Uint8),
]

SDL_version = struct_SDL_version # /usr/include/SDL/SDL_version.h: 51

# /usr/include/SDL/SDL_mixer.h: 65
if hasattr(_libs['SDL_mixer'], 'Mix_Linked_Version'):
    Mix_Linked_Version = _libs['SDL_mixer'].Mix_Linked_Version
    Mix_Linked_Version.argtypes = []
    Mix_Linked_Version.restype = POINTER(SDL_version)

enum_anon_35 = c_int # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_FLAC = 1 # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_MOD = 2 # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_MP3 = 4 # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_OGG = 8 # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_FLUIDSYNTH = 16 # /usr/include/SDL/SDL_mixer.h: 74

MIX_InitFlags = enum_anon_35 # /usr/include/SDL/SDL_mixer.h: 74

# /usr/include/SDL/SDL_mixer.h: 80
if hasattr(_libs['SDL_mixer'], 'Mix_Init'):
    Mix_Init = _libs['SDL_mixer'].Mix_Init
    Mix_Init.argtypes = [c_int]
    Mix_Init.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 83
if hasattr(_libs['SDL_mixer'], 'Mix_Quit'):
    Mix_Quit = _libs['SDL_mixer'].Mix_Quit
    Mix_Quit.argtypes = []
    Mix_Quit.restype = None

# /usr/include/SDL/SDL_mixer.h: 107
class struct_Mix_Chunk(Structure):
    pass

struct_Mix_Chunk.__slots__ = [
    'allocated',
    'abuf',
    'alen',
    'volume',
]
struct_Mix_Chunk._fields_ = [
    ('allocated', c_int),
    ('abuf', POINTER(Uint8)),
    ('alen', Uint32),
    ('volume', Uint8),
]

Mix_Chunk = struct_Mix_Chunk # /usr/include/SDL/SDL_mixer.h: 107

enum_anon_36 = c_int # /usr/include/SDL/SDL_mixer.h: 114

MIX_NO_FADING = 0 # /usr/include/SDL/SDL_mixer.h: 114

MIX_FADING_OUT = (MIX_NO_FADING + 1) # /usr/include/SDL/SDL_mixer.h: 114

MIX_FADING_IN = (MIX_FADING_OUT + 1) # /usr/include/SDL/SDL_mixer.h: 114

Mix_Fading = enum_anon_36 # /usr/include/SDL/SDL_mixer.h: 114

enum_anon_37 = c_int # /usr/include/SDL/SDL_mixer.h: 127

MUS_NONE = 0 # /usr/include/SDL/SDL_mixer.h: 127

MUS_CMD = (MUS_NONE + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_WAV = (MUS_CMD + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_MOD = (MUS_WAV + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_MID = (MUS_MOD + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_OGG = (MUS_MID + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_MP3 = (MUS_OGG + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_MP3_MAD = (MUS_MP3 + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_FLAC = (MUS_MP3_MAD + 1) # /usr/include/SDL/SDL_mixer.h: 127

MUS_MODPLUG = (MUS_FLAC + 1) # /usr/include/SDL/SDL_mixer.h: 127

Mix_MusicType = enum_anon_37 # /usr/include/SDL/SDL_mixer.h: 127

# /usr/include/SDL/SDL_mixer.h: 130
class struct__Mix_Music(Structure):
    pass

Mix_Music = struct__Mix_Music # /usr/include/SDL/SDL_mixer.h: 130

# /usr/include/SDL/SDL_mixer.h: 133
if hasattr(_libs['SDL_mixer'], 'Mix_OpenAudio'):
    Mix_OpenAudio = _libs['SDL_mixer'].Mix_OpenAudio
    Mix_OpenAudio.argtypes = [c_int, Uint16, c_int, c_int]
    Mix_OpenAudio.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 141
if hasattr(_libs['SDL_mixer'], 'Mix_AllocateChannels'):
    Mix_AllocateChannels = _libs['SDL_mixer'].Mix_AllocateChannels
    Mix_AllocateChannels.argtypes = [c_int]
    Mix_AllocateChannels.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 146
if hasattr(_libs['SDL_mixer'], 'Mix_QuerySpec'):
    Mix_QuerySpec = _libs['SDL_mixer'].Mix_QuerySpec
    Mix_QuerySpec.argtypes = [POINTER(c_int), POINTER(Uint16), POINTER(c_int)]
    Mix_QuerySpec.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 149
if hasattr(_libs['SDL_mixer'], 'Mix_LoadWAV_RW'):
    Mix_LoadWAV_RW = _libs['SDL_mixer'].Mix_LoadWAV_RW
    Mix_LoadWAV_RW.argtypes = [POINTER(SDL_RWops), c_int]
    Mix_LoadWAV_RW.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 151
if hasattr(_libs['SDL_mixer'], 'Mix_LoadMUS'):
    Mix_LoadMUS = _libs['SDL_mixer'].Mix_LoadMUS
    Mix_LoadMUS.argtypes = [String]
    Mix_LoadMUS.restype = POINTER(Mix_Music)

# /usr/include/SDL/SDL_mixer.h: 155
if hasattr(_libs['SDL_mixer'], 'Mix_LoadMUS_RW'):
    Mix_LoadMUS_RW = _libs['SDL_mixer'].Mix_LoadMUS_RW
    Mix_LoadMUS_RW.argtypes = [POINTER(SDL_RWops)]
    Mix_LoadMUS_RW.restype = POINTER(Mix_Music)

# /usr/include/SDL/SDL_mixer.h: 158
if hasattr(_libs['SDL_mixer'], 'Mix_LoadMUSType_RW'):
    Mix_LoadMUSType_RW = _libs['SDL_mixer'].Mix_LoadMUSType_RW
    Mix_LoadMUSType_RW.argtypes = [POINTER(SDL_RWops), Mix_MusicType, c_int]
    Mix_LoadMUSType_RW.restype = POINTER(Mix_Music)

# /usr/include/SDL/SDL_mixer.h: 161
if hasattr(_libs['SDL_mixer'], 'Mix_QuickLoad_WAV'):
    Mix_QuickLoad_WAV = _libs['SDL_mixer'].Mix_QuickLoad_WAV
    Mix_QuickLoad_WAV.argtypes = [POINTER(Uint8)]
    Mix_QuickLoad_WAV.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 164
if hasattr(_libs['SDL_mixer'], 'Mix_QuickLoad_RAW'):
    Mix_QuickLoad_RAW = _libs['SDL_mixer'].Mix_QuickLoad_RAW
    Mix_QuickLoad_RAW.argtypes = [POINTER(Uint8), Uint32]
    Mix_QuickLoad_RAW.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 167
if hasattr(_libs['SDL_mixer'], 'Mix_FreeChunk'):
    Mix_FreeChunk = _libs['SDL_mixer'].Mix_FreeChunk
    Mix_FreeChunk.argtypes = [POINTER(Mix_Chunk)]
    Mix_FreeChunk.restype = None

# /usr/include/SDL/SDL_mixer.h: 168
if hasattr(_libs['SDL_mixer'], 'Mix_FreeMusic'):
    Mix_FreeMusic = _libs['SDL_mixer'].Mix_FreeMusic
    Mix_FreeMusic.argtypes = [POINTER(Mix_Music)]
    Mix_FreeMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 189
if hasattr(_libs['SDL_mixer'], 'Mix_GetNumChunkDecoders'):
    Mix_GetNumChunkDecoders = _libs['SDL_mixer'].Mix_GetNumChunkDecoders
    Mix_GetNumChunkDecoders.argtypes = []
    Mix_GetNumChunkDecoders.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 190
if hasattr(_libs['SDL_mixer'], 'Mix_GetChunkDecoder'):
    Mix_GetChunkDecoder = _libs['SDL_mixer'].Mix_GetChunkDecoder
    Mix_GetChunkDecoder.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Mix_GetChunkDecoder.restype = ReturnString
    else:
        Mix_GetChunkDecoder.restype = String
        Mix_GetChunkDecoder.errcheck = ReturnString

# /usr/include/SDL/SDL_mixer.h: 191
if hasattr(_libs['SDL_mixer'], 'Mix_GetNumMusicDecoders'):
    Mix_GetNumMusicDecoders = _libs['SDL_mixer'].Mix_GetNumMusicDecoders
    Mix_GetNumMusicDecoders.argtypes = []
    Mix_GetNumMusicDecoders.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 192
if hasattr(_libs['SDL_mixer'], 'Mix_GetMusicDecoder'):
    Mix_GetMusicDecoder = _libs['SDL_mixer'].Mix_GetMusicDecoder
    Mix_GetMusicDecoder.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Mix_GetMusicDecoder.restype = ReturnString
    else:
        Mix_GetMusicDecoder.restype = String
        Mix_GetMusicDecoder.errcheck = ReturnString

# /usr/include/SDL/SDL_mixer.h: 197
if hasattr(_libs['SDL_mixer'], 'Mix_GetMusicType'):
    Mix_GetMusicType = _libs['SDL_mixer'].Mix_GetMusicType
    Mix_GetMusicType.argtypes = [POINTER(Mix_Music)]
    Mix_GetMusicType.restype = Mix_MusicType

# /usr/include/SDL/SDL_mixer.h: 203
if hasattr(_libs['SDL_mixer'], 'Mix_SetPostMix'):
    Mix_SetPostMix = _libs['SDL_mixer'].Mix_SetPostMix
    Mix_SetPostMix.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(Uint8), c_int), POINTER(None)]
    Mix_SetPostMix.restype = None

# /usr/include/SDL/SDL_mixer.h: 209
if hasattr(_libs['SDL_mixer'], 'Mix_HookMusic'):
    Mix_HookMusic = _libs['SDL_mixer'].Mix_HookMusic
    Mix_HookMusic.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(Uint8), c_int), POINTER(None)]
    Mix_HookMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 215
if hasattr(_libs['SDL_mixer'], 'Mix_HookMusicFinished'):
    Mix_HookMusicFinished = _libs['SDL_mixer'].Mix_HookMusicFinished
    Mix_HookMusicFinished.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    Mix_HookMusicFinished.restype = None

# /usr/include/SDL/SDL_mixer.h: 218
if hasattr(_libs['SDL_mixer'], 'Mix_GetMusicHookData'):
    Mix_GetMusicHookData = _libs['SDL_mixer'].Mix_GetMusicHookData
    Mix_GetMusicHookData.argtypes = []
    Mix_GetMusicHookData.restype = POINTER(None)

# /usr/include/SDL/SDL_mixer.h: 228
if hasattr(_libs['SDL_mixer'], 'Mix_ChannelFinished'):
    Mix_ChannelFinished = _libs['SDL_mixer'].Mix_ChannelFinished
    Mix_ChannelFinished.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int)]
    Mix_ChannelFinished.restype = None

Mix_EffectFunc_t = CFUNCTYPE(UNCHECKED(None), c_int, POINTER(None), c_int, POINTER(None)) # /usr/include/SDL/SDL_mixer.h: 252

Mix_EffectDone_t = CFUNCTYPE(UNCHECKED(None), c_int, POINTER(None)) # /usr/include/SDL/SDL_mixer.h: 263

# /usr/include/SDL/SDL_mixer.h: 312
if hasattr(_libs['SDL_mixer'], 'Mix_RegisterEffect'):
    Mix_RegisterEffect = _libs['SDL_mixer'].Mix_RegisterEffect
    Mix_RegisterEffect.argtypes = [c_int, Mix_EffectFunc_t, Mix_EffectDone_t, POINTER(None)]
    Mix_RegisterEffect.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 324
if hasattr(_libs['SDL_mixer'], 'Mix_UnregisterEffect'):
    Mix_UnregisterEffect = _libs['SDL_mixer'].Mix_UnregisterEffect
    Mix_UnregisterEffect.argtypes = [c_int, Mix_EffectFunc_t]
    Mix_UnregisterEffect.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 338
if hasattr(_libs['SDL_mixer'], 'Mix_UnregisterAllEffects'):
    Mix_UnregisterAllEffects = _libs['SDL_mixer'].Mix_UnregisterAllEffects
    Mix_UnregisterAllEffects.argtypes = [c_int]
    Mix_UnregisterAllEffects.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 378
if hasattr(_libs['SDL_mixer'], 'Mix_SetPanning'):
    Mix_SetPanning = _libs['SDL_mixer'].Mix_SetPanning
    Mix_SetPanning.argtypes = [c_int, Uint8, Uint8]
    Mix_SetPanning.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 418
if hasattr(_libs['SDL_mixer'], 'Mix_SetPosition'):
    Mix_SetPosition = _libs['SDL_mixer'].Mix_SetPosition
    Mix_SetPosition.argtypes = [c_int, Sint16, Uint8]
    Mix_SetPosition.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 448
if hasattr(_libs['SDL_mixer'], 'Mix_SetDistance'):
    Mix_SetDistance = _libs['SDL_mixer'].Mix_SetDistance
    Mix_SetDistance.argtypes = [c_int, Uint8]
    Mix_SetDistance.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 495
if hasattr(_libs['SDL_mixer'], 'Mix_SetReverseStereo'):
    Mix_SetReverseStereo = _libs['SDL_mixer'].Mix_SetReverseStereo
    Mix_SetReverseStereo.argtypes = [c_int, c_int]
    Mix_SetReverseStereo.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 504
if hasattr(_libs['SDL_mixer'], 'Mix_ReserveChannels'):
    Mix_ReserveChannels = _libs['SDL_mixer'].Mix_ReserveChannels
    Mix_ReserveChannels.argtypes = [c_int]
    Mix_ReserveChannels.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 514
if hasattr(_libs['SDL_mixer'], 'Mix_GroupChannel'):
    Mix_GroupChannel = _libs['SDL_mixer'].Mix_GroupChannel
    Mix_GroupChannel.argtypes = [c_int, c_int]
    Mix_GroupChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 516
if hasattr(_libs['SDL_mixer'], 'Mix_GroupChannels'):
    Mix_GroupChannels = _libs['SDL_mixer'].Mix_GroupChannels
    Mix_GroupChannels.argtypes = [c_int, c_int, c_int]
    Mix_GroupChannels.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 520
if hasattr(_libs['SDL_mixer'], 'Mix_GroupAvailable'):
    Mix_GroupAvailable = _libs['SDL_mixer'].Mix_GroupAvailable
    Mix_GroupAvailable.argtypes = [c_int]
    Mix_GroupAvailable.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 524
if hasattr(_libs['SDL_mixer'], 'Mix_GroupCount'):
    Mix_GroupCount = _libs['SDL_mixer'].Mix_GroupCount
    Mix_GroupCount.argtypes = [c_int]
    Mix_GroupCount.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 526
if hasattr(_libs['SDL_mixer'], 'Mix_GroupOldest'):
    Mix_GroupOldest = _libs['SDL_mixer'].Mix_GroupOldest
    Mix_GroupOldest.argtypes = [c_int]
    Mix_GroupOldest.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 528
if hasattr(_libs['SDL_mixer'], 'Mix_GroupNewer'):
    Mix_GroupNewer = _libs['SDL_mixer'].Mix_GroupNewer
    Mix_GroupNewer.argtypes = [c_int]
    Mix_GroupNewer.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 538
if hasattr(_libs['SDL_mixer'], 'Mix_PlayChannelTimed'):
    Mix_PlayChannelTimed = _libs['SDL_mixer'].Mix_PlayChannelTimed
    Mix_PlayChannelTimed.argtypes = [c_int, POINTER(Mix_Chunk), c_int, c_int]
    Mix_PlayChannelTimed.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 539
if hasattr(_libs['SDL_mixer'], 'Mix_PlayMusic'):
    Mix_PlayMusic = _libs['SDL_mixer'].Mix_PlayMusic
    Mix_PlayMusic.argtypes = [POINTER(Mix_Music), c_int]
    Mix_PlayMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 542
if hasattr(_libs['SDL_mixer'], 'Mix_FadeInMusic'):
    Mix_FadeInMusic = _libs['SDL_mixer'].Mix_FadeInMusic
    Mix_FadeInMusic.argtypes = [POINTER(Mix_Music), c_int, c_int]
    Mix_FadeInMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 543
if hasattr(_libs['SDL_mixer'], 'Mix_FadeInMusicPos'):
    Mix_FadeInMusicPos = _libs['SDL_mixer'].Mix_FadeInMusicPos
    Mix_FadeInMusicPos.argtypes = [POINTER(Mix_Music), c_int, c_int, c_double]
    Mix_FadeInMusicPos.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 545
if hasattr(_libs['SDL_mixer'], 'Mix_FadeInChannelTimed'):
    Mix_FadeInChannelTimed = _libs['SDL_mixer'].Mix_FadeInChannelTimed
    Mix_FadeInChannelTimed.argtypes = [c_int, POINTER(Mix_Chunk), c_int, c_int, c_int]
    Mix_FadeInChannelTimed.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 552
if hasattr(_libs['SDL_mixer'], 'Mix_Volume'):
    Mix_Volume = _libs['SDL_mixer'].Mix_Volume
    Mix_Volume.argtypes = [c_int, c_int]
    Mix_Volume.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 553
if hasattr(_libs['SDL_mixer'], 'Mix_VolumeChunk'):
    Mix_VolumeChunk = _libs['SDL_mixer'].Mix_VolumeChunk
    Mix_VolumeChunk.argtypes = [POINTER(Mix_Chunk), c_int]
    Mix_VolumeChunk.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 554
if hasattr(_libs['SDL_mixer'], 'Mix_VolumeMusic'):
    Mix_VolumeMusic = _libs['SDL_mixer'].Mix_VolumeMusic
    Mix_VolumeMusic.argtypes = [c_int]
    Mix_VolumeMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 557
if hasattr(_libs['SDL_mixer'], 'Mix_HaltChannel'):
    Mix_HaltChannel = _libs['SDL_mixer'].Mix_HaltChannel
    Mix_HaltChannel.argtypes = [c_int]
    Mix_HaltChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 558
if hasattr(_libs['SDL_mixer'], 'Mix_HaltGroup'):
    Mix_HaltGroup = _libs['SDL_mixer'].Mix_HaltGroup
    Mix_HaltGroup.argtypes = [c_int]
    Mix_HaltGroup.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 559
if hasattr(_libs['SDL_mixer'], 'Mix_HaltMusic'):
    Mix_HaltMusic = _libs['SDL_mixer'].Mix_HaltMusic
    Mix_HaltMusic.argtypes = []
    Mix_HaltMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 565
if hasattr(_libs['SDL_mixer'], 'Mix_ExpireChannel'):
    Mix_ExpireChannel = _libs['SDL_mixer'].Mix_ExpireChannel
    Mix_ExpireChannel.argtypes = [c_int, c_int]
    Mix_ExpireChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 571
if hasattr(_libs['SDL_mixer'], 'Mix_FadeOutChannel'):
    Mix_FadeOutChannel = _libs['SDL_mixer'].Mix_FadeOutChannel
    Mix_FadeOutChannel.argtypes = [c_int, c_int]
    Mix_FadeOutChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 572
if hasattr(_libs['SDL_mixer'], 'Mix_FadeOutGroup'):
    Mix_FadeOutGroup = _libs['SDL_mixer'].Mix_FadeOutGroup
    Mix_FadeOutGroup.argtypes = [c_int, c_int]
    Mix_FadeOutGroup.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 573
if hasattr(_libs['SDL_mixer'], 'Mix_FadeOutMusic'):
    Mix_FadeOutMusic = _libs['SDL_mixer'].Mix_FadeOutMusic
    Mix_FadeOutMusic.argtypes = [c_int]
    Mix_FadeOutMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 576
if hasattr(_libs['SDL_mixer'], 'Mix_FadingMusic'):
    Mix_FadingMusic = _libs['SDL_mixer'].Mix_FadingMusic
    Mix_FadingMusic.argtypes = []
    Mix_FadingMusic.restype = Mix_Fading

# /usr/include/SDL/SDL_mixer.h: 577
if hasattr(_libs['SDL_mixer'], 'Mix_FadingChannel'):
    Mix_FadingChannel = _libs['SDL_mixer'].Mix_FadingChannel
    Mix_FadingChannel.argtypes = [c_int]
    Mix_FadingChannel.restype = Mix_Fading

# /usr/include/SDL/SDL_mixer.h: 580
if hasattr(_libs['SDL_mixer'], 'Mix_Pause'):
    Mix_Pause = _libs['SDL_mixer'].Mix_Pause
    Mix_Pause.argtypes = [c_int]
    Mix_Pause.restype = None

# /usr/include/SDL/SDL_mixer.h: 581
if hasattr(_libs['SDL_mixer'], 'Mix_Resume'):
    Mix_Resume = _libs['SDL_mixer'].Mix_Resume
    Mix_Resume.argtypes = [c_int]
    Mix_Resume.restype = None

# /usr/include/SDL/SDL_mixer.h: 582
if hasattr(_libs['SDL_mixer'], 'Mix_Paused'):
    Mix_Paused = _libs['SDL_mixer'].Mix_Paused
    Mix_Paused.argtypes = [c_int]
    Mix_Paused.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 585
if hasattr(_libs['SDL_mixer'], 'Mix_PauseMusic'):
    Mix_PauseMusic = _libs['SDL_mixer'].Mix_PauseMusic
    Mix_PauseMusic.argtypes = []
    Mix_PauseMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 586
if hasattr(_libs['SDL_mixer'], 'Mix_ResumeMusic'):
    Mix_ResumeMusic = _libs['SDL_mixer'].Mix_ResumeMusic
    Mix_ResumeMusic.argtypes = []
    Mix_ResumeMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 587
if hasattr(_libs['SDL_mixer'], 'Mix_RewindMusic'):
    Mix_RewindMusic = _libs['SDL_mixer'].Mix_RewindMusic
    Mix_RewindMusic.argtypes = []
    Mix_RewindMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 588
if hasattr(_libs['SDL_mixer'], 'Mix_PausedMusic'):
    Mix_PausedMusic = _libs['SDL_mixer'].Mix_PausedMusic
    Mix_PausedMusic.argtypes = []
    Mix_PausedMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 596
if hasattr(_libs['SDL_mixer'], 'Mix_SetMusicPosition'):
    Mix_SetMusicPosition = _libs['SDL_mixer'].Mix_SetMusicPosition
    Mix_SetMusicPosition.argtypes = [c_double]
    Mix_SetMusicPosition.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 601
if hasattr(_libs['SDL_mixer'], 'Mix_Playing'):
    Mix_Playing = _libs['SDL_mixer'].Mix_Playing
    Mix_Playing.argtypes = [c_int]
    Mix_Playing.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 602
if hasattr(_libs['SDL_mixer'], 'Mix_PlayingMusic'):
    Mix_PlayingMusic = _libs['SDL_mixer'].Mix_PlayingMusic
    Mix_PlayingMusic.argtypes = []
    Mix_PlayingMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 605
if hasattr(_libs['SDL_mixer'], 'Mix_SetMusicCMD'):
    Mix_SetMusicCMD = _libs['SDL_mixer'].Mix_SetMusicCMD
    Mix_SetMusicCMD.argtypes = [String]
    Mix_SetMusicCMD.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 608
if hasattr(_libs['SDL_mixer'], 'Mix_SetSynchroValue'):
    Mix_SetSynchroValue = _libs['SDL_mixer'].Mix_SetSynchroValue
    Mix_SetSynchroValue.argtypes = [c_int]
    Mix_SetSynchroValue.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 609
if hasattr(_libs['SDL_mixer'], 'Mix_GetSynchroValue'):
    Mix_GetSynchroValue = _libs['SDL_mixer'].Mix_GetSynchroValue
    Mix_GetSynchroValue.argtypes = []
    Mix_GetSynchroValue.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 612
if hasattr(_libs['SDL_mixer'], 'Mix_SetSoundFonts'):
    Mix_SetSoundFonts = _libs['SDL_mixer'].Mix_SetSoundFonts
    Mix_SetSoundFonts.argtypes = [String]
    Mix_SetSoundFonts.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 613
if hasattr(_libs['SDL_mixer'], 'Mix_GetSoundFonts'):
    Mix_GetSoundFonts = _libs['SDL_mixer'].Mix_GetSoundFonts
    Mix_GetSoundFonts.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        Mix_GetSoundFonts.restype = ReturnString
    else:
        Mix_GetSoundFonts.restype = String
        Mix_GetSoundFonts.errcheck = ReturnString

# /usr/include/SDL/SDL_mixer.h: 614
if hasattr(_libs['SDL_mixer'], 'Mix_EachSoundFont'):
    Mix_EachSoundFont = _libs['SDL_mixer'].Mix_EachSoundFont
    Mix_EachSoundFont.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, POINTER(None)), POINTER(None)]
    Mix_EachSoundFont.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 619
if hasattr(_libs['SDL_mixer'], 'Mix_GetChunk'):
    Mix_GetChunk = _libs['SDL_mixer'].Mix_GetChunk
    Mix_GetChunk.argtypes = [c_int]
    Mix_GetChunk.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 622
if hasattr(_libs['SDL_mixer'], 'Mix_CloseAudio'):
    Mix_CloseAudio = _libs['SDL_mixer'].Mix_CloseAudio
    Mix_CloseAudio.argtypes = []
    Mix_CloseAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 103
try:
    AUDIO_S16LSB = 32784
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 41
try:
    SDL_MIXER_MAJOR_VERSION = 1
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 42
try:
    SDL_MIXER_MINOR_VERSION = 2
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 43
try:
    SDL_MIXER_PATCHLEVEL = 12
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 56
try:
    MIX_MAJOR_VERSION = SDL_MIXER_MAJOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 57
try:
    MIX_MINOR_VERSION = SDL_MIXER_MINOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 58
try:
    MIX_PATCHLEVEL = SDL_MIXER_PATCHLEVEL
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 88
try:
    MIX_CHANNELS = 8
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 92
try:
    MIX_DEFAULT_FREQUENCY = 22050
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 94
try:
    MIX_DEFAULT_FORMAT = AUDIO_S16LSB
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 98
try:
    MIX_DEFAULT_CHANNELS = 2
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 99
try:
    MIX_MAX_VOLUME = 128
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 150
def Mix_LoadWAV(file):
    return (Mix_LoadWAV_RW ((SDL_RWFromFile (file, c_char_p(b'rb'))), 1))

# /usr/include/SDL/SDL_mixer.h: 233
try:
    MIX_CHANNEL_POST = (-2)
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 341
try:
    MIX_EFFECTSMAXSPEED = 'MIX_EFFECTSMAXSPEED'
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 536
def Mix_PlayChannel(channel, chunk, loops):
    return (Mix_PlayChannelTimed (channel, chunk, loops, (-1)))

# /usr/include/SDL/SDL_mixer.h: 544
def Mix_FadeInChannel(channel, chunk, loops, ms):
    return (Mix_FadeInChannelTimed (channel, chunk, loops, ms, (-1)))

# /usr/include/SDL/SDL_mixer.h: 625
try:
    Mix_SetError = SDL_SetError
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 626
try:
    Mix_GetError = SDL_GetError
except:
    pass

Mix_Chunk = struct_Mix_Chunk # /usr/include/SDL/SDL_mixer.h: 107

_Mix_Music = struct__Mix_Music # /usr/include/SDL/SDL_mixer.h: 130

# No inserted files

