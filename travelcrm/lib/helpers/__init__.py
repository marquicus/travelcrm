# -*-coding: utf-8-*-
from __future__ import absolute_import
import json

from .common import *
from .fields import *
from .permisions import *
from webhelpers2.html import tags
from webhelpers2.html import builder


# need it to possibility use of data-options
# def attr_decode():
#     from webhelpers2.html.builder import _attr_decode
#
#     def _helpers_attr_decode(v):
#         if v == 'data_options':
#             return 'data-options'
#         return _attr_decode(v)
#     return _helpers_attr_decode
#
# builder._attr_decode = attr_decode()
