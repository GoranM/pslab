'''Wrapper for SDL_ttf.h

Generated with:
/usr/bin/ctypesgen -lSDL_ttf /usr/include/SDL/SDL_ttf.h -o sdlttf.py

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

_libs["SDL_ttf"] = load_library("SDL_ttf")

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
if hasattr(_libs['SDL_ttf'], 'SDL_SetError'):
    _func = _libs['SDL_ttf'].SDL_SetError
    _restype = None
    _argtypes = [String]
    SDL_SetError = _variadic_function(_func,_restype,_argtypes)

# /usr/include/SDL/SDL_error.h: 44
if hasattr(_libs['SDL_ttf'], 'SDL_GetError'):
    SDL_GetError = _libs['SDL_ttf'].SDL_GetError
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

# /usr/include/SDL/SDL_video.h: 53
class struct_SDL_Rect(Structure):
    pass

struct_SDL_Rect.__slots__ = [
    'x',
    'y',
    'w',
    'h',
]
struct_SDL_Rect._fields_ = [
    ('x', Sint16),
    ('y', Sint16),
    ('w', Uint16),
    ('h', Uint16),
]

SDL_Rect = struct_SDL_Rect # /usr/include/SDL/SDL_video.h: 53

# /usr/include/SDL/SDL_video.h: 60
class struct_SDL_Color(Structure):
    pass

struct_SDL_Color.__slots__ = [
    'r',
    'g',
    'b',
    'unused',
]
struct_SDL_Color._fields_ = [
    ('r', Uint8),
    ('g', Uint8),
    ('b', Uint8),
    ('unused', Uint8),
]

SDL_Color = struct_SDL_Color # /usr/include/SDL/SDL_video.h: 60

# /usr/include/SDL/SDL_video.h: 66
class struct_SDL_Palette(Structure):
    pass

struct_SDL_Palette.__slots__ = [
    'ncolors',
    'colors',
]
struct_SDL_Palette._fields_ = [
    ('ncolors', c_int),
    ('colors', POINTER(SDL_Color)),
]

SDL_Palette = struct_SDL_Palette # /usr/include/SDL/SDL_video.h: 66

# /usr/include/SDL/SDL_video.h: 91
class struct_SDL_PixelFormat(Structure):
    pass

struct_SDL_PixelFormat.__slots__ = [
    'palette',
    'BitsPerPixel',
    'BytesPerPixel',
    'Rloss',
    'Gloss',
    'Bloss',
    'Aloss',
    'Rshift',
    'Gshift',
    'Bshift',
    'Ashift',
    'Rmask',
    'Gmask',
    'Bmask',
    'Amask',
    'colorkey',
    'alpha',
]
struct_SDL_PixelFormat._fields_ = [
    ('palette', POINTER(SDL_Palette)),
    ('BitsPerPixel', Uint8),
    ('BytesPerPixel', Uint8),
    ('Rloss', Uint8),
    ('Gloss', Uint8),
    ('Bloss', Uint8),
    ('Aloss', Uint8),
    ('Rshift', Uint8),
    ('Gshift', Uint8),
    ('Bshift', Uint8),
    ('Ashift', Uint8),
    ('Rmask', Uint32),
    ('Gmask', Uint32),
    ('Bmask', Uint32),
    ('Amask', Uint32),
    ('colorkey', Uint32),
    ('alpha', Uint8),
]

SDL_PixelFormat = struct_SDL_PixelFormat # /usr/include/SDL/SDL_video.h: 91

# /usr/include/SDL/SDL_video.h: 105
class struct_private_hwdata(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 115
class struct_SDL_BlitMap(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 122
class struct_SDL_Surface(Structure):
    pass

struct_SDL_Surface.__slots__ = [
    'flags',
    'format',
    'w',
    'h',
    'pitch',
    'pixels',
    'offset',
    'hwdata',
    'clip_rect',
    'unused1',
    'locked',
    'map',
    'format_version',
    'refcount',
]
struct_SDL_Surface._fields_ = [
    ('flags', Uint32),
    ('format', POINTER(SDL_PixelFormat)),
    ('w', c_int),
    ('h', c_int),
    ('pitch', Uint16),
    ('pixels', POINTER(None)),
    ('offset', c_int),
    ('hwdata', POINTER(struct_private_hwdata)),
    ('clip_rect', SDL_Rect),
    ('unused1', Uint32),
    ('locked', Uint32),
    ('map', POINTER(struct_SDL_BlitMap)),
    ('format_version', c_uint),
    ('refcount', c_int),
]

SDL_Surface = struct_SDL_Surface # /usr/include/SDL/SDL_video.h: 122

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

# /usr/include/SDL/SDL_ttf.h: 64
if hasattr(_libs['SDL_ttf'], 'TTF_Linked_Version'):
    TTF_Linked_Version = _libs['SDL_ttf'].TTF_Linked_Version
    TTF_Linked_Version.argtypes = []
    TTF_Linked_Version.restype = POINTER(SDL_version)

# /usr/include/SDL/SDL_ttf.h: 74
if hasattr(_libs['SDL_ttf'], 'TTF_ByteSwappedUNICODE'):
    TTF_ByteSwappedUNICODE = _libs['SDL_ttf'].TTF_ByteSwappedUNICODE
    TTF_ByteSwappedUNICODE.argtypes = [c_int]
    TTF_ByteSwappedUNICODE.restype = None

# /usr/include/SDL/SDL_ttf.h: 77
class struct__TTF_Font(Structure):
    pass

TTF_Font = struct__TTF_Font # /usr/include/SDL/SDL_ttf.h: 77

# /usr/include/SDL/SDL_ttf.h: 80
if hasattr(_libs['SDL_ttf'], 'TTF_Init'):
    TTF_Init = _libs['SDL_ttf'].TTF_Init
    TTF_Init.argtypes = []
    TTF_Init.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 86
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFont'):
    TTF_OpenFont = _libs['SDL_ttf'].TTF_OpenFont
    TTF_OpenFont.argtypes = [String, c_int]
    TTF_OpenFont.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 87
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFontIndex'):
    TTF_OpenFontIndex = _libs['SDL_ttf'].TTF_OpenFontIndex
    TTF_OpenFontIndex.argtypes = [String, c_int, c_long]
    TTF_OpenFontIndex.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 88
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFontRW'):
    TTF_OpenFontRW = _libs['SDL_ttf'].TTF_OpenFontRW
    TTF_OpenFontRW.argtypes = [POINTER(SDL_RWops), c_int, c_int]
    TTF_OpenFontRW.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 89
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFontIndexRW'):
    TTF_OpenFontIndexRW = _libs['SDL_ttf'].TTF_OpenFontIndexRW
    TTF_OpenFontIndexRW.argtypes = [POINTER(SDL_RWops), c_int, c_int, c_long]
    TTF_OpenFontIndexRW.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 97
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontStyle'):
    TTF_GetFontStyle = _libs['SDL_ttf'].TTF_GetFontStyle
    TTF_GetFontStyle.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontStyle.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 98
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontStyle'):
    TTF_SetFontStyle = _libs['SDL_ttf'].TTF_SetFontStyle
    TTF_SetFontStyle.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontStyle.restype = None

# /usr/include/SDL/SDL_ttf.h: 99
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontOutline'):
    TTF_GetFontOutline = _libs['SDL_ttf'].TTF_GetFontOutline
    TTF_GetFontOutline.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontOutline.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 100
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontOutline'):
    TTF_SetFontOutline = _libs['SDL_ttf'].TTF_SetFontOutline
    TTF_SetFontOutline.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontOutline.restype = None

# /usr/include/SDL/SDL_ttf.h: 107
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontHinting'):
    TTF_GetFontHinting = _libs['SDL_ttf'].TTF_GetFontHinting
    TTF_GetFontHinting.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontHinting.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 108
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontHinting'):
    TTF_SetFontHinting = _libs['SDL_ttf'].TTF_SetFontHinting
    TTF_SetFontHinting.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontHinting.restype = None

# /usr/include/SDL/SDL_ttf.h: 111
if hasattr(_libs['SDL_ttf'], 'TTF_FontHeight'):
    TTF_FontHeight = _libs['SDL_ttf'].TTF_FontHeight
    TTF_FontHeight.argtypes = [POINTER(TTF_Font)]
    TTF_FontHeight.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 116
if hasattr(_libs['SDL_ttf'], 'TTF_FontAscent'):
    TTF_FontAscent = _libs['SDL_ttf'].TTF_FontAscent
    TTF_FontAscent.argtypes = [POINTER(TTF_Font)]
    TTF_FontAscent.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 121
if hasattr(_libs['SDL_ttf'], 'TTF_FontDescent'):
    TTF_FontDescent = _libs['SDL_ttf'].TTF_FontDescent
    TTF_FontDescent.argtypes = [POINTER(TTF_Font)]
    TTF_FontDescent.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 124
if hasattr(_libs['SDL_ttf'], 'TTF_FontLineSkip'):
    TTF_FontLineSkip = _libs['SDL_ttf'].TTF_FontLineSkip
    TTF_FontLineSkip.argtypes = [POINTER(TTF_Font)]
    TTF_FontLineSkip.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 127
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontKerning'):
    TTF_GetFontKerning = _libs['SDL_ttf'].TTF_GetFontKerning
    TTF_GetFontKerning.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontKerning.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 128
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontKerning'):
    TTF_SetFontKerning = _libs['SDL_ttf'].TTF_SetFontKerning
    TTF_SetFontKerning.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontKerning.restype = None

# /usr/include/SDL/SDL_ttf.h: 131
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaces'):
    TTF_FontFaces = _libs['SDL_ttf'].TTF_FontFaces
    TTF_FontFaces.argtypes = [POINTER(TTF_Font)]
    TTF_FontFaces.restype = c_long

# /usr/include/SDL/SDL_ttf.h: 134
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaceIsFixedWidth'):
    TTF_FontFaceIsFixedWidth = _libs['SDL_ttf'].TTF_FontFaceIsFixedWidth
    TTF_FontFaceIsFixedWidth.argtypes = [POINTER(TTF_Font)]
    TTF_FontFaceIsFixedWidth.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 135
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaceFamilyName'):
    TTF_FontFaceFamilyName = _libs['SDL_ttf'].TTF_FontFaceFamilyName
    TTF_FontFaceFamilyName.argtypes = [POINTER(TTF_Font)]
    if sizeof(c_int) == sizeof(c_void_p):
        TTF_FontFaceFamilyName.restype = ReturnString
    else:
        TTF_FontFaceFamilyName.restype = String
        TTF_FontFaceFamilyName.errcheck = ReturnString

# /usr/include/SDL/SDL_ttf.h: 136
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaceStyleName'):
    TTF_FontFaceStyleName = _libs['SDL_ttf'].TTF_FontFaceStyleName
    TTF_FontFaceStyleName.argtypes = [POINTER(TTF_Font)]
    if sizeof(c_int) == sizeof(c_void_p):
        TTF_FontFaceStyleName.restype = ReturnString
    else:
        TTF_FontFaceStyleName.restype = String
        TTF_FontFaceStyleName.errcheck = ReturnString

# /usr/include/SDL/SDL_ttf.h: 139
if hasattr(_libs['SDL_ttf'], 'TTF_GlyphIsProvided'):
    TTF_GlyphIsProvided = _libs['SDL_ttf'].TTF_GlyphIsProvided
    TTF_GlyphIsProvided.argtypes = [POINTER(TTF_Font), Uint16]
    TTF_GlyphIsProvided.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 145
if hasattr(_libs['SDL_ttf'], 'TTF_GlyphMetrics'):
    TTF_GlyphMetrics = _libs['SDL_ttf'].TTF_GlyphMetrics
    TTF_GlyphMetrics.argtypes = [POINTER(TTF_Font), Uint16, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    TTF_GlyphMetrics.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 150
if hasattr(_libs['SDL_ttf'], 'TTF_SizeText'):
    TTF_SizeText = _libs['SDL_ttf'].TTF_SizeText
    TTF_SizeText.argtypes = [POINTER(TTF_Font), String, POINTER(c_int), POINTER(c_int)]
    TTF_SizeText.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 151
if hasattr(_libs['SDL_ttf'], 'TTF_SizeUTF8'):
    TTF_SizeUTF8 = _libs['SDL_ttf'].TTF_SizeUTF8
    TTF_SizeUTF8.argtypes = [POINTER(TTF_Font), String, POINTER(c_int), POINTER(c_int)]
    TTF_SizeUTF8.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 152
if hasattr(_libs['SDL_ttf'], 'TTF_SizeUNICODE'):
    TTF_SizeUNICODE = _libs['SDL_ttf'].TTF_SizeUNICODE
    TTF_SizeUNICODE.argtypes = [POINTER(TTF_Font), POINTER(Uint16), POINTER(c_int), POINTER(c_int)]
    TTF_SizeUNICODE.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 160
if hasattr(_libs['SDL_ttf'], 'TTF_RenderText_Solid'):
    TTF_RenderText_Solid = _libs['SDL_ttf'].TTF_RenderText_Solid
    TTF_RenderText_Solid.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderText_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 162
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUTF8_Solid'):
    TTF_RenderUTF8_Solid = _libs['SDL_ttf'].TTF_RenderUTF8_Solid
    TTF_RenderUTF8_Solid.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderUTF8_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 164
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUNICODE_Solid'):
    TTF_RenderUNICODE_Solid = _libs['SDL_ttf'].TTF_RenderUNICODE_Solid
    TTF_RenderUNICODE_Solid.argtypes = [POINTER(TTF_Font), POINTER(Uint16), SDL_Color]
    TTF_RenderUNICODE_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 174
if hasattr(_libs['SDL_ttf'], 'TTF_RenderGlyph_Solid'):
    TTF_RenderGlyph_Solid = _libs['SDL_ttf'].TTF_RenderGlyph_Solid
    TTF_RenderGlyph_Solid.argtypes = [POINTER(TTF_Font), Uint16, SDL_Color]
    TTF_RenderGlyph_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 182
if hasattr(_libs['SDL_ttf'], 'TTF_RenderText_Shaded'):
    TTF_RenderText_Shaded = _libs['SDL_ttf'].TTF_RenderText_Shaded
    TTF_RenderText_Shaded.argtypes = [POINTER(TTF_Font), String, SDL_Color, SDL_Color]
    TTF_RenderText_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 184
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUTF8_Shaded'):
    TTF_RenderUTF8_Shaded = _libs['SDL_ttf'].TTF_RenderUTF8_Shaded
    TTF_RenderUTF8_Shaded.argtypes = [POINTER(TTF_Font), String, SDL_Color, SDL_Color]
    TTF_RenderUTF8_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 186
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUNICODE_Shaded'):
    TTF_RenderUNICODE_Shaded = _libs['SDL_ttf'].TTF_RenderUNICODE_Shaded
    TTF_RenderUNICODE_Shaded.argtypes = [POINTER(TTF_Font), POINTER(Uint16), SDL_Color, SDL_Color]
    TTF_RenderUNICODE_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 196
if hasattr(_libs['SDL_ttf'], 'TTF_RenderGlyph_Shaded'):
    TTF_RenderGlyph_Shaded = _libs['SDL_ttf'].TTF_RenderGlyph_Shaded
    TTF_RenderGlyph_Shaded.argtypes = [POINTER(TTF_Font), Uint16, SDL_Color, SDL_Color]
    TTF_RenderGlyph_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 203
if hasattr(_libs['SDL_ttf'], 'TTF_RenderText_Blended'):
    TTF_RenderText_Blended = _libs['SDL_ttf'].TTF_RenderText_Blended
    TTF_RenderText_Blended.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderText_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 205
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUTF8_Blended'):
    TTF_RenderUTF8_Blended = _libs['SDL_ttf'].TTF_RenderUTF8_Blended
    TTF_RenderUTF8_Blended.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderUTF8_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 207
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUNICODE_Blended'):
    TTF_RenderUNICODE_Blended = _libs['SDL_ttf'].TTF_RenderUNICODE_Blended
    TTF_RenderUNICODE_Blended.argtypes = [POINTER(TTF_Font), POINTER(Uint16), SDL_Color]
    TTF_RenderUNICODE_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 216
if hasattr(_libs['SDL_ttf'], 'TTF_RenderGlyph_Blended'):
    TTF_RenderGlyph_Blended = _libs['SDL_ttf'].TTF_RenderGlyph_Blended
    TTF_RenderGlyph_Blended.argtypes = [POINTER(TTF_Font), Uint16, SDL_Color]
    TTF_RenderGlyph_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 228
if hasattr(_libs['SDL_ttf'], 'TTF_CloseFont'):
    TTF_CloseFont = _libs['SDL_ttf'].TTF_CloseFont
    TTF_CloseFont.argtypes = [POINTER(TTF_Font)]
    TTF_CloseFont.restype = None

# /usr/include/SDL/SDL_ttf.h: 231
if hasattr(_libs['SDL_ttf'], 'TTF_Quit'):
    TTF_Quit = _libs['SDL_ttf'].TTF_Quit
    TTF_Quit.argtypes = []
    TTF_Quit.restype = None

# /usr/include/SDL/SDL_ttf.h: 234
if hasattr(_libs['SDL_ttf'], 'TTF_WasInit'):
    TTF_WasInit = _libs['SDL_ttf'].TTF_WasInit
    TTF_WasInit.argtypes = []
    TTF_WasInit.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 237
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontKerningSize'):
    TTF_GetFontKerningSize = _libs['SDL_ttf'].TTF_GetFontKerningSize
    TTF_GetFontKerningSize.argtypes = [POINTER(TTF_Font), c_int, c_int]
    TTF_GetFontKerningSize.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 40
try:
    SDL_TTF_MAJOR_VERSION = 2
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 41
try:
    SDL_TTF_MINOR_VERSION = 0
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 42
try:
    SDL_TTF_PATCHLEVEL = 11
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 55
try:
    TTF_MAJOR_VERSION = SDL_TTF_MAJOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 56
try:
    TTF_MINOR_VERSION = SDL_TTF_MINOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 57
try:
    TTF_PATCHLEVEL = SDL_TTF_PATCHLEVEL
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 67
try:
    UNICODE_BOM_NATIVE = 65279
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 68
try:
    UNICODE_BOM_SWAPPED = 65534
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 92
try:
    TTF_STYLE_NORMAL = 0
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 93
try:
    TTF_STYLE_BOLD = 1
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 94
try:
    TTF_STYLE_ITALIC = 2
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 95
try:
    TTF_STYLE_UNDERLINE = 4
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 96
try:
    TTF_STYLE_STRIKETHROUGH = 8
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 103
try:
    TTF_HINTING_NORMAL = 0
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 104
try:
    TTF_HINTING_LIGHT = 1
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 105
try:
    TTF_HINTING_MONO = 2
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 106
try:
    TTF_HINTING_NONE = 3
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 220
def TTF_RenderText(font, text, fg, bg):
    return (TTF_RenderText_Shaded (font, text, fg, bg))

# /usr/include/SDL/SDL_ttf.h: 222
def TTF_RenderUTF8(font, text, fg, bg):
    return (TTF_RenderUTF8_Shaded (font, text, fg, bg))

# /usr/include/SDL/SDL_ttf.h: 224
def TTF_RenderUNICODE(font, text, fg, bg):
    return (TTF_RenderUNICODE_Shaded (font, text, fg, bg))

# /usr/include/SDL/SDL_ttf.h: 240
try:
    TTF_SetError = SDL_SetError
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 241
try:
    TTF_GetError = SDL_GetError
except:
    pass

_TTF_Font = struct__TTF_Font # /usr/include/SDL/SDL_ttf.h: 77

# No inserted files

