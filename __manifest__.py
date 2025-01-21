# -*- coding: utf-8 -*-
{
    'name': "Zoo Management",
    'license': 'LGPL-3',

    'summary': "Gestió de zoològics, animals i espècies",

    'description': """
Aquest mòdul permet la gestió de zoològics, incloent la informació dels animals i les espècies associades.
Permet als usuaris gestionar:
- Zoològics: ubicació, mida i dades generals.
- Animals: informació individual, origen i relacions amb zoològics.
- Espècies: noms científics, noms vulgars i estats de perill d'extinció.
    """,

    'author': "Francesc Albert Soler",
    'website': "",

    'category': 'Management',
    'version': '0.1',

    # Mòduls necessaris per al funcionament
    'depends': ['base'],

    # Fitxers carregats sempre
    'data': [
        'security/ir.model.access.csv',  # Permisos d'accés
        'data/groups.xml', # Grups d'usuaris
        'views/zoo_views.xml', # Vistes de zoològics
        ],


    'installable': True,
    'application': True,
    'auto_install': False,

    # Fitxers carregats només en mode demostració
    'demo': [],
}
