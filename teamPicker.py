# Pokemon Battle Simulator: Version 112 (TP)
#################################################
# teamPicker.py
# This file chooses the teams
#
# Your name: JanetLou Guan
# Your andrew id: janetlog
#################################################
import random


# list pokemon in alphabetical order 0 to n
pokemonNUM = {
  0: {"mon": "Abra"},
  1: {"mon": "Aerodactyl"},
  2: {"mon": "Venusaur"},
  3: {"mon": "Lapras"},
  4: {"mon": "Arcanine"},
  5: {"mon": "Mew"},
  
  }

class teamPick:
    
    def __init__(self):
        self.team = []
     
    # 3 mon teams
    def choose(self):
        
        while (len(self.team) < 3):
            index = random.randint(0, 5)
            
            # shouldn't be any duplicates on the same team
            # but there can be up to two duplicates on opposing teams
            if (pokemonNUM[index]["mon"] not in self.team):
                self.team.append(pokemonNUM[index]["mon"])
                
        for num in self.team:
            print()
        return self.team
    