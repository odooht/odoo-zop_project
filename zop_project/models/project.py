# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


    
class Project(models.Model):
    _inherit = "project.project"
    
    # inherit from project
    #name = fields.Char("Name", index=True, required=True, track_visibility='onchange')
    
    # customer, employer
    #partner_id = fields.Many2one('res.partner', string='Customer', auto_join=True, track_visibility='onchange')
    
    # contractor ?
    #company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.user.company_id)

    code = fields.Char("Code", index=True, required=True)

    constructor_id = fields.Many2one('res.partner', string='Constructor Company',
                                     domain=[('is_company','=',True )] )
    supervisor_id = fields.Many2one('res.partner', string='Supervisor Company',
                                     domain=[('is_company','=',True )] )
    designer_id = fields.Many2one('res.partner', string='Designer Company',
                                     domain=[('is_company','=',True )] )
    consultor_id = fields.Many2one('res.partner', string='Consultor Company',
                                     domain=[('is_company','=',True )] )
    
class Task(models.Model):
    _inherit = "project.task"
    _rec_name = 'full_name'
    _order = 'code'
    
    # inherit from project.task
    #name = fields.Char(string='Title', track_visibility='always', required=True, index=True)
    #description = fields.Html(string='Description')
    #tag_ids = fields.Many2many('project.tags', string='Tags', oldname='categ_ids')
    
    #date_start = fields.Datetime(string='Starting Date',)
    #date_end = fields.Datetime(string='Ending Date', index=True, copy=False)
    #date_deadline = fields.Date(string='Deadline', index=True, copy=False, track_visibility='onchange')
    #project_id = fields.Many2one('project.project', string='Project',
    #partner_id = fields.Many2one('res.partner', string='Customer',)
    #parent_id = fields.Many2one('project.task', string='Parent Task', index=True)
    #child_ids = fields.One2many('project.task', 'parent_id', string="Sub-tasks", context={'active_test': False})
    #subtask_count = fields.Integer("Sub-task count", compute='_compute_subtask_count')

    code = fields.Char("Code", index=True, required=True)
    full_name = fields.Char('Name', compute='_compute_name')
    
    is_leaf = fields.Boolean()
    
    uom_id = fields.Many2one('product.uom', 'Unit of Measure')
    qty = fields.Float('Planed Quantity', default=0.0)
    price = fields.Float('Price', default=0.0 )
    amount = fields.Float('Planed Amount', default=0.0, compute = '_compute_amount')

    qty_acc = fields.Float('Accumulate Quantity', default=0.0, compute = '_compute_acc')
    amount_acc = fields.Float('Accumulate Amount', default=0.0, compute = '_compute_acc')
    
    rate = fields.Float('Rate', default=0.0, compute = '_compute_rate' )
    
    daywork_ids = fields.One2many('project.task.daywork','task_id',string='Task Dayworks')

    @api.multi
    @api.depends('project_id','parent_id.full_name')
    def _compute_name(self):
        for rec in self:
            if rec.parent_id:
                rec.full_name  = rec.parent_id.full_name + '.' + rec.name
            else:
                rec.full_name  = rec.name

    @api.multi
    @api.depends('amount','rate')
    def _compute_rate(self):
        for rec in self:
            rec.rate = ( rec.amount and rec.amount_acc 
                       ) and ( rec.amount_acc / rec.amount ) or 0.0


    @api.multi
    @api.depends('is_leaf','daywork_ids.qty_close')
    def _compute_acc(self):
        for rec in self:
            if rec.is_leaf:
                works = rec.daywork_ids.sorted(key='date', reverse=True)
                if works:
                    rec.qty_acc = works[0].qty_close
                    rec.amount_acc = works[0].qty_close * rec.price
                else:
                    rec.qty_acc = 0
                    rec.amount_acc = 0
            else:
                rec.amount_acc = sum( rec.child_ids.mapped('amount_acc') )


    @api.multi
    @api.depends('is_leaf','qty','price','child_ids.amount')
    def _compute_amount(self):
        for rec in self:
            if rec.is_leaf:
                rec.amount = rec.qty * rec.price
            else:
                rec.amount = sum( rec.child_ids.mapped('amount') )

    
    

class TaskDaywork(models.Model):
    _name = "project.task.daywork"
    _description = "Project Task Daywork"
    _rec_name = 'full_name'

    name = fields.Char('Name', compute='_compute_name')
    full_name = fields.Char('Name', compute='_compute_name')
    date = fields.Date('Date',required=True,index=True )
    
    project_id = fields.Many2one(related='task_id.project_id')
    task_id = fields.Many2one('project.task', 'Task')
    uom_id = fields.Many2one(related='task_id.uom_id')
    price = fields.Float(related='task_id.price')

    last_daywork_id = fields.Many2one('project.task.daywork', 'Last Daywork')
    qty = fields.Float('Quantity', default=0.0)
    qty_open = fields.Float('Open Quantity', default=0.0, compute = '_compute_qty')
    qty_close = fields.Float('Close Quantity', default=0.0, compute = '_compute_qty')

    @api.multi
    @api.depends('task_id.full_name')
    def _compute_name(self):
        for rec in self:
            if rec.task_id:
                rec.name  = rec.task_id.name + '.' + fields.Date.to_string(rec.date)
                rec.full_name = rec.task_id.full_name + '.' + fields.Date.to_string(rec.date)


    @api.multi
    @api.depends('qty','last_daywork_id.qty_close')
    def _compute_qty(self):
        for rec in self:
            if rec.last_daywork_id:
                rec.qty_open = rec.last_daywork_id.qty_close
                rec.qty_close = rec.last_daywork_id.qty_close + rec.qty
            else:
                rec.qty_open = 0
                rec.qty_close = rec.qty





