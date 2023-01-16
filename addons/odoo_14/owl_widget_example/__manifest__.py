# -*- coding: utf-8 -*-
{
    'name': "owl_widget_example",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    "qweb": [
        "static/src/js/components/widgetkevin.xml"
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        # 'views/templates.xml',
    ],
    'demo': [],
}
