# Pokemon Battle Simulator: Version 112 (TP)
#################################################
# battler_List.py
# This file stores the Pokémon information
#
# Your name: JanetLou Guan
# Your andrew id: janetlog
#################################################
import random

import sprites
import moves

# dict from https://pkmn.github.io/randbats/data/gen1randombattle.json
# all stats taken from https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_I)
pokemon = {
  "Abra": {"level": 88, "moves": ["Fire Blast", "Psychic", "Blizzard", "Seismic Toss", "Psywave"], "stats": [256, 199, 138, 145, 192], "type": ["Psychic"]},
  "Aerodactyl": {"level": 74, "moves": ["Double-Edge", "Fire Blast", "Hyper Beam", "Earthquake", "Flamethrower"], "stats": [258, 199, 138, 145, 192], "type": ["Rock", "Flying"]},
  "Arcanine": {"level": 77, "moves": ["Body Slam", "Fire Blast", "Flamethrower", "Hyper Beam"], "stats": [220, 275, 160, 145, 192], "type": ["Fire"]},
  "Mew": {"level": 65, "moves": ["Blizzard", "Earthquake", "Psychic", "Hyper Beam", "Psywave", "Thunderbolt"], "stats": [360, 260, 260, 260, 260], "type": ["Psychic"]},
  "Lapras": {"level": 71, "moves": ["Blizzard", "Body Slam", "Surf", "Thunderbolt"], "stats": [245, 150, 245, 200, 174], "type": ["Water", "Ice"]},
  
  
  "Doduo": {"level": 88, "moves": ["Gust", "Body Slam", "Double-Edge", "Drill Peck"], "stats": [232, 212, 220, 156, 274], "type": ["Flying", "Normal"]},
  
  "Venusaur": {"level": 74, "moves": ["Body Slam", "Hyper Beam", "Razor Leaf", "Mega Drain"], "stats": [345, 170, 162, 236, 170], "type": ["Grass", "Poison"]},
  }

class battlerList:

    def __init__(self, name):    

        self.name = name
        self.alive = True
        
        # stats
        self.HP = pokemon[name]['stats'][0]
        self.TotalHP = pokemon[name]['stats'][0]
        self.ATK = pokemon[name]['stats'][1]
        self.DEF = pokemon[name]['stats'][2]
        self.SPC = pokemon[name]['stats'][3]
        self.SPD = pokemon[name]['stats'][4]
        
        # level
        self.LV = pokemon[name]['level']
        
        # types
        self.type1 = pokemon[name]['type'][0]
        self.type2 = None
        
        if (len(pokemon[name]['type']) == 2):
            self.type2 = pokemon[name]['type'][1]
          
        # generate a random move set from all possible moves
        # self.moves = pokemon[name]['moves']
        
        self.moves = []
        
        while (len(self.moves) < 4):
            index = random.randint(0, len(pokemon[name]['moves']) - 1)
            
            # shouldn't be any duplicate moves
            if (pokemon[name]['moves'][index] not in self.moves):
                self.moves.append(pokemon[name]['moves'][index])
                
    def __repr__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def getLevel(self):
        return self.LV
    
    def getType(self):
        return self.type1, self.type2
    
    def getMoves(self):
        return self.moves
    
    # stats ordered: HP, Attack, Defense, Special, Speed
    def getStats(self):
        return pokemon[self.name]['stats']
    
    def getSprite(self, index):
        s = sprites.Sprites(self.name)
        return s.getSpriteName(self.name, index)
    
    def getHP(self):
        return self.HP
    
    def getTotalHP(self):
        return self.TotalHP
    
    def getHPPercent(self):
        return int(self.HP / self.TotalHP * 100)
    
    def setHP(self, HP):
        self.HP = HP
    
    def isAlive(self):
        return self.alive
    
    # for moves such as Double-Edge
    def getRecoil(self, damage):
        
        recoil = damage // 4
        
        if (recoil > self.HP):
            recoil = self.HP
            self.alive = False
        
        self.HP -= recoil
    
    def getDmg(self, other, move):
        
        m = moves.Moves(move)
        
        type1, type2 = self.getType()
        otype1, otype2 = other.getType()
        level = self.LV
        
        if (m.getName() == "Seismic Toss" or m.getName() == "Night Shade"):
            
                damage = self.LV
            
        else: 
            if (m.getType() == otype1 or m.getType() == otype2):
                STAB = 1.5
            else: 
                STAB = 1  
            
            power = m.getPower()
            r = random.randint(217, 255) / 255
            
            # calculate effectiveness (strength)
            type1E = m.getStrength(otype1)
            type2E = m.getStrength(otype2)
            
            
            # default, or m.kind == PHYS
            A = self.ATK
            D = other.DEF
            
            if (m.getKind() == 'SPC'):
                A = self.SPC
                D = other.SPC
            
            # equation from https://bulbapedia.bulbagarden.net/wiki/Damage
            damage = int((((((2 * level) / 5) * power * (A / D) / 50) + 2)) * STAB * type1E * type2E * r)
            
        return damage
    
    def dealDmg(self, other, move):
        
        m = moves.Moves(move)
        
        type1, type2 = self.getType()
        otype1, otype2 = other.getType()
        level = self.LV
        
        
        if (m.getName() == "Seismic Toss" or m.getName() == "Night Shade"):
            
            if (other.HP < level):
                damage = other.HP
                other.HP -= level
            else:
                other.HP -= level
                damage = level
                
            if (other.HP <= 0):
                other.HP = 0
                other.alive = False
            return 
            
        else: 
            if (m.getType() == otype1 or m.getType() == otype2):
                STAB = 1.5
            else: 
                STAB = 1
                
            
            power = m.getPower()
            r = random.randint(217, 255) / 255
            
            # calculate effectiveness (strength)
            type1E = m.getStrength(otype1)
            type2E = m.getStrength(otype2)
            
            
            # default, or m.kind == PHYS
            A = self.ATK
            D = other.DEF
            
            if (m.getKind() == 'SPC'):
                A = self.SPC
                D = other.SPC
                
            # equation from https://bulbapedia.bulbagarden.net/wiki/Damage
            damage = int((((((2 * level) / 5) * power * (A / D) / 50) + 2)) * STAB * type1E * type2E * r)
            
            if (damage > other.HP):
                damage = other.HP
            
            other.HP -= damage
            
        if (other.HP <= 0):
            other.HP = 0
            other.alive = False
            
        
        if (m.getName() == "Double-Edge"):
            self.getRecoil(damage)
        

    def getTurn(self, other, move):
        self.getHit(other, move)
 

'''
electrode: 251, 153, 184, 199, 292

'''