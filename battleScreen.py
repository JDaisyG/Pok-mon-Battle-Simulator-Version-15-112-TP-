# Pokemon Battle Simulator: Version 112 (TP)
#################################################
# battleScreen.py
# This file displays the graphics and actions
#
# Your name: JanetLou Guan
# Your andrew id: janetlog
#################################################

from cmu_112_graphics import*
import math
import random

import battler_List
import sprites
import getTurn
import teamPicker

def appStarted(app):
    
    # game
    app.turn = 0
    app.gameOver = False
    app.playerWin = False
    app.oppWin = False
    
    app.canMove = False
    
    app.turnSwitch = False
    
    app.bHPcolor = 'green'
    app.oHPcolor = 'green'
    
    app.showText = True
    app.isTurn = False
    app.oppTurn = False
    app.oSwitch = False
    
    
    app.cx = 0
    app.cy = 0
    
    # generates 3 random (distinct) pokemon for each team
    
    app.t = teamPicker.teamPick()
    app.ot = teamPicker.teamPick()
    
    app.playerMons = app.t.choose()
    app.oppMons = app.ot.choose()
    
    
    # player team
    app.battler1 = battler_List.battlerList(app.playerMons[0])
    app.battler2 = battler_List.battlerList(app.playerMons[1])
    app.battler3 = battler_List.battlerList(app.playerMons[2])
    
    app.playerTeam = [app.battler1, app.battler2, app.battler3]
    
    # opponent team
    app.opp1 = battler_List.battlerList(app.oppMons[0])
    app.opp2 = battler_List.battlerList(app.oppMons[1])
    app.opp3 = battler_List.battlerList(app.oppMons[2])
    
    app.oppTeam = [app.opp1, app.opp2, app.opp3]
    app.oTeam = getTurn.Opponent(app.oppTeam)
    
    #app.opp = getTurn.Opponent(app.oppTeam)
    
    app.currentBattler = app.battler1
    app.currentOpp = app.opp1
    app.oppSMon = app.currentOpp
    
    # choose random moves for now
    app.yourMove = ''
    app.oppMove = ''
    
    app.show = True
    app.select = ''
    app.switch = False
    
    app.battlerSprite = app.loadImage(app.currentBattler.getSprite(1))
    app.battlerSprite = app.scaleImage(app.battlerSprite, 2.5)
    
    app.oppSprite = app.loadImage(app.currentOpp.getSprite(0))
    app.oppSprite = app.scaleImage(app.oppSprite, 2.5)
    
    app.battleBackground = app.loadImage('battleBackground.png')
    app.battleBackground = app.scaleImage(app.battleBackground, 2/3)
    
    app.battlerIcons = app.loadImage('battlerIcons.png')
    app.battlerIcons = app.scaleImage(app.battlerIcons, 2/3)
    
    app.HPBar = app.loadImage('HPBar.png')
    app.HPBar = app.scaleImage(app.HPBar, 2/3)
    
    app.HPBar2 = app.scaleImage(app.HPBar, 2/3)
    
    app.textBox = app.loadImage('textBox.png')
    app.textBox = app.scaleImage(app.textBox, 2/3)

    app.text = "Battle START!"
    app.t = ''

    
    doStep(app)

def doStep(app):
    
    # keep track of the turns
    app.turn += 1
    
    checkGameOver(app)
    if (app.gameOver):
        app.showText = True


def timerFired(app):
    
    setHPColor(app)
    
    if (not app.showText and app.isTurn):
        yourTurn(app)
        checkGameOver(app)
        app.isTurn = False
        app.oppTurn = True
        
    if (not app.showText and app.oppTurn):
        oppTurn(app)
        
        if (app.oSwitch):
            app.showText = True
            time.sleep(3)
            oppSwitch(app, app.oppSMon)
        checkGameOver(app)
        #app.showText = True
        
        app.oppTurn = False

def mousePressed(app, event):
    
    
    app.cx = event.x
    app.cy = event.y
    
    if (not app.gameOver and app.currentBattler.isAlive() and not app.showText):  
        
        #canvas.create_rectangle(10 + i * 143, 410, (i + 1) * 143, 460, fill = 'white')
        
        if (10 < app.cx < 143 and 410 < app.cy < 460):
            app.yourMove = app.currentBattler.getMoves()[0]
            app.showText = True
            app.text = f"{app.currentBattler} used {app.yourMove}!"
            
            
        elif (153 < app.cx < 286 and 410 < app.cy < 460):
            app.yourMove = app.currentBattler.getMoves()[1]
            app.showText = True
            app.text = f"{app.currentBattler} used {app.yourMove}!"
           
        elif (296 < app.cx < 429 and 410 < app.cy < 460):
            app.yourMove = app.currentBattler.getMoves()[2]
            app.showText = True
            app.text = f"{app.currentBattler} used {app.yourMove}!"
            
        elif (439 < app.cx < 572 and 410 < app.cy < 460):
            app.yourMove = app.currentBattler.getMoves()[3]
            app.showText = True
            app.text = f"{app.currentBattler} used {app.yourMove}!"
            
        else:
            return
            
 
        app.showText = True
        app.isTurn = True
        
        
            
        doStep(app)
        
def yourTurn(app):
    
    if (not app.gameOver):
        app.currentBattler.dealDmg(app.currentOpp, (app.yourMove))
        app.oTeam.fillBattlerInfo(app.currentBattler)
        app.oTeam.fillMoveInfo(app.currentBattler, app.yourMove)
        
        
        checkGameOver(app)
        

def oppTurn(app):
    if (not app.gameOver):
                
        app.oppMove = app.oTeam.findAttack(app.currentOpp, app.currentBattler, app.currentOpp.getMoves(), app.oppTeam)
      
        if (app.oppMove in app.oppMons):
            for m in app.oppTeam:
                if (m.getName() == app.oppMove):
                    app.oSwitch = True
                    app.oppSMon = m
                    
                    app.showText = True
                    app.text = f"Come back {app.currentOpp}!"
                
                    
                    
        else:
            
            app.currentOpp.dealDmg(app.currentBattler, (app.oppMove))
            app.showText = True
            app.text = f"Foe {app.currentOpp} used {app.oppMove}!"
        
        checkGameOver(app)        

def keyPressed(app, event):
    
    if (event.key == 'Enter'):
        app.showText = False
     
    if (not app.gameOver):
        
        if (not app.currentBattler.isAlive()):
            app.turnSwitch = True
        
        if (event.key == '1'):
            if (not app.battler1.isAlive()):
                app.text = f'{app.battler1} has no energy left!'
                app.showText = True
                
            elif (app.currentBattler != app.battler1):
                switch(app, app.battler1)
                
            else:
                app.text = f'{app.currentBattler} is already in battle!'
                app.showText = True
                
        if (event.key == '2'):
            if (not app.battler2.isAlive()):
                app.text = f'{app.battler2} has no energy left!'
                app.showText = True
            elif (app.currentBattler != app.battler2):
                switch(app, app.battler2)
            else:
                app.text = f'{app.currentBattler} is already in battle!'
                app.showText = True
                
        if (event.key == '3'):
            if (not app.battler3.isAlive()):
                app.text = f'{app.battler3} has no energy left!'
                app.showText = True
            elif (app.currentBattler != app.battler3):
                switch(app, app.battler3)
            else:
                app.text = f'{app.currentBattler} is already in battle!'
                app.showText = True
                
# switch your own pokemon out                
def switch(app, battler):
    
    app.currentBattler = battler
    
    app.showText = True
    app.text = f"Go {app.currentBattler.getName()}!"
    app.text = f"Come back {app.currentOpp.getName()}!"
    print(1)
    
    app.battlerSprite = app.loadImage(app.currentBattler.getSprite(1))
    app.battlerSprite = app.scaleImage(app.battlerSprite, 2.5)
    
    if (not app.turnSwitch):
        #oppTurn(app)
        checkGameOver(app)
    else:
        app.turnSwitch = False
    
    doStep(app)
    
def oppSwitch(app, battler):
    
    
    #if (not app.showText):
    
    app.currentOpp = battler
    
    app.showText = True
    
    if (app.oppMove in app.currentOpp.getMoves()):
        app.text = f"Foe {app.currentOpp.getName()} used {app.oppMove}!"
    
    else:
        app.text = f"Go {app.currentOpp.getName()}!"
    
    app.oppSprite = app.loadImage(app.currentOpp.getSprite(0))
    app.oppSprite = app.scaleImage(app.oppSprite, 2.5)
    
    
    doStep(app)
   
def checkGameOver(app):
    
    if (not app.currentBattler.isAlive()):
        
        
        app.text = f'{app.currentBattler.getName()} fainted!\n'
        app.showText = True
        
        for mon in app.playerTeam:
            
            if (mon.isAlive()):
                return
        app.oppWin = True 
        app.gameOver = True
    
    elif (not app.currentOpp.isAlive()):
        
        for mon in app.oppTeam:
            
            if (mon.isAlive()):
                app.currentOpp = mon
                
                
                app.oppSprite = app.loadImage(app.currentOpp.getSprite(0))
                app.oppSprite = app.scaleImage(app.oppSprite, 2.5)
                
                return
        app.playerWin = True
        app.gameOver = True
             

#def HPBars(app, canvas):
def HPBounds(app):
    battlerHP = app.currentBattler.getHPPercent()
    oppHP = app.currentOpp.getHPPercent()
    
    # length of HP bar = 162
    return (90, 215, 90 + battlerHP * 1.62, 220), (376, 86, 376 + oppHP * 1.08, 89)

def setHPColor(app):
    
    # battler HP
    if (app.currentBattler.getHPPercent() > 50):
        app.bHPcolor = 'green'
    
    if (25 < app.currentBattler.getHPPercent() < 50):
        app.bHPcolor = 'yellow'
        
    if (app.currentBattler.getHPPercent() < 25):
        app.bHPcolor = 'red'
     
        # opponent HP
    if (app.currentOpp.getHPPercent() > 50):
        app.oHPcolor = 'green'
        
    if (25 < app.currentOpp.getHPPercent() < 50):
        app.oHPcolor = 'yellow'
        
    if (app.currentOpp.getHPPercent() < 25):
        app.oHPcolor = 'red'

def backSprites(app, canvas):
    if(app.currentBattler.getHP() != 0):
        canvas.create_image(150, 305, image = ImageTk.PhotoImage(app.battlerSprite))
    

def oppSprites(app, canvas):
    if(app.currentOpp.getHP() != 0):
        canvas.create_image(435, 165, image = ImageTk.PhotoImage(app.oppSprite))
    
# battle background from pokemonshowdown.com
# text boxes drawn by me
def background(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = '#B0B1B3')
    canvas.create_image(290, 240, image = ImageTk.PhotoImage(app.battleBackground))
    canvas.create_text(65, 32, text = f'Turn {app.turn}', font = ('04b03','20'))

    canvas.create_image(285, 315, image = ImageTk.PhotoImage(app.battlerIcons))
    
    for i in range(len(app.playerMons)):
        canvas.create_text(20 + (140 * i ) + 50 * i, 500, text = f'{i + 1}: {app.playerMons[i]}', font = ('04b03','15'), anchor = 'nw')

    # width = 162, 108
    # height = 5, 3
    canvas.create_rectangle(HPBounds(app)[0], fill = app.bHPcolor, outline = app.bHPcolor)    
    canvas.create_rectangle(HPBounds(app)[1], fill = app.oHPcolor, outline = app.oHPcolor) 
    

    canvas.create_text(50, 175, text = f'{app.currentBattler.getName()}: Lv. {app.currentBattler.getLevel()}', font = ('04b03','25'), anchor = 'nw')
    canvas.create_image(290, 260, image = ImageTk.PhotoImage(app.HPBar))
    
    canvas.create_text(350, 65, text = f'{app.currentOpp.getName()}: Lv. {app.currentOpp.getLevel()}', font = ('04b03','15'), anchor = 'nw')
    canvas.create_image(510, 115, image = ImageTk.PhotoImage(app.HPBar2))
    

    for i in range(4):
        canvas.create_text(20 + i * 143, 425, text = app.currentBattler.getMoves()[i], font = ('04b03','12'), anchor = 'nw')

# create textbox
def textBox(app, canvas):
    canvas.create_rectangle(0, 400, app.width, app.height, fill = '#B0B1B3', outline = '#B0B1B3')
    canvas.create_image(290, 290, image = ImageTk.PhotoImage(app.textBox))
       
    canvas.create_text(50, 455, text = app.text, font = ('04b03','20'), anchor = 'nw')

# draw game over textbox
def drawGameOver(app, canvas):
    if (app.gameOver):
        canvas.create_rectangle(0, 400, app.width, app.height, fill = '#B0B1B3', outline = '#B0B1B3')
        canvas.create_image(290, 290, image = ImageTk.PhotoImage(app.textBox))
           
        if (app.playerWin):
            canvas.create_text(50, 455, text = "Battle OVER: You WIN!", font = ('04b03','20'), anchor = 'nw')
        elif (app.oppWin):
            canvas.create_text(50, 455, text = "Battle OVER: You LOSE...", font = ('04b03','20'), anchor = 'nw')

def redrawAll(app, canvas):
    background(app, canvas)
    
    if (app.showText):
        textBox(app, canvas)
    
    oppSprites(app, canvas)
    backSprites(app, canvas)
    drawGameOver(app, canvas)

def main():
    runApp(width=580, height=550, title = 'Pokémon Battle Simulator: Version 112')

    
if __name__ == '__main__':
    main()
    