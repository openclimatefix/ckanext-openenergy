# -*- coding: utf-8 -*- 

import os
from logging import getLogger

from pylons import request

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IConfigurer
from ckan.plugins import IRoutes

import ckan.lib.base as base

import routes.mapper

log = getLogger(__name__)


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
        config['ckan.site_about'] = """
The energy ecosystem must implement an architecture which can scale in data-type, volume and connectivity, across use-cases, organisational and logistical boundaries, sectors and jurisdictions. It must deliver this in a secure, safe, robust and adaptable environment which addresses governance.

Data users are diverse: from asset managers to [Distribution Network Operators](https://en.wikipedia.org/wiki/Distribution_network_operator) (DNOs) to consumers. Our research has confirmed:

1. User needs are diverse, encompassing thousands of organisations, customers and society as a whole.
2. There is no ‘single data platform’ approach that will (or should) address all needs.
3. There is a material risk to implementation unless governance is addressed.

Centralised data architectures have not scaled effectively in any sector. Interviewees expressed the need for a clear roadmap to transition from a fragmented data landscape to a robust, decentralised, federated data infrastructure. They believed that “there can be no single platform for all data and use-cases” and “there will be significant barriers to adoption around the centralisation of commercial data”. With Presumed Open as a guiding principle, we must also apply the precautionary principle to innovation to address potential unintended consequences (e.g. unexpected monopolies). 

The architectural approach to developing domain-specific platforms, hubs, analytic networks, asset registries, catalogues, systems maps and so on requires a shift in thinking from ‘push’ to ‘pull’—as websites enable search engines to find and index them, a distributed architecture creates a dynamic market between data suppliers and consumers. This enables markets for many solutions including platforms, apps and related services, while control is retained at the organisational level.

We heard from dozens of experts that they see “no viable alternative” than to “address the upstream needs of data supply through an open, decentralised architecture with strong governance”. Further, “should that exist it would enable a multitude of solutions to emerge”.     

Fortunately, we have 30-years evidence of the most successful information architecture in history: the web. We believe the energy sector must now embrace a ‘web of data’ approach. 

We propose the development of an Open Governance Platform in concert with the market and regulators to establish a common approach to data-sharing, a cohesive and viable market architecture.

Our Phase One consultation process is summarised below. We will update with further details on this page as this programme develops.

[> Learn more](https://icebreakerone.org/energy/)        
"""

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
