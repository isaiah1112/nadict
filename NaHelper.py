# coding=utf-8
"""A Python helper for doing various NetApp API operations.
"""
from __future__ import print_function, division
try:
    from NaServer import NaServer
    from NaElement import NaElement
except ImportError:
    # You need to download the SDK from NetApp
    raise ImportError('Unable to find NetApp SDK Modules in your PYTHONPATH')

__author__ = 'Jesse Almanrode (jesse@almanrode.com)'
__version__ = '1.2'


class OntapApiException(Exception):
    """An Error occurred while using the NetApp API
    """
    pass


def netapp_cli(apiobj, cmd):
    """Passes a command to the filer cli via the API

    .. warning::

        Only use this method if a command isn't supported by the API.

    :param apiobj: API object (from netapp_api)
    :param cmd: The command to execute
    :return: NaElement object
    """
    # Pulled from
    # http://community.netapp.com/t5/Software-Development-Kit-SDK-and-API-Discussions/Is-there-an-ONTAP-SDK-interface-to-change-a-qtree-s-security-style/td-p/51251
    args = NaElement('args')
    for arg in cmd.split():
        args.child_add(NaElement('arg', arg))
    cli = NaElement('system-cli')
    cli.child_add(args)
    result = apiobj.invoke_elem(cli)
    if result.results_status() == "failed":
        raise OntapApiException(result.results_errno(), result.results_reason())
    return result


def netapp_api(filer, username, password, version='1.3'):
    """Connect to a filer API object

    :param filer: FQDN of the filer you wish to connect to
    :param username: Username to connect with
    :param password: Password to connect with
    :param version: Version string to use for the API (default = 1.3)
    :return: NaServer Object
    :raises: OntapApiException
    """
    major, minor = version.split('.')
    session = NaServer(filer, major, minor)
    session.set_style("LOGIN")
    session.set_admin_user(username, password)
    session.set_transport_type("HTTP")
    result = session.invoke('system-get-info')
    if result.results_status() == "failed":
        raise OntapApiException(result.results_errno(), result.results_reason())
    else:
        return session


def sprintf(element):
    """Shortcut to 'print element.sprintf()'

    :param element: The NaObject, NaElement to print
    :return: None
    """
    print(element.sprintf())


def convert_bytes(intbytes):
    """Convert bytes to a human readable format (for creating volumes via the API)

    :param intbytes: Positive Integer
    :return: String
    :raises: ValueError
    """
    intbytes = int(intbytes)
    if intbytes < 0:
        raise ValueError(str(intbytes) + " is not a positive integer")
    if intbytes >= 1073741824:
        gigabytes = intbytes / 1073741824
        size = '%.0fg' % gigabytes
        return size
    megabytes = intbytes / 1048576
    size = '%.0fm' % megabytes
    return size
