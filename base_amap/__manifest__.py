# -*- coding: utf-8 -*-
# Copyright(c): 2019 Freshoo (<www.freshoo.cn>)

{
    'name': 'Amap Service',
    'version': '13.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Tools',
    'description': """
Integrate Amap Service to Odoo
===================================
Geocoding

Weather

Search POI

Coordinate Convert

Input Tips

IP Query

Address Query
""",
    'author': 'dong@freshoo.cn',
    'website': 'https://www.freshoo.cn',
    'images': ['static/description/banner.png'],
    'depends': ['base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'data/base_amap_data.xml',
        'data/base.amap.poi_category.csv',
        'views/base_amap_poi_category_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': True,
}
