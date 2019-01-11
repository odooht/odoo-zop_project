# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Schdule Manage',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Project Schdule Manage',
    'description': """
This module is for Project Schdule Manage.
===========================================================================

Project Schdule Manage.
    """,
    'author': 'Beijing OdooHT Co. LTD.',
    'website': 'https://www.odooht.com',
    'depends': ['project', 'uom'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
    ],
    'demo': [
        #
        #
    ],
    'installable': True,
    'auto_install': False,
}
