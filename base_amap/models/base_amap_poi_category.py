# -*- coding: utf-8 -*-
# Copyright(c): 2019 Freshoo (<www.freshoo.cn>)

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class AmapPoiCategory(models.Model):
    _name = 'base.amap.poi_category'
    _description = 'Amap Point of Information Types'
    """ POI Data: https://lbs.amap.com/api/webservice/download """

    name = fields.Char(string='Name', required=True, translate=True)
    code = fields.Char(string='Code', required=True, index=True)
    parent_id = fields.Many2one('base.amap.poi_category', string='Parent Category', index=True, ondelete='cascade')
    child_ids = fields.One2many('base.amap.poi_category', 'parent_id', string='Child Categories')
    active = fields.Boolean('Active', default=True)

    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_('You can not create recursive POI categories.'))

    def name_get(self):
        """ Return the categories' display name, including their direct
            parent by default.

            If ``context['poi_category_display']`` is ``'short'``, the short
            version of the category name (without the direct parent) is used.
            The default is the long version.
        """
        if self._context.get('poi_category_display') == 'short':
            return super(AmapPoiCategory, self).name_get()

        res = []
        for category in self:
            names = []
            current = category
            while current:
                names.append(current.name)
                current = current.parent_id
            res.append((category.id, ' / '.join(reversed(names))))
        return res

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            args = [('name', operator, name)] + args
        poi_category_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return models.lazy_name_get(self.browse(poi_category_ids).with_user(name_get_uid))
