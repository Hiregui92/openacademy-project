'''
Controller for interpret browser requests and send data back
'''
# -*- coding: utf-8 -*-
from openerp import http


class Academy(http.Controller):
    '''
    This class handles routing
    '''
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([]),
        })

