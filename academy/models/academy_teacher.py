'''
This module create module of teacher
'''
# -*- coding: utf-8 -*-
from openerp import models, fields


class Teachers(models.Model):
    '''
    This class create module of Teacher
    '''
    _name = 'academy.teachers'
    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")

