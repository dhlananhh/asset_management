# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AssetManagement(models.Model):
    _name = "asset.management"
    _description = "Asset Management for Departments"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    def _get_default_reference(self):
        """Generate a unique reference for the asset"""
        return self.env["ir.sequence"].next_by_code("asset.management.sequence")

    name = fields.Char(string="Asset Name", required=True, tracking=True)
    reference = fields.Char(
        string="Reference",
        required=True,
        index=True,
        copy=False,
        default=_get_default_reference,
        readonly=True,
    )

    category_id = fields.Many2one(
        "asset.category", string="Asset Category", tracking=True
    )

    assign_date = fields.Date(string="Assigned Date", default=fields.Date.context_today)

    purchase_date = fields.Date(
        string="Purchase Date", required=True, default=fields.Date.today
    )
    value = fields.Float(string="Value", required=True, tracking=True)

    employee_id = fields.Many2one("hr.employee", string="Assigned to", tracking=True)

    technician_id = fields.Many2one("hr.employee", string="Technician")

    department_id = fields.Many2one(
        "hr.department",
        string="Department",
        related="employee_id.department_id",
        store=True,
        readonly=False,
    )

    state = fields.Selection(
        [
            ("new", "New"),
            ("in_use", "In Use"),
            ("repair", "Under Repair"),
            ("retired", "Retired"),
        ],
        string="Status",
        default="new",
        required=True,
        tracking=True,
    )

    notes = fields.Text(string="Description")

    @api.constrains("value")
    def _check_value(self):
        for record in self:
            if record.value < 0:
                raise ValidationError("The asset value cannot be negative.")
