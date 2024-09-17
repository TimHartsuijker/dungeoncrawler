class Monster:
    Name = None
    HP = None
    Damage = None
    
    def __init__(self, name, hp, damage):
        self.Name = name
        self.HP = hp
        self.Damage = damage

    
Monster1 = Monster("Demon dog", 3, 5)
Monster1Name = Monster1.Name

print(Monster1Name)