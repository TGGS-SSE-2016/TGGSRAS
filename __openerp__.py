# -*- coding: utf-8 -*-
{
    'name': "TGGS Research and Academic Service",

    'summary': """
        This module can serve the staffs in TGGS Research and Academic Service Department""",

    'description': """
        This is a module for TGGS Research and Academic Service Department
    """,

    'author': "Sarin Suriyakoon",
    'website': "http://tggs.kmutnb.ac.th/",

    'category': 'TGGS',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/tggsras_security.xml',
        'tggsras_project/tggsras_project.xml',
        'tggsras_project/project_workflow.xml',
        'tggsras_project_progress/tggsras_project_progress.xml',
        'tggsras_building/tggsras_building.xml',
        'tggsras_building/building_workflow.xml',
        'tggsras_supply/tggsras_supply.xml',
        'tggsras_supply/supply_workflow.xml',
        'tggsras_torannounce/tggsras_torannounce.xml',
        'menu/tggsras_menu.xml',
        'report/tggsras_building/invoice.xml',
        'report/tggsras_project/proposal.xml',
        'report/tggsras_supply/invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
