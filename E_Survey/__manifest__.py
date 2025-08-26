# -*- coding: utf-8 -*-
{
    'name': "E-Survey",
    'author': "Hadeel Hamoud",
    'category': 'Surveys',
    'version': '0.1',

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,
    'website': "",

    'depends': ['web'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/survey.xml',
        'views/welcome_page.xml',
        'views/thanks_page.xml'
    ],

    "application": True,
    'installable': True,
    'qweb': [],
    'routes': [
        '/hayyak_survey',
        '/survey_form',
        '/survey_submitted'
    ]
}
