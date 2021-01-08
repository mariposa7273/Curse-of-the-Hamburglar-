#Imports
import random
import time
import sys
delay = 0.06
#delay = 0.0
inventory = []
notdone = "playing"

#Functions
#p prints out words letter by letter to make it look like a retro game
def p (words):
    for letter in words:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print("")
def plist (words):
  for letter in words:
    print(letter, end='', flush=True)
    time.sleep(delay)
    print("")
  print("")

#into code and choosing your character for the rest of the game
def choose_character ():
    global notdone
    if notdone == 'restart':
      print("\n")
    notdone = "playing"
    p("Welcome to the Curse of the Hamburglar.")
    p("You must go an quest to defeat the evil hamburglar who has reigned as an evil tryrant over your home, and cause much misery and death to its people.")
    p("Along the way you must best enemies and collect new items in order to gain enough power to defeat him.")
    p("Choose your Dfficulty")
    p("Here are your options:")
    p("1. Difficulty: Easy")
    p("Character: Fredrick the third - a halfling bard whose only wish in life is to have a nice nap and play music")
    p("2. Difficulty: Hard")
    p("Character: Alaine - a half-orc ranger who has a vendetta against plants")
    p(("Which one do you choose?, Fredrick or Alaine "))
    global character
    character = input("> ")
    if character.lower() == "fredrick":
        character = "Fredrick"
        p("You've selected Fredrick")
    elif character.lower() == "alaine":
        character = "Alaine"
        p("You've selected Alaine")
    else:
        character_list = ["Fredrick", "Alaine"]
        p("Unfortunatly that character is at the grocery store and cannot be reached right now. You will be assigned a random character in their stead.")
        character = random.choice(character_list)
        print("Your randomly selected character is", character+".")

#character goes north or south and depending on direction gets enemy or item first
def scene_one (character):
    global notdone
    p("You look around to find yourself in a clearing in the middle of a dense patch of pine trees.")
    if character == "Fredrick":
        p("You only have a spare change of clothes and your trusty accordion with you.")
        inventory.append("Change of clothes")
        inventory.append("Trusty accordion")
        p("Your inventory:")
        plist(inventory)
    else:
        p("You only have a weed whacker and your trusty sidekick Anklebiter- a land shark- with you.")
        inventory.append("Weed Whacker")
        inventory.append("Anklebiter the land shark")
        p("Your inventory:")
        plist(inventory)
    p ("You are on a dirt path. The path leads two direction, North or South")
    p("Which way will you go? North or South ")
    path_direction = input("> ")
    if path_direction == "North" or path_direction == "north":
        enemy1 (character)
        item1(character)
           
    elif path_direction == "South" or path_direction == "south":
        item1(character)
        if notdone == "restart":
               return False
        enemy1 (character)
        if notdone == "restart":
               return False
    else:
      #bad input just becomes the south option but with a bird
        p("As you stand still, a bird swoops down from the sky and attacks you, to avoid the bird you run North up the path.")
        enemy1(character)
        if notdone == "restart":
            return False
        item1(character)
        if notdone == "restart":
            return False 


#first level - mini game is different per character
def enemy1(character):
    global notdone

#Fredrick's first level - unscramble song lyrics Difficulty: easy
    if character == "Fredrick":
      p("As you follow the path, you stumble upon a small ecampment in the woods.")
      p("There sits your fellow bard and known accomplice of the Hamburglar, Reyna.")
      p("She challenges to a sing-off and you must accept, this is the first step in defeating the evil hamburglar and ending his reign.")
      p("In order to win you must unscramble the following song lyrics.")
      song_list = ["Twinkle" , "Twinkle", "Little" , "Star"]
      #puts words in the song list in a random order
      random.shuffle(song_list)
      print(song_list)
			#repl really doesn't like this line for no damn reason- Fixed by turning tabs into spaces
      p("What is it?")
      song_guess = input("> ")
      if song_guess.lower() == "twinkle twinkle little star":
          p('"You have managed to best me this time but I will have my revenge".')
          p("You've gained experience points and leveled up to level 2.")
          p("You will now be able to aquire new items and best stronger foes.")
          p("Be warned there are no second chances anymore.")
          p("After defeating Reyna, You follow the path out of her encampment, you need to keep moving if you want to defeat the hanburgalar.")
      else:
          p('"You are so bad at being a bard, why dont you just give up music?" taunts Reyna. "I will give you one last chance to prove your a cool bard like the rest of us".')
          song_list2 = ["Happy", "Birthday"]
          random.shuffle(song_list2)
          print (song_list2)
          p("What is the song title?")
          song_guess2 = input("> ")
          if song_guess2.lower() ==  "happy birthday":
            p('"You barely beat me this time, next time you will not be so lucky," Reyna says.')
            p("You've gained experience points and leveled up to level 2.")
            p("You will now be able to aquire new items and best stronger foes.")
            p("Be warned there are no second chances anymore.")
            p("After defeating Reyna, You follow the path out of her encampment, you need to keep moving if you want to defeat the hamburglar.")
          else:
             p('"You have failed. Game Over. Maybe try the other route huh or learn basic some human knowledege".')
             notdone = "blobl"
             checkend()
             if notdone == "restart":
               return False
        
    
#Alaine's 1st level - riddles Difficulty: easy
    elif character == "Alaine":
      p('You approach a gnarly tree. All its branches block the trail. Suddenly the trees knots for into a face. The tree says, "I am Splintertrunk the wise eldertree and I will not allow you to pass to into the hamburglars territory until you have proven you worthiness. Answer this riddle and you may venture forth." His riddle is as follows:')
      p("This thing has a dorsal fin but doesn't swim. An anklebiter and squirrel chaser but not a fighter.")
      p("What is it?")
      guess1 = input("> ")
      if guess1.lower() == "land shark":
        p('"You may pass young ranger." Splintertrunk says and his branches retract to reveal the wide open road."You have proven yourself worthy of continuining on your quest."')
        p("You've gained experience points and leveled up to level 2")
        p("You will now be able to aquire new items and be able to best stronger foes")
        p("Be warned there are no second chances anymore")
        p("After passing by Splintertrunk, You follow the path out of that section of the forest, you need to keep moving if you want to defeat the hamburglar. ")
      else:
        p('"Wow. If only you paid attention to the details. I will give you one last chance to prove yourself worthy," spoke Splintertrunk')
        p('"Samuel was out for a walk when it started to rain. He did not have an umbrella and he was not wearing a hat. His clothes were soaked, yet not a single hair on his head got wet. How could this have happened?"')
        p("What is the answer? a. because he is a salamander, b. because he is bald, or c. because he is walking on his head")
        guess2 = input('> ')
        if guess2.lower() == "b" or guess2.lower() == "b. because he is bald":
          p('"You may be dim of wit but I will allow you to pass this time. Carry on." And with that Splintertrunk reluctantly retracts his branches to reveal the wide open road')
          p("You've gained experience points and leveled up to level 2")
          p("You will now be able to aquire new items and be able to best stronger foes")
          p("Be warned there are no second chances anymore")
          p("After passing Splintertrunk, You follow the path out of that sections of the forest, you need to keep moving if you want to defeat the hanburgalar")
        else:
          p('"You are so dumb. We cannot let someone as idiotic as you prance through the forest as they wish!" says Splintertrunk. Splintertrunk shouts into the forest and a giant tarantua comes at his call. It eats you and you die a slow and painful death in its stomach. Game Over.')
          notdone = "brur"
          checkend()
          if notdone == "restart":
            return False
				
#first item pick up, tool gets added to inventory
def item1(character):
    global notdone
    p('You walk along the trail, down a gravel path until you come to a rocky outcropping, you see a mysterious light coming from within and soon discover the entrance to a cave. You enter and see a mysterious figure in the firelight. He turns around and says to you, "I am Wizard OGrimacey and you, young adventurer have come far.')
    if character == "Fredrick":
      p('"I bestow to you brave bard to help in your quest, a microphone blessed by the goddess of music, Brie."')
      p("You've recived a Mystical Microphone!")
      inventory.append("Mystical Microphone")
      p("Your inventory:")
      plist(inventory)
      p("You continue down the path with determined to defeat the Hamburglar ")
    else:
      p('"I bestow to you brave ranger to help in your quest, a mighty chainsaw forged by the count of the gates, Macsimillion."')
      p("You've received a Mighty Chainsaw!")
      inventory.append("Mighty Chainsaw")
      p("Your inventory:")
      plist(inventory)
      p("You continue down the path with determined to defeat the Hamburglar ")

def scene_two(character):
  global notdone
  
  #Fredrick's second level: rhyming Dificulty - medium
  if (character) == "Fredrick":
      p("You come to a villiage and in the town square you see. the jester to the Hamburgaler, Mike the Microphone. He is performing for a crowd. You need to taunt him, you can do so with your new magic microphone or with an impromtu accordian solo. What item do you choose?")
      item_used = input("> ")
      if item_used.lower() == "accordion":
        p('You play a solo so epic Mike is stunned by your skill.')
        ('"Impressive" Mike says, "but I was thinking something a little less polka. How a rap battle?" You accept.')
      elif item_used == "Microphone" or item_used == "microphone":
         p('You brandish your microphone and Mike says, "Ready for a rap battle are ya? Well you are on!"')
      else:
         print('"Impressive use of {thing}" Mike says "How a rap battle?" You accept.'.format(thing = item_used))
      p("Fill in the blank with a rhyming word.")
      #rhyme level one
      p("I had a little kitten")
      p("she was wearing a _")
      r1 = input("> ")
      if r1.endswith("itten"):
        p("She had a stuffed duck")
        p("Who liked to say _")
        r2 = input("> ")
        #rhyme level two
        if r2.endswith("uck"):
          p("She and her friend rat")
          p("Looked at a _")
          r3 = input("> ")
          #rhyme level three
          if r3.endswith("at"):
            p("Good job you won the rap battle!")
            p("You've gained experience:")
            p("You leveled up to level 3 and gained enough strength to fight the Hamburglar.")
          #third fail
          else:
            p("That's no rhyme! You got no game. Game Over")
            notdone = "dfsk"
            print(notdone)
            checkend()
            print(notdone)
            if notdone == "restart":
              return False
        #second fail
        else:
          p("That's no rhyme! You got no game. Game Over")
          notdone = "dfsk"
          print(notdone)
          checkend()
          print(notdone)
          if notdone == "restart":
            return False
      #first fail
      else:
        p("That's no rhyme! You got no game. Game Over")
        notdone = "dfsk"
        print(notdone)
        checkend()
        print(notdone)
        if notdone == "restart":
          return False
  else:
    #Alaine's second level - ??
    obstacle_list = ["tree", "weed", "squirrel"]
    p("You end up in a thick patch of undergrowth and trees in the woods. Use the appropiate items in your inventory to get through. Your inventory is:")
    plist(inventory)
    for i in range (3):
      obstacle = random.choice(obstacle_list)
      string = ("You approach a "+obstacle+"! What item from your inventory do you use?" )
      p(string)
      tool = input("> ")
      if obstacle == "tree" and tool.lower() == "chain saw":
        #this one didn't work and sent the code to the else statement
        p("Nice, you got past!")
      elif obstacle == "squirrel" and tool.lower() == "land shark":
        p("Nice, you got past!")
      elif obstacle == "squirrel" and tool.lower() == "anklebiter":
        p("Nice, you got past!")
      elif obstacle == "squirrel" and tool.lower() == "anklebiter the land shark":
        p("Nice, you got past!")
      elif obstacle == "weed" and tool.lower() == "weed whacker":
        p("Nice, you got past!")
      else:
        p("Wrong tool! You're now eternally lost in the woods and starve to death. Game Over.")
        notdone = "dfsk"
        checkend()
        if notdone == "restart":
          return False


def final_battle(character):
  global notdone
  threat_list = ["throw a pie at you", "stab you with a french fry sword"]
  actions = []
  p("You have gotten to the Hamburgalar's lair. He challenges you to a duel.")
  if character != "Fredrick":
    p("Anklebiter is so intmidated that it runs away.")
  if character == "Fredrick":
    actions.append("play accodion")
    actions.append("dance to the side")
    p("Your actions are 'play accordion' - an attack move or 'dance to the side' - a dodge move")
  else:
    actions.append("cut with chainsaw")
    actions.append("roll to the side")
    p("Your actions are 'cut with chainsaw' - an attack move or 'roll to the side' - a dodge move")


  if character == "Fredrick":
    health = 3
  else:
    health = 5
  string = ("The Hamburgalar has "+str(health)+" health.")
  p(string)
  while health > 0:
      threat = random.choice(threat_list)
      string = ("The Hamburgalar is about to "+threat+"! What do you do?" )
      p(string)
      action = input("> ")
      if threat == "throw a pie" and action.lower() == "dance to the side":
        p("Nice, you dodged!")
      elif threat == "stab you with a french fry sword" and action.lower() == "play accordion":
        p("Nice, you parried and attacked!")
        health -= 1
        string = ("The Hamburgalar has "+str(health)+" health left.")
        p(string)
      elif threat == "throw a pie" and action.lower() == "roll to the side":
        p("Nice, you dodged!")
      elif threat == "stab you with a french fry sword" and action.lower() == "cut with chainsaw":
        p("Nice, you parried and attacked!")
        string = ("The Hamburgalar has "+str(health)+" health left.")
        p(string)
      else:
        p("Wrong move! The hamburglar attacks you and you die. Game Over.")
        notdone = "dfsk"
        checkend()
        if notdone == "restart":
          return False
  p("You won! The Hamburglar is dead and peace has returned to the kingdom!")
  notdone = "dfsk"
  checkend()
  if notdone == "restart":
    return False

#Running Functions

#checkend isn't working because first the game kept assigning the variable to the first assignment and now it says "UnboundLocalError: local variable 'notdone' referenced before assignment"
#Update: variables needed to be  global and returning False to exit out of functions
def checkend():
  global notdone
  if notdone != "playing":
      p("Would you like to play again? Yes or no")
      playagain = input("> ")
      if playagain.lower() == 'yes':
        notdone = "restart"
      else:
        p("Game closing...")
        #repl will say "repl process died unexpectedly" but this is, in fact, expected and the way to terminate the code
        sys.exit(0)

while notdone == "playing" or notdone == "restart":
  choose_character ()
  if notdone != "restart":
    scene_one(character)
    if notdone != "restart":
      scene_two(character)
      if notdone != "restart":
        final_battle(character)
