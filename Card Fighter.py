#this code is designed to be used in python 3.2 with the pygame addon.
import pygame, time, sys, ctypes, os
from pygame.locals import *
import random

#set size of window
WINDOWWIDTH = 800
WINDOWHEIGHT = 800

#set colours
#             R    G    B
BLACK     = (  0,   0,   0)
DARKPINK  = (255,  20, 147)
GREEN     = (  0, 255,   0)
WHITE     = (255, 255, 255)
DARKGREEN = (  0, 155,   0)
GREY      = (211, 211, 211)
BGCOLOR = WHITE

#set up display
pygame.display.init()
global wn, BASICFONT
pygame.init()
wn = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #set the width of the window
BASICFONT = pygame.font.SysFont('ActionIsShaded', 24) #set font to be used
pygame.display.set_caption('Card Fighter')
screen=pygame.display.set_mode((0,0))

def terminate():
    #code which closes the windows after the game is over
    #time.sleep(2)
    pygame.quit()
    sys.exit()

def drawGrid():
    global vertline
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines inbetween cells.
        pygame.draw.line(wn, WHITE, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines inbetween cells.
        vertline = pygame.draw.line(wn, WHITE, (0, y), (WINDOWWIDTH, y))
    pygame.display.update()

#draws grid after key press
wn.fill(BGCOLOR)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#funtion to display text/buttons
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour) #extact purpose unkown but seems to be needed
    return textSurface, textSurface.get_rect()

def message_display(text, x, y, font_size, colour):
    largeText = pygame.font.Font('freesansbold.ttf',font_size) #load font
    TextSurf, TextRect = text_objects(text, largeText, colour) #render text
    TextRect.center = ((x),(y)) #place text
    #screen=pygame.display.set_mode((0,0)) uncomenting this lets fixes the screen not defined bug - but also causes problems displaying text if let uncommented.
    screen.blit(TextSurf, TextRect) #send to screen, needs to be updated/fliped to be worked

#function for buttoms
#example syntax to call button("return",150,450,100,50,DARKGREEN,GREEN,BLACK,action) note the lack of brackets on action function.
def txt_button(msg,x,y,w,h,inactive_colour,active_colour,text_colour,name_of_function_to_call_when_clicked):
    #need pygame.flip/update outside of function
    click = pygame.mouse.get_pressed() #get mouse state (clicked/not clicked)
    mouse = pygame.mouse.get_pos() #get mouse coords
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #check if mouse is on button
        pygame.draw.rect(screen, active_colour,(x,y,w,h)) #change to active colour
        if click[0] == 1: #check click (above if checks mouse is on button)
            name_of_function_to_call_when_clicked() #do this when clicked (veriable needs not to have brackets)
    else:
        pygame.draw.rect(screen, inactive_colour,(x,y,w,h)) #mouse not on button, switch to inactive colour

    smallText = pygame.font.SysFont("freesansbold.ttf", 30) #load font
    textSurf, textRect = text_objects(msg, smallText,text_colour) #place text in button through text funtion
    textRect.center = ( (x+(w/2)), (y+(h/2)) ) #location of text
    screen.blit(textSurf, textRect) #send to screen (but not update)

def img_button(x,y,w,h,name_of_function_to_call_when_clicked,filename):
    #need pygame.flip/update outside of function
    click = pygame.mouse.get_pressed() #get mouse state (clicked/not clicked)
    mouse = pygame.mouse.get_pos() #get mouse coords
    image = pygame.image.load(os.path.join("cards",filename))
    screen.blit(image, (x,y)) #the location of the image
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #check if mouse is on button
        print("on card "+str(filename))
        if click[0] == 1: #check click (above if checks mouse is on button)
            name_of_function_to_call_when_clicked() #do this when clicked (veriable needs not to have brackets)

def menu():
    global menu
    menu=1 #loop reacuent
    while menu==1:
        for event in pygame.event.get():
            txt_button("Single player",150,50,200,50,GREEN,DARKGREEN,BLACK,single) #make singplayer button
            txt_button("Muilti player",450,50,200,50,GREEN,DARKGREEN,BLACK,muilti) #make muiltiplayer button
            txt_button("Close",300,150,200,50,GREEN,DARKGREEN,BLACK,terminate) #make close button
            pygame.display.flip() #update pygame
        time.sleep(0.1)

def single(): #single player function
    global menu
    menu=0
    turn_1()

def ignore():
    pass

def keyboard():
    txt_button('A',213.5,200,30,30,GREY,GREEN,BLACK,ignore)
    txt_button('B',244.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('C',275.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('D',306.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('E',337.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('F',368.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('G',399.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('H',430.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('I',461.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('J',492.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('K',523.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('L',554.5,200,30,30,GREY,GREY,BLACK,ignore)
    txt_button('M',585.5,200,30,30,GREY,GREY,BLACK,ignore)

    txt_button('N',213.5,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('O',440,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('P',470,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('Q',500,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('R',530,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('S',560,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('T',590,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('U',620,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('V',650,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('W',680,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('X',710,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('Y',740,230,30,30,WHITE,GREY,BLACK,ignore)
    txt_button('Z',770,230,30,30,WHITE,GREY,BLACK,ignore)
    pygame.display.flip()

def muilti(): #muiltiplayer function
    global menu, wn
    menu = 0 #stops the menu screen
    wn.fill(BGCOLOR)
    pygame.display.flip()
    global first
    first = True #first turn is true

    def set_cards(): #set up the cards function
        global cards, card_list
        cards = {}
#   cards['Name of card'] = name, health modifer, amour modifer, weapon modifer, duribility, card type
#   card types
#   0:  Heal
#   1:  Weapon
#   2:  Amour
#   3:  card type
        cards['0001'] = ['Iron Kettle',0,0,2,10,2]
        cards['0002'] = ['Sting',-1,0,1,10,1]
        cards['0003'] = ['Lambas Bread',5,0,0,1,0]

        card_list = [] #list of all card names
        for card_name in cards:
            card_list.append(card_name) #add card names to list

    def set_enemy(): #set up enemy player
        global ehealth, eamour, eweapons, ename, edeck, ehand, eamourm, eweaponsm, edurability
        ehealth = 20 #there health
        eamour = 5 #there amour
        eamourm = 0 #there amour mod
        eweapons = 1 #there weapons
        eweaponsm = 0 #there weapons mod
        edurability = 0 #there durability
        ename = str(input("What is the name of your champion player2: ")) #there name
        edeck = []
        for i in range(20): #20 card deck
            card = random.choice(card_list) #get random card from cardlist
            edeck.append(cards[card]) #add that card to there deck
        ehand = []
        for i in range(5): #5 card hand
            card = random.choice(edeck) #get random card from deck
            edeck.remove(card) #remove this card from deck
            ehand.append(card) #add this card to hand


    def set_player():
        global health, amour, weapons, name, deck, hand, weaponsm, amourm, durability
        health = 20 #there health
        amour = 5 #there amour
        amourm = 0 #there amour mod
        weapons = 1 #there weapons
        weaponsm = 0 #there weaponsm
        durability = 0 #there durability

        keyboard()

        #txt_button('A',50,200,40,40,GREY,GREEN,BLACK,ignore)
        #pygame.display.flip()


        name = str(input("What is the name of your champion player1: ")) #there name

        text = 'Health: ' + str(health)
        message_display(text,50,25,15,BLACK)
        text = 'Armour: ' + str(amour+amourm)
        message_display(text,50,40,15,BLACK)
        text = 'Weapons: ' + str(weapons+weaponsm)
        message_display(text,50,55,15,BLACK)
        pygame.display.flip()

        deck = []
        for i in range(20): #20 card deck
            card = random.choice(card_list) #get random card from cardlist
            deck.append(cards[card]) #add that card to there deck
        hand = []
        for i in range(5): #5 card hand
            card = random.choice(deck) #get random card from deck
            deck.remove(card) #remove this card from deck
            hand.append(card) #add this card to hand

    def turn():
        global health, amour, weapons, name, deck, hand, ehealth, eamour, eweapons, ename, edeck, ehand, first, amourm, weaponsm, eamourm, ewaponsm, durability, edurability
        if first == True: #if first time run say who fighting who.
            print("Champion " + name + " you are fighting champion " + ename + ".")
            first == False #make it so its no longer first time run
    #   players turn
        print("Player1's turn") #say whos turn it is
        print("Your hand is:")
        for card in hand:
            print(card[0]) #say what cards are in hand
        print("\nYour stats are:")
        print("Health: " + str(health)) #say what there health is
        print("Amour: " + str(amour)) #say what there amour is
        print("weapons " + str(weapons)) #say what there weapons are
        turn = True
        while turn: #run loop for there actions
            action = str(input("Enter your action")) #ask what there action is
            if action == 'End': #if action end, end turn
                turn = False
            elif action == 'Attack': #if action attak
                damage = (weapons + weaponsm)/(eamour + eamourm) #damage is weapons total agaisnt eamout total
                if damage <= 0: #stops them doing negative damge
                    print("You do no damage.")
                else:
                    ehealth -= damage #takes of damge dealt
                    print("You do " + str(damage) + " damage.")
                durability -= 1 #lowers weapons durability
                if durability == 0:
                    print("You weapon broke") #says if weapon broke
                    weaponsm = 0 #reset weapon mod
                turn = False #end turn
            else:
                for card in hand: #get all cards from hand
                    if action == card[0]: #see if action is one
                        hand.remove(card) #remove the card from hand
                        action = None #change action to stop it removeing reacorsense
                        health += card[1] #apply health
                        amourm = card[2] #apply amourm
                        weaponsm = card[3] #apply weaponsm
                        durability = card[4] #apply durability
        if deck.len() == 0: #see if any deck is left
            print("You have no deck left")
        else:
            hand.append(deck[0]) #add the first in deck to hand
            deck.remove(deck[0]) #remove the first item in deck
    #   computers turn

    set_cards() #run set up cards
    set_player() #run set up player1
    set_enemy() #run set up player2
    turn() #run the turn loop

def turn_1():
    global wn, turn
    wn.fill(BGCOLOR)
    pygame.display.flip()
    ctypes.windll.user32.MessageBoxW(0, "Player 1, take turn?", "Continue", 0)
    hand1=[1,2,3,4]
    turn=1
    while turn==1:
        for event in pygame.event.get():
            for i in range (len(hand1)):
                txt_button("Close",300,100,200,50,GREEN,DARKGREEN,BLACK,terminate)
                img_button((i*150)+100,600,150,200,terminate,str(i+1)+".jpg")
        pygame.display.flip()
        time.sleep(0.2)

menu()
terminate()
