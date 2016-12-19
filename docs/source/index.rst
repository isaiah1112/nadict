.. NaDict documentation master file, created by
   sphinx-quickstart on Thu Nov  5 15:18:27 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _home:

NaDict and NaHelper
===================

NaDict and NaHelper are Python Modules designed to help make working with the `NetApp`_ APIs easier and more "Pythonic" 
in nature.

Getting Started
---------------

Getting started with NaDict and NaHelper requires a bit of pre work.  First, you must download the `NetApp Python SDK`_ 
from NetApp's Website.  Once you have downloaded the SDK and have the folder somewhere where you can access it from 
Python's PATH, you can add the NaDict and NaHelper scripts to that directory.

For example:

.. code-block:: bash

    # Say we have a project called my-netapp directory in our home folder,
    # We copy the NetAppSDK directory into our project folder:
    cp ~/Downloads/NetAppSDK ~/my-netapp/
    # Then, we add NaDict and NaHelper to that directory:
    cp ~/Downloads/NaDict.py ~/my-netapp/NetAppSDK/
    cp ~/Downloads/NaHelper.py ~/my-netapp/NetAppSDK/
    
Now we are ready to add that directory to our Python PATH and import the scripts!

.. code-block:: python

    from __future__ import print_function
    import os
    import sys
    # Add our project root based on this script and add our NetAppSDK directory to the Python Path
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(project_root + '/NetAppSDK')
    # Now import stuff
    from NaDict import encode, decode
    from NaHelper import netapp_api, sprintf
    
Now you are ready to begin working with the NetApp API.  

Connecting to the NetApp API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Do connect to the NetApp API simply use the :code:`netapp_api` method:

.. code-block:: python

    napi = netapp_api('myfiler.example.com', 'jdoe', 'password1234')
    
    
If you are successful at logging in and running the :code:`system-get-info` API command then you will get a NaServer ojbect
back from the method and you will be ready to begin making calls to the API!

.. note::

    Permissions in the NetApp API are very granular and it can be a pain to get them all configured properly to allow you
    the right commands you need.  Be patient with your NetApp admin! :)
    
Encoding and Decoding NaElements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The primary feature of NaDict is to convert the *NaElement* XML Objects that the NetApp API uses for communication to
a dictionary that is easily manipulated in Python and then back to an *NaElement* XML Object.

.. code-block:: python

    volinfo = session.invoke('volume-list-info')
    sprintf(volinfo)  # Shows that the value returned is actually an NaElement object
    volinfo = decode(volinfo)
    print(volinfo)  # We have decoded the NaElement object into a dictionary
    volinfo = encode(volinfo)
    sprintf(volinfo)  # We have now converted the dictionary back to an NaElement object

Also worth noting in this example is our use of the :code:`sprintf` function from **NaHelper**.  This is just a shortcut
I came up with to access the :code:`NaElement.sprintf()` function each *NaElement* object contains.  It just seems a bit
more "Pythonic" with a call like this.

NaDict and NaHelper APIs
------------------------

To learn what methods are available to NaDict and NaHelper please read the following documents:

.. toctree::
   :maxdepth: 1

   nadict
   nahelper
   
You can also find some examples of how these two modules can be used by looking in the *EXAMPLES* file in the NaDict git
repo on Bitbucket.

Compatibility
-------------

As of version 1.2, NaDict now supports both Python 2.7 and 3.5.

Links
-----

* :ref:`genindex`

.. _NetApp : http://www.netapp.com/
.. _NetApp Python SDK : https://mysupport.netapp.com/documentation/productlibrary/index.html?productID=60427