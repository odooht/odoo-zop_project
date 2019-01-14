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
    _rec_name = 'full_name'
    _parent_store = True

    name = fields.Char('Name')
    code = fields.Char("Code"  )
    full_name = fields.Char('Full Name')
    
    @api.multi
    @api.onchange('name','parent_id.full_name')
    def _set_full_name(self):
        for rec in self:
            if rec.parent_id:
                rec.full_name = rec.parent_id.full_name + '.' + rec.name
            else:
                rec.full_name = rec.name
                

    date_from = fields.Datetime(string='Starting Date')
    date_thru = fields.Datetime(string='Ending Date' )
    project_id = fields.Many2one('project.project', string='Project')
    partner_id = fields.Many2one('res.partner', string='Customer',)
    
    parent_id = fields.Many2one('project.work', string='Parent Work')
    child_ids = fields.One2many('project.work', 'parent_id', string="Sub-works")
    subwork_count = fields.Integer("Sub-work count", compute='_compute_subwork_count')
    parent_path = fields.Char(index=True)

    @api.depends('child_ids')
    def _compute_subwork_count(self):
        """ Note: since we accept only one level subwork, we can use a read_group here """
        work_data = self.env['project.work'].read_group([('parent_id', 'in', self.ids)], ['parent_id'], ['parent_id'])
        mapping = dict((data['parent_id'][0], data['parent_id_count']) for data in work_data)
        for work in self:
            work.subwork_count = mapping.get(work.id, 0)


    work_type = fields.Selection([
        ('group','Group'),
        ('node','Node'),
        ('item','Item'),
    ], default='group')
    
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure')
    qty = fields.Float('Planed Quantity', default=0.0)
    
    price = fields.Float('Price', default=0.0 )
    amount = fields.Float('Planed Amount', default=0.0, compute='_compute_amount' )
    
    @api.multi
    @api.onchange('child_ids.amount')
    def _set_price(self):
        for rec in self:
            if rec.work_type == 'group' or ( rec.work_type == 'node' and rec.child_ids ):
                childs = rec.search([('id','child_of', rec.id), ('child_ids','=',False)])
                amount =  sum( childs.mapped('amount') )
                rec.price = amount and rec.qty and amount / rec.qty or 0

    @api.multi
    @api.depends('qty','price')
    def _compute_amount(self):
        for rec in self:
            rec.amount = rec.qty * rec.price

    @api.multi
    def write(self,vals):
        old_parent_id = self.parent_id.id
        ret = super(Work, self).write(vals)
        if vals.get('name') or vals.get('parent_id'):
            self._set_full_name()

        if vals.get('parent_id') or val.get('price') or val.get('qty'):
            old_parents = self.search([('id','parent_of', old_parent_id)])
            parents = self.search([('id','parent_of', self.id)])
            parents |= old_parents
            
            for parent in parents:
                parent._set_price()

        
        return ret

    @api.model
    def create(self,vals):
        work = super(Work, self).create(vals)
        work._set_full_name()
        
        parents = work.search([('id','parent_of', work.id)])
        for parent in parents:
            parent._set_price()
            
        return work


    """ 
    price_me = fields.Float('Price Me', default=0.0 )
    price_childs = fields.Float('Price Childs', default=0.0,compute='_compute_price_childs' )
    price = fields.Float('Price', default=0.0,compute='_compute_price' )
    
    amount_me = fields.Float('Planed Amount by Me', default=0.0, compute='_compute_amount_me')
    amount_childs = fields.Float('Planed Amount by Childs', default=0.0)
    amount = fields.Float('Planed Amount', default=0.0, compute='_compute_amount')

    @api.multi
    @api.depends('qty','amount_childs')
    def _compute_price_childs(self):
        for rec in self:
            rec.price_childs = rec.amount_childs and rec.qty and rec.amount_childs / rec.qty or 0
    
    @api.multi
    @api.depends('qty','price')
    def _compute_price(self):
        for rec in self:
            
            if rec.work_type == 'item':
                rec.price = rec.price_me
            elif rec.child_ids:
                rec.price = rec.price_childs
            else:
                rec.price = rec.price_me
    

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
    
    @api.multi
    @api.onchange('child_ids.amount')
    def _set_amount_childs(self):
        for rec in self:
            rec.amount_childs = sum(rec.childs.mapped('amount') )
            #childs = self.search([('id','child_of', self.id), ('child_ids','=',False)])
            #self.amount_childs =  sum( childs.mapped('amount') )
    """

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
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('post', 'Post'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], string='Status', default='draft')

    @api.multi
    @api.onchange('date','number','work_id.code')
    def _set_code(self):
        for rec in self:
            rec.code = ( rec.work_id.code or '' ) + '.' + (
                         rec.date and fields.Date.to_string( rec.date ) or '' ) + '.' + (
                         str( rec.number or 0 ) )

    @api.multi
    @api.onchange('date','number','work_id.name')
    def _set_name(self):
        for rec in self:
            rec.name = ( rec.work_id.name or '' ) + '.' + (
                         rec.date and fields.Date.to_string( rec.date ) or '' ) + '.' + (
                         str( rec.number or 0 ) )

    @api.multi
    @api.onchange('date','number','work_id.name')
    def _set_full_name(self):
        for rec in self:
            rec.full_name = ( rec.work_id.full_name or '' ) + '.' + (
                              rec.date and fields.Date.to_string( rec.date ) or '' ) + '.' + (
                              str( rec.number or 0 ) )

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
    work_type = fields.Selection(related='work_id.work_type')

    qty = fields.Float('Planed Quantity', default=0.0, related='work_id.qty')
    amount = fields.Float('Planed Amount', default=0.0, related='work_id.amount')

    @api.multi
    @api.onchange('daykey','work_id.name')
    def _set_name(self):
        for rec in self:
            rec.name = ( rec.work_id.name or '' ) + '.' + str(rec.daykey)

    @api.multi
    @api.onchange('daykey','work_id.full_name')
    def _set_full_name(self):
        for rec in self:
            rec.full_name = ( rec.work_id.full_name or '' ) + '.' + str(rec.daykey)


    worksheet_ids = fields.Many2many('project.worksheet')
    last_workfact_id = fields.Many2one('project.workfact', 'Open Workfact')

    qty_delta = fields.Float('Delta Quantity', default=0.0  )
    qty_open = fields.Float('Open Quantity', default=0.0 , 
        help='related last_workfact_id.qty_close, but no compute ' )
        
    qty_close = fields.Float('Close Quantity', default=0.0, compute='_compute_qty_close' )

    @api.multi
    @api.onchange('worksheet_ids.qty')
    def _set_qty_delta(self):
        for rec in self:
            rec.qty_delta = sum(rec.worksheet_ids.mapped('qty') )

    @api.multi
    @api.onchange('last_workfact_id.qty_close')
    def _set_qty_open(self):
        for rec in self:
            if rec.last_workfact_id:
                rec.qty_open = rec.last_workfact_id.qty_close
            else:
                rec.qty_open = 0

    @api.multi
    @api.depends('qty_delta','qty_open')
    def _compute_qty_close(self):
        for rec in self:
            rec.qty_close = rec.qty_open + rec.qty_delta

    amount_open  = fields.Float('Open Amount', default=0.0 )
    amount_delta = fields.Float('Delta Amount', default=0.0 )
    amount_close = fields.Float('Close Amount', default=0.0 )
    
    rate = fields.Float('Rate', default=0.0, compute='_compute_rate'  )
    
    @api.multi
    @api.depends('amount','amount_close')
    def _compute_rate(self):
        for rec in self:
            rec.rate = ( rec.amount and rec.amount_close 
                       ) and ( rec.amount_close / rec.amount ) or 0.0

    

""" 
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
            if rec.work_type == 'group':
                rec.amount_open  = rec.amount_open_childs
                rec.amount_delta = rec.amount_delta_childs
                rec.amount_close = rec.amount_close_childs
            else:
                rec.amount_open  = rec.amount_open_me
                rec.amount_delta = rec.amount_delta_me
                rec.amount_close = rec.amount_close_me
    
   
"""