from openerp import fields, models

'''
This module  create module of Courso
'''


class Course(models.Model):
    '''
    This class create module of Course
    '''

    _name = 'openacademy.course'  # Model odoo name

    name = fields.Char(string='Title', required=True)   # Field reserved to identified name rec
    description = fields.Text(string='Description')
