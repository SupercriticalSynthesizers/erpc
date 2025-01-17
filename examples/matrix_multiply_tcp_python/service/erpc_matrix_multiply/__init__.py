# Copyright 2017 NXP
# All rights reserved.
#
#
# SPDX-License-Identifier: BSD-3-Clause

#
# Generated by erpcgen 1.10.0 on Thu Oct 13 21:22:10 2022.
#
# AUTOGENERATED - DO NOT EDIT
#

try:
    from erpc import erpc_version
    version = erpc_version.ERPC_VERSION
except ImportError:
    version = "unknown"
if version != "1.10.0":
    raise ValueError("The generated shim code version (1.10.0) is different to the rest of eRPC code (%s). \
Install newer version by running \"python setup.py install\" in folder erpc/erpc_python/." % repr(version))

from . import common
from . import client
from . import server
from . import interface
