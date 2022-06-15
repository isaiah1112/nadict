## Overview
[NaDict] is a wrapper for [NetApps's Python SDK](https://mysupport.netapp.com/documentation/productlibrary/index.html?productID=60427).
It simplifies the decoding and encoding of NaElement objects, which the NetApp API uses to pass data back and forth.

## License
[NaDict] is released under the [GNU Lesser General Public License v3.0][],
see the file LICENSE and LICENSE.lesser for the license text.

## Installation
The most straightforward way to get the [NaDict] module working for you is:

 1. Download the [NetApps's Python SDK](https://mysupport.netapp.com/documentation/productlibrary/index.html?productID=60427)
 2. Copy the **NaDict.py** and **NaHelper.py** file into the directory containing the following scripts:
  - NaElement.py
  - NaServer.py
  - Ontap.py
 3. You should then be able to import the **NaDict** and **NaHelper** modules without any issue

## Documentation

You can build the HTML documentation for [NaDict] by running:
```commandline
make docs
```

Then simply open **docs/build/html/index.html** in your browser.

## Contributing
Comments and enhancements are very welcome.

Report any issues or feature requests on the [BitBucket bug
tracker](https://bitbucket.org/isaiah1112/nadict/issues?status=new&status=open). Please include a minimal
(not-) working example which reproduces the bug and, if appropriate, the
 traceback information.  Please do not request features already being worked
towards.

Code contributions are encouraged: please feel free to [fork the
project](https://bitbucket.org/isaiah1112/nadict/fork) and submit pull requests to the develop branch.

## More information

- [NetApp Storage](http://www.netapp.com/)

[GNU Lesser General Public License v3.0]: http://choosealicense.com/licenses/lgpl-3.0/ "LGPL v3"

[NaDict]: https://bitbucket.org/isaiah1112/nadict "NaDict Module"
