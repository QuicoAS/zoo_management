from odoo import models, fields

class Restaurant(models.Model):
    _name = 'zoo.restaurant'
    _description = 'Restaurant dins del Zoològic'

    # Camps generals
    name = fields.Char(string="Nom", required=True, help="Nom del restaurant dins del zoològic")
    capacity = fields.Integer(string="Capacitat Màxima", help="Nombre màxim de persones que pot acollir el restaurant")
    services = fields.Text(string="Serveis", help="Serveis disponibles al restaurant (ex: menjar ràpid, menjar a la carta, etc.)")
    restaurant_type = fields.Selection(
        [
            ('cafeteria', 'Cafeteria Ràpida'),
            ('buffet', 'Buffet Autoservei'),
            ('thematic', 'Restaurant Temàtic'),
            ('vip', 'Àrea VIP'),
            ('foodtruck', 'Food Truck'),
            ('healthy', 'Zona Saludable')
        ],
        string="Tipus de Restaurant",
        default='cafeteria',
        required=True,
        help="Tipus de restaurant o espai gastronòmic dins del zoològic"
    )
    address = fields.Char(string="Adreça", help="Ubicació del restaurant dins del zoològic")

    # Relacions amb altres model
    tags_ids = fields.Many2many('tags.management', string="Etiquetes")
    zoo_id = fields.Many2one('zoo.management', string="Zoològic")
  
    # Camps de control
    image = fields.Binary(string="Imatge del Restaurant", help="Imatge representativa del restaurant")
    notes = fields.Text(string="Notes", help="Informació addicional sobre el restaurant")
