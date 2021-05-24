'''
Title: Mental Health Experiments Comps Grammar
Author: Aishee Mukherji
File Name: comps_grammar_am.py
Usage: python3 comps_grammar_am.py
Description: Generates strings of web search and social media post content for each of the 3 study groups:
- Control (no psychiatric illness)
- Mood Disorder
- Schizophrenia
'''
import sys
import tracery
from tracery.modifiers import base_english
from colorama import Fore
from colorama import Style


md = {
   "origin":["#posts#","#websearch#"],
   "websearch":["#mood_disorder# symptoms","#medication#","What are the side effects of #medication#?","side effects of #medication#","How long will my #mood_disorder# last?","How do I deal with my #mood_disorder#?"],
   "mood_disorder":["major depression","dysthymia","bipolar disorder","mood disorder"],
   "medication":["seroquel","lithium","valproic acid","divalproex sodium","carbamazepine","abilify"],
   "posts":[
      "I am #feeling#.",
      "My #noun# makes me #feeling#!",
      "I am #verb#ing.",
      "I am doing #verb#ing by myself.",
      "My #swear# #noun# #verb#s and I am #feeling#!",
      "How could this #swear# #noun# hurt like this?",
      "My #swear# #noun# makes me #verb#.",
      "I cannot #action#."
   ],
   "feeling":[
      "#angryfeel#",
      "#lonelyfeel#",
      "#sadfeel#",
      "#lonelyfeel#",
      "#sadfeel#",
      "#sadfeel#"
   ],
   "angryfeel":[
      "angry",
      "upset",
      "hateful",
      "irked",
      "disgusted",
      "rage",
      "annoyed",
      "pissed"
   ],
   "lonelyfeel":[
      "lonely",
      "alone"
   ],
   "sadfeel":[
      "sad",
      "down",
      "hurt",
      "in pain",
      "tearful",
      "depressed",
      "teary",
      "melancholy",
      "gutted",
      "anxious",
      "unworthy",
      "worthless",
      "insecure",
      "useless",
      "stressed",
      "overwhelmed",
      "failure",
      "tired",
      "exhausted"
   ],
   "noun":[
      "life",
      "hate",
      "hurt",
      "pain",
      "tears",
      "blood",
      "loneliness",
      "depression",
      "mood",
      "heart",
      "sickness",
      "lungs"
   ],
   "verb":[
      "fall",
      "die",
      "kill",
      "ache",
      "stab",
      "drown",
      "yell",
      "scream",
      "cry"
   ],
   "action":[
      "sleep",
      "eat",
      "focus"
   ],
   "swear":[
      "",
      "",
      "",
      "fucking",
      "fucked up",
      "shitty",
      "shit",
      "hell",
      "damn"
   ]
}



schiz = {
   "origin":["#posts#","#websearch#"],
   "websearch":["schizophrenia symptoms","#medication#","what are the side effects of #medication#","side effects of #medication#","why does my schizophrenia make me feel","Services to treat schizophrenia","Risk factors of schizophrenia","Prognosis of schizophrenia"],
   "medication":["thorazine","prolixin","haldol","clozapine","caplyta"],
   "posts":[
      "#netspeak# #pronoun# make me feel #feeling##emphatic#",
      "hear #swear# #noun1# in my head#emphatic#",
      "#verb1# #verb##emphatic#",
      "#noun# is #swear# #verb##emphatic#",
      "#verb##emphatic#",
      "my #swear# #noun# #verb# and feeling #feeling##emphatic#",
      "#pronoun# make #swear# #noun# hurt like this#emphatic#",
      "#swear# #noun# makes me feel #feeling##emphatic#",
      "#pronoun# made me feel #feeling#",
      "cant #action#",
      "#pronoun# are out to #theyverb#",
      "not #crazy# for thinking #animal# are #swear# out to #theyverb#",
      "#verb# #animal# #verb#"
   ],
   "feeling":[
      "#angryfeel#"
   ],
   "angryfeel":[
      "angry",
      "upset",
      "hateful",
      "irked",
      "disgusted",
      "rage",
      "annoyed",
      "pissed"
   ],
   "noun":[
      "life",
      "hate",
      "hurt",
      "pain",
      "tears",
      "blood",
      "loneliness",
      "depression",
      "mood",
      "heart",
      "guts",
      "death"
   ],
   "noun1":[
      "voices",
      "music",
      "nagging",
      "god",
      "jesus"
   ],
   "verb":[
      "stabbing me in the back",
      "killing me",
      "fucking with me",
      "coming after me"
   ],
   "verb1":[
      "see you",
      "hear you",
      "feel you"
   ],
   "verb2":[
      "see",
      "hear",
      "feel"
   ],
   "swear":[
      "",
      "",
      "",
      "fucking",
      "fucked up",
      "shitty",
      "shit",
      "hell",
      "damn"
   ],
   "netspeak":[
      "ugh",
      "btw",
      "lol",
      "thx"
   ],
   "emphatic":[
      "",
      "",
      "...",
      "!!!!"
   ],
   "action":[
      "sleep",
      "hear my own thoughts"
   ],
   "theyverb":[
      "get me",
      "bring me down"
   ],
   "pronoun":[
      "you",
      "they",
      "they",
      "they"
   ],
   "crazy":[
      "crazy",
      "psycho"
   ],
   "animal":[
      "aliens",
      "doctors",
      "therapists"
   ]
}


control = {
   "origin":"#posts#",
   "posts":[
      "#greeting# The #noun# #verb#.",
      "Went to #location# with my #group#.",
      "#adj.capitalize# day at #location# with the #group#.",
      "I am #emotion#."
   ],
   "adj":[
      "good",
      "great",
      "joyful",
      "wonderful"
   ],
   "greeting":[
      "",
      "Hello!",
      "Greetings!",
      "Howdy!",
      "Hey!"
   ],
   "location":[
      "the concert",
      "the mall",
      "travel",
      "school",
      "the beach",
      "restaurant",
      "the hotel"
   ],
   "noun":[
      "party",
      "dog",
      "day",
      "dinner",
      "family",
      "rave",
      "lunch",
      "breakfast"
   ],
   "verb":[
      "plays",
      "rocks",
      "dances",
      "jumps",
      "laughs",
      "sings",
      "is the best",
      "is joyful"
   ],
   "emotion":[
      "joyful",
      "happy",
      "peaceful",
      "grateful",
      "full of pride",
      "serene",
      "interested",
      "amused",
      "hopeful",
      "inspired",
      "in awe",
      "in love"
   ],
   "group":[
      "friends",
      "gang",
      "boyfriend",
      "girlfriend",
      "partner",
      "friend",
      "best friends"
   ]
}



grammar_md = tracery.Grammar(md)
grammar_schiz = tracery.Grammar(schiz)
grammar_control = tracery.Grammar(control)

grammar_md.add_modifiers(base_english)
grammar_schiz.add_modifiers(base_english)
grammar_control.add_modifiers(base_english)

def singleOutput():
   print(f'{Fore.BLUE}Mood Disorder{Style.RESET_ALL}')
   print(grammar_md.flatten("#origin#"))
   print()

   print(f'{Fore.RED}Schizophrenia{Style.RESET_ALL}')
   print(grammar_schiz.flatten("#origin#"))
   print()

   print(f'{Fore.GREEN}Control{Style.RESET_ALL}')
   print(grammar_control.flatten("#origin#"))
   print()
   menu()


def multipleOutputs(num, grp):
   i = 0
   if grp == "a":
      print("************Mood Disorder:",num,"Outputs************")
      print()
      while i < num:
         print(grammar_md.flatten("#origin#"))
         i = i + 1
   elif grp =="b":
      print("************Schizophrenia:",num,"Outputs************")
      print()
      while i < num:
         print(grammar_schiz.flatten("#origin#"))
         i = i + 1
   elif grp =="c":
      print("************Control:",num,"Outputs************")
      print()
      while i < num:
         print(grammar_control.flatten("#origin#"))
         i = i + 1
   print()
   print()
   multipleOutputsMenu()



def multipleOutputsMenu():
   choice = input("""************************Pick a study group************************:

A: Mood Disorder
B: Schizophrenia
C: Control
Q: Quit

Please enter your choice: """)
   if choice == "A" or choice == "a":
      grp = "a"
   elif choice == "B" or choice == "b":
      grp = "b"
   elif choice == "C" or choice == "c":
      grp = "c"
   elif choice == "q":
      sys.exit
      return
   else:
      print("Invalid input")
      multipleOutputsMenu()
   try:
      num = int(input('Number of string outputs: '))
      multipleOutputs(num, grp)
   except (ValueError, TypeError):
      pass

def menu():
   print("************Comps: Google Search String Generator**************")
   choice = input("""
A: Return Single Output for Each Group
B: Return Multiple Outputs for a Group
Q: Logout

Please enter your choice: """)
   if choice == "A" or choice =="a":
      singleOutput()
   elif choice == "B" or choice =="b":
      multipleOutputsMenu()
   elif choice=="Q" or choice=="q":
      sys.exit
   else:
      print("You must only select either A or B")
      print("Please try again")
      menu()

def main():
   menu()

main()
