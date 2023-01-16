# -*- coding: utf-8 -*-
{
    'name': "Modulo de Prueba",

    'summary': """
        Modulo de prueba""",

    'description': """
Modulo de Prueba    """,

    'author': "Edooit / Keivn Rojas",
    'website': "https://www.edooit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
