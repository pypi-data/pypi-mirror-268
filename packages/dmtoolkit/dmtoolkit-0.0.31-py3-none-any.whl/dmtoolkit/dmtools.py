from dmtoolkit.apis.dndbeyondapi import DnDBeyondAPI
from dmtoolkit.apis.open5e.open5eitem import Open5eItem
from dmtoolkit.apis.open5e.open5emonster import Open5eMonster
from dmtoolkit.apis.open5e.open5espell import Open5eSpell


def get_dndbeyond_character(dnd_id):
    return DnDBeyondAPI.getcharacter(dnd_id)


def get_monster(obj_id):
    return Open5eMonster.get(index=obj_id)


def get_item(obj_id):
    return Open5eItem.get(index=obj_id)


def get_spell(obj_id):
    return Open5eSpell.get(index="animate-objects")


def search_monster(name):
    return Open5eMonster.search(name)


def search_item(name):
    return Open5eItem.search(name)


def search_spell(name):
    return Open5eSpell.search(name)
