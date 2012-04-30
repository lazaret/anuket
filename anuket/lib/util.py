# -*- coding: utf-8 -*-
import os


def verify_directory(dir):
    """ Create and/or verify a filesystemp directory."""
    if not os.path.exists(dir):
        try:
            os.makedirs(dir, 0775)
        except:
            raise