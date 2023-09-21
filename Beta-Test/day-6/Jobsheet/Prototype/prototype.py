class Character:
    def __init__(self, name, HP, atk) -> None:
        self.name = name
        self.HP = HP
        self.atk = atk
    
    def clone(self, name:str = None, HP:int = None, atk:int = None):
        return Character(self.name if name is None else name, self.HP if HP is None else HP, self.atk if atk is None else atk)

class Warrior(Character):
    def __init__(self, name:str) -> None:
        HP = 120
        atk = 15
        self.energy = 100
        super().__init__(name, HP, atk)
    
    def clone(self, name:str = None, HP:int = None, atk:int = None, energy:int = None):
        obj = Warrior(self.name if name is None else name)
        obj.HP = self.HP if HP is None else HP
        obj.atk = self.atk if atk is None else atk
        obj.energy = self.energy if energy is None else energy
        return obj

class Mage(Character):
    def __init__(self, name:str) -> None:
        HP = 80
        atk = 20
        self.mana = 100
        super().__init__(name, HP, atk)
    
    def clone(self, name:str = None, HP:int = None, atk:int = None, mana:int = None):
        obj = Mage(self.name if name is None else name)
        obj.HP = self.HP if HP is None else HP
        obj.atk = self.atk if atk is None else atk
        obj.mana = self.mana if mana is None else mana
        return obj

if __name__ == "__main__":
    warrior_char = Warrior("Warrior Prototype")
    mage_char = Mage("Mage Prototype")
    
    warrior1 = warrior_char.clone(name="FlaB")
    
    warrior2 = warrior_char.clone(name="noklentt")
    
    mage1 = mage_char.clone(name="Gopar")
    
    mage2 = mage_char.clone(name="xyz")