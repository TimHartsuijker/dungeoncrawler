class Monster:
    Name = None
    HP = None
    Damage = None
    
    def __init__(self, name, hp, damage):
        self.Name = name
        self.HP = hp
        self.Damage = damage


class Item:
    Name = None
    Rarity = None
    Description = None
    Effect = None
    Modifier = None

    def __init__(self, name, rarity, description, effect, modifier):
        self.Name = name
        self.Rarity = rarity
        self.Description = description
        self.Effect = effect
        self.Modifier = modifier

Monster1 = Monster("Demon dog", 3, 5)
Monster1Name = Monster1.Name

Item1 = Item("Shadow blade", "Uncommon", "Using this ring you can summon the Shadow blade", "Summon sword", 5)
Item1Name = Item1.Name
print(Monster1Name, Item1Name)    