{
    'name':'My Inventory',
    'version': '0.1',
    'author': 'John Raymark',
    'summary': "My Personal Odoo Files",
    'sequence': 1,
    'description': "",
    'category': 'Application',
    'website': '',
    'depends': ['base'

    ],
    'data':[
        "views/inv_data_view.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",

        # 'demo/school_demo_data.xml'
    ],
    'demo': [

    ]

}