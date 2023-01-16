# -*- coding: utf-8 -*-
from odoo import http


class Test1Angular(http.Controller):
    @http.route('/test1-angular', auth="public", website=True)
    def index(self, **kw):
        return http.request.render('test1-angular.index')
