class Combat_Round:
    def __init__(self):
        self.combat_max_time = 300 # 5 minutes for DPS calculation. increase for boss fights
        self.rotation = []

    def list_rotation(self):
        print(self.rotation)

    def add_to_rotation(self, spell):
        self.rotation.append(spell)
        self.list_rotation()

    def remove_from_rotation(self, spell):
        index_to_remove = self.rotation.index(spell)
        del self.rotation[index_to_remove]
        self.list_rotation()
    
    def execute_rotation(self):
        for each_spell in self.rotation:
            pass


if __name__ == "__main__":
    pass