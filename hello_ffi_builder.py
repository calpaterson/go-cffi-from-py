#!/usr/bin/env python3

from cffi import FFI


def main():
    ffibuilder = FFI()

    ffibuilder.set_source(
        "pyhello",
        '# include "hello.h"',
        extra_objects=["hello.so"])
    ffibuilder.cdef("extern void Hello();")
    ffibuilder.compile(verbose=True)


if __name__ == "__main__":
    main()
