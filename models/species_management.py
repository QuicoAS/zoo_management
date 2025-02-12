from odoo import models, fields, api

class Species(models.Model):
    _name = 'species.management'
    _description = 'Gestió d´Espècies'
    _order = 'common_name asc'

    # Camps generals
    scientific_name = fields.Char(string="Nom Científic", required=True)
    common_name = fields.Char(string="Nom Vulgar", required=True)
    name = fields.Char(string="Nom Complet", compute='_compute_name', store=True)

    # Estat de conservació
    iucn_endangered_status = fields.Selection(
        selection=[
            ('lc', 'Least Concern'),
            ('nt', 'Near Threatened'),
            ('vu', 'Vulnerable'),
            ('en', 'Endangered'),
            ('cr', 'Critically Endangered'),
            ('ew', 'Extinct in the Wild'),
            ('ex', 'Extinct')
        ],
        string="Estat de Conservació (UICN)",
        required=True,
    )

    # Imatges i notes
    image = fields.Binary(string="Imatge")
    notes = fields.Text(string="Notes")

    # Característiques biològiques
    avg_lifespan = fields.Integer(string="Vida Promig (anys)")
    avg_weight = fields.Float(string="Pes Promig (kg)")
    diet_type = fields.Selection(
        [
            ('carnivore', 'Carnívor'),
            ('herbivore', 'Herbívor'),
            ('omnivore', 'Omnívor'),
            ('insectivore', 'Insectívor')
        ],
        string="Tipus de Dieta"
    )

    # Activitat
    activity = fields.Selection([
        ('diurnal', 'Diürn'),
        ('nocturnal', 'Nocturn'),
        ('crepuscular', 'Crepuscular')
    ], string="Activitat", required=True, default='diurnal', help="Tipus d'activitat principal")
    
    # Relacions amb altres models
    animals_ids = fields.One2many(
        'animal.management', 'species_id', string="Animals"
    )
    zoo_id = fields.Many2one('zoo.management', string="Zoològic")
    tags_ids = fields.Many2many(
        'tags.management', string="Tags"
    )

    # Mètode per calcular el camp name
    @api.depends('common_name', 'scientific_name')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.common_name} ({record.scientific_name})" if record.scientific_name else record.common_name
