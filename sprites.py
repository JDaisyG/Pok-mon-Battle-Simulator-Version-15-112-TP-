# Pokemon Battle Simulator: Version 112 (TP)
#################################################
# sprites.py
# This file stores the sprites
#
# Your name: JanetLou Guan
# Your andrew id: janetlog
#################################################

import battler_List

# front sprites from https://archives.bulbagarden.net/wiki/Category:Red_and_Blue_sprites
# back sprites from https://archives.bulbagarden.net/wiki/Category:Generation_I_back_sprites
sprites = {
  "Abra": ["AbraF.png", "AbraB.png"],
  "Aerodactyl": ["AerodactylF.png", "AerodactylB.png"],
  "Arcanine": ["ArcanineF.png", "ArcanineB.png"],
  "Lapras": ["LaprasF.png", "LaprasB.png"],
  "Mew": ["MewF.png", "MewB.png"],
  "Venusaur": ["VenusaurF.png", "VenusaurB.png"],
  }

class Sprites:

    def __init__(self, name):   
        self.name = name
        
    # 0 for front, 1 for back
    def getSpriteName(self, name, index):
        return sprites[name][index]