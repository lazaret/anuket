# -*- coding: utf-8 -*-
""" Javascripts and css resources for Anuket."""

#from __future__ import absolute_import

from js.bootstrap import bootstrap_responsive_css, bootstrap_js
from fanstatic import Group, Library, Resource


anuket_library = Library("anuket", "static")

anuket_css = Resource(anuket_library, "css/style.css",
    depends=[bootstrap_responsive_css])

anuket_js = Resource(anuket_library, "js/anuket.js",
    depends=[bootstrap_js])

anuket_resources = Group([anuket_css, anuket_js])

#TODO html5shim ?