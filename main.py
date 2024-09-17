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

class Player:
    X = None
    Y = None
    HP = None
    Weapon = None
    Item = None
    Armour = None

    def __init__(Self, x, y, hp, weapon, item, armour):
        Self.X = x
        Self.Y = y
        Self.HP = hp
        Self.Weapon = weapon
        Self.Item = item
        Self.Armour = armour

# weapons (rarity, name, description, damage)
class Weapons:
    Rarity = None
    Name = None
    Description = None
    Damage = None

    def __init__(Self, rarity, name, description, damage):
        Self.Rarity = rarity
        Self.Name = name
        Self.Description = description
        Self.Damage = damage

# rooms (x, y, monsters, items)
class rooms:
    X = None
    Y = None
    Monsters = None
    Items = None

    def __init__(Self, x, y, monsters, items):
        Self.X = x
        Self.y = y
        Self.Monsters = monsters
        Self.Items = items
        
class Armour:
    Name = None
    Modifier = None

    def __init__(self, name, modifier):
        self.Name = name
        self.Modifier = modifier
Monster1 = Monster("Demon dog", 3, 5)
Monster1Name = Monster1.Name

Item1 = Item("Shadow blade", "Uncommon", "Using this ring you can summon the Shadow blade", "Summon sword", 5)
Item1Name = Item1.Name

Armour1 = Armour("Armour of Agathys", 7)
Armour1Name = Armour1.Name

print(Monster1Name, Item1Name, Armour1Name)    
