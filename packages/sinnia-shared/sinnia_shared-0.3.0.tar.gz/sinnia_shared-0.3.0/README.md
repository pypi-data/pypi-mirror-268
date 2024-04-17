# Sinnia Utils

Python utilities for Sinnia

 - AMQP Utils
 - Timezone Utils
 - Miscellaneous Utils


### To publish changes to this library in PyPi

For tutorial click [here](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives "Python packaging")

#### To publish for the first time:

`python3 -m pip install --upgrade build`

`python3 -m pip install --user --upgrade twine`

Edit the version in setup.py

`python3 -m build`

`python3 -m twine upload dist/{package_with_version}`

#### To publish subsequent versions:

Edit the version in setup.py

`python3 -m build`

`python3 -m twine upload dist/{package_with_version}`

#### Auth must have been configured in `$HOME/.pypirc`



----
### Dependencies:

Using python 3.9.12

* build==0.8.0
* bleach==5.0.0
* certifi==2021.10.8
* charset-normalizer==2.0.12
* commonmark==0.9.1
* docutils==0.18.1
* idna==3.3
* importlib-metadata==4.11.3
* keyring==23.5.0
* pkginfo==1.8.2
* Pygments==2.12.0
* PyMySQL==1.0.2
* PyYAML==6.0
* readme-renderer==35.0
* requests==2.27.1
* requests-toolbelt==0.9.1
* rfc3986==2.0.0
* rich==12.3.0
* six==1.16.0
* twine==4.0.0
* urllib3==1.26.9
* webencodings==0.5.1
* zipp==3.8.0

