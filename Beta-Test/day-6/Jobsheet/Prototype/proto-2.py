from multipledispatch import dispatch

class Character:
    @dispatch(str, int, int)
    def __init__(self, name, HP, atk) -> None:
        self.name = name
        self.HP = HP
        self.atk = atk
    
    @dispatch(object)
    def __init__(self, source) -> None:
        assert isinstance(source, Character)
        self.name = source.name
        self.HP = source.HP
        self.atk = source.atk
    
    def clone(self, name:str = None, HP:int = None, atk:int = None):
        obj = Character(self)
        obj.name = self.name if name is None else name
        obj.HP = self.HP if HP is None else HP
        obj.atk = self.atk if atk is None else atk
        return obj

class Warrior(Character):
    @dispatch(str)
    def __init__(self, name:str) -> None:
        self.energy = 100
        super().__init__(name, 120, 15)
    
    @dispatch(object)
    def __init__(self, source) -> None:
        assert isinstance(source, Warrior)
        self.energy = source.energy
        super().__init__(source)
    
    def clone(self, name:str = None, HP:int = None, atk:int = None, energy:int = None):
        obj = Warrior(self)
        obj.name = self.name if name is None else name
        obj.HP = self.HP if HP is None else HP
        obj.atk = self.atk if atk is None else atk
        obj.energy = self.energy if energy is None else energy
        return obj

class Mage(Character):
    @dispatch(str)
    def __init__(self, name:str) -> None:
        self.mana = 100
        super().__init__(name, 80, 20)
    
    @dispatch(object)
    def __init__(self, source) -> None:
        assert isinstance(source, Mage)
        self.mana = source.mana
        super().__init__(source)
    
    def clone(self, name:str = None, HP:int = None, atk:int = None, mana:int = None):
        obj = Mage(self)
        obj.name = self.name if name is None else name
        obj.HP = self.HP if HP is None else HP
        obj.atk = self.atk if atk is None else atk
        obj.mana = self.mana if mana is None else mana
        return obj

if __name__ == "__main__":
    warrior_char = Warrior("Warrior Prototype")
    
    mage_char = Mage("Mage Prototype")
    
    warrior1 = warrior_char.clone("FlaB")
    
    warrior2 = warrior_char.clone("noklentt")
    
    mage1 = mage_char.clone("Gopar")
    
    mage2 = mage_char.clone("xyz")