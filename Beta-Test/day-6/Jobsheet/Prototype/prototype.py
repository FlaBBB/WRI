class character:
    def __init__(self, name, HP, atk) -> None:
        self.name = name
        self.HP = HP
        self.atk = atk
    
    def clone(self):
        return character(self.name, self.HP, self.atk)

class warrior(character):
    def __init__(self, name:str) -> None:
        HP = 120
        atk = 15
        self.energy = 100
        super().__init__(name, HP, atk)
    
    def clone(self):
        obj = warrior(self.name)
        obj.HP = self.HP
        obj.atk = self.atk
        obj.energy = self.energy
        return obj

class mage(character):
    def __init__(self, name:str) -> None:
        HP = 80
        atk = 20
        self.mana = 100
        super().__init__(name, HP, atk)
    
    def clone(self):
        obj = mage(self.name)
        obj.HP = self.HP
        obj.atk = self.atk
        obj.mana = self.mana
        return obj

if __name__ == "__main__":
    warrior_char = warrior("Warrior Prototype")
    mage_char = mage("Mage Prototype")
    
    warrior1 = warrior_char.clone()
    warrior1.name = "FlaB"
    
    warrior2 = warrior_char.clone()
    warrior2.name = "noklentt"
    
    mage1 = mage_char.clone()
    mage1.name = "Gopar"
    
    mage2 = mage_char.clone()
    mage2.name = "xyz"