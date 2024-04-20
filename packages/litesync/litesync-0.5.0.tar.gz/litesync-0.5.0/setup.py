# -*- coding: ISO-8859-1 -*-
# setup.py: the distutils script
#
import os
import setuptools
import shutil
import sys

from distutils import log
from distutils.command.build_ext import build_ext
from setuptools import Extension

# If you need to change anything, it should be enough to change setup.cfg.

PACKAGE_NAME = 'litesync'
VERSION = '0.5.0'

# define sqlite sources
sources = [os.path.join('src', source)
           for source in ["module.c", "connection.c", "cursor.c", "cache.c",
                          "microprotocols.c", "prepare_protocol.c",
                          "statement.c", "util.c", "row.c", "blob.c"]]

# define packages
packages = [PACKAGE_NAME]
EXTENSION_MODULE_NAME = "._sqlite3"

# Work around clang raising hard error for unused arguments
if sys.platform == "darwin":
    os.environ['CFLAGS'] = "-Qunused-arguments"
    log.info("CFLAGS: " + os.environ['CFLAGS'])

def quote_argument(arg):
    q = '"'   #if sys.platform == 'win32' and sys.version_info < (3, 8) else '"'
    return q + arg + q

define_macros = [('MODULE_NAME', quote_argument(PACKAGE_NAME + '.dbapi2'))]


with open("README.md", "r") as fh:
    long_description = fh.read()


class SystemLibSqliteBuilder(build_ext):
    description = "Builds a C extension linking against the litesync library"

    def build_extension(self, ext):
        log.info(self.description)
        ext.libraries.append('litesync')
        if sys.platform == "win32":
            ext.include_dirs.append(".")
        build_ext.build_extension(self, ext)


def get_setup_args():
    return dict(
        name=PACKAGE_NAME,
        version=VERSION,
        description="DB-API 2.0 interface for LiteSync",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Bernardo Ramos",
        author_email="contact@litesync.io",
        license="zlib/libpng",
        platforms="ALL",
        url="https://gitlab.com/litesync/litesync-python3",
        package_dir={PACKAGE_NAME: "litesync"},
        packages=packages,
        ext_modules=[Extension(
            name=PACKAGE_NAME + EXTENSION_MODULE_NAME,
            sources=sources,
            define_macros=define_macros)
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: zlib/libpng License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Programming Language :: C",
            "Programming Language :: Python",
            "Topic :: Database :: Database Engines/Servers",
            "Topic :: Software Development :: Libraries :: Python Modules"],
        cmdclass={
            "build_ext": SystemLibSqliteBuilder
        }
    )


if __name__ == "__main__":
    setuptools.setup(**get_setup_args())
