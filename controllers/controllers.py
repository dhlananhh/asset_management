# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/omAssetManagement(http.Controller):
#     @http.route('/custom_addons/om_asset_management/custom_addons/om_asset_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/om_asset_management/custom_addons/om_asset_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/om_asset_management.listing', {
#             'root': '/custom_addons/om_asset_management/custom_addons/om_asset_management',
#             'objects': http.request.env['custom_addons/om_asset_management.custom_addons/om_asset_management'].search([]),
#         })

#     @http.route('/custom_addons/om_asset_management/custom_addons/om_asset_management/objects/<model("custom_addons/om_asset_management.custom_addons/om_asset_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/om_asset_management.object', {
#             'object': obj
#         })

