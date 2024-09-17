from random import randrange

# the items in each list are ordered as name, health, speed, damage
Monsters = [ 

    ['demon dog', 3, 10, 5], 
    ['soldier', 10, 5, 7], 
    ['zombie', 1, 1, 10],

]

# the items in each list are ordered as name, damagetype, damage, new weapon
weapons = [
    ['greatsword', 'slashing', 5],
    ['flamethrower', 'fire', 3],
]

# the items in each list are ordered as name, effect explanation, type, modifier
items = [
    ['hp pendant', 'increases base hp', 'hpBoost', 2],
    ['sharpening stone', 'boosts all slashing damage', 'slashingBoost', 2],
    ['dragons boost', 'boosts all fire damage', 'fireBoost', 10],
]

# the items in each list are ordered as name, health modifier
armour = [
    ['leather armour', 5],
]

# player data is ordered by x, y, health, weapon, item 1, item 2, armour
player = [
    [randrange(0, 10), randrange(0, 10), 50, weapons[0], items[0], items[1], armour[0]]
]

# all possible coordinates (gets filled in CreateMap())
Coordinates = [
    
]

# def CheckItems(newPlayer):
#     match newPlayer[0][3][2]:
#         case 'hpBoost':
#             newPlayer[0][2] += newPlayer[0][3][3]
#         case 'slashingBoost':
#             if newPlayer[0][3][1] == 'slashing':
#                 newPlayer[0][3][2] += newPlayer[0][3][3]
#         case 'fireBoost':
#             if newPlayer[0][3][1] == 'fire':
#                 newPlayer[0][3][2] += newPlayer[0][3][3]

def CreateMap():

    column = 0
    row = 0

    while column <= 10:
        while row <= 10:
            NewCoordinate = [column, row]
            Coordinates.append(NewCoordinate)
            row +=1
        column += 1
        row = 0
    
    for x in range(len(Coordinates)):
        print(Coordinates[x])


def Createplayer(x, y, health, weapon, item1, item2, armour):
    # create new player and keep track of the base stats, newPlayer gets modified with items and armour. baseStats remains untouched
    baseStats =[
        [x, y, health, weapon, item1, item2, armour]
    ]

    newPlayer = [
        [x, y, health, weapon, item1, item2, armour]
    ]

    print(newPlayer)


    # check the player's initial items to apply modifiers
    # CheckItems(newPlayer)
    # CheckItems(newPlayer)

    # check th player's initial armour to apply
    newPlayer[0][2] += newPlayer[0][6][1]
    print(newPlayer)
    return newPlayer

CreateMap()
Createplayer(randrange(0, 10), randrange(0, 10), 5, weapons[0], items[0], items[1], armour[0])