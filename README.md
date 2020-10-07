[![Downloads]][1]

[![Latest Version]][2]

[![Development Status]][2]

[![License]][2]


# ckanext-openenergy

## Requirements

For example, you might want to mention here which versions of CKAN this
extension works with.

## Installation

To install ckanext-openenergy:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-openenergy Python package into your virtual
    environment:

        pip install ckanext-openenergy

3.  Add `openenergy` to the `ckan.plugins` setting in your CKAN config
    file (by default the config file is located at
    `/etc/ckan/default/production.ini`).

4.  Restart CKAN. For example if you've deployed CKAN with Apache on
    Ubuntu:

        sudo service apache2 reload

## Config Settings

Document any optional config settings here. For example:

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.openenergy.some_setting = some_default_value

## Development Installation

To install ckanext-openenergy for development, activate your CKAN
virtualenv and do:

    git clone https://github.com/openclimatefix/ckanext-openenergy.git
    cd ckanext-openenergy
    python setup.py develop
    pip install -r dev-requirements.txt




  [Downloads]: https://img.shields.io/pypi/dm/ckanext-openenergy
  [1]: https://pypi.python.org/pypi/ckanext-openenergy/
  [Latest Version]: https://pypip.in/version/ckanext-openenergy/badge.svg
  [2]: https://pypi.python.org/pypi/ckanext-openenergy/
  [Development Status]: https://pypip.in/status/ckanext-openenergy/badge.svg
  [License]: https://img.shields.io/pypi/l/ckanext-openenergy