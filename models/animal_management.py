from odoo import models, fields

class Animal(models.Model):
    _name = 'animal.management'
    _description = 'Gestió d´Animals'

    # Identificació i informació bàsica
    id_code = fields.Char(string="Identificador Únic", required=True)
    birth_date = fields.Date(string="Data de Naixement")
    gender = fields.Selection([('male', 'Mascle'), ('female', 'Femella')], string="Gènere", required=True)
    weight = fields.Float(string="Pes (kg)")
    height = fields.Float(string="Alçada (cm)")
    length = fields.Float(string="Longitud (m)")
    
    behaviour = fields.Selection([('dangerous', 'Perillós per a humans'), ('docile', 'Dòcil'), ('neutral', 'Neutral')], string="Comportament", required=True, default='neutral')

    # Origen i adquisició
    origin_continent = fields.Selection([
        ('africa', 'Àfrica'), ('asia', 'Àsia'), ('europe', 'Europa'),
        ('north_america', 'Amèrica del Nord'), ('south_america', 'Amèrica del Sud'),
        ('australia', 'Austràlia'), ('antarctica', 'Antàrtida')],
        string="Continent d´Origen")
    origin_country = fields.Many2one('res.country', string="País d´Origen")
    acquisition_type = fields.Selection([
        ('rescued', 'Rescatat'), ('zoo_born', 'Nascut al zoològic'),
        ('donated', 'Donat'), ('transferred', 'Transferit des d´una altra institució')],
        string="Tipus d´Adquisició")
    acquisition_date = fields.Date(string="Data d´Adquisició")

    # Imatges i notes
    image = fields.Binary(string="Imatge de l'Animal")
    notes = fields.Text(string="Notes")

    # Relacions amb altres models
    species_id = fields.Many2one('species.management', string="Espècie", required=True)
    zoo_id = fields.Many2one('zoo.management', string="Zoològic")
    tags_ids = fields.Many2many('tags.management', 'animal_tag_rel', 'animal_id', 'tag_id', string="Tags")
