class Monster:
    Name = None
    HP = None
    Damage = None
    
    def __init__(self, name, hp, damage):
        self.Name = name
        self.HP = hp
        self.Damage = damage

    
Monser1 = Monster("Demon dog", 3, 5)

print(Monser1.Name)