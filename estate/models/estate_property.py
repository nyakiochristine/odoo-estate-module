from odoo import models, fields
from odoo import api
from odoo.exceptions import ValidationError,UserError


class EstateProperty(models.Model):
    #name is the unique identifier for thi model
    _name= "estate.property"
    _description = "Real Estate Property"

    #basic fields
    name =fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    #computed fields
    # Computed field
    total_area = fields.Integer(compute="_compute_total_area")

    #new filed
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], required=True, copy=False, default='new')
    

   
    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Buyer', copy=False)


    @api.depends('living_area', 'garden_area')
    #readonly field that is calculated based on the living area and garden area
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.onchange("garden")
    #onchange method that updates the garden area and orientation based on the value of the garden field
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False
    
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 'The expected price must be strictly positive!'),
        
        ('check_selling_price', 'CHECK(selling_price >0)', 'The selling price must be positive!')
    ]

    @api.constrains('selling_price', 'expected_price')
    @api.constrains('selling_price', 'expected_price')
    def _check_price_difference(self):
        for record in self:
            if record.selling_price > 0 and record.selling_price < (record.expected_price * 0.9):
                # Use ValidationError directly here
                raise ValidationError("The selling price cannot be less than 90% of the expected price!")

    

    def action_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("A canceled property cannot be sold.")
            record.state = 'sold'
        return True

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("A sold property cannot be canceled.")
            record.state = 'canceled'
        return True
    
    def action_cancel(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'estate.cancel.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_property_id': self.id}, # Passes current property to wizard
        }

class EstatePropertyType(models.Model):
     _name = "estate.property.type"
     _description = "Property Type"

     name = fields.Char(required=True)

class EstatePropertyTag(models.Model):
        _name = "estate.property.tag"
        _description = "Property Tag"
    
        name = fields.Char(required=True)