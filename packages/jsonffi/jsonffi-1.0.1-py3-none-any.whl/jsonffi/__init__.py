import json
from cffi import FFI

__copyright__    = 'Copyright (C) 2024 JavaCommons Technologies'
__version__      = '1.0.1'
__license__      = 'MIT'
__author__       = 'JavaCommons Technologies'
__author_email__ = 'javacommmons@gmail.com'
__url__          = 'https://github.com/javacommons/py-jsonffi'
__all__ = ['JsonFFI']

class JsonFFI:
    def __init__(self, dllSpec):
        self.ffi = FFI()
        self.ffi.cdef("const char *Call(const char *, const char *);")
        self.ffi.cdef("const char *LastError();")
        self.clib = self.ffi.dlopen(dllSpec)
    def call(self, name, args):
        answer = self.ffi.string(self.clib.Call(name.encode(), json.dumps(args).encode())).decode()
        error_ptr = self.clib.LastError()
        if error_ptr == self.ffi.cast("char *", 0):
            return json.loads(answer)
        error_msg = self.ffi.string(error_ptr).decode()
        raise Exception(error_msg)
