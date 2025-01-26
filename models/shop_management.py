from odoo import models, fields

class Shop(models.Model):
    _name = 'zoo.shop'
    _description = 'Botiga dins del Zoològic'

    # Camps generals
    name = fields.Char(string="Nom", required=True, help="Nom de la botiga dins del zoològic")
    size = fields.Float(string="Mida (m2)", help="Mida de la botiga en metres quadrats")
    shop_type = fields.Selection(
        [
            ('souvenir', 'Botiga de Records'),
            ('food', 'Botiga de Menjar'),
            ('educational', 'Material Educatiu'),
            ('artisan', 'Productes Artesans'),
        ],
        string="Tipus de Botiga",
        default='souvenir',
        required=True,
        help="Tipus de productes que es venen a la botiga"
    )
    notes = fields.Text(string="Notes", help="Notes addicionals sobre la botiga")
    image = fields.Binary(string="Imatge", help="Imatge representativa de la botiga")
    active = fields.Boolean(string="Actiu", default=True, help="Indica si la botiga està activa o no")
    total_capacity = fields.Integer(string="Capacitat Màxima", help="Nombre màxim de clients que pot atendre la botiga")

    # Relacions amb altres models
    zoo_id = fields.Many2one('zoo.management', string="Zoològic", help="Zoològic on es troba la botiga")
    tags_ids = fields.Many2many('tags.management', string="Etiquetes", help="Etiquetes que descriuen la botiga")
