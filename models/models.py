# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Zoo(models.Model):
    _name = 'zoo.management'
    _description = 'Gestió de Zoològics'

    name = fields.Char(string="Nom", required=True)
    city = fields.Char(string="Ciutat", required=True)
    country = fields.Char(string="País", required=True)
    size = fields.Integer(string="Grandària", help="Superfície del zoològic en metres quadrats")

    # Relació amb els animals (1 zoològic té molts animals)
    animals_ids = fields.One2many('animal.management', 'zoo_id', string="Animals")


class Animal(models.Model):
    _name = 'animal.management'
    _description = 'Gestió d’Animals'

    id_code = fields.Char(string="Identificador Únic", required=True, help="Codi únic per identificar l'animal")
    birth_date = fields.Date(string="Data de Naixement", help="Data de naixement de l'animal")
    origin_continent = fields.Selection(
        [('africa', 'Àfrica'), ('asia', 'Àsia'), ('europe', 'Europa'), 
         ('north_america', 'Amèrica del Nord'), ('south_america', 'Amèrica del Sud'), 
         ('australia', 'Austràlia'), ('antarctica', 'Antàrtida')],
        string="Continent d’Origen"
    )
    origin_country = fields.Char(string="País d’Origen")
    gender = fields.Selection(
        [('male', 'Mascle'), ('female', 'Femella')],
        string="Sexe", required=True
    )
    diet = fields.Selection(
        [('carnivore', 'Carnívor'),
         ('omnivore', 'Omnívor'),
         ('herbivore', 'Herbívor'),
         ('other', 'Altres')],
        string="Dieta", required=True, help="Tipus de dieta de l'animal"
    )
    # Relació amb l'espècie (1 animal pertany a 1 espècie)
    species_id = fields.Many2one('species.management', string="Espècie", required=True)
    # Relació amb el zoològic (1 animal pertany a 1 zoològic
    zoo_id = fields.Many2one('zoo.management', string="Zoològic")

class Species(models.Model):
    _name = 'species.management'
    _description = 'Gestió d’Espècies'

    scientific_name = fields.Char(string="Nom Científic", required=True)
    common_name = fields.Char(string="Nom Vulgar", required=True)
    family = fields.Char(string="Família", help="Família biològica de l'espècie")
    endangered_status = fields.Selection(
        [('not_endangered', 'No amenaçada'), ('vulnerable', 'Vulnerable'),
         ('endangered', 'En perill'), ('critically_endangered', 'En perill crític')],
        string="Perill d’Extinció", required=True
    )

    # Relació amb els animals (1 espècie té molts animals)
    animal_ids = fields.One2many('animal.management', 'species_id', string="Animals")
