# -*- coding: utf-8 -*-
{
    "name": "Asset Management",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "summary": "Manage internal assets for employees and departments.",
    "description": """
        A simple module to manage asset registrations, track status,
        and assign assets to employees within a department.
    """,
    "author": "Duong Hoang Lan Anh",
    "category": "Human Resources",
    "depends": [
        "base",
        "hr",
        "mail",
    ],
    "data": [
        # Security files must be loaded first
        "security/asset_management_security.xml",
        "security/ir.model.access.csv",
        # Data files next
        "data/sequence_data.xml",
        # View files
        "views/asset_management_views.xml",
        "views/menu.xml",
    ],
    "demo": [
        "data/demo_data.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
