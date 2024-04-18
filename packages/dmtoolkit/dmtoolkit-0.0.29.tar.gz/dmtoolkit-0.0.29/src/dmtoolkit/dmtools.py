from apis.dndbeyondapi import DnDBeyondAPI
from apis.open5e.open5emonster import Open5eMonster
from apis.open5e.open5eitem import Open5eItem
from apis.open5e.open5espell import Open5eSpell


def get_dndbeyond_character(dnd_id):
    return DnDBeyondAPI.getcharacter(dnd_id)


def search_dnd5e_monster(name):
    return Open5eMonster.search(name)


def search_dnd5e_item(name):
    return Open5eItem.search(name)


def search_dnd5e_spell(name):
    return Open5eSpell.search(name)
