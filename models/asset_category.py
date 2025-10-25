# -*- coding: utf-8 -*-

from odoo import fields, models


class AssetCategory(models.Model):
    _name = "asset.category"
    _description = "Asset Category"

    name = fields.Char(string="Name", required=True)
