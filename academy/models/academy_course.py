'''
This module create module of Course
'''
from openerp import fields, models


class Courses(models.Model):
    '''
    This class create module of Course
    '''
#    _name = 'academy.courses'
    _inherit = 'product.template'

#    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")

