from odoo import models, fields

class Tags(models.Model):
    _name = 'tags.management'
    _description = 'Gestió de Tags Generals'
    
    # Camps generals
    name = fields.Char(string="Nom del Tag", required=True)
    color = fields.Integer(string="Color")
    description = fields.Text(string="Descripció")
    tag_type = fields.Selection([
        ('general', 'General'), ('health', 'Salut'), ('food', 'Menjar'),
        ('behaviour', 'Comportament'), ('circumstantial', 'Circumstancial')],
        string="Tipus de Tag", required=True)
    active = fields.Boolean(string="Actiu", default=True)
    end_date = fields.Date(string="Data de finalització")
    icon = fields.Binary(string="Imatge del Tag")
    notes = fields.Text(string="Notes")

    # Relacions Many2many amb animals, espècies i zoològics
    animal_ids = fields.Many2many('animal.management', string="Animals")
    species_ids = fields.Many2many('species.management', string="Espècies")
    zoo_ids = fields.Many2many('zoo.management', string="Zoos")