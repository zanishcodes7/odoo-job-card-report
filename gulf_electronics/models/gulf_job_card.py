from odoo import models, fields, api


class GulfJobCard(models.Model):
    _name = 'gulf.job.card'
    _description = 'Gulf Electronics Job Card'
    _order = 'id desc'

    name = fields.Char(string='Job No.', required=True, default='New', copy=False)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)

    # Header Info
    model_no = fields.Char(string='Model No.')
    serial_no = fields.Char(string='Serial No.')
    complain = fields.Text(string='Complain')
    condition = fields.Char(string='Condition')
    accessories = fields.Char(string='Accessories')
    received_by = fields.Char(string='Received By')  # <--- Added Received By
    date_order = fields.Datetime(string='Date', default=fields.Datetime.now)

    # Lines
    line_ids = fields.One2many('gulf.job.card.line', 'job_card_id', string='Job Lines')

    # Fixed Charges
    home_visit_charge = fields.Float(string='Home Visit Charges')
    service_charge = fields.Float(string='Service Charges')

    # Summary Totals
    untaxed_amount = fields.Float(string='Untaxed Amount', compute='_compute_totals', store=True)
    tax_amount = fields.Float(string='Taxes', compute='_compute_totals', store=True)
    total_charges = fields.Float(string='Total', compute='_compute_totals', store=True)

    @api.depends('line_ids.price_subtotal', 'line_ids.tax_id', 'home_visit_charge', 'service_charge')
    def _compute_totals(self):
        for record in self:
            lines_subtotal = sum(line.price_subtotal for line in record.line_ids)
            lines_untaxed = lines_subtotal + record.home_visit_charge + record.service_charge

            total_tax = 0.0
            for line in record.line_ids:
                if line.tax_id:
                    taxes = line.tax_id.compute_all(line.unit_price, quantity=line.product_qty)
                    total_tax += sum(t['amount'] for t in taxes['taxes'])

            record.untaxed_amount = lines_untaxed
            record.tax_amount = total_tax
            record.total_charges = lines_untaxed + total_tax

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                seq = self.env['ir.sequence'].next_by_code('gulf.job.card')
                if not seq:
                    seq = f"JOB/{self.env['gulf.job.card'].search_count([]) + 1:05d}"
                vals['name'] = seq
        return super(GulfJobCard, self).create(vals_list)


class GulfJobCardLine(models.Model):
    _name = 'gulf.job.card.line'
    _description = 'Gulf Electronics Job Card Line'

    job_card_id = fields.Many2one('gulf.job.card', string='Job Card Reference', ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Char(string='Part Description')
    product_qty = fields.Float(string='Quantity', default=1.0)
    unit_price = fields.Float(string='Price')
    tax_id = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Amount', compute='_compute_subtotal', store=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.description = self.product_id.display_name
            self.unit_price = self.product_id.lst_price

    @api.depends('product_qty', 'unit_price')
    def _compute_subtotal(self):
        for line in self:
            line.price_subtotal = line.product_qty * line.unit_price