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
    
    date_from = fields.Datetime(string='Starting Date')
    date_thru = fields.Datetime(string='Ending Date' )
    project_id = fields.Many2one('project.project', string='Project')
    partner_id = fields.Many2one('res.partner', string='Customer',)
    
    parent_id = fields.Many2one('project.work', string='Parent Work')
    child_ids = fields.One2many('project.work', 'parent_id', string="Sub-works")
    subwork_count = fields.Integer("Sub-work count", compute='_compute_subwork_count')
    parent_path = fields.Char(index=True)

    work_type = fields.Selection([
        ('group','Group'),
        ('node','Node'),
        ('item','Item'),
    ], default='group')
    
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure')
    
    qty = fields.Float('Planed Quantity', default=0.0)
    
    price = fields.Float('Price', default=0.0 )
    amount = fields.Float('Planed Amount', default=0.0, compute='_compute_amount' )
    
    worksheet_ids = fields.One2many('project.worksheet','work_id',string='Worksheets')

    @api.multi
    @api.onchange('name','parent_id.full_name')
    def _set_full_name(self):
        for rec in self:
            fname = []
            if rec.parent_id:
                pname = rec.parent_id.full_name
                fname.append( pname and pname or '' )
            fname.append(rec.name and rec.name or '') 
            rec.full_name = '.'.join(fname)
                
    @api.multi
    def set_full_name(self):
        for rec in self:
            fname = []
            if rec.parent_id:
                pname = rec.parent_id.full_name
                if not pname:
                    rec.parent_id.set_full_name()
                    pname = rec.parent_id.full_name or ''
                fname.append( pname and pname or '' )
            fname.append(rec.name and rec.name or '') 
            rec.full_name = '.'.join(fname)
            

    @api.depends('child_ids')
    def _compute_subwork_count(self):
        """ Note: since we accept only one level subwork, we can use a read_group here """
        work_data = self.env['project.work'].read_group([('parent_id', 'in', self.ids)], ['parent_id'], ['parent_id'])
        mapping = dict((data['parent_id'][0], data['parent_id_count']) for data in work_data)
        for work in self:
            work.subwork_count = mapping.get(work.id, 0)

    @api.multi
    @api.onchange('child_ids.amount')
    def _set_price(self):
        for rec in self:
            if rec.work_type == 'group' or ( rec.work_type == 'node' and rec.child_ids ):
                if not rec.qty:
                    rec.qty = 1
                childs = rec.search([('id','child_of', rec.id), ('child_ids','=',False)])
                amount =  sum( childs.mapped('amount') )
                rec.price = amount and rec.qty and amount / rec.qty or 0

    @api.multi
    @api.depends('qty','price')
    def _compute_amount(self):
        for rec in self:
            rec.amount = rec.qty * rec.price

    @api.multi
    def set_amount(self):
        for rec in self:
            rec._set_price()
            parents = rec.search([('id','parent_of', rec.id)])
            for parent in parents:
                parent._set_price()

    @api.multi
    def write(self,vals):
        set_full_name = vals.get('set_full_name')
        set_amount = vals.get('set_amount')
        
        if set_full_name:
            del vals['set_full_name']
        
        if set_amount:
            del vals['set_amount']
        
        ret = super(Work, self).write(vals)
        
        if set_full_name:
            self.set_full_name()
        
        if set_amount:
            self.set_amount()

        return ret

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

    @api.multi
    def set_name(self):
        for rec in self:
            rec._set_code()
            rec._set_name()
            rec._set_full_name()
    
    def _post_one(self):
        fact = self.env[('project.workfact')].find_or_create(self.work_id, self.date, 'day')
        fact.post(self)
    
    @api.multi
    def post(self):
        for rec in self:
            rec.state = 'post'
            rec._post_one()

    @api.multi
    def write(self,vals):
        set_name = vals.get('set_name')
        post = vals.get('post')
        
        if post:
            del vals['post']
        
        if set_name:
            del vals['set_name']
        
        ret = super(Worksheet, self).write(vals)
        
        if set_name:
            self.set_name()
        
        if post:
            self.post()

        return ret

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

    @api.model
    def create_and_set_name(self, vals):
        fact = self.create(vals)
        fact._set_full_name()
        fact._set_name()
        return fact
    

    @api.model
    def find_or_create(self,work_id,date,date_type ):
        dimdate = self.env['olap.dim.date'].search([('date','=', date)], limit=1)
        fact = self.search([
            ('work_id','=', work_id.id),
            ('date_id','=',dimdate.id),
            ('date_type','=',date_type)], limit=1 )

        if fact:
            return fact
        
        last_fact = self.search([
            ('work_id','=', work_id.id), 
            ('date_type','=',date_type),
            ('date','<',date)])
            
        if not last_fact:
            return self.create_and_set_name({
                'work_id': work_id.id,
                'date_id': dimdate.id,
                'date_type': date_type })

        print(last_fact)
        last_fact.sorted(key='date', reverse=True)
        print(last_fact)
        last_fact = last_fact[0]
        print(last_fact)
        
        last_dimdates = self.env['olap.dim.date'].search([
            ('date','>', last_fact.date),
            ('date','<', date)], order='date' )
                
        for last_dimdate in last_dimdates:
            last_fact = self.create_and_set_name({ 
                'work_id': work_id.id,
                'date_id': last_dimdate.id,
                'date_type': date_type,
                'last_workfact_id': last_fact.id })
            
        return self.create_and_set_name({
                'work_id': work_id.id,
                'date_id': dimdate.id,
                'date_type': date_type,
                'last_workfact_id': last_fact.id  })

    @api.multi
    def post(self,worksheets):
        self.ensure_one()
        self.worksheet_ids |= worksheets
        self._set_qty_delta()
        self._set_qty_open()

    #@api.multi
    #def set_qty_delta(self):
        
    