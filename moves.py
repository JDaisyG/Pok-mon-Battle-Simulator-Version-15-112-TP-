# Pokemon Battle Simulator: Version 112 (TP)
#################################################
# moves.py
# This file contains the information for the moves
#
# Your name: JanetLou Guan
# Your andrew id: janetlog
#################################################


# list of pokemon moves
# data taken from https://bulbapedia.bulbagarden.net/wiki/List_of_moves
moves = {
    "Blizzard": {"power": 120, "type": "Ice", "kind": "SPC"},
    "Body Slam": {"power": 90, "type": "Normal", "kind": "PHYS"},
    "Double-Edge": {"power": 120, "type": "Normal", "kind": "PHYS"},
    "Earthquake": {"power": 100, "type": "Ground", "kind": "PHYS"},
    "Fire Blast": {"power": 120, "type": "Fire", "kind": "SPC"},
    "Hyper Beam": {"power": 150, "type": "Normal", "kind": "SPC"},
    "Psychic": {"power": 90, "type": "Psychic", "kind": "SPC"},
    "Razor Leaf": {"power": 65, "type": "Grass", "kind": "PHYS"},
    "Mega Drain": {"power": 65, "type": "Grass", "kind": "SPC"},
    "Seismic Toss": {"power": 1, "type": "Fighting", "kind": "PHYS"},
    "Psywave": {"power": 65, "type": "Psychic", "kind": "SPEC"},
    "Flamethrower": {"power": 95, "type": "Fire", "kind": "SPEC"},
    "Fire Blast": {"power": 110, "type": "Fire", "kind": "SPEC"},
    "Night Shade": {"power": 1, "type": "Ghost", "kind": "SPEC"},
    "Surf": {"power": 90, "type": "Water", "kind": "SPEC"},
    "Thunderbolt": {"power": 95, "type": "Electric", "kind": "SPEC"},
    }

class Moves:
    
    def __init__(self, name):
        
        self.name = name
        self.type = moves[name]["type"]
        self.kind = moves[name]["kind"]
    
    def __repr__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type
    
    def getKind(self):
        return self.kind
    
    def getPower(self):
        return moves[self.name]['power']
    
    # self against opponent's type
    def getStrength(self, typeOther):
        
        # {0: immunitiy, 0.5: resist, 2: strong against}
        effectiveness = {
            "Normal": {0: {"Ghost"}, 0.5: {"Rock"}, 2: {}},
            "Fighting": {0: {"Ghost"}, 0.5: {"Psychic"}, 2: {"Dragon"}},
            "Fire": {0: {}, 0.5: {"Water", "Rock", "Fire"}, 2: {"Grass", "Ice", "Bug"}},
            "Flying": {0.5: {}, 2: {"Dragon"}},
            "Ground": {0: {"Flying"}, 0.5: {"Grass", "Bug"}, 2: {"Rock", "Fire", "Poison"}},
            "Psychic": {0: {}, 0.5: {"Psychic"}, 2: {"Fighting", "Poison"}},
            "Ice": {0: {}, 0.5: {"Ice", "Water"}, 2: {"Dragon", "Flying"}},
            "Dragon": {0.5: {}, 2: {"Dragon"}},
            "Rock": {0: {}, 0.5: {"Ground"}, 2: {"Fire", "Bug", "Ice", "Flying"}},
            "Grass": {0: {}, 0.5: {"Fire", "Flying", "Bug"}, 2: {"Water", "Rock", "Ground"}},
            "Ghost": {0: {"Normal"}, 0.5: {}, 2: {"Psychic"}},
            "Electric": {0: {"Ground"}, 0.5: {"Grass", "Electric"}, 2: {"Water", "Flying"}},
            "Water": {0: {}, 0.5: {"Grass", "Water"}, 2: {"Fire", "Rock", "Ground"}}
            
            }
        
        if(typeOther == None):
            return 1
        elif (typeOther in effectiveness[self.type][0]):
            return 0
        elif (typeOther in effectiveness[self.type][0.5]):
            return 0.5
        elif (typeOther in effectiveness[self.type][2]):
            return 2
        else:
            return 1
    
