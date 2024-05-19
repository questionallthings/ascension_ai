from bs4 import BeautifulSoup as bs
import json
import re
import requests
import copy
import character
import combat

#Ascension Spells and Enchants Data
asc_api_url = 'https://api.ascension.gg/api/builder'
asc_spells_enchants_req = requests.get(asc_api_url)
asc_spells_enchants_json = asc_spells_enchants_req.json()

spell_list = {}
enchant_list = []
# 0 = Area-52
for each_spell in asc_spells_enchants_json[0]['spells']:
    for each_specialization in each_spell['specializations']:
        for each_talent in each_specialization['talents'][0:5]:
            for each_spell in each_talent['spells']:
                spell_data = each_spell
                talent_strip = copy.deepcopy(each_talent)
                del talent_strip['id']
                del talent_strip['spells']
                talent_strip['type'] = each_specialization['name']
                cat_spell_data = spell_data | talent_strip
                spell_name = cat_spell_data['name']
                del cat_spell_data['name']
                del cat_spell_data['image_url']
                del cat_spell_data['image_class']
                del cat_spell_data['row']
                del cat_spell_data['column']
                del cat_spell_data['mana_cost_percentage']
                del cat_spell_data['search_description']
                description = re.sub(r'<span.+?>', '', cat_spell_data['description'])
                description = re.sub(r'</span>', '', description)
                description = re.sub(r'<br>', '', description)
                description = re.sub(r'\n', ' ', description)
                cat_spell_data['description'] = description
                if spell_name not in spell_list:
                    spell_list[spell_name] = [cat_spell_data]
                else:
                    spell_list[spell_name].append(cat_spell_data)
        for each_ability in each_specialization['abilities']:
            description = re.sub(r'<span.+?>', '', each_ability['description'])
            description = re.sub(r'</span>', '', description)
            description = re.sub(r'<br>', '', description)
            description = re.sub(r'\n', ' ', description)
            ability_data = each_ability
            ability_data['type'] = each_specialization['name']
            ability_data['description'] = description
            ability_name = ability_data['name']
            del ability_data['name']
            del ability_data['image_url']
            del ability_data['image_class']
            del ability_data['search_description']
            spell_list[ability_name] = ability_data
for each_enchant in asc_spells_enchants_json[0]['random_enchant']:
    description = re.sub(r'<span.+?>', '', each_enchant['description'])
    description = re.sub(r'</span>', '', description)
    description = re.sub(r'<br>', '', description)
    description = re.sub(r'\n', ' ', description)
    each_enchant['description'] = description
    del each_enchant['search_description']
    del each_enchant['wflocation']
    del each_enchant['image_url']
    del each_enchant['image_class']
    enchant_list.append(each_enchant)
spell_sorted = {k: spell_list[k] for k in sorted(spell_list)}

search_term_1 = 'Tank Stance'
search_term_2 = ' '

for each_spell in spell_sorted:
    if type(spell_sorted[each_spell]) == list:
        for each in spell_sorted[each_spell]:
            if search_term_1 in each['description'] and search_term_2 in each['description']:
                print(f"{each_spell} :: {each['description']}")
    else:
        if search_term_1 in spell_sorted[each_spell]['description'] and search_term_2 in spell_sorted[each_spell]['description']:
            print(f"{each_spell} :: {spell_sorted[each_spell]['description']}")

#current_character = character.Character()


#current_character.add_enchant('World in Flames')


#for each_spell in current_character.spells:
#    print(current_character.spells[each_spell])
#for each_spell in current_character.enchants:
#    print(current_character.enchants[each_spell])
