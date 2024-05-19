class Character:
    def __init__(self):
        self.info = {'primary_stat':'',
                     'pve_power': 0,
                     'pvp_power': 0,
                     'item_level': 0,
                     'prestige_level': 0}
        self.attributes = {'strength': 0,
                           'agility': 0,
                           'intelligence': 0,
                           'spirit': 0,
                           'stamina': 0}
        self.melee = {'damage_min': 0,
                      'damage_max': 0,
                      'speed_main_hand': 0, # Number to the left of / is main hand.
                      'speed_off_hand': 0, # Number to the right of / is off-hand.
                      'power': 0,
                      'hit_rating_current': 0, # Number to the left of / is current rating.
                      'hit_rating_max': 0, # Number to the right of / is is maximum rating.
                      'off_hand_hit_rating_current': 0, # Number to the left of / is current rating.
                      'off_hand_hit_rating_max': 0, # Number to the right of / is is maximum rating.
                      'crit_chance': 0}
        self.ranged = {'damage_min': 0,
                       'damage_max': 0,
                       'speed': 0,
                       'power': 0,
                       'hit_rating_current': 0, # Number to the left of / is current rating.
                       'hit_rating_max': 0, # Number to the right of / is is maximum rating.
                       'crit_chance': 0}
        self.spell = {'bonus_damage': 0,
                      'bonus_healing': 0,
                      'hit_rating_current': 0, # Number to the left of / is current rating.
                      'hit_rating_max': 0, # Number to the right of / is is maximum rating.
                      'haste_rating': 0,
                      'crit_chance': 0,
                      'mana_regen': 0}
        self.defense = {'armor': 0,
                        'defense': 0,
                        'dodge': 0,
                        'parry': 0,
                        'block': 0,
                        'resilience': 0}
        self.resistances = {'arcane': 0,
                            'fire': 0,
                            'nature': 0,
                            'frost': 0,
                            'shadow': 0}
        self.spells = {}
        self.enchants = {}
        self.essence_legendary_max = 6
        self.essence_epic_max = 11
        self.essence_rare_max = 12
        self.essence_uncommon_max = 10
        self.essence_ability_max = 70
        self.essence_talent_max = 61
        self.enchant_max = 17
        self.enchant_legendary_max = 1
        self.enchant_epic_max = 3
        self.enchant_rare_max = 16
        self.enchant_uncommon_max = 16

    def add_talent(self, talent):
        pass

    def add_ability(self, ability):
        pass

    def add_enchant(self, enchant):
        pass


if __name__ == "__main__":
    pass