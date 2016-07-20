# coding=utf-8
"""A Python helper module that works along with the NetApp python SDK.  The module includes functions
for decoding NaElement objects into dictionaries (using similar parsing to the sprintf function).  It also includes
an encode function for turning a dictionary back into the nested NaElement objects.
"""
# Copyright (C) 2015 Jesse Almanrode
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Lesser General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Lesser General Public License for more details.
#
#     You should have received a copy of the GNU Lesser General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import print_function
import re
try:
    from NaElement import NaElement
except ImportError:
    # You need to download the SDK from NetApp
    raise ImportError('Unable to find NetApp SDK Modules in your PYTHONPATH')

__author__ = 'Jesse Almanrode (jesse@almanrode.com'
__version__ = '1.2'


class NaDictError(Exception):
    """Exception occurred during encode or decode
    """
    pass


def decode(naobject):
    """Allows you to convert an NaObject into a dictionary

    :param naobject: NaObject or NaElement
    :return: Dictionary
    :raises: NaDictError
    """
    nadict = dict()
    name = naobject.element['name']
    nadict[name] = dict()
    keys = naobject.element['attrkeys']
    vals = naobject.element['attrvals']
    j = 0
    nadict[name] = dict()
    for i in keys:
        nadict[name][i] = str(vals[j])
        j += 1
    children = naobject.element['children']

    for i in children:
        c = i
        if not re.search('NaElement.NaElement', str(c.__class__), re.I):
            err = "Unexpected reference found, expected NaElement.NaElement not " + str(c.__class__) + "\n"
            raise NaDictError(err)
        cdict = decode(c)
        nadict[name] = __update__(nadict[name], cdict)

    naobject.element['content'] = naobject.escapeHTML(naobject.element['content'])
    content = str(naobject.element['content'])
    if content != '':
        nadict[name] = content
    return nadict


def encode(nadict):
    """Allows you to encode a dictionary into an NaElement or NaObject

    :param nadict: Dictionary to encode
    :return: NaElement or NaObject
    :raises: NaDictError
    """
    if type(nadict) is not dict:
        raise NaDictError("NaDict is not a dictionary")
    if len(nadict.keys()) > 1:
        raise NaDictError("NaDict does not have a single top-level key")
    try:
        topkey = nadict.keys()[0]
    except IndexError:
        raise NaDictError("NaDict needs at least 1 key to start the tree")
    newelement = NaElement(topkey)
    return __encode_child__(nadict[topkey], newelement)


def __encode_child__(nadict, parent):
    """Private Function for parsing NaDict objects back to NaElement objects

    :param nadict: Dictionary to be turned into an NaElement object
    :param parent: Parent NaElement object to add children/values to
    :return: Finished NaElement object
    """
    for key, value in nadict.items():
        if type(value) is dict:
            newchild = NaElement(key)
            newchild = __encode_child__(value, newchild)
            parent.child_add(newchild)
        elif type(value) is list:
            for item in value:
                if type(item) is str:
                    newchild = NaElement(key, item)
                    parent.child_add(newchild)
                else:
                    newchild = NaElement(key)
                    newchild = __encode_child__(item, newchild)
                    parent.child_add(newchild)
        else:
            newchild = NaElement(key, value)
            parent.child_add(newchild)
    return parent


def __update__(target, source):
    """Private function to take two NaDict objects and apply the changes from dict2 to dict1 (without overwriting values)

    :param target: NaDict dictionary
    :param source: NaDict dictionary
    :return: Updated NaDict dictionary
    """
    for key2, value2 in source.items():
        if key2 in target.keys():
            if type(target[key2]) is list:
                target[key2].append(value2)
            else:
                target[key2] = [target[key2], value2]
        else:
            target[key2] = value2
    return target
