# -*- coding: utf-8 -*-
{
    'name': 'pos ticket',
    'summary': '修改打印小票格式',
    'description': """

    """,
    'category': 'other',
    'version': '1.0',
    'author': '今晨科技',
    'website': 'http://www.168nz.cn/',
    'depends': ['point_of_sale'],
    'data': [
        'views/template.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': True,
}