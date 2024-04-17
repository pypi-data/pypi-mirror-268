# pylint: disable-msg=W0622
"""cubicweb-conference application packaging information"""

from os import listdir as _listdir
from os.path import join, isdir
from glob import glob

modname = "conference"
distname = f"cubicweb-{modname}"

numversion = (1, 0, 1)
version = ".".join(str(num) for num in numversion)

license = "LGPL"
description = "conference component for the CubicWeb framework"
author = "Logilab"
author_email = "contact@logilab.fr"
web = f"https://forge.extranet.logilab.fr/cubicweb/cubes/{distname}"

classifiers = [
    "Environment :: Web Environment",
    "Framework :: CubicWeb",
    "Programming Language :: Python :: 3",
    "Programming Language :: JavaScript",
]

__depends__ = {
    "cubicweb": ">= 4.0.0, < 5.0.0",
    "cubicweb-web": ">= 1.0.0, < 2.0.0",
    "cubicweb-addressbook": ">= 2.0.0, < 3.0.0",
    "cubicweb-card": ">= 2.0.0, < 3.0.0",
    "cubicweb-comment": ">= 3.0.0, < 4.0.0",
    "cubicweb-file": ">= 4.0.0, < 5.0.0",
    "cubicweb-tag": ">= 3.0.0, < 4.0.0",
    "cubicweb-seo": ">= 1.0.0, < 2.0.0",
}

# packaging ###

THIS_CUBE_DIR = join("share", "cubicweb", "cubes", modname)


def listdir(dirpath):
    return [
        join(dirpath, fname)
        for fname in _listdir(dirpath)
        if fname[0] != "."
        and not fname.endswith(".pyc")
        and not fname.endswith("~")
        and not isdir(join(dirpath, fname))
    ]


data_files = [
    # common files
    [THIS_CUBE_DIR, [fname for fname in glob("*.py") if fname != "setup.py"]],
]
# check for possible extended cube layout
for dirname in (
    "entities",
    "views",
    "sobjects",
    "hooks",
    "schema",
    "data",
    "i18n",
    "migration",
    "wdoc",
):
    if isdir(dirname):
        data_files.append([join(THIS_CUBE_DIR, dirname), listdir(dirname)])
# Note: here, you'll need to add subdirectories if you want
# them to be included in the debian package
