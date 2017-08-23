# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TMD Holdings Base Package',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Intial configurations & customizations to the base database
        """,
    'depends': ['base','stock','stock_dropshipping'],
    'data': [
        'data/inventory_locations.xml',
        'data/custom_routes.xml',
        #'data/ir_actions_act_window.xml',
        #'data/ir_actions_server.xml',
        #'data/ir_ui_view.xml',
        #'data/ir_ui_menu.xml',
        #'data/base_automation.xml',
    ],
    'installable': True,
    'application': True,
}
