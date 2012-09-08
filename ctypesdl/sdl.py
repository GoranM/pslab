'''Wrapper for SDL.h

Generated with:
/usr/bin/ctypesgen -lSDL /usr/include/SDL/SDL.h /usr/include/SDL/SDL_video.h /usr/include/SDL/SDL_audio.h /usr/include/SDL/SDL_keyboard.h /usr/include/SDL/SDL_mouse.h /usr/include/SDL/SDL_events.h /usr/include/SDL/SDL_keysym.h /usr/include/SDL/SDL_error.h -o sdl.py

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

_libs["SDL"] = load_library("SDL")

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

enum_anon_27 = c_int # /usr/include/SDL/SDL_stdinc.h: 96

SDL_bool = enum_anon_27 # /usr/include/SDL/SDL_stdinc.h: 96

Uint8 = c_uint8 # /usr/include/SDL/SDL_stdinc.h: 99

Sint16 = c_int16 # /usr/include/SDL/SDL_stdinc.h: 100

Uint16 = c_uint16 # /usr/include/SDL/SDL_stdinc.h: 101

Sint32 = c_int32 # /usr/include/SDL/SDL_stdinc.h: 102

Uint32 = c_uint32 # /usr/include/SDL/SDL_stdinc.h: 103

# /usr/include/SDL/SDL_error.h: 43
if hasattr(_libs['SDL'], 'SDL_SetError'):
    _func = _libs['SDL'].SDL_SetError
    _restype = None
    _argtypes = [String]
    SDL_SetError = _variadic_function(_func,_restype,_argtypes)

# /usr/include/SDL/SDL_error.h: 44
if hasattr(_libs['SDL'], 'SDL_GetError'):
    SDL_GetError = _libs['SDL'].SDL_GetError
    SDL_GetError.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_GetError.restype = ReturnString
    else:
        SDL_GetError.restype = String
        SDL_GetError.errcheck = ReturnString

# /usr/include/SDL/SDL_error.h: 45
if hasattr(_libs['SDL'], 'SDL_ClearError'):
    SDL_ClearError = _libs['SDL'].SDL_ClearError
    SDL_ClearError.argtypes = []
    SDL_ClearError.restype = None

enum_anon_29 = c_int # /usr/include/SDL/SDL_error.h: 62

SDL_ENOMEM = 0 # /usr/include/SDL/SDL_error.h: 62

SDL_EFREAD = (SDL_ENOMEM + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_EFWRITE = (SDL_EFREAD + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_EFSEEK = (SDL_EFWRITE + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_UNSUPPORTED = (SDL_EFSEEK + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_LASTERROR = (SDL_UNSUPPORTED + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_errorcode = enum_anon_29 # /usr/include/SDL/SDL_error.h: 62

# /usr/include/SDL/SDL_error.h: 63
if hasattr(_libs['SDL'], 'SDL_Error'):
    SDL_Error = _libs['SDL'].SDL_Error
    SDL_Error.argtypes = [SDL_errorcode]
    SDL_Error.restype = None

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
if hasattr(_libs['SDL'], 'SDL_RWFromFile'):
    SDL_RWFromFile = _libs['SDL'].SDL_RWFromFile
    SDL_RWFromFile.argtypes = [String, String]
    SDL_RWFromFile.restype = POINTER(SDL_RWops)

# /usr/include/SDL/SDL_audio.h: 93
class struct_SDL_AudioSpec(Structure):
    pass

struct_SDL_AudioSpec.__slots__ = [
    'freq',
    'format',
    'channels',
    'silence',
    'samples',
    'padding',
    'size',
    'callback',
    'userdata',
]
struct_SDL_AudioSpec._fields_ = [
    ('freq', c_int),
    ('format', Uint16),
    ('channels', Uint8),
    ('silence', Uint8),
    ('samples', Uint16),
    ('padding', Uint16),
    ('size', Uint32),
    ('callback', CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(Uint8), c_int)),
    ('userdata', POINTER(None)),
]

SDL_AudioSpec = struct_SDL_AudioSpec # /usr/include/SDL/SDL_audio.h: 93

# /usr/include/SDL/SDL_audio.h: 126
class struct_SDL_AudioCVT(Structure):
    pass

struct_SDL_AudioCVT.__slots__ = [
    'needed',
    'src_format',
    'dst_format',
    'rate_incr',
    'buf',
    'len',
    'len_cvt',
    'len_mult',
    'len_ratio',
    'filters',
    'filter_index',
]
struct_SDL_AudioCVT._fields_ = [
    ('needed', c_int),
    ('src_format', Uint16),
    ('dst_format', Uint16),
    ('rate_incr', c_double),
    ('buf', POINTER(Uint8)),
    ('len', c_int),
    ('len_cvt', c_int),
    ('len_mult', c_int),
    ('len_ratio', c_double),
    ('filters', POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_SDL_AudioCVT), Uint16)) * 10),
    ('filter_index', c_int),
]

SDL_AudioCVT = struct_SDL_AudioCVT # /usr/include/SDL/SDL_audio.h: 138

# /usr/include/SDL/SDL_audio.h: 150
if hasattr(_libs['SDL'], 'SDL_AudioInit'):
    SDL_AudioInit = _libs['SDL'].SDL_AudioInit
    SDL_AudioInit.argtypes = [String]
    SDL_AudioInit.restype = c_int

# /usr/include/SDL/SDL_audio.h: 151
if hasattr(_libs['SDL'], 'SDL_AudioQuit'):
    SDL_AudioQuit = _libs['SDL'].SDL_AudioQuit
    SDL_AudioQuit.argtypes = []
    SDL_AudioQuit.restype = None

# /usr/include/SDL/SDL_audio.h: 159
if hasattr(_libs['SDL'], 'SDL_AudioDriverName'):
    SDL_AudioDriverName = _libs['SDL'].SDL_AudioDriverName
    SDL_AudioDriverName.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_AudioDriverName.restype = ReturnString
    else:
        SDL_AudioDriverName.restype = String
        SDL_AudioDriverName.errcheck = ReturnString

# /usr/include/SDL/SDL_audio.h: 178
if hasattr(_libs['SDL'], 'SDL_OpenAudio'):
    SDL_OpenAudio = _libs['SDL'].SDL_OpenAudio
    SDL_OpenAudio.argtypes = [POINTER(SDL_AudioSpec), POINTER(SDL_AudioSpec)]
    SDL_OpenAudio.restype = c_int

enum_anon_34 = c_int # /usr/include/SDL/SDL_audio.h: 184

SDL_AUDIO_STOPPED = 0 # /usr/include/SDL/SDL_audio.h: 184

SDL_AUDIO_PLAYING = (SDL_AUDIO_STOPPED + 1) # /usr/include/SDL/SDL_audio.h: 184

SDL_AUDIO_PAUSED = (SDL_AUDIO_PLAYING + 1) # /usr/include/SDL/SDL_audio.h: 184

SDL_audiostatus = enum_anon_34 # /usr/include/SDL/SDL_audio.h: 184

# /usr/include/SDL/SDL_audio.h: 187
if hasattr(_libs['SDL'], 'SDL_GetAudioStatus'):
    SDL_GetAudioStatus = _libs['SDL'].SDL_GetAudioStatus
    SDL_GetAudioStatus.argtypes = []
    SDL_GetAudioStatus.restype = SDL_audiostatus

# /usr/include/SDL/SDL_audio.h: 196
if hasattr(_libs['SDL'], 'SDL_PauseAudio'):
    SDL_PauseAudio = _libs['SDL'].SDL_PauseAudio
    SDL_PauseAudio.argtypes = [c_int]
    SDL_PauseAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 215
if hasattr(_libs['SDL'], 'SDL_LoadWAV_RW'):
    SDL_LoadWAV_RW = _libs['SDL'].SDL_LoadWAV_RW
    SDL_LoadWAV_RW.argtypes = [POINTER(SDL_RWops), c_int, POINTER(SDL_AudioSpec), POINTER(POINTER(Uint8)), POINTER(Uint32)]
    SDL_LoadWAV_RW.restype = POINTER(SDL_AudioSpec)

# /usr/include/SDL/SDL_audio.h: 224
if hasattr(_libs['SDL'], 'SDL_FreeWAV'):
    SDL_FreeWAV = _libs['SDL'].SDL_FreeWAV
    SDL_FreeWAV.argtypes = [POINTER(Uint8)]
    SDL_FreeWAV.restype = None

# /usr/include/SDL/SDL_audio.h: 234
if hasattr(_libs['SDL'], 'SDL_BuildAudioCVT'):
    SDL_BuildAudioCVT = _libs['SDL'].SDL_BuildAudioCVT
    SDL_BuildAudioCVT.argtypes = [POINTER(SDL_AudioCVT), Uint16, Uint8, c_int, Uint16, Uint8, c_int]
    SDL_BuildAudioCVT.restype = c_int

# /usr/include/SDL/SDL_audio.h: 247
if hasattr(_libs['SDL'], 'SDL_ConvertAudio'):
    SDL_ConvertAudio = _libs['SDL'].SDL_ConvertAudio
    SDL_ConvertAudio.argtypes = [POINTER(SDL_AudioCVT)]
    SDL_ConvertAudio.restype = c_int

# /usr/include/SDL/SDL_audio.h: 258
if hasattr(_libs['SDL'], 'SDL_MixAudio'):
    SDL_MixAudio = _libs['SDL'].SDL_MixAudio
    SDL_MixAudio.argtypes = [POINTER(Uint8), POINTER(Uint8), Uint32, c_int]
    SDL_MixAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 268
if hasattr(_libs['SDL'], 'SDL_LockAudio'):
    SDL_LockAudio = _libs['SDL'].SDL_LockAudio
    SDL_LockAudio.argtypes = []
    SDL_LockAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 269
if hasattr(_libs['SDL'], 'SDL_UnlockAudio'):
    SDL_UnlockAudio = _libs['SDL'].SDL_UnlockAudio
    SDL_UnlockAudio.argtypes = []
    SDL_UnlockAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 275
if hasattr(_libs['SDL'], 'SDL_CloseAudio'):
    SDL_CloseAudio = _libs['SDL'].SDL_CloseAudio
    SDL_CloseAudio.argtypes = []
    SDL_CloseAudio.restype = None

enum_anon_36 = c_int # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UNKNOWN = 0 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_FIRST = 0 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BACKSPACE = 8 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_TAB = 9 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_CLEAR = 12 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RETURN = 13 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PAUSE = 19 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_ESCAPE = 27 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SPACE = 32 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_EXCLAIM = 33 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_QUOTEDBL = 34 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_HASH = 35 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_DOLLAR = 36 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_AMPERSAND = 38 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_QUOTE = 39 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LEFTPAREN = 40 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RIGHTPAREN = 41 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_ASTERISK = 42 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PLUS = 43 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_COMMA = 44 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_MINUS = 45 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PERIOD = 46 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SLASH = 47 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_0 = 48 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_1 = 49 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_2 = 50 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_3 = 51 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_4 = 52 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_5 = 53 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_6 = 54 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_7 = 55 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_8 = 56 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_9 = 57 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_COLON = 58 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SEMICOLON = 59 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LESS = 60 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_EQUALS = 61 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_GREATER = 62 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_QUESTION = 63 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_AT = 64 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LEFTBRACKET = 91 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BACKSLASH = 92 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RIGHTBRACKET = 93 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_CARET = 94 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UNDERSCORE = 95 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BACKQUOTE = 96 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_a = 97 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_b = 98 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_c = 99 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_d = 100 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_e = 101 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_f = 102 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_g = 103 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_h = 104 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_i = 105 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_j = 106 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_k = 107 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_l = 108 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_m = 109 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_n = 110 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_o = 111 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_p = 112 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_q = 113 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_r = 114 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_s = 115 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_t = 116 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_u = 117 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_v = 118 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_w = 119 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_x = 120 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_y = 121 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_z = 122 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_DELETE = 127 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_0 = 160 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_1 = 161 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_2 = 162 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_3 = 163 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_4 = 164 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_5 = 165 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_6 = 166 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_7 = 167 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_8 = 168 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_9 = 169 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_10 = 170 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_11 = 171 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_12 = 172 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_13 = 173 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_14 = 174 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_15 = 175 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_16 = 176 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_17 = 177 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_18 = 178 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_19 = 179 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_20 = 180 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_21 = 181 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_22 = 182 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_23 = 183 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_24 = 184 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_25 = 185 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_26 = 186 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_27 = 187 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_28 = 188 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_29 = 189 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_30 = 190 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_31 = 191 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_32 = 192 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_33 = 193 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_34 = 194 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_35 = 195 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_36 = 196 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_37 = 197 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_38 = 198 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_39 = 199 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_40 = 200 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_41 = 201 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_42 = 202 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_43 = 203 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_44 = 204 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_45 = 205 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_46 = 206 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_47 = 207 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_48 = 208 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_49 = 209 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_50 = 210 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_51 = 211 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_52 = 212 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_53 = 213 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_54 = 214 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_55 = 215 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_56 = 216 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_57 = 217 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_58 = 218 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_59 = 219 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_60 = 220 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_61 = 221 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_62 = 222 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_63 = 223 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_64 = 224 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_65 = 225 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_66 = 226 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_67 = 227 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_68 = 228 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_69 = 229 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_70 = 230 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_71 = 231 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_72 = 232 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_73 = 233 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_74 = 234 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_75 = 235 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_76 = 236 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_77 = 237 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_78 = 238 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_79 = 239 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_80 = 240 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_81 = 241 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_82 = 242 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_83 = 243 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_84 = 244 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_85 = 245 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_86 = 246 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_87 = 247 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_88 = 248 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_89 = 249 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_90 = 250 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_91 = 251 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_92 = 252 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_93 = 253 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_94 = 254 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_95 = 255 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP0 = 256 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP1 = 257 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP2 = 258 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP3 = 259 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP4 = 260 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP5 = 261 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP6 = 262 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP7 = 263 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP8 = 264 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP9 = 265 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_PERIOD = 266 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_DIVIDE = 267 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_MULTIPLY = 268 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_MINUS = 269 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_PLUS = 270 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_ENTER = 271 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_EQUALS = 272 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UP = 273 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_DOWN = 274 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RIGHT = 275 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LEFT = 276 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_INSERT = 277 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_HOME = 278 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_END = 279 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PAGEUP = 280 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PAGEDOWN = 281 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F1 = 282 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F2 = 283 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F3 = 284 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F4 = 285 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F5 = 286 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F6 = 287 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F7 = 288 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F8 = 289 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F9 = 290 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F10 = 291 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F11 = 292 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F12 = 293 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F13 = 294 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F14 = 295 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F15 = 296 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_NUMLOCK = 300 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_CAPSLOCK = 301 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SCROLLOCK = 302 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RSHIFT = 303 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LSHIFT = 304 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RCTRL = 305 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LCTRL = 306 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RALT = 307 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LALT = 308 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RMETA = 309 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LMETA = 310 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LSUPER = 311 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RSUPER = 312 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_MODE = 313 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_COMPOSE = 314 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_HELP = 315 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PRINT = 316 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SYSREQ = 317 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BREAK = 318 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_MENU = 319 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_POWER = 320 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_EURO = 321 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UNDO = 322 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LAST = (SDLK_UNDO + 1) # /usr/include/SDL/SDL_keysym.h: 302

SDLKey = enum_anon_36 # /usr/include/SDL/SDL_keysym.h: 302

enum_anon_37 = c_int # /usr/include/SDL/SDL_keysym.h: 319

KMOD_NONE = 0 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LSHIFT = 1 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RSHIFT = 2 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LCTRL = 64 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RCTRL = 128 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LALT = 256 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RALT = 512 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LMETA = 1024 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RMETA = 2048 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_NUM = 4096 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_CAPS = 8192 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_MODE = 16384 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RESERVED = 32768 # /usr/include/SDL/SDL_keysym.h: 319

SDLMod = enum_anon_37 # /usr/include/SDL/SDL_keysym.h: 319

# /usr/include/SDL/SDL_keyboard.h: 64
class struct_SDL_keysym(Structure):
    pass

struct_SDL_keysym.__slots__ = [
    'scancode',
    'sym',
    'mod',
    'unicode',
]
struct_SDL_keysym._fields_ = [
    ('scancode', Uint8),
    ('sym', SDLKey),
    ('mod', SDLMod),
    ('unicode', Uint16),
]

SDL_keysym = struct_SDL_keysym # /usr/include/SDL/SDL_keyboard.h: 64

# /usr/include/SDL/SDL_keyboard.h: 82
if hasattr(_libs['SDL'], 'SDL_EnableUNICODE'):
    SDL_EnableUNICODE = _libs['SDL'].SDL_EnableUNICODE
    SDL_EnableUNICODE.argtypes = [c_int]
    SDL_EnableUNICODE.restype = c_int

# /usr/include/SDL/SDL_keyboard.h: 98
if hasattr(_libs['SDL'], 'SDL_EnableKeyRepeat'):
    SDL_EnableKeyRepeat = _libs['SDL'].SDL_EnableKeyRepeat
    SDL_EnableKeyRepeat.argtypes = [c_int, c_int]
    SDL_EnableKeyRepeat.restype = c_int

# /usr/include/SDL/SDL_keyboard.h: 99
if hasattr(_libs['SDL'], 'SDL_GetKeyRepeat'):
    SDL_GetKeyRepeat = _libs['SDL'].SDL_GetKeyRepeat
    SDL_GetKeyRepeat.argtypes = [POINTER(c_int), POINTER(c_int)]
    SDL_GetKeyRepeat.restype = None

# /usr/include/SDL/SDL_keyboard.h: 110
if hasattr(_libs['SDL'], 'SDL_GetKeyState'):
    SDL_GetKeyState = _libs['SDL'].SDL_GetKeyState
    SDL_GetKeyState.argtypes = [POINTER(c_int)]
    SDL_GetKeyState.restype = POINTER(Uint8)

# /usr/include/SDL/SDL_keyboard.h: 115
if hasattr(_libs['SDL'], 'SDL_GetModState'):
    SDL_GetModState = _libs['SDL'].SDL_GetModState
    SDL_GetModState.argtypes = []
    SDL_GetModState.restype = SDLMod

# /usr/include/SDL/SDL_keyboard.h: 121
if hasattr(_libs['SDL'], 'SDL_SetModState'):
    SDL_SetModState = _libs['SDL'].SDL_SetModState
    SDL_SetModState.argtypes = [SDLMod]
    SDL_SetModState.restype = None

# /usr/include/SDL/SDL_keyboard.h: 126
if hasattr(_libs['SDL'], 'SDL_GetKeyName'):
    SDL_GetKeyName = _libs['SDL'].SDL_GetKeyName
    SDL_GetKeyName.argtypes = [SDLKey]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_GetKeyName.restype = ReturnString
    else:
        SDL_GetKeyName.restype = String
        SDL_GetKeyName.errcheck = ReturnString

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

SDL_blit = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_Surface), POINTER(SDL_Rect), POINTER(struct_SDL_Surface), POINTER(SDL_Rect)) # /usr/include/SDL/SDL_video.h: 166

# /usr/include/SDL/SDL_video.h: 188
class struct_SDL_VideoInfo(Structure):
    pass

struct_SDL_VideoInfo.__slots__ = [
    'hw_available',
    'wm_available',
    'UnusedBits1',
    'UnusedBits2',
    'blit_hw',
    'blit_hw_CC',
    'blit_hw_A',
    'blit_sw',
    'blit_sw_CC',
    'blit_sw_A',
    'blit_fill',
    'UnusedBits3',
    'video_mem',
    'vfmt',
    'current_w',
    'current_h',
]
struct_SDL_VideoInfo._fields_ = [
    ('hw_available', Uint32, 1),
    ('wm_available', Uint32, 1),
    ('UnusedBits1', Uint32, 6),
    ('UnusedBits2', Uint32, 1),
    ('blit_hw', Uint32, 1),
    ('blit_hw_CC', Uint32, 1),
    ('blit_hw_A', Uint32, 1),
    ('blit_sw', Uint32, 1),
    ('blit_sw_CC', Uint32, 1),
    ('blit_sw_A', Uint32, 1),
    ('blit_fill', Uint32, 1),
    ('UnusedBits3', Uint32, 16),
    ('video_mem', Uint32),
    ('vfmt', POINTER(SDL_PixelFormat)),
    ('current_w', c_int),
    ('current_h', c_int),
]

SDL_VideoInfo = struct_SDL_VideoInfo # /usr/include/SDL/SDL_video.h: 188

# /usr/include/SDL/SDL_video.h: 217
class struct_private_yuvhwfuncs(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 218
class struct_private_yuvhwdata(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 226
class struct_SDL_Overlay(Structure):
    pass

struct_SDL_Overlay.__slots__ = [
    'format',
    'w',
    'h',
    'planes',
    'pitches',
    'pixels',
    'hwfuncs',
    'hwdata',
    'hw_overlay',
    'UnusedBits',
]
struct_SDL_Overlay._fields_ = [
    ('format', Uint32),
    ('w', c_int),
    ('h', c_int),
    ('planes', c_int),
    ('pitches', POINTER(Uint16)),
    ('pixels', POINTER(POINTER(Uint8))),
    ('hwfuncs', POINTER(struct_private_yuvhwfuncs)),
    ('hwdata', POINTER(struct_private_yuvhwdata)),
    ('hw_overlay', Uint32, 1),
    ('UnusedBits', Uint32, 31),
]

SDL_Overlay = struct_SDL_Overlay # /usr/include/SDL/SDL_video.h: 226

enum_anon_38 = c_int # /usr/include/SDL/SDL_video.h: 248

SDL_GL_RED_SIZE = 0 # /usr/include/SDL/SDL_video.h: 248

SDL_GL_GREEN_SIZE = (SDL_GL_RED_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_BLUE_SIZE = (SDL_GL_GREEN_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ALPHA_SIZE = (SDL_GL_BLUE_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_BUFFER_SIZE = (SDL_GL_ALPHA_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_DOUBLEBUFFER = (SDL_GL_BUFFER_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_DEPTH_SIZE = (SDL_GL_DOUBLEBUFFER + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_STENCIL_SIZE = (SDL_GL_DEPTH_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_RED_SIZE = (SDL_GL_STENCIL_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_GREEN_SIZE = (SDL_GL_ACCUM_RED_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_BLUE_SIZE = (SDL_GL_ACCUM_GREEN_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_ALPHA_SIZE = (SDL_GL_ACCUM_BLUE_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_STEREO = (SDL_GL_ACCUM_ALPHA_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_MULTISAMPLEBUFFERS = (SDL_GL_STEREO + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_MULTISAMPLESAMPLES = (SDL_GL_MULTISAMPLEBUFFERS + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCELERATED_VISUAL = (SDL_GL_MULTISAMPLESAMPLES + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_SWAP_CONTROL = (SDL_GL_ACCELERATED_VISUAL + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GLattr = enum_anon_38 # /usr/include/SDL/SDL_video.h: 248

# /usr/include/SDL/SDL_video.h: 275
if hasattr(_libs['SDL'], 'SDL_VideoInit'):
    SDL_VideoInit = _libs['SDL'].SDL_VideoInit
    SDL_VideoInit.argtypes = [String, Uint32]
    SDL_VideoInit.restype = c_int

# /usr/include/SDL/SDL_video.h: 276
if hasattr(_libs['SDL'], 'SDL_VideoQuit'):
    SDL_VideoQuit = _libs['SDL'].SDL_VideoQuit
    SDL_VideoQuit.argtypes = []
    SDL_VideoQuit.restype = None

# /usr/include/SDL/SDL_video.h: 284
if hasattr(_libs['SDL'], 'SDL_VideoDriverName'):
    SDL_VideoDriverName = _libs['SDL'].SDL_VideoDriverName
    SDL_VideoDriverName.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_VideoDriverName.restype = ReturnString
    else:
        SDL_VideoDriverName.restype = String
        SDL_VideoDriverName.errcheck = ReturnString

# /usr/include/SDL/SDL_video.h: 292
if hasattr(_libs['SDL'], 'SDL_GetVideoSurface'):
    SDL_GetVideoSurface = _libs['SDL'].SDL_GetVideoSurface
    SDL_GetVideoSurface.argtypes = []
    SDL_GetVideoSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 300
if hasattr(_libs['SDL'], 'SDL_GetVideoInfo'):
    SDL_GetVideoInfo = _libs['SDL'].SDL_GetVideoInfo
    SDL_GetVideoInfo.argtypes = []
    SDL_GetVideoInfo.restype = POINTER(SDL_VideoInfo)

# /usr/include/SDL/SDL_video.h: 313
if hasattr(_libs['SDL'], 'SDL_VideoModeOK'):
    SDL_VideoModeOK = _libs['SDL'].SDL_VideoModeOK
    SDL_VideoModeOK.argtypes = [c_int, c_int, c_int, Uint32]
    SDL_VideoModeOK.restype = c_int

# /usr/include/SDL/SDL_video.h: 324
if hasattr(_libs['SDL'], 'SDL_ListModes'):
    SDL_ListModes = _libs['SDL'].SDL_ListModes
    SDL_ListModes.argtypes = [POINTER(SDL_PixelFormat), Uint32]
    SDL_ListModes.restype = POINTER(POINTER(SDL_Rect))

# /usr/include/SDL/SDL_video.h: 384
if hasattr(_libs['SDL'], 'SDL_SetVideoMode'):
    SDL_SetVideoMode = _libs['SDL'].SDL_SetVideoMode
    SDL_SetVideoMode.argtypes = [c_int, c_int, c_int, Uint32]
    SDL_SetVideoMode.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 394
if hasattr(_libs['SDL'], 'SDL_UpdateRects'):
    SDL_UpdateRects = _libs['SDL'].SDL_UpdateRects
    SDL_UpdateRects.argtypes = [POINTER(SDL_Surface), c_int, POINTER(SDL_Rect)]
    SDL_UpdateRects.restype = None

# /usr/include/SDL/SDL_video.h: 400
if hasattr(_libs['SDL'], 'SDL_UpdateRect'):
    SDL_UpdateRect = _libs['SDL'].SDL_UpdateRect
    SDL_UpdateRect.argtypes = [POINTER(SDL_Surface), Sint32, Sint32, Uint32, Uint32]
    SDL_UpdateRect.restype = None

# /usr/include/SDL/SDL_video.h: 414
if hasattr(_libs['SDL'], 'SDL_Flip'):
    SDL_Flip = _libs['SDL'].SDL_Flip
    SDL_Flip.argtypes = [POINTER(SDL_Surface)]
    SDL_Flip.restype = c_int

# /usr/include/SDL/SDL_video.h: 424
if hasattr(_libs['SDL'], 'SDL_SetGamma'):
    SDL_SetGamma = _libs['SDL'].SDL_SetGamma
    SDL_SetGamma.argtypes = [c_float, c_float, c_float]
    SDL_SetGamma.restype = c_int

# /usr/include/SDL/SDL_video.h: 438
if hasattr(_libs['SDL'], 'SDL_SetGammaRamp'):
    SDL_SetGammaRamp = _libs['SDL'].SDL_SetGammaRamp
    SDL_SetGammaRamp.argtypes = [POINTER(Uint16), POINTER(Uint16), POINTER(Uint16)]
    SDL_SetGammaRamp.restype = c_int

# /usr/include/SDL/SDL_video.h: 449
if hasattr(_libs['SDL'], 'SDL_GetGammaRamp'):
    SDL_GetGammaRamp = _libs['SDL'].SDL_GetGammaRamp
    SDL_GetGammaRamp.argtypes = [POINTER(Uint16), POINTER(Uint16), POINTER(Uint16)]
    SDL_GetGammaRamp.restype = c_int

# /usr/include/SDL/SDL_video.h: 466
if hasattr(_libs['SDL'], 'SDL_SetColors'):
    SDL_SetColors = _libs['SDL'].SDL_SetColors
    SDL_SetColors.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Color), c_int, c_int]
    SDL_SetColors.restype = c_int

# /usr/include/SDL/SDL_video.h: 485
if hasattr(_libs['SDL'], 'SDL_SetPalette'):
    SDL_SetPalette = _libs['SDL'].SDL_SetPalette
    SDL_SetPalette.argtypes = [POINTER(SDL_Surface), c_int, POINTER(SDL_Color), c_int, c_int]
    SDL_SetPalette.restype = c_int

# /usr/include/SDL/SDL_video.h: 492
if hasattr(_libs['SDL'], 'SDL_MapRGB'):
    SDL_MapRGB = _libs['SDL'].SDL_MapRGB
    SDL_MapRGB.argtypes = [POINTER(SDL_PixelFormat), Uint8, Uint8, Uint8]
    SDL_MapRGB.restype = Uint32

# /usr/include/SDL/SDL_video.h: 499
if hasattr(_libs['SDL'], 'SDL_MapRGBA'):
    SDL_MapRGBA = _libs['SDL'].SDL_MapRGBA
    SDL_MapRGBA.argtypes = [POINTER(SDL_PixelFormat), Uint8, Uint8, Uint8, Uint8]
    SDL_MapRGBA.restype = Uint32

# /usr/include/SDL/SDL_video.h: 506
if hasattr(_libs['SDL'], 'SDL_GetRGB'):
    SDL_GetRGB = _libs['SDL'].SDL_GetRGB
    SDL_GetRGB.argtypes = [Uint32, POINTER(SDL_PixelFormat), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
    SDL_GetRGB.restype = None

# /usr/include/SDL/SDL_video.h: 513
if hasattr(_libs['SDL'], 'SDL_GetRGBA'):
    SDL_GetRGBA = _libs['SDL'].SDL_GetRGBA
    SDL_GetRGBA.argtypes = [Uint32, POINTER(SDL_PixelFormat), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
    SDL_GetRGBA.restype = None

# /usr/include/SDL/SDL_video.h: 553
if hasattr(_libs['SDL'], 'SDL_CreateRGBSurface'):
    SDL_CreateRGBSurface = _libs['SDL'].SDL_CreateRGBSurface
    SDL_CreateRGBSurface.argtypes = [Uint32, c_int, c_int, c_int, Uint32, Uint32, Uint32, Uint32]
    SDL_CreateRGBSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 557
if hasattr(_libs['SDL'], 'SDL_CreateRGBSurfaceFrom'):
    SDL_CreateRGBSurfaceFrom = _libs['SDL'].SDL_CreateRGBSurfaceFrom
    SDL_CreateRGBSurfaceFrom.argtypes = [POINTER(None), c_int, c_int, c_int, c_int, Uint32, Uint32, Uint32, Uint32]
    SDL_CreateRGBSurfaceFrom.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 560
if hasattr(_libs['SDL'], 'SDL_FreeSurface'):
    SDL_FreeSurface = _libs['SDL'].SDL_FreeSurface
    SDL_FreeSurface.argtypes = [POINTER(SDL_Surface)]
    SDL_FreeSurface.restype = None

# /usr/include/SDL/SDL_video.h: 580
if hasattr(_libs['SDL'], 'SDL_LockSurface'):
    SDL_LockSurface = _libs['SDL'].SDL_LockSurface
    SDL_LockSurface.argtypes = [POINTER(SDL_Surface)]
    SDL_LockSurface.restype = c_int

# /usr/include/SDL/SDL_video.h: 581
if hasattr(_libs['SDL'], 'SDL_UnlockSurface'):
    SDL_UnlockSurface = _libs['SDL'].SDL_UnlockSurface
    SDL_UnlockSurface.argtypes = [POINTER(SDL_Surface)]
    SDL_UnlockSurface.restype = None

# /usr/include/SDL/SDL_video.h: 589
if hasattr(_libs['SDL'], 'SDL_LoadBMP_RW'):
    SDL_LoadBMP_RW = _libs['SDL'].SDL_LoadBMP_RW
    SDL_LoadBMP_RW.argtypes = [POINTER(SDL_RWops), c_int]
    SDL_LoadBMP_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 599
if hasattr(_libs['SDL'], 'SDL_SaveBMP_RW'):
    SDL_SaveBMP_RW = _libs['SDL'].SDL_SaveBMP_RW
    SDL_SaveBMP_RW.argtypes = [POINTER(SDL_Surface), POINTER(SDL_RWops), c_int]
    SDL_SaveBMP_RW.restype = c_int

# /usr/include/SDL/SDL_video.h: 615
if hasattr(_libs['SDL'], 'SDL_SetColorKey'):
    SDL_SetColorKey = _libs['SDL'].SDL_SetColorKey
    SDL_SetColorKey.argtypes = [POINTER(SDL_Surface), Uint32, Uint32]
    SDL_SetColorKey.restype = c_int

# /usr/include/SDL/SDL_video.h: 633
if hasattr(_libs['SDL'], 'SDL_SetAlpha'):
    SDL_SetAlpha = _libs['SDL'].SDL_SetAlpha
    SDL_SetAlpha.argtypes = [POINTER(SDL_Surface), Uint32, Uint8]
    SDL_SetAlpha.restype = c_int

# /usr/include/SDL/SDL_video.h: 647
if hasattr(_libs['SDL'], 'SDL_SetClipRect'):
    SDL_SetClipRect = _libs['SDL'].SDL_SetClipRect
    SDL_SetClipRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_SetClipRect.restype = SDL_bool

# /usr/include/SDL/SDL_video.h: 654
if hasattr(_libs['SDL'], 'SDL_GetClipRect'):
    SDL_GetClipRect = _libs['SDL'].SDL_GetClipRect
    SDL_GetClipRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_GetClipRect.restype = None

# /usr/include/SDL/SDL_video.h: 668
if hasattr(_libs['SDL'], 'SDL_ConvertSurface'):
    SDL_ConvertSurface = _libs['SDL'].SDL_ConvertSurface
    SDL_ConvertSurface.argtypes = [POINTER(SDL_Surface), POINTER(SDL_PixelFormat), Uint32]
    SDL_ConvertSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 748
if hasattr(_libs['SDL'], 'SDL_UpperBlit'):
    SDL_UpperBlit = _libs['SDL'].SDL_UpperBlit
    SDL_UpperBlit.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_UpperBlit.restype = c_int

# /usr/include/SDL/SDL_video.h: 754
if hasattr(_libs['SDL'], 'SDL_LowerBlit'):
    SDL_LowerBlit = _libs['SDL'].SDL_LowerBlit
    SDL_LowerBlit.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_LowerBlit.restype = c_int

# /usr/include/SDL/SDL_video.h: 767
if hasattr(_libs['SDL'], 'SDL_FillRect'):
    SDL_FillRect = _libs['SDL'].SDL_FillRect
    SDL_FillRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), Uint32]
    SDL_FillRect.restype = c_int

# /usr/include/SDL/SDL_video.h: 781
if hasattr(_libs['SDL'], 'SDL_DisplayFormat'):
    SDL_DisplayFormat = _libs['SDL'].SDL_DisplayFormat
    SDL_DisplayFormat.argtypes = [POINTER(SDL_Surface)]
    SDL_DisplayFormat.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 795
if hasattr(_libs['SDL'], 'SDL_DisplayFormatAlpha'):
    SDL_DisplayFormatAlpha = _libs['SDL'].SDL_DisplayFormatAlpha
    SDL_DisplayFormatAlpha.argtypes = [POINTER(SDL_Surface)]
    SDL_DisplayFormatAlpha.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 807
if hasattr(_libs['SDL'], 'SDL_CreateYUVOverlay'):
    SDL_CreateYUVOverlay = _libs['SDL'].SDL_CreateYUVOverlay
    SDL_CreateYUVOverlay.argtypes = [c_int, c_int, Uint32, POINTER(SDL_Surface)]
    SDL_CreateYUVOverlay.restype = POINTER(SDL_Overlay)

# /usr/include/SDL/SDL_video.h: 811
if hasattr(_libs['SDL'], 'SDL_LockYUVOverlay'):
    SDL_LockYUVOverlay = _libs['SDL'].SDL_LockYUVOverlay
    SDL_LockYUVOverlay.argtypes = [POINTER(SDL_Overlay)]
    SDL_LockYUVOverlay.restype = c_int

# /usr/include/SDL/SDL_video.h: 812
if hasattr(_libs['SDL'], 'SDL_UnlockYUVOverlay'):
    SDL_UnlockYUVOverlay = _libs['SDL'].SDL_UnlockYUVOverlay
    SDL_UnlockYUVOverlay.argtypes = [POINTER(SDL_Overlay)]
    SDL_UnlockYUVOverlay.restype = None

# /usr/include/SDL/SDL_video.h: 820
if hasattr(_libs['SDL'], 'SDL_DisplayYUVOverlay'):
    SDL_DisplayYUVOverlay = _libs['SDL'].SDL_DisplayYUVOverlay
    SDL_DisplayYUVOverlay.argtypes = [POINTER(SDL_Overlay), POINTER(SDL_Rect)]
    SDL_DisplayYUVOverlay.restype = c_int

# /usr/include/SDL/SDL_video.h: 823
if hasattr(_libs['SDL'], 'SDL_FreeYUVOverlay'):
    SDL_FreeYUVOverlay = _libs['SDL'].SDL_FreeYUVOverlay
    SDL_FreeYUVOverlay.argtypes = [POINTER(SDL_Overlay)]
    SDL_FreeYUVOverlay.restype = None

# /usr/include/SDL/SDL_video.h: 837
if hasattr(_libs['SDL'], 'SDL_GL_LoadLibrary'):
    SDL_GL_LoadLibrary = _libs['SDL'].SDL_GL_LoadLibrary
    SDL_GL_LoadLibrary.argtypes = [String]
    SDL_GL_LoadLibrary.restype = c_int

# /usr/include/SDL/SDL_video.h: 842
if hasattr(_libs['SDL'], 'SDL_GL_GetProcAddress'):
    SDL_GL_GetProcAddress = _libs['SDL'].SDL_GL_GetProcAddress
    SDL_GL_GetProcAddress.argtypes = [String]
    SDL_GL_GetProcAddress.restype = POINTER(None)

# /usr/include/SDL/SDL_video.h: 847
if hasattr(_libs['SDL'], 'SDL_GL_SetAttribute'):
    SDL_GL_SetAttribute = _libs['SDL'].SDL_GL_SetAttribute
    SDL_GL_SetAttribute.argtypes = [SDL_GLattr, c_int]
    SDL_GL_SetAttribute.restype = c_int

# /usr/include/SDL/SDL_video.h: 858
if hasattr(_libs['SDL'], 'SDL_GL_GetAttribute'):
    SDL_GL_GetAttribute = _libs['SDL'].SDL_GL_GetAttribute
    SDL_GL_GetAttribute.argtypes = [SDL_GLattr, POINTER(c_int)]
    SDL_GL_GetAttribute.restype = c_int

# /usr/include/SDL/SDL_video.h: 863
if hasattr(_libs['SDL'], 'SDL_GL_SwapBuffers'):
    SDL_GL_SwapBuffers = _libs['SDL'].SDL_GL_SwapBuffers
    SDL_GL_SwapBuffers.argtypes = []
    SDL_GL_SwapBuffers.restype = None

# /usr/include/SDL/SDL_video.h: 870
if hasattr(_libs['SDL'], 'SDL_GL_UpdateRects'):
    SDL_GL_UpdateRects = _libs['SDL'].SDL_GL_UpdateRects
    SDL_GL_UpdateRects.argtypes = [c_int, POINTER(SDL_Rect)]
    SDL_GL_UpdateRects.restype = None

# /usr/include/SDL/SDL_video.h: 871
if hasattr(_libs['SDL'], 'SDL_GL_Lock'):
    SDL_GL_Lock = _libs['SDL'].SDL_GL_Lock
    SDL_GL_Lock.argtypes = []
    SDL_GL_Lock.restype = None

# /usr/include/SDL/SDL_video.h: 872
if hasattr(_libs['SDL'], 'SDL_GL_Unlock'):
    SDL_GL_Unlock = _libs['SDL'].SDL_GL_Unlock
    SDL_GL_Unlock.argtypes = []
    SDL_GL_Unlock.restype = None

# /usr/include/SDL/SDL_video.h: 885
if hasattr(_libs['SDL'], 'SDL_WM_SetCaption'):
    SDL_WM_SetCaption = _libs['SDL'].SDL_WM_SetCaption
    SDL_WM_SetCaption.argtypes = [String, String]
    SDL_WM_SetCaption.restype = None

# /usr/include/SDL/SDL_video.h: 889
if hasattr(_libs['SDL'], 'SDL_WM_GetCaption'):
    SDL_WM_GetCaption = _libs['SDL'].SDL_WM_GetCaption
    SDL_WM_GetCaption.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    SDL_WM_GetCaption.restype = None

# /usr/include/SDL/SDL_video.h: 897
if hasattr(_libs['SDL'], 'SDL_WM_SetIcon'):
    SDL_WM_SetIcon = _libs['SDL'].SDL_WM_SetIcon
    SDL_WM_SetIcon.argtypes = [POINTER(SDL_Surface), POINTER(Uint8)]
    SDL_WM_SetIcon.restype = None

# /usr/include/SDL/SDL_video.h: 904
if hasattr(_libs['SDL'], 'SDL_WM_IconifyWindow'):
    SDL_WM_IconifyWindow = _libs['SDL'].SDL_WM_IconifyWindow
    SDL_WM_IconifyWindow.argtypes = []
    SDL_WM_IconifyWindow.restype = c_int

# /usr/include/SDL/SDL_video.h: 921
if hasattr(_libs['SDL'], 'SDL_WM_ToggleFullScreen'):
    SDL_WM_ToggleFullScreen = _libs['SDL'].SDL_WM_ToggleFullScreen
    SDL_WM_ToggleFullScreen.argtypes = [POINTER(SDL_Surface)]
    SDL_WM_ToggleFullScreen.restype = c_int

enum_anon_39 = c_int # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_QUERY = (-1) # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_OFF = 0 # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_ON = 1 # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_FULLSCREEN = (SDL_GRAB_ON + 1) # /usr/include/SDL/SDL_video.h: 928

SDL_GrabMode = enum_anon_39 # /usr/include/SDL/SDL_video.h: 928

# /usr/include/SDL/SDL_video.h: 937
if hasattr(_libs['SDL'], 'SDL_WM_GrabInput'):
    SDL_WM_GrabInput = _libs['SDL'].SDL_WM_GrabInput
    SDL_WM_GrabInput.argtypes = [SDL_GrabMode]
    SDL_WM_GrabInput.restype = SDL_GrabMode

# /usr/include/SDL/SDL_video.h: 942
if hasattr(_libs['SDL'], 'SDL_SoftStretch'):
    SDL_SoftStretch = _libs['SDL'].SDL_SoftStretch
    SDL_SoftStretch.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_SoftStretch.restype = c_int

# /usr/include/SDL/SDL_mouse.h: 40
class struct_WMcursor(Structure):
    pass

WMcursor = struct_WMcursor # /usr/include/SDL/SDL_mouse.h: 40

# /usr/include/SDL/SDL_mouse.h: 48
class struct_SDL_Cursor(Structure):
    pass

struct_SDL_Cursor.__slots__ = [
    'area',
    'hot_x',
    'hot_y',
    'data',
    'mask',
    'save',
    'wm_cursor',
]
struct_SDL_Cursor._fields_ = [
    ('area', SDL_Rect),
    ('hot_x', Sint16),
    ('hot_y', Sint16),
    ('data', POINTER(Uint8)),
    ('mask', POINTER(Uint8)),
    ('save', POINTER(Uint8) * 2),
    ('wm_cursor', POINTER(WMcursor)),
]

SDL_Cursor = struct_SDL_Cursor # /usr/include/SDL/SDL_mouse.h: 48

# /usr/include/SDL/SDL_mouse.h: 57
if hasattr(_libs['SDL'], 'SDL_GetMouseState'):
    SDL_GetMouseState = _libs['SDL'].SDL_GetMouseState
    SDL_GetMouseState.argtypes = [POINTER(c_int), POINTER(c_int)]
    SDL_GetMouseState.restype = Uint8

# /usr/include/SDL/SDL_mouse.h: 65
if hasattr(_libs['SDL'], 'SDL_GetRelativeMouseState'):
    SDL_GetRelativeMouseState = _libs['SDL'].SDL_GetRelativeMouseState
    SDL_GetRelativeMouseState.argtypes = [POINTER(c_int), POINTER(c_int)]
    SDL_GetRelativeMouseState.restype = Uint8

# /usr/include/SDL/SDL_mouse.h: 70
if hasattr(_libs['SDL'], 'SDL_WarpMouse'):
    SDL_WarpMouse = _libs['SDL'].SDL_WarpMouse
    SDL_WarpMouse.argtypes = [Uint16, Uint16]
    SDL_WarpMouse.restype = None

# /usr/include/SDL/SDL_mouse.h: 85
if hasattr(_libs['SDL'], 'SDL_CreateCursor'):
    SDL_CreateCursor = _libs['SDL'].SDL_CreateCursor
    SDL_CreateCursor.argtypes = [POINTER(Uint8), POINTER(Uint8), c_int, c_int, c_int, c_int]
    SDL_CreateCursor.restype = POINTER(SDL_Cursor)

# /usr/include/SDL/SDL_mouse.h: 93
if hasattr(_libs['SDL'], 'SDL_SetCursor'):
    SDL_SetCursor = _libs['SDL'].SDL_SetCursor
    SDL_SetCursor.argtypes = [POINTER(SDL_Cursor)]
    SDL_SetCursor.restype = None

# /usr/include/SDL/SDL_mouse.h: 98
if hasattr(_libs['SDL'], 'SDL_GetCursor'):
    SDL_GetCursor = _libs['SDL'].SDL_GetCursor
    SDL_GetCursor.argtypes = []
    SDL_GetCursor.restype = POINTER(SDL_Cursor)

# /usr/include/SDL/SDL_mouse.h: 103
if hasattr(_libs['SDL'], 'SDL_FreeCursor'):
    SDL_FreeCursor = _libs['SDL'].SDL_FreeCursor
    SDL_FreeCursor.argtypes = [POINTER(SDL_Cursor)]
    SDL_FreeCursor.restype = None

# /usr/include/SDL/SDL_mouse.h: 112
if hasattr(_libs['SDL'], 'SDL_ShowCursor'):
    SDL_ShowCursor = _libs['SDL'].SDL_ShowCursor
    SDL_ShowCursor.argtypes = [c_int]
    SDL_ShowCursor.restype = c_int

enum_anon_40 = c_int # /usr/include/SDL/SDL_events.h: 83

SDL_NOEVENT = 0 # /usr/include/SDL/SDL_events.h: 83

SDL_ACTIVEEVENT = (SDL_NOEVENT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_KEYDOWN = (SDL_ACTIVEEVENT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_KEYUP = (SDL_KEYDOWN + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_MOUSEMOTION = (SDL_KEYUP + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_MOUSEBUTTONDOWN = (SDL_MOUSEMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_MOUSEBUTTONUP = (SDL_MOUSEBUTTONDOWN + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYAXISMOTION = (SDL_MOUSEBUTTONUP + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYBALLMOTION = (SDL_JOYAXISMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYHATMOTION = (SDL_JOYBALLMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYBUTTONDOWN = (SDL_JOYHATMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYBUTTONUP = (SDL_JOYBUTTONDOWN + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_QUIT = (SDL_JOYBUTTONUP + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_SYSWMEVENT = (SDL_QUIT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVEDA = (SDL_SYSWMEVENT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVEDB = (SDL_EVENT_RESERVEDA + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_VIDEORESIZE = (SDL_EVENT_RESERVEDB + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_VIDEOEXPOSE = (SDL_VIDEORESIZE + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED2 = (SDL_VIDEOEXPOSE + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED3 = (SDL_EVENT_RESERVED2 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED4 = (SDL_EVENT_RESERVED3 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED5 = (SDL_EVENT_RESERVED4 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED6 = (SDL_EVENT_RESERVED5 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED7 = (SDL_EVENT_RESERVED6 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_USEREVENT = 24 # /usr/include/SDL/SDL_events.h: 83

SDL_NUMEVENTS = 32 # /usr/include/SDL/SDL_events.h: 83

SDL_EventType = enum_anon_40 # /usr/include/SDL/SDL_events.h: 83

enum_anon_41 = c_int # /usr/include/SDL/SDL_events.h: 114

SDL_ACTIVEEVENTMASK = (1 << SDL_ACTIVEEVENT) # /usr/include/SDL/SDL_events.h: 114

SDL_KEYDOWNMASK = (1 << SDL_KEYDOWN) # /usr/include/SDL/SDL_events.h: 114

SDL_KEYUPMASK = (1 << SDL_KEYUP) # /usr/include/SDL/SDL_events.h: 114

SDL_KEYEVENTMASK = ((1 << SDL_KEYDOWN) | (1 << SDL_KEYUP)) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEMOTIONMASK = (1 << SDL_MOUSEMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEBUTTONDOWNMASK = (1 << SDL_MOUSEBUTTONDOWN) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEBUTTONUPMASK = (1 << SDL_MOUSEBUTTONUP) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEEVENTMASK = (((1 << SDL_MOUSEMOTION) | (1 << SDL_MOUSEBUTTONDOWN)) | (1 << SDL_MOUSEBUTTONUP)) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYAXISMOTIONMASK = (1 << SDL_JOYAXISMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYBALLMOTIONMASK = (1 << SDL_JOYBALLMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYHATMOTIONMASK = (1 << SDL_JOYHATMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYBUTTONDOWNMASK = (1 << SDL_JOYBUTTONDOWN) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYBUTTONUPMASK = (1 << SDL_JOYBUTTONUP) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYEVENTMASK = (((((1 << SDL_JOYAXISMOTION) | (1 << SDL_JOYBALLMOTION)) | (1 << SDL_JOYHATMOTION)) | (1 << SDL_JOYBUTTONDOWN)) | (1 << SDL_JOYBUTTONUP)) # /usr/include/SDL/SDL_events.h: 114

SDL_VIDEORESIZEMASK = (1 << SDL_VIDEORESIZE) # /usr/include/SDL/SDL_events.h: 114

SDL_VIDEOEXPOSEMASK = (1 << SDL_VIDEOEXPOSE) # /usr/include/SDL/SDL_events.h: 114

SDL_QUITMASK = (1 << SDL_QUIT) # /usr/include/SDL/SDL_events.h: 114

SDL_SYSWMEVENTMASK = (1 << SDL_SYSWMEVENT) # /usr/include/SDL/SDL_events.h: 114

SDL_EventMask = enum_anon_41 # /usr/include/SDL/SDL_events.h: 114

# /usr/include/SDL/SDL_events.h: 123
class struct_SDL_ActiveEvent(Structure):
    pass

struct_SDL_ActiveEvent.__slots__ = [
    'type',
    'gain',
    'state',
]
struct_SDL_ActiveEvent._fields_ = [
    ('type', Uint8),
    ('gain', Uint8),
    ('state', Uint8),
]

SDL_ActiveEvent = struct_SDL_ActiveEvent # /usr/include/SDL/SDL_events.h: 123

# /usr/include/SDL/SDL_events.h: 131
class struct_SDL_KeyboardEvent(Structure):
    pass

struct_SDL_KeyboardEvent.__slots__ = [
    'type',
    'which',
    'state',
    'keysym',
]
struct_SDL_KeyboardEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('state', Uint8),
    ('keysym', SDL_keysym),
]

SDL_KeyboardEvent = struct_SDL_KeyboardEvent # /usr/include/SDL/SDL_events.h: 131

# /usr/include/SDL/SDL_events.h: 141
class struct_SDL_MouseMotionEvent(Structure):
    pass

struct_SDL_MouseMotionEvent.__slots__ = [
    'type',
    'which',
    'state',
    'x',
    'y',
    'xrel',
    'yrel',
]
struct_SDL_MouseMotionEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('state', Uint8),
    ('x', Uint16),
    ('y', Uint16),
    ('xrel', Sint16),
    ('yrel', Sint16),
]

SDL_MouseMotionEvent = struct_SDL_MouseMotionEvent # /usr/include/SDL/SDL_events.h: 141

# /usr/include/SDL/SDL_events.h: 150
class struct_SDL_MouseButtonEvent(Structure):
    pass

struct_SDL_MouseButtonEvent.__slots__ = [
    'type',
    'which',
    'button',
    'state',
    'x',
    'y',
]
struct_SDL_MouseButtonEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('button', Uint8),
    ('state', Uint8),
    ('x', Uint16),
    ('y', Uint16),
]

SDL_MouseButtonEvent = struct_SDL_MouseButtonEvent # /usr/include/SDL/SDL_events.h: 150

# /usr/include/SDL/SDL_events.h: 158
class struct_SDL_JoyAxisEvent(Structure):
    pass

struct_SDL_JoyAxisEvent.__slots__ = [
    'type',
    'which',
    'axis',
    'value',
]
struct_SDL_JoyAxisEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('axis', Uint8),
    ('value', Sint16),
]

SDL_JoyAxisEvent = struct_SDL_JoyAxisEvent # /usr/include/SDL/SDL_events.h: 158

# /usr/include/SDL/SDL_events.h: 167
class struct_SDL_JoyBallEvent(Structure):
    pass

struct_SDL_JoyBallEvent.__slots__ = [
    'type',
    'which',
    'ball',
    'xrel',
    'yrel',
]
struct_SDL_JoyBallEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('ball', Uint8),
    ('xrel', Sint16),
    ('yrel', Sint16),
]

SDL_JoyBallEvent = struct_SDL_JoyBallEvent # /usr/include/SDL/SDL_events.h: 167

# /usr/include/SDL/SDL_events.h: 180
class struct_SDL_JoyHatEvent(Structure):
    pass

struct_SDL_JoyHatEvent.__slots__ = [
    'type',
    'which',
    'hat',
    'value',
]
struct_SDL_JoyHatEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('hat', Uint8),
    ('value', Uint8),
]

SDL_JoyHatEvent = struct_SDL_JoyHatEvent # /usr/include/SDL/SDL_events.h: 180

# /usr/include/SDL/SDL_events.h: 188
class struct_SDL_JoyButtonEvent(Structure):
    pass

struct_SDL_JoyButtonEvent.__slots__ = [
    'type',
    'which',
    'button',
    'state',
]
struct_SDL_JoyButtonEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('button', Uint8),
    ('state', Uint8),
]

SDL_JoyButtonEvent = struct_SDL_JoyButtonEvent # /usr/include/SDL/SDL_events.h: 188

# /usr/include/SDL/SDL_events.h: 198
class struct_SDL_ResizeEvent(Structure):
    pass

struct_SDL_ResizeEvent.__slots__ = [
    'type',
    'w',
    'h',
]
struct_SDL_ResizeEvent._fields_ = [
    ('type', Uint8),
    ('w', c_int),
    ('h', c_int),
]

SDL_ResizeEvent = struct_SDL_ResizeEvent # /usr/include/SDL/SDL_events.h: 198

# /usr/include/SDL/SDL_events.h: 203
class struct_SDL_ExposeEvent(Structure):
    pass

struct_SDL_ExposeEvent.__slots__ = [
    'type',
]
struct_SDL_ExposeEvent._fields_ = [
    ('type', Uint8),
]

SDL_ExposeEvent = struct_SDL_ExposeEvent # /usr/include/SDL/SDL_events.h: 203

# /usr/include/SDL/SDL_events.h: 208
class struct_SDL_QuitEvent(Structure):
    pass

struct_SDL_QuitEvent.__slots__ = [
    'type',
]
struct_SDL_QuitEvent._fields_ = [
    ('type', Uint8),
]

SDL_QuitEvent = struct_SDL_QuitEvent # /usr/include/SDL/SDL_events.h: 208

# /usr/include/SDL/SDL_events.h: 216
class struct_SDL_UserEvent(Structure):
    pass

struct_SDL_UserEvent.__slots__ = [
    'type',
    'code',
    'data1',
    'data2',
]
struct_SDL_UserEvent._fields_ = [
    ('type', Uint8),
    ('code', c_int),
    ('data1', POINTER(None)),
    ('data2', POINTER(None)),
]

SDL_UserEvent = struct_SDL_UserEvent # /usr/include/SDL/SDL_events.h: 216

# /usr/include/SDL/SDL_events.h: 219
class struct_SDL_SysWMmsg(Structure):
    pass

SDL_SysWMmsg = struct_SDL_SysWMmsg # /usr/include/SDL/SDL_events.h: 220

# /usr/include/SDL/SDL_events.h: 224
class struct_SDL_SysWMEvent(Structure):
    pass

struct_SDL_SysWMEvent.__slots__ = [
    'type',
    'msg',
]
struct_SDL_SysWMEvent._fields_ = [
    ('type', Uint8),
    ('msg', POINTER(SDL_SysWMmsg)),
]

SDL_SysWMEvent = struct_SDL_SysWMEvent # /usr/include/SDL/SDL_events.h: 224

# /usr/include/SDL/SDL_events.h: 242
class union_SDL_Event(Union):
    pass

union_SDL_Event.__slots__ = [
    'type',
    'active',
    'key',
    'motion',
    'button',
    'jaxis',
    'jball',
    'jhat',
    'jbutton',
    'resize',
    'expose',
    'quit',
    'user',
    'syswm',
]
union_SDL_Event._fields_ = [
    ('type', Uint8),
    ('active', SDL_ActiveEvent),
    ('key', SDL_KeyboardEvent),
    ('motion', SDL_MouseMotionEvent),
    ('button', SDL_MouseButtonEvent),
    ('jaxis', SDL_JoyAxisEvent),
    ('jball', SDL_JoyBallEvent),
    ('jhat', SDL_JoyHatEvent),
    ('jbutton', SDL_JoyButtonEvent),
    ('resize', SDL_ResizeEvent),
    ('expose', SDL_ExposeEvent),
    ('quit', SDL_QuitEvent),
    ('user', SDL_UserEvent),
    ('syswm', SDL_SysWMEvent),
]

SDL_Event = union_SDL_Event # /usr/include/SDL/SDL_events.h: 242

# /usr/include/SDL/SDL_events.h: 251
if hasattr(_libs['SDL'], 'SDL_PumpEvents'):
    SDL_PumpEvents = _libs['SDL'].SDL_PumpEvents
    SDL_PumpEvents.argtypes = []
    SDL_PumpEvents.restype = None

enum_anon_42 = c_int # /usr/include/SDL/SDL_events.h: 257

SDL_ADDEVENT = 0 # /usr/include/SDL/SDL_events.h: 257

SDL_PEEKEVENT = (SDL_ADDEVENT + 1) # /usr/include/SDL/SDL_events.h: 257

SDL_GETEVENT = (SDL_PEEKEVENT + 1) # /usr/include/SDL/SDL_events.h: 257

SDL_eventaction = enum_anon_42 # /usr/include/SDL/SDL_events.h: 257

# /usr/include/SDL/SDL_events.h: 277
if hasattr(_libs['SDL'], 'SDL_PeepEvents'):
    SDL_PeepEvents = _libs['SDL'].SDL_PeepEvents
    SDL_PeepEvents.argtypes = [POINTER(SDL_Event), c_int, SDL_eventaction, Uint32]
    SDL_PeepEvents.restype = c_int

# /usr/include/SDL/SDL_events.h: 284
if hasattr(_libs['SDL'], 'SDL_PollEvent'):
    SDL_PollEvent = _libs['SDL'].SDL_PollEvent
    SDL_PollEvent.argtypes = [POINTER(SDL_Event)]
    SDL_PollEvent.restype = c_int

# /usr/include/SDL/SDL_events.h: 290
if hasattr(_libs['SDL'], 'SDL_WaitEvent'):
    SDL_WaitEvent = _libs['SDL'].SDL_WaitEvent
    SDL_WaitEvent.argtypes = [POINTER(SDL_Event)]
    SDL_WaitEvent.restype = c_int

# /usr/include/SDL/SDL_events.h: 296
if hasattr(_libs['SDL'], 'SDL_PushEvent'):
    SDL_PushEvent = _libs['SDL'].SDL_PushEvent
    SDL_PushEvent.argtypes = [POINTER(SDL_Event)]
    SDL_PushEvent.restype = c_int

SDL_EventFilter = CFUNCTYPE(UNCHECKED(c_int), POINTER(SDL_Event)) # /usr/include/SDL/SDL_events.h: 300

# /usr/include/SDL/SDL_events.h: 323
if hasattr(_libs['SDL'], 'SDL_SetEventFilter'):
    SDL_SetEventFilter = _libs['SDL'].SDL_SetEventFilter
    SDL_SetEventFilter.argtypes = [SDL_EventFilter]
    SDL_SetEventFilter.restype = None

# /usr/include/SDL/SDL_events.h: 329
if hasattr(_libs['SDL'], 'SDL_GetEventFilter'):
    SDL_GetEventFilter = _libs['SDL'].SDL_GetEventFilter
    SDL_GetEventFilter.argtypes = []
    SDL_GetEventFilter.restype = SDL_EventFilter

# /usr/include/SDL/SDL_events.h: 348
if hasattr(_libs['SDL'], 'SDL_EventState'):
    SDL_EventState = _libs['SDL'].SDL_EventState
    SDL_EventState.argtypes = [Uint8, c_int]
    SDL_EventState.restype = Uint8

# /usr/include/SDL/SDL.h: 76
if hasattr(_libs['SDL'], 'SDL_Init'):
    SDL_Init = _libs['SDL'].SDL_Init
    SDL_Init.argtypes = [Uint32]
    SDL_Init.restype = c_int

# /usr/include/SDL/SDL.h: 79
if hasattr(_libs['SDL'], 'SDL_InitSubSystem'):
    SDL_InitSubSystem = _libs['SDL'].SDL_InitSubSystem
    SDL_InitSubSystem.argtypes = [Uint32]
    SDL_InitSubSystem.restype = c_int

# /usr/include/SDL/SDL.h: 82
if hasattr(_libs['SDL'], 'SDL_QuitSubSystem'):
    SDL_QuitSubSystem = _libs['SDL'].SDL_QuitSubSystem
    SDL_QuitSubSystem.argtypes = [Uint32]
    SDL_QuitSubSystem.restype = None

# /usr/include/SDL/SDL.h: 88
if hasattr(_libs['SDL'], 'SDL_WasInit'):
    SDL_WasInit = _libs['SDL'].SDL_WasInit
    SDL_WasInit.argtypes = [Uint32]
    SDL_WasInit.restype = Uint32

# /usr/include/SDL/SDL.h: 93
if hasattr(_libs['SDL'], 'SDL_Quit'):
    SDL_Quit = _libs['SDL'].SDL_Quit
    SDL_Quit.argtypes = []
    SDL_Quit.restype = None

# /usr/include/SDL/SDL_error.h: 53
try:
    SDL_OutOfMemory = (SDL_Error (SDL_ENOMEM))
except:
    pass

# /usr/include/SDL/SDL_error.h: 54
try:
    SDL_Unsupported = (SDL_Error (SDL_UNSUPPORTED))
except:
    pass

# /usr/include/SDL/SDL_audio.h: 100
try:
    AUDIO_U8 = 8
except:
    pass

# /usr/include/SDL/SDL_audio.h: 101
try:
    AUDIO_S8 = 32776
except:
    pass

# /usr/include/SDL/SDL_audio.h: 102
try:
    AUDIO_U16LSB = 16
except:
    pass

# /usr/include/SDL/SDL_audio.h: 103
try:
    AUDIO_S16LSB = 32784
except:
    pass

# /usr/include/SDL/SDL_audio.h: 104
try:
    AUDIO_U16MSB = 4112
except:
    pass

# /usr/include/SDL/SDL_audio.h: 105
try:
    AUDIO_S16MSB = 36880
except:
    pass

# /usr/include/SDL/SDL_audio.h: 106
try:
    AUDIO_U16 = AUDIO_U16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 107
try:
    AUDIO_S16 = AUDIO_S16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 114
try:
    AUDIO_U16SYS = AUDIO_U16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 115
try:
    AUDIO_S16SYS = AUDIO_S16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 218
def SDL_LoadWAV(file, spec, audio_buf, audio_len):
    return (SDL_LoadWAV_RW ((SDL_RWFromFile (file, 'rb')), 1, spec, audio_buf, audio_len))

# /usr/include/SDL/SDL_audio.h: 250
try:
    SDL_MIX_MAXVOLUME = 128
except:
    pass

# /usr/include/SDL/SDL_keysym.h: 321
try:
    KMOD_CTRL = (KMOD_LCTRL | KMOD_RCTRL)
except:
    pass

# /usr/include/SDL/SDL_keysym.h: 322
try:
    KMOD_SHIFT = (KMOD_LSHIFT | KMOD_RSHIFT)
except:
    pass

# /usr/include/SDL/SDL_keysym.h: 323
try:
    KMOD_ALT = (KMOD_LALT | KMOD_RALT)
except:
    pass

# /usr/include/SDL/SDL_keysym.h: 324
try:
    KMOD_META = (KMOD_LMETA | KMOD_RMETA)
except:
    pass

# /usr/include/SDL/SDL_keyboard.h: 67
try:
    SDL_ALL_HOTKEYS = 4294967295
except:
    pass

# /usr/include/SDL/SDL_keyboard.h: 84
try:
    SDL_DEFAULT_REPEAT_DELAY = 500
except:
    pass

# /usr/include/SDL/SDL_keyboard.h: 85
try:
    SDL_DEFAULT_REPEAT_INTERVAL = 30
except:
    pass

# /usr/include/SDL/SDL_video.h: 44
try:
    SDL_ALPHA_OPAQUE = 255
except:
    pass

# /usr/include/SDL/SDL_video.h: 45
try:
    SDL_ALPHA_TRANSPARENT = 0
except:
    pass

SDL_Colour = SDL_Color # /usr/include/SDL/SDL_video.h: 61

# /usr/include/SDL/SDL_video.h: 131
try:
    SDL_SWSURFACE = 0
except:
    pass

# /usr/include/SDL/SDL_video.h: 132
try:
    SDL_HWSURFACE = 1
except:
    pass

# /usr/include/SDL/SDL_video.h: 133
try:
    SDL_ASYNCBLIT = 4
except:
    pass

# /usr/include/SDL/SDL_video.h: 138
try:
    SDL_ANYFORMAT = 268435456
except:
    pass

# /usr/include/SDL/SDL_video.h: 139
try:
    SDL_HWPALETTE = 536870912
except:
    pass

# /usr/include/SDL/SDL_video.h: 140
try:
    SDL_DOUBLEBUF = 1073741824
except:
    pass

# /usr/include/SDL/SDL_video.h: 141
try:
    SDL_FULLSCREEN = 2147483648
except:
    pass

# /usr/include/SDL/SDL_video.h: 142
try:
    SDL_OPENGL = 2
except:
    pass

# /usr/include/SDL/SDL_video.h: 143
try:
    SDL_OPENGLBLIT = 10
except:
    pass

# /usr/include/SDL/SDL_video.h: 144
try:
    SDL_RESIZABLE = 16
except:
    pass

# /usr/include/SDL/SDL_video.h: 145
try:
    SDL_NOFRAME = 32
except:
    pass

# /usr/include/SDL/SDL_video.h: 150
try:
    SDL_HWACCEL = 256
except:
    pass

# /usr/include/SDL/SDL_video.h: 151
try:
    SDL_SRCCOLORKEY = 4096
except:
    pass

# /usr/include/SDL/SDL_video.h: 152
try:
    SDL_RLEACCELOK = 8192
except:
    pass

# /usr/include/SDL/SDL_video.h: 153
try:
    SDL_RLEACCEL = 16384
except:
    pass

# /usr/include/SDL/SDL_video.h: 154
try:
    SDL_SRCALPHA = 65536
except:
    pass

# /usr/include/SDL/SDL_video.h: 155
try:
    SDL_PREALLOC = 16777216
except:
    pass

# /usr/include/SDL/SDL_video.h: 161
def SDL_MUSTLOCK(surface):
    return ((surface.contents.offset) or ((((surface.contents.flags).value) & ((SDL_HWSURFACE | SDL_ASYNCBLIT) | SDL_RLEACCEL)) != 0))

# /usr/include/SDL/SDL_video.h: 200
try:
    SDL_YV12_OVERLAY = 842094169
except:
    pass

# /usr/include/SDL/SDL_video.h: 201
try:
    SDL_IYUV_OVERLAY = 1448433993
except:
    pass

# /usr/include/SDL/SDL_video.h: 202
try:
    SDL_YUY2_OVERLAY = 844715353
except:
    pass

# /usr/include/SDL/SDL_video.h: 203
try:
    SDL_UYVY_OVERLAY = 1498831189
except:
    pass

# /usr/include/SDL/SDL_video.h: 204
try:
    SDL_YVYU_OVERLAY = 1431918169
except:
    pass

# /usr/include/SDL/SDL_video.h: 252
try:
    SDL_LOGPAL = 1
except:
    pass

# /usr/include/SDL/SDL_video.h: 253
try:
    SDL_PHYSPAL = 2
except:
    pass

# /usr/include/SDL/SDL_video.h: 518
try:
    SDL_AllocSurface = SDL_CreateRGBSurface
except:
    pass

# /usr/include/SDL/SDL_video.h: 592
def SDL_LoadBMP(file):
    return (SDL_LoadBMP_RW ((SDL_RWFromFile (file, 'rb')), 1))

# /usr/include/SDL/SDL_video.h: 603
def SDL_SaveBMP(surface, file):
    return (SDL_SaveBMP_RW (surface, (SDL_RWFromFile (file, 'wb')), 1))

# /usr/include/SDL/SDL_video.h: 743
try:
    SDL_BlitSurface = SDL_UpperBlit
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 122
def SDL_BUTTON(X):
    return (1 << (X - 1))

# /usr/include/SDL/SDL_mouse.h: 123
try:
    SDL_BUTTON_LEFT = 1
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 124
try:
    SDL_BUTTON_MIDDLE = 2
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 125
try:
    SDL_BUTTON_RIGHT = 3
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 126
try:
    SDL_BUTTON_WHEELUP = 4
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 127
try:
    SDL_BUTTON_WHEELDOWN = 5
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 128
try:
    SDL_BUTTON_X1 = 6
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 129
try:
    SDL_BUTTON_X2 = 7
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 130
try:
    SDL_BUTTON_LMASK = (SDL_BUTTON (SDL_BUTTON_LEFT))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 131
try:
    SDL_BUTTON_MMASK = (SDL_BUTTON (SDL_BUTTON_MIDDLE))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 132
try:
    SDL_BUTTON_RMASK = (SDL_BUTTON (SDL_BUTTON_RIGHT))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 133
try:
    SDL_BUTTON_X1MASK = (SDL_BUTTON (SDL_BUTTON_X1))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 134
try:
    SDL_BUTTON_X2MASK = (SDL_BUTTON (SDL_BUTTON_X2))
except:
    pass

# /usr/include/SDL/SDL_events.h: 47
try:
    SDL_RELEASED = 0
except:
    pass

# /usr/include/SDL/SDL_events.h: 48
try:
    SDL_PRESSED = 1
except:
    pass

# /usr/include/SDL/SDL_events.h: 87
def SDL_EVENTMASK(X):
    return (1 << X)

# /usr/include/SDL/SDL_events.h: 115
try:
    SDL_ALLEVENTS = 4294967295
except:
    pass

# /usr/include/SDL/SDL_events.h: 334
try:
    SDL_QUERY = (-1)
except:
    pass

# /usr/include/SDL/SDL_events.h: 335
try:
    SDL_IGNORE = 0
except:
    pass

# /usr/include/SDL/SDL_events.h: 336
try:
    SDL_DISABLE = 0
except:
    pass

# /usr/include/SDL/SDL_events.h: 337
try:
    SDL_ENABLE = 1
except:
    pass

# /usr/include/SDL/SDL.h: 61
try:
    SDL_INIT_TIMER = 1
except:
    pass

# /usr/include/SDL/SDL.h: 62
try:
    SDL_INIT_AUDIO = 16
except:
    pass

# /usr/include/SDL/SDL.h: 63
try:
    SDL_INIT_VIDEO = 32
except:
    pass

# /usr/include/SDL/SDL.h: 64
try:
    SDL_INIT_CDROM = 256
except:
    pass

# /usr/include/SDL/SDL.h: 65
try:
    SDL_INIT_JOYSTICK = 512
except:
    pass

# /usr/include/SDL/SDL.h: 66
try:
    SDL_INIT_NOPARACHUTE = 1048576
except:
    pass

# /usr/include/SDL/SDL.h: 67
try:
    SDL_INIT_EVENTTHREAD = 16777216
except:
    pass

# /usr/include/SDL/SDL.h: 68
try:
    SDL_INIT_EVERYTHING = 65535
except:
    pass

SDL_AudioSpec = struct_SDL_AudioSpec # /usr/include/SDL/SDL_audio.h: 93

SDL_AudioCVT = struct_SDL_AudioCVT # /usr/include/SDL/SDL_audio.h: 126

SDL_keysym = struct_SDL_keysym # /usr/include/SDL/SDL_keyboard.h: 64

SDL_Rect = struct_SDL_Rect # /usr/include/SDL/SDL_video.h: 53

SDL_Color = struct_SDL_Color # /usr/include/SDL/SDL_video.h: 60

SDL_Palette = struct_SDL_Palette # /usr/include/SDL/SDL_video.h: 66

SDL_PixelFormat = struct_SDL_PixelFormat # /usr/include/SDL/SDL_video.h: 91

private_hwdata = struct_private_hwdata # /usr/include/SDL/SDL_video.h: 105

SDL_BlitMap = struct_SDL_BlitMap # /usr/include/SDL/SDL_video.h: 115

SDL_Surface = struct_SDL_Surface # /usr/include/SDL/SDL_video.h: 122

SDL_VideoInfo = struct_SDL_VideoInfo # /usr/include/SDL/SDL_video.h: 188

private_yuvhwfuncs = struct_private_yuvhwfuncs # /usr/include/SDL/SDL_video.h: 217

private_yuvhwdata = struct_private_yuvhwdata # /usr/include/SDL/SDL_video.h: 218

SDL_Overlay = struct_SDL_Overlay # /usr/include/SDL/SDL_video.h: 226

WMcursor = struct_WMcursor # /usr/include/SDL/SDL_mouse.h: 40

SDL_Cursor = struct_SDL_Cursor # /usr/include/SDL/SDL_mouse.h: 48

SDL_ActiveEvent = struct_SDL_ActiveEvent # /usr/include/SDL/SDL_events.h: 123

SDL_KeyboardEvent = struct_SDL_KeyboardEvent # /usr/include/SDL/SDL_events.h: 131

SDL_MouseMotionEvent = struct_SDL_MouseMotionEvent # /usr/include/SDL/SDL_events.h: 141

SDL_MouseButtonEvent = struct_SDL_MouseButtonEvent # /usr/include/SDL/SDL_events.h: 150

SDL_JoyAxisEvent = struct_SDL_JoyAxisEvent # /usr/include/SDL/SDL_events.h: 158

SDL_JoyBallEvent = struct_SDL_JoyBallEvent # /usr/include/SDL/SDL_events.h: 167

SDL_JoyHatEvent = struct_SDL_JoyHatEvent # /usr/include/SDL/SDL_events.h: 180

SDL_JoyButtonEvent = struct_SDL_JoyButtonEvent # /usr/include/SDL/SDL_events.h: 188

SDL_ResizeEvent = struct_SDL_ResizeEvent # /usr/include/SDL/SDL_events.h: 198

SDL_ExposeEvent = struct_SDL_ExposeEvent # /usr/include/SDL/SDL_events.h: 203

SDL_QuitEvent = struct_SDL_QuitEvent # /usr/include/SDL/SDL_events.h: 208

SDL_UserEvent = struct_SDL_UserEvent # /usr/include/SDL/SDL_events.h: 216

SDL_SysWMmsg = struct_SDL_SysWMmsg # /usr/include/SDL/SDL_events.h: 219

SDL_SysWMEvent = struct_SDL_SysWMEvent # /usr/include/SDL/SDL_events.h: 224

SDL_Event = union_SDL_Event # /usr/include/SDL/SDL_events.h: 242

# No inserted files

