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
    amount = fields.Float('Planed Amount', default=0.0)

    qty_acc = fields.Float('Accumulate Quantity', default=0.0)
    amount_acc = fields.Float('Accumulate Amount', default=0.0)
    
    rate = fields.Float('Rate', default=0.0  )
    
    daywork_ids = fields.One2many('project.task.daywork','task_id',string='Task Dayworks')
    
    
    def _set_full_name(self):
        if self.parent_id:
            self.full_name = self.parent_id.full_name + '.' + self.name
        else:
            self.full_name = self.name

    def _set_amount(self):
        if self.is_leaf:
            self.amount = self.qty * self.price
        else:
            self.amount =  sum( self.child_ids.mapped('amount') )

    @api.multi
    def write(self, vals):
        old_parent = self.parent_id
        ret = super(Task, self).write(vals)
        if not vals.get('full_name'):
            if vals.get('parent_id') or vals.get('name')
                self._set_full_name()
        
        todo = 0
        
        if vals.get('qty') != None  or vals.get('price') != None:
            if self.is_leaf:
                self._set_amount()
                todo = 1
        
        if vals.get('parent_id')
            old_parent._set_amount()
            todo = 1
            
        if todo and self.parent_id:
            self.parent_id._set_amount()
        
        return ret

    """ 
    def write2(self, vals):
        name = vals.get('name',None)
        full_name = vals.get('full_name', None)
        parent_id = vals.get('parent_id')
        
        old_parent = self.parent_id
        if not full_name and ( parent_id or name ):
            fname = []
            if parent_id:
                fname.append( self.parent_id.browse(parent_id).full_name )
            elif old_parent:
                fname.append( old_parent.full_name )
        
            fname.append( name and name or self.name )
            vals['full_name'] = '.'.join(fname)
            
        qty = vals.get('qty',None)
        price = vals.get('price', None)
        
        if qty != None or price != None:
            qty1 = ( qty != None and [qty] or [self.qty] )[0]
            price1 = ( price != None and [price] or [self.price] )[0]
            vals['amount'] = qty1 * price1
            
        if parent_id:
            # recompute parent amount
            pass
            
        return super(Task, self).write(vals)
    """
    
    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals)
        if not vals.get('full_name'):
            task._set_full_name()
        
        if vals.get('qty') or vals.get('price'):
            if task.is_leaf:
                task._set_amount()
        
        if task.parent_id and task.amount:
            task.parent_id._set_amount()
        
        return task


""" 

    @api.multi
    @api.depends('amount','amount_acc')
    def _compute_rate(self):
        for rec in self:
            rec.rate = ( rec.amount and rec.amount_acc 
                       ) and ( rec.amount_acc / rec.amount ) or 0.0


    @api.multi
    @api.depends('is_leaf','price','daywork_ids.qty_close')
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


"""    
    

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
    qty_open = fields.Float('Open Quantity', default=0.0  )
    qty_close = fields.Float('Close Quantity', default=0.0 )

    @api.multi
    def write(self, vals):
        date = vals.get('date')
        if date:
            vals['name'] = self.task_id.name + '.' + date
            vals['full_name'] = self.task_id.full_name + '.' + date

        qty = vals.get('qty',None)
        last_daywork_id = vals.get('last_daywork_id',None)

        if last_daywork_id:
            qty_open = self.last_daywork_id.browse(last_daywork_id).qty_close
            vals['qty_open'] = qty_open
            
            if qty != None:
                qty1 = qty
            else:
                qty1 = self.qty
            
            vals['qty_close'] = qty_open + qty1
        
        elif qty != None:
            vals['qty_close'] = self.qty_open + qty
        
        return super(TaskDaywork, self).write(vals)
        
    
    @api.model
    def create(self, vals):
        date = vals.get('date','')
        task_id = vals.get('task_id')
        if task_id:
            task = self.task_id.browse(task_id)
            vals['name'] = task.name + '.' + date
            vals['full_name'] = task.full_name + '.' + date

        qty = vals.get('qty',0)
        last_daywork_id = vals.get('last_daywork_id',None)
        
        qty_open = 0
        if last_daywork_id:
            qty_open = self.last_daywork_id.browse(last_daywork_id).qty_close

        vals['qty_open'] = qty_open
        vals['qty_close'] = qty_open + qty
        

        return super(TaskDaywork, self).create(vals)

