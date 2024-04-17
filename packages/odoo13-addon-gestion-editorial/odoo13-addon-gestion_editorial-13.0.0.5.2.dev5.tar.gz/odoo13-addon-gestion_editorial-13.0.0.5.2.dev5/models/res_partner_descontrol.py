from odoo import models, fields

class EditorialPartners(models.Model):
    """ Extend res.partner template for editorial management """

    _description = "Editorial Partners"
    _inherit = 'res.partner'
    # we inherited res.partner model which is Odoo built in model and edited several fields in that model.
    cliente_num = fields.Integer(string="Num. cliente",
                           help="Número interno de cliente")
    is_author = fields.Boolean(string="Es autor", default=False,
                           help="Indica que el contacto es autor")
    tipo_cliente = fields.Selection([('libreria', 'Librería'), ('parada_distri', 'Parada distri'), ('institucional', 'Institucional'), ('otro','Otro')], default='libreria')
    purchase_liq_pricelist = fields.Many2one(
        comodel_name='product.pricelist',
        string="Tarifa liquidaciones de compras",
        company_dependent=False,
        domain=lambda self: [('company_id', 'in', (self.env.company.id, False))],
        help="Esta tarifa se usará por defecto para liquidaciones de compra en depósito de este contacto")
    default_purchase_type = fields.Many2one(
        comodel_name='stock.picking.type',
        string="Tipo de compra",
        help="Este tipo de compra se usará por defecto en los pedidos de compra de este contacto",
        domain="[('code', '=', 'incoming')]"
    )
