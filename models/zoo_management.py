from odoo import models, fields, api

class Zoo(models.Model):
    _name = 'zoo.management'
    _description = 'Gestió de Zoològics'

    # Camps generals
    name = fields.Char(string="Nom", required=True)
    city = fields.Char(string="Ciutat", required=True)
    country_id = fields.Many2one('res.country', string="País")
    state_id = fields.Many2one('res.country.state', string="Província")
    size = fields.Float(string="Grandària (m2)", help="Superfície en metres quadrats")

    # Compta animals i espècies
    animal_count = fields.Integer(string="Núm. d'Animals", compute='_compute_animal_count')
    species_count = fields.Integer(string="Núm. d'Espècies", compute='_compute_species_count')

    # Infraestructura del zoològic
    restaurant = fields.Boolean(string="Restaurant")
    parking_capacity = fields.Integer(string="Capacitat d'Aparcament")
    shop = fields.Boolean(string="Botiga")
    cafeteria = fields.Boolean(string="Cafeteria")
    ticket_price = fields.Float(string="Preu d'Entrada")
    
    # Imatges i notes
    image = fields.Binary(string="Imatge")
    notes = fields.Text(string="Notes")
    
    # Relacions amb altres models
    animals_ids = fields.One2many('animal.management', 'zoo_id', string="Animals")
    species_ids = fields.One2many('species.management', 'zoo_id', string="Espècies")
    tags_ids = fields.Many2many('tags.management', string="Tags")
    restaurant_ids = fields.One2many('zoo.restaurant', 'zoo_id', string="Restaurants")
    shop_ids = fields.One2many('zoo.shop', 'zoo_id', string="Botigues")
    
    @api.depends('animals_ids')
    def _compute_animal_count(self):
        for record in self:
            record.animal_count = len(record.animals_ids)
    
    @api.depends('species_ids')
    def _compute_species_count(self):
        for record in self:
            record.species_count = len(record.species_ids)

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}