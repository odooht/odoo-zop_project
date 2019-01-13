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

    code = fields.Char("Code", index=True)

    constructor_id = fields.Many2one('res.partner', string='Constructor Company',
                                     domain=[('is_company','=',True )] )
    supervisor_id = fields.Many2one('res.partner', string='Supervisor Company',
                                     domain=[('is_company','=',True )] )
    designer_id = fields.Many2one('res.partner', string='Designer Company',
                                     domain=[('is_company','=',True )] )
    consultor_id = fields.Many2one('res.partner', string='Consultor Company',
                                     domain=[('is_company','=',True )] )
    
class Work(models.Model):
    _name = "project.work"
    _order = 'code'
    _parent_store = True

    name = fields.Char('Name')
    code = fields.Char("Code"  )
    full_name = fields.Char('Full Name')
    
    date_from = fields.Datetime(string='Starting Date')
    date_thru = fields.Datetime(string='Ending Date' )
    project_id = fields.Many2one('project.project', string='Project')
    partner_id = fields.Many2one('res.partner', string='Customer',)
    
    parent_id = fields.Many2one('project.work', string='Parent Work')
    child_ids = fields.One2many('project.work', 'parent_id', string="Sub-works")
    parent_path = fields.Char(index=True)

    work_type = fields.Selection([
        ('group','Group'),
        ('node','Node'),
        ('item','Item'),
    ])
    
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure')
    qty = fields.Float('Planed Quantity', default=0.0)
    price = fields.Float('Price', default=0.0 )
    amount_me = fields.Float('Planed Amount by Me', default=0.0, compute='_compute_amount_me')
    amount_childs = fields.Float('Planed Amount by Childs', default=0.0)
    amount = fields.Float('Planed Amount', default=0.0, compute='_compute_amount')

    @api.multi
    @api.depends('qty','price')
    def _compute_amount_me(self):
        for rec in self:
            rec.amount_me = rec.qty * rec.price
    
    @api.multi
    @api.depends('amount_me','work_type','amount_childs')
    def _compute_amount(self):
        for rec in self:
            if rec.work_type == 'group':
                rec.amount = rec.amount_childs
            else:
                rec.amount = rec.amount_me
    
    def _set_full_name(self):
        if self.parent_id:
            self.full_name = self.parent_id.full_name + '.' + self.name
        else:
            self.full_name = self.name

    def _set_amount_childs(self):
        childs = self.search[('id','child_of', self.id)]
        self.amount_childs =  sum( childs.mapped('amount') )
        if self.parent_id:
            self.parent_id._set_amount_childs()

    @api.multi
    def write(self, vals):
        old_parent_id = self.parent_id.id
        old_amount = self.amount
        
        ret = super(Work, self).write(vals)
        
        if not vals.get('full_name'):
            if vals.get('parent_id') or vals.get('name'):
                self._set_full_name()
        
        if self.parent_id.id != old_parent_id:
            if old_parent_id:
                old_parent = self.browse(old_parent_id)
                old_parent._set_amount_childs()

        if self.parent_id.id != old_parent_id or self.amount != old_amount:
            if self.parent_id:
                self.parent_id._set_amount_childs()

        return ret

    @api.model
    def create(self, vals):
        work = super(Work, self).create(vals)
        if not vals.get('full_name'):
            work._set_full_name()
        
        if work.parent_id and work.amount:
            work.parent_id._set_amount_childs()
        
        return work

    worksheet_ids = fields.One2many('project.worksheet','work_id',string='Worksheets')


class Worksheet(models.Model):
    _name = "project.worksheet"
    _description = "Project Worksheet"
    _rec_name = 'full_name'

    code = fields.Char()
    sequence = fields.Integer()
    number = fields.Integer()
    name = fields.Char('Name' )
    full_name = fields.Char('Full Name' )
    date = fields.Date('Date',required=True,index=True )
    
    work_id = fields.Many2one('project.work', 'Work')
    project_id = fields.Many2one(related='work_id.project_id')
    uom_id = fields.Many2one(related='work_id.uom_id')
    price = fields.Float(related='work_id.price')
    qty = fields.Float('Quantity', default=0.0)

    def _set_code(self):
        self.code = ( self.work_id.code or '' ) + '.' + (
                      self.date and fields.Date.to_string( self.date ) or '' ) + '.' + (
                      str( self.number or 0 ) )

    def _set_name(self):
        self.name = ( self.work_id.name or '' ) + '.' + (
                      self.date and fields.Date.to_string( self.date ) or '' ) + '.' + (
                      str( self.number or 0 ) )

    def _set_full_name(self):
        self.full_name = ( self.work_id.full_name or '' ) + '.' + (
                      self.date and fields.Date.to_string( self.date ) or '' ) + '.' + (
                      str( self.number or 0 ) )

    @api.multi
    def write(self, vals):
        old_date = self.date
        old_code = self.code
        old_work = self.work_id
        
        ret = super(Worksheet, self).write(vals)
        
        if old_work != self.work_id or old_date != self.date or old_code != self.code:
            if not vals.get('code'):
                self._set_code()
                
            if not vals.get('name'):
                self._set_name()
                
            if not vals.get('full_name'):
                self._set_full_name()

        return ret

    @api.model
    def create(self, vals):
        worksheet = super(Worksheet, self).create(vals)
        if not vals.get('code'):
            worksheet._set_code()

        if not vals.get('name'):
            worksheet._set_name()

        if not vals.get('full_name'):
            worksheet._set_full_name()
        
        return worksheet

class DateDimention(models.Model):
    _name = "olap.dim.date"
    _description = "OLAP Dimention Date"
    _rec_name = 'daykey'
    
    date = fields.Date('Date',required=True,index=True )
    daykey = fields.Integer(help='yyyymmdd')
    weekkey = fields.Integer(help='yyyyww')
    monthkey = fields.Integer(help='yyyymm')
    quarterkey = fields.Integer(help='yyyy0q')

    year = fields.Integer(help='yyyy')
    quarter = fields.Integer(help='q')
    month = fields.Integer(help='m')
    week = fields.Integer(help='w')
    day = fields.Integer(help='d')


class Workfact(models.Model):
    _name = "project.workfact"
    _description = "Project Workfact"
    _rec_name = 'full_name'

    name = fields.Char('Name' )
    full_name = fields.Char('Full Name' )
    date_id = fields.Many2one('olap.dim.date', 'Dimention Date')
    date_type = fields.Selection([
        ('day','Day'),
        ('week','Week'),
        ('month','Month'),
        ('quarter','Quarter'),
        ('year','Year'),
    ])
    
    date = fields.Date(related='date_id.date' )
    daykey = fields.Integer( related='date_id.daykey' )
    weekkey = fields.Integer(related='date_id.weekkey')
    monthkey = fields.Integer(related='date_id.monthkey')
    quarterkey = fields.Integer(related='date_id.quarterkey')
    day = fields.Integer( related='date_id.day' )
    week = fields.Integer(related='date_id.week')
    month = fields.Integer(related='date_id.month')
    quarter = fields.Integer(related='date_id.quarter')
    year = fields.Integer(related='date_id.year')
    

    project_id = fields.Many2one(related='work_id.project_id')
    work_id = fields.Many2one('project.work', 'Work')
    uom_id = fields.Many2one(related='work_id.uom_id')
    price = fields.Float(related='work_id.price')
    is_leaf = fields.Boolean(related='work_id.is_leaf')

    worksheet_ids = fields.Many2many('project.worksheet')
    last_workfact_id = fields.Many2one('project.workfact', 'Open Workfact')

    qty_delta = fields.Float('Delta Quantity', default=0.0, compute='_compute_qty_delta' )
    qty_open = fields.Float('Open Quantity', default=0.0 , 
        help='related last_workfact_id.qty_close, but no compute ' )
        
    qty_close = fields.Float('Close Quantity', default=0.0, compute='_compute_qty_close' )

    qty = fields.Float('Planed Quantity', default=0.0, related='work_id.qty')
    amount = fields.Float('Planed Amount', default=0.0, related='work_id.amount')

    amount_open_me  = fields.Float('Open Amount by Me', default=0.0,compute='_compute_amount_open_me' )
    amount_delta_me = fields.Float('Delta Amount by Me', default=0.0,compute='_compute_amount_delta_me' )
    amount_close_me = fields.Float('Close Amount by Me', default=0.0,compute='_compute_amount_close_me' )

    amount_open_childs  = fields.Float('Open Amount by childs', default=0.0 )
    amount_delta_childs = fields.Float('Delta Amount by childs', default=0.0 )
    amount_close_childs = fields.Float('Close Amount by childs', default=0.0 )

    amount_open  = fields.Float('Open Amount by Me', default=0.0,compute='_compute_amount' )
    amount_delta = fields.Float('Delta Amount by Me', default=0.0,compute='_compute_amount' )
    amount_close = fields.Float('Close Amount by Me', default=0.0,compute='_compute_amount' )

    rate = fields.Float('Rate', default=0.0, compute='_compute_rate'  )

    def _set_name(self):
        self.name = ( self.work_id.name or '' ) + '.' + str(self.daykey)

    def _set_full_name(self):
        self.full_name = ( self.work_id.full_name or '' ) + '.' + str(self.daykey)

    @api.multi
    def write(self, vals):
        old_daykey = self.daykey
        old_work = self.work_id
        old_last_workfact_id = self.last_workfact_id
        
        ret = super(Workfact, self).write(vals)
        
        if old_work != self.work_id or old_daykey != self.daykey:
            if not vals.get('name'):
                self._set_name()
                
            if not vals.get('full_name'):
                self._set_full_name()

        if old_last_workfact_id != self.last_workfact_id:
            if not vals.get('qty_open'):
                self._set_qty_open()
        

        return ret

    @api.model
    def create(self, vals):
        workfact = super(Workfact, self).create(vals)
        if not vals.get('name'):
            workfact._set_name()

        if not vals.get('full_name'):
            workfact._set_full_name()

        if not vals.get('qty_open'):
            workfact._set_qty_open()
        
        return workfact
    
    @api.multi
    @api.depends('worksheet_ids.qty')
    def _compute_qty_delta(self):
        for rec in self:
            rec.qty_delta = sum(rec.worksheet_ids.mapped('qty') )

    def _set_qty_open(self):
        if self.last_workfact_id:
            self.qty_open = self.last_workfact_id.qty_close
        else:
            self.qty_open = 0

    @api.multi
    @api.depends('qty_delta','qty_open')
    def _compute_qty_close(self):
        for rec in self:
            rec.qty_close = rec.qty_open + rec.qty_delta


    @api.multi
    @api.depends('qty_open','price')
    def _compute_amount_open_me(self):
        for rec in self:
            rec.amount_open_me = rec.qty_open * rec.price
    
    @api.multi
    @api.depends('qty_delta','price')
    def _compute_amount_delta_me(self):
        for rec in self:
            rec.amount_delta_me = rec.qty_delta * rec.price
    
    @api.multi
    @api.depends('qty_close','price')
    def _compute_amount_close_me(self):
        for rec in self:
            rec.amount_close_me = rec.qty_close * rec.price

    def _set_amount_childs(self):
        child_worksheet_ids = self.work_id.child_ids.mapped('worksheet_ids')
        
        open  = sum( child_worksheet_ids.mapped('amount_open_childs') )
        delta = sum( child_worksheet_ids.mapped('amount_delta_childs') )
        self.amount_open_childs  = open
        self.amount_delta_childs = delta
        self.amount_close_childs = open + delta
        if self.parent_id:
            self.parent_id._set_amount_childs()

    
    @api.multi
    @api.depends('amount_open_me','amount_delta_me','amount_close_me',
                 'amount_open_childs','amount_delta_childs','amount_close_childs')
    def _compute_amount(self):
        for rec in self:
            if rec.is_leaf:
                rec.amount_open  = rec.amount_open_me
                rec.amount_delta = rec.amount_delta_me
                rec.amount_close = rec.amount_close_me
            else:
                rec.amount_open  = rec.amount_open_childs
                rec.amount_delta = rec.amount_delta_childs
                rec.amount_close = rec.amount_close_childs
    
   
    @api.multi
    @api.depends('amount','amount_close')
    def _compute_rate(self):
        for rec in self:
            rec.rate = ( rec.amount and rec.amount_close 
                       ) and ( rec.amount_close / rec.amount ) or 0.0
