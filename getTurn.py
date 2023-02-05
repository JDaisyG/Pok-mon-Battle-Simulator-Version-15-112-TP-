# Pokemon Battle Simulator: Version 112 (TP)
#################################################
# getTurn.py
# This file contains enemy AI
#
# Your name: JanetLou Guan
# Your andrew id: janetlog
#################################################
import battler_List
import moves

effectiveness = {
    "Normal": {0: {"Ghost"}, 0.5: {"Rock"}, 2: {}},
    "Fighting": {0: {"Ghost"}, 0.5: {"Psychic"}, 2: {"Dragon"}},
    "Fire": {0: {}, 0.5: {"Water", "Rock", "Fire"}, 2: {"Grass", "Ice", "Bug"}},
    "Flying": {0.5: {}, 2: {"Dragon"}},
    "Ground": {0: {"Flying"}, 0.5: {"Grass", "Bug"}, 2: {"Rock", "Fire", "Poison"}},
    "Psychic": {0: {}, 0.5: {"Psychic"}, 2: {"Fighting", "Poison"}},
    "Ice": {0: {}, 0.5: {"Ice", "Water"}, 2: {"Dragon", "Flying", "Grass"}},
    "Dragon": {0.5: {}, 2: {"Dragon"}},
    "Poison": {0: {}, 0.5: {}, 2: {"Grass"}},
    "Rock": {0: {}, 0.5: {"Ground"}, 2: {"Fire", "Bug", "Ice", "Flying"}},
    "Electric": {0: {"Ground"}, 0.5: {"Grass", "Electric"}, 2: {"Water", "Flying"}},
    "Water": {0: {}, 0.5: {"Grass", "Water"}, 2: {"Fire", "Rock", "Ground"}},
    "Grass": {0: {}, 0.5: {"Grass", "Fire", "Flying"}, 2: {"Water", "Rock", "Ground"}}
    }

class Opponent:
    
    def __init__(self, battlerList):
        self.battlerList = battlerList
        
        self.oppTeam = dict()
        self.oppSPD = 0
        
        # setup like: oppTeam = {"Abra": {"moves": [], "SPD": 0}, "Mew": ...}
        
    # keep track of the player's Pokémon and their moves
    
    def fillBattlerInfo(self, other):
        
        if (other not in self.oppTeam):
            self.oppTeam[other] = {"moves": []}
    
    def fillMoveInfo(self, other, move):
        
        if (move not in self.oppTeam[other]["moves"]):
            self.oppTeam[other]["moves"].append(move)
            
    def getMoveInfo(self, other):
        return self.oppTeam[other]["moves"]
    
    # check to see if you're weak against the opponent's types
    def checkAdvantage(self, you, other):
        
        notWeak = False
        t1, t2 = other.getType()
        
        for t in other.getType():
            if (t != None and (you.getType()[0] not in effectiveness[t][2] and you.getType()[1] not in effectiveness[t][2])):
                notWeak = True
        
        return notWeak
        
    # search for a Pokémon that resists the move the player prev used
    def findSwitch(self, you, other, team):
        
        switch = False
        t1, t2 = other.getType()
        for b in team:
            if (b.isAlive()):
                if (b.getName() != you.getName() and len(self.getMoveInfo(other)) != 0):
                
                    mt1, mt2 = b.getType()
                    
                    
                    for i in range(len(self.getMoveInfo(other))):
                        move = self.getMoveInfo(other)[i]
                        m = moves.Moves(move)
                        if (mt1 not in effectiveness[m.getType()][2] and mt2 not in effectiveness[m.getType()][2]):
                            switch = True
                        else:
                            break
                    
                    if (switch):
                        return b.getName()
        return False
    
    
    def findAttack(self, you, other, possibleMoves, team):
        count = 0
        # checks the opp typings
        for b in team:
            if (b.isAlive() and b.getName() != you.getName()):
                count += 1
        if (count > 0 and not self.checkAdvantage(you, other)):
                return self.findSwitch(you, other, team)
        
        else:
        
            # find and use the move that will do the most damage
            
            strongestMove = possibleMoves[0]
            
            
            for m in possibleMoves:
                if (you.getDmg(other, m) > you.getDmg(other, strongestMove)):
                    strongestMove = m
            
            return strongestMove
  