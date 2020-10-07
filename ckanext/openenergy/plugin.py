import os
from logging import getLogger

from pylons import request

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IConfigurer
from ckan.plugins import IRoutes

import ckan.lib.base as base

import routes.mapper

log = getLogger(__name__)


def _get_file_content(path):
    with open(path, "r+") as file:
        contents = file.read()
    return contents


class OpenenergyPlugin(SingletonPlugin):
    """This plugin demonstrates how a theme packaged as a CKAN
    extension might extend CKAN behaviour.

    In this case, we implement three extension interfaces:

      - ``IConfigurer`` allows us to override configuration normally
        found in the ``ini``-file.  Here we use it to specify the site
        title, and to tell CKAN to look in this package for templates
        and resources that customise the core look and feel.

      - ``IRoutes`` allows us to add new URLs, or override existing
        URLs.  In this example we use it to override the default
        ``/register`` behaviour with a custom controller
    """
    implements(IConfigurer, inherit=True)
    implements(IRoutes, inherit=True)

    def update_config(self, config):
        """This IConfigurer implementation causes CKAN to look in the
        ```public``` and ```templates``` directories present in this
        package for any customisations.

        It also shows how to set the site title here (rather than in
        the main site .ini file), and causes CKAN to use the
        customised package form defined in ``package_form.py`` in this
        directory.
        """
        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))
        our_public_dir = os.path.join(rootdir, 'ckanext',
                                      'openenergy', 'public')
        template_dir = os.path.join(rootdir, 'ckanext',
                                    'openenergy', 'templates')

        # print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
        # # print(_get_file_content(os.path.join(rootdir, 'ckanext',
        # #                               'openenergy', 'texts', 'intro.md')))
        # print("FIN")

        # set our local template and resource overrides
        config['extra_public_paths'] = ','.join([our_public_dir,
                                                 config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
                                                   config.get('extra_template_paths', '')])

        # add in the extra.css
        config['ckan.template_head_end'] = config.get('ckan.template_head_end', '') +\
            '<link rel="stylesheet" href="/css/extra.css" type="text/css"> ' +\
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">'

        # set the title
        config['ckan.site_title'] = "Open Energy Data Portal"
        config['ckan.site_intro_text'] = _get_file_content(os.path.join(rootdir, 'ckanext',
                                      'openenergy', 'texts', 'intro.md'))
        config['ckan.site_about'] = _get_file_content(os.path.join(rootdir, 'ckanext',
                                      'openenergy', 'texts', 'about.md'))

        # set the customised package form (see ``setup.py`` for entry point)
        config['package_form'] = "example_form"


    def before_map(self, route_map):
        """This IRoutes implementation overrides the standard
        ``/user/register`` behaviour with a custom controller.  You
        might instead use it to provide a completely new page, for
        example.

        Note that we have also provided a custom register form
        template at ``theme/templates/user/register.html``.
        """

        with routes.mapper.SubMapper(route_map,
                controller='ckanext.openenergy.plugin:ExtraPagesController') as m:
            m.connect('changelog', '/changelog', action='changelog')
            m.connect('request_data', '/request-data', action='request_data')
        
        return route_map


class ExtraPagesController(base.BaseController):
    def changelog(self):
        return base.render('changelog.html')
    
    def request_data(self):
        return base.render('request_data.html')
