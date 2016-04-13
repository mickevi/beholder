#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys
import os

__author__ = 'Mikael Viklund <mikael.viklund@forsakringskassan.se>'

libdir = os.path.realpath(os.path.abspath(os.path.dirname(sys.argv[0])))[:-4] + "/beholder"
if libdir not in sys.path:
    sys.path.insert(0, libdir)
# __import__('code').interact(local={k: v for ns in (globals(), locals()) for k, v in ns.items()})
if __name__ == "__main__":
    import beholder

    beholder.main()
