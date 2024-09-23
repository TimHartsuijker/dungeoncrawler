class Monster:
    Name = None
    HP = None
    Damage = None
    
    def __init__(self, name, hp, damage):
        self.Name = name
        self.HP = hp
        self.Damage = damage

# Item effects that are currently implemented:

# item effects that have been tested:

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

class Weapon:
    Rarity = None
    Name = None
    Description = None
    Damage = None

    def __init__(Self, rarity, name, description, damage):
        Self.Rarity = rarity
        Self.Name = name
        Self.Description = description
        Self.Damage = damage

class Room:
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

class Player:
    Room = None 
    HP = None
    Weapon = None
    Item = None
    Armour = None

    def __init__(Self, room, hp, weapon, item, armour):
        Self.Room = room
        Self.HP = hp
        Self.Weapon = weapon
        Self.Item = item
        Self.Armour = armour

Monster1 = Monster("Demon dog", 3, 5)
Monster1Name = Monster1.Name

Item1 = Item("Shadow blade", "Uncommon", "Using this ring you can summon the Shadow blade", "SummonSword", 5)
Item1Name = Item1.Name

Armour1 = Armour("Armour of Agathys", 7)
Armour1Name = Armour1.Name

Weapon1 = Weapon("common", "greatsword", "sword does bonk", 5)
Weapon1Name = Weapon1.Name

Room1 = Room(0, 0, Monster1, Item1)
Room1X = Room1.X

Player1 = Player(Room1, 10, Weapon1, Item1, Armour1)
Player1Room = Player1.Room.X
Player1HP = Player1.HP
Player1Weapon = Player1.Weapon.Name
Player1Item = Player1.Item.Name
Player1Armour = Player1.Armour.Name
print(Player1Room, Player1HP, Player1Weapon, Player1Item, Player1Armour)