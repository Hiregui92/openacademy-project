'''
Controller for interpret browser requests and send data back
'''
# -*- coding: utf-8 -*-
from openerp import http


class Academy(http.Controller):
    '''
    This class handles routing
    '''
    @http.route('/academy/academy/', auth='public')
    def index(self, **kw):
        return "Hello, world"

