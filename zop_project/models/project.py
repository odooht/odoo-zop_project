# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


    
class Project(models.Model):
    _inherit = "project.project"
    
    # inherit from project
    #name = fields.Char("Name", index=True, required=True, track_visibility='onchange')

    #tasks = fields.One2many('project.task', 'project_id', string="Task Activities")
    #user_id = fields.Many2one('res.users', string='Project Manager', default=lambda self: self.env.user, track_visibility="onchange")
    #date_start = fields.Date(string='Start Date')
    #date = fields.Date(string='Expiration Date', index=True, track_visibility='onchange')

    
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
    full_name = fields.Char('Name')
    
    is_leaf = fields.Boolean()
    
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure')
    qty = fields.Float('Planed Quantity', default=0.0)
    price = fields.Float('Price', default=0.0 )
    amount_me = fields.Float('Planed Amount by Me', default=0.0, compute='_compute_amount_me')
    amount_childs = fields.Float('Planed Amount by Childs', default=0.0)
    amount = fields.Float('Planed Amount', default=0.0, compute='_compute_amount')

    daywork_ids = fields.One2many('project.task.daywork','task_id',string='Task Dayworks')
    
    last_daywork_id = fields.Many2one('project.task.daywork', string='Last Daywork')
    
    qty_acc_me = fields.Float('Accumulate Quantity by Me', default=0.0, related='last_daywork_id.qty_close' )
    amount_acc_me = fields.Float('Accumulate Amount by Me', default=0.0,compute='_compute_amount_acc_me' )
    amount_acc_childs = fields.Float('Accumulate Amount by childs', default=0.0 )
    amount_acc = fields.Float('Accumulate Amount', default=0.0,compute='_compute_amount_acc' )
    rate = fields.Float('Rate', default=0.0, compute='_compute_rate'  )

    @api.multi
    @api.depends('qty','price')
    def _compute_amount_me(self):
        for rec in self:
            rec.amount_me = rec.qty * rec.price
    
    @api.multi
    @api.depends('amount_me','is_leaf','amount_childs')
    def _compute_amount(self):
        for rec in self:
            if rec.is_leaf:
                rec.amount = rec.amount_me
            else:
                rec.amount = rec.amount_childs
    
    @api.multi
    @api.depends('qty','price')
    def _compute_amount_acc_me(self):
        for rec in self:
            rec.amount_acc_me = rec.qty_acc_me * rec.price
    
    @api.multi
    @api.depends('amount_me','is_leaf','amount_childs')
    def _compute_amount_acc(self):
        for rec in self:
            if rec.is_leaf:
                rec.amount_acc = rec.amount_acc_me
            else:
                rec.amount_acc = rec.amount_acc_childs
    
    @api.multi
    @api.depends('amount','qty_acc','price')
    def _compute_rate(self):
        for rec in self:
            rec.rate = ( rec.amount and rec.amount_acc 
                       ) and ( rec.amount_acc / rec.amount ) or 0.0
    
    def _set_full_name(self):
        if self.parent_id:
            self.full_name = self.parent_id.full_name + '.' + self.name
        else:
            self.full_name = self.name

    def _set_amount_childs(self):
        self.amount_childs =  sum( self.child_ids.mapped('amount') )
        if self.parent_id:
            self.parent_id._set_amount_childs()

    @api.multi
    def write(self, vals):
        old_parent_id = self.parent_id.id
        old_amount = self.amount
        
        ret = super(Task, self).write(vals)
        
        if not vals.get('full_name'):
            if vals.get('parent_id') or vals.get('name'):
                self._set_full_name()
        
        if self.parent_id.id != old_parent_id:
            if old_parent_id:
                self.browse(old_parent_id)._set_amount_childs()

        if self.parent_id.id != old_parent_id or self.amount != old_amount:
            if self.parent_id:
                self.parent_id._set_amount_childs()

        return ret

    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals)
        if not vals.get('full_name'):
            task._set_full_name()
        
        if task.parent_id and task.amount:
            task.parent_id._set_amount_childs()
        
        return task

class TaskDaywork(models.Model):
    _name = "project.task.daywork"
    _description = "Project Task Daywork"
    _rec_name = 'full_name'

    name = fields.Char('Name' )
    full_name = fields.Char('Name' )
    date = fields.Date('Date',required=True,index=True )
    
    project_id = fields.Many2one(related='task_id.project_id')
    task_id = fields.Many2one('project.task', 'Task')
    uom_id = fields.Many2one(related='task_id.uom_id')
    price = fields.Float(related='task_id.price')

    last_daywork_id = fields.Many2one('project.task.daywork', 'Last Daywork')
    qty = fields.Float('Quantity', default=0.0)
    qty_open = fields.Float('Open Quantity', default=0.0 )
    qty_close = fields.Float('Close Quantity', default=0.0, compute='_compute_qty_close' )

    @api.multi
    @api.depends('qty','qty_open')
    def _compute_qty_close(self):
        for rec in self:
            rec.qty_close = rec.qty_open + rec.qty

    def _set_name(self):
        self.name = ( self.task_id.name or '' ) + '.' + (
                      self.data and fields.Date.to_string( self.data ) or '' )

    def _set_full_name(self):
        self.full_name = ( self.task_id.full_name or '' ) + '.' + (
                      self.data and fields.Date.to_string( self.data ) or '' )

    def _set_qty_open(self):
        if self.last_daywork_id:
            self.qty_open = self.last_daywork_id.qty_close
        else:
            self.qty_open = 0
            
    @api.multi
    def write(self, vals):
        old_date = self.date
        old_task = self.task_id
        old_last_daywork_id = self.last_daywork_id.id
        
        ret = super(TaskDaywork, self).write(vals)
        
        if old_task != self.task_id or old_date != self.date:
            if not vals.get('name'):
                daywork._set_name()
                
            if not vals.get('full_name'):
                daywork._set_full_name()

        if old_last_daywork_id != self.last_daywork_id.id
            if not vals.get('qty_open'):
                self._set_qty_open()

        return ret

    @api.model
    def create(self, vals):
        daywork = super(TaskDaywork, self).create(vals)
        if not vals.get('name'):
            daywork._set_name()

        if not vals.get('full_name'):
            daywork._set_full_name()
        
        if not vals.get('qty_open'):
            daywork._set_qty_open()
        
        return daywork
