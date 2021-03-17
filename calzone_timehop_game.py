import time

futures = ["2100","3000"]
pasts = ["440bc", "1980s"]

def name_choosing():

    print('''\n╭━━━━╮╱╱╱╱╱╱╭╮╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱┃┃╱┃┃
╰╯┃┃┣╋╮╭┳━━╮┃╰━╯┣━━┳━━╮
╱╱┃┃┣┫╰╯┃┃━┫┃╭━╮┃╭╮┃╭╮┃
╱╱┃┃┃┃┃┃┃┃━┫┃┃╱┃┃╰╯┃╰╯┃
╱╱╰╯╰┻┻┻┻━━╯╰╯╱╰┻━━┫╭━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯''')

    print("\nChoose your name between: ")
    time.sleep(1)
    print()
    print ("A. Astrid")
    time.sleep(1)
    print ("B. Skyler")
    time.sleep(1)
    print("C. Your own name")
    time.sleep(1)
    print()
    name_choice = input("A, B or C?: ")
    name_choice_lower = name_choice.lower()
    answer_c="Your own name".lower()
    print()

    if name_choice_lower == "a" or name_choice_lower == "astrid":
        time.sleep(1)
        print("Welcome Astrid")
        time.sleep(1)
        general_intro()

    elif name_choice_lower == "b" or name_choice_lower == "skyler":
        time.sleep(1)
        print("Welcome Skyler")
        time.sleep(1)
        general_intro()
        
    elif name_choice_lower == "c" or name_choice_lower == "my own name" or name_choice_lower in answer_c:
        time.sleep(1)
        own_name=input("What's your name? ")
        time.sleep(1)
        print()
        print(f"Welcome {own_name}")
        time.sleep(1)
        general_intro()
  
def general_intro():
    print("\nThe year is 2019.")
    time.sleep(1)
    print("\nYou are an inventor and you have dedicated your life to studying time travel.\n")
    time.sleep(1)
    print("You finally think you have cracked the code but you won't know until you test the machine.\n")
    time.sleep(1)
    print("Do you go back in time or fast forward to the future?")
    time.sleep(1)
    print ("\nPick wisely.")
    check_years()


def check_years():  
    while pasts == [] and futures == []:
        print("You've reached the end of your journey!")
        print("\nThanks for playing!")
        exit
        break
    else:
        future_past()

def future_past():
    choice = input("\nFuture or Past?: ").lower()
    if choice == "future":
        if futures == []:
            print("\nThere are no more future years, please choose a past year")
            past()  
        else:
            future() 

    elif choice == "past":
        if pasts == []:
            print("\nThere are no more past years, please choose a future year")
            future()
        else:
            past()
    else:
        print("\nPlease state 'Future' or 'Past'...")
        future_past()

def future():
    time.sleep(1)
    print(f"\nYears available: {futures}")
    year = input("\nChoose the year/era: ")    

    if year == "2100":
        time.sleep(1)
        futures.remove(year)
        td31()

    elif year == "3000":
        futures.remove(year)
        time.sleep(1)
        td41()   

    else:
        print("Please type the year!")
        future()

def past():
    time.sleep(1)
    print(f"\nYears available: {pasts}")
    year = input("\nChoose the year/era: ").lower()

    if year == "440bc":
        pasts.remove(year)
        time.sleep(1)
        intro_440()

    elif year == "1980s":
        pasts.remove(year)
        time.sleep(1)
        td2()

    else:
        print("\nPlease type the year!")
        past()

#440 BC
def intro_440():

    print("\nIt is a warm summer day circa 440 BC.")
    time.sleep(1)
    print("You have just stepped out of your time machine.")
    time.sleep(1)
    print("You decide to take a walk to examine your surroundings.")
    time.sleep(1)
    print("You are not sure which part of the world you landed in.")
    time.sleep(1)
    print("You hope it is:")
    time.sleep(1)
    print("A. Egypt")
    time.sleep(1)
    print("B. Greece")
    time.sleep(1)
    world = input("\nA or B?:").upper()
    if world == "A":
        egypt()

    elif world == "B":
        greece()

    else:
        print("Please choose A or B...")
        time.sleep(1)
        intro_440()

def egypt():
    print()
    print("You find yourself in the great Library of Alexandria.")
    time.sleep(1)
    print()
    print("What do you want to do?")
    time.sleep(1)
    print()
    print ("A. Read the biggest scroll you can find to absorb some juicy ancient wisdom")
    time.sleep(1)
    print ("B. Study ancient machine sketches")
    time.sleep(1)
    print()
    scroll_curator = input("Your answer: ")
    scroll_curator_lower = scroll_curator.lower()
    answer_a = "Read the biggest scroll you can find to absorb some juicy ancient wisdom".lower()
    answer_b = "Study ancient machine sketches".lower()
    print()

    if scroll_curator_lower == "a" or scroll_curator_lower in answer_a and scroll_curator_lower != "b":
        print("The scroll is located on the highest shelf.")
        time.sleep(1)
        print("Unfortunately, while you are trying to reach for it,")
        time.sleep(1)
        print("you loose your balance and make the whole bookcase collapse.")
        time.sleep(1)
        print("You fall down and die with some serious knowledge dropped on yo' head.")
        time.sleep(1)
        print()
        print("THE END")
        time.sleep(1)
        print()

    elif scroll_curator_lower == "b" or scroll_curator_lower in answer_b:
        print("You found a sketch of a mechanism that looks almost exactly like one you used in your time machine.")
        time.sleep(1)
        print("\nIt helps you make the machine work again so you decide to go for another time adventure.\n")
        check_years()

def greece():
    print()
    print("You are exploring Athens.")
    time.sleep(1)
    print("Suddenly a large gathering of ancient people catches your eye.")
    time.sleep(1)
    print("It turns out it's Socrates who is having a lively discussion with the citizens.")
    time.sleep(1)
    print("He invites you to weigh in.")
    time.sleep(1)
    print()
    print("What would like to talk to him about?")
    time.sleep(1)
    print()
    print ("A. The Good")
    time.sleep(1)
    print ("B. The Justice")
    time.sleep(1)
    print()
    good_justice = input("Your answer: ")
    good_justice_lower = good_justice.lower()
    answer_a = "The Good".lower()
    answer_b = "The Justice".lower()
    print()

    if good_justice_lower == "a" or good_justice_lower in answer_a and good_justice_lower != "The".lower():
        print("A conversation with Socrates leads you to an unexpected conclusion that the Good is the greatest virtue.")
        time.sleep(1)
        print("Now you believe you should sumbit your whole life to it.")
        time.sleep(1)
        print("You are so astonished by the idea that you decide to stay in Greece and become a philosopher yourself.")
        time.sleep(1)
        print()
        print("THE END")
        time.sleep(1)
        print()

    elif good_justice_lower == "b" or good_justice_lower in answer_b and good_justice_lower != "The".lower() :
        print("Socrates' approach to the Justice makes you decide to go back to your time travel.")
        time.sleep(1)
        print("You want to educate the rotten and ignorant societies of all the centuries and try to make them better.")
        time.sleep(1)
        check_years()

def egypt_greece():
    choice = input("Your answer: ")
    choice_lower = choice.lower()
    if choice_lower == "a" or choice_lower == "egypt":
        egypt() 
        
    elif choice_lower == "b" or choice_lower == "greece":
        greece()


#1980s
def td2():
    print("\nYour time machine indicates you've been taken to the 1980's! With limited charge you're given two moments within the era to visit, which do you choose?")
    time.sleep(1)
    print("\nA) Sidestage experience watching Ozzy Osbourne performing live")
    print("\nB) Visit The New York Stock Exchange, Wall Street\n")
    time.sleep(1)
    choice = input("A or B?: ").upper()
    if choice == "A":
        ozzy()

    elif choice == "B":
        nyse()

    else:
      print("Please enter A or B")
      time.sleep(1)
      td2()
#Option A - Ozzy Osbourne
def ozzy():
    print("\nThe time machines stops you hear loud rock music coming from the building in front of you, Ozzy approaches you; 'Here have this, I thought it was a bloody rubber one!'\nhe hands you a decapitated bat. What do you do with it?")
    time.sleep(1)
    print("\nA) Keep the bat as a souvenir from your journey, this is one of the most legendary things Ozzy has done after all!")
    print("\nB) Throw it away in disgust, that's gross!\n")
    time.sleep(1)
    choice = input("A or B?: ").upper()
    if choice == "A":
        bat_y()

    elif choice =="B":
        bat_n()

    else:
      print("Please enter A or B")
      time.sleep(1)
      ozzy()

#When player takes bat
def bat_y():
    print("\nYou get back into your time machine and return to 2019, during the journey the machine runs out of charge. You could be stuck for hours or days whilst it recharges, \nyou have nothing but the bat for food, do you eat it?")
    time.sleep(1)
    print("\nA) Sure, gotta' do what it takes to survive!")
    print("\nB) Absolutely not! I'd rather die of starvation!\n")
    time.sleep(1)
    choice = input("A or B?: ").upper()
    if choice == "A":
        print("\nYou chow down on the bat; it keeps your hunger low until you return home to your family. You fall ill days later, and eventually succumb to the illness. \nYou are patient zero of the Covid-19 virus.")
        exit 

    elif choice == "B": 
        eat_n()

    else:
      print("Please enter A or B")
      time.sleep(1)
      bat_y()

#When Player doesn't eat bat. 
def eat_n():
    #points for preventing covid
    print("\nHours maybe days have past, you don't know?! The machine suddenly boots up again and you return home and feast like a king. Ready for more adventure?")
    time.sleep(1)
    print("\nA) Absolutely!")
    print("\nB) No I want to stay home!\n")
    time.sleep(1)
    choice = input("A or B?: ").upper()
    if choice == "A":
        check_years()

    elif choice == "B":
        print("Thanks for playing!")
        exit

    else:
      print("Please enter A or B")
      time.sleep(1)
      eat_n()

#When player doesn't take the bat
def bat_n():
    print("\nYou return to your time machine after you scrub your hands of the bats blood, what a 'crazy train' of events! Where next?!")
    time.sleep(1)
    print("\nA) I'm not done yet, lets do some more time travelling!")
    print("\nB) Take me home I've seen enough\n")
    time.sleep(1)
    choice = input("A or B?: ").upper()
    if choice == "A":
        check_years()
        return
    elif choice == "B":
        print("Thanks for playing!")
        exit
        return
    else:
      print("Please enter A or B")
      time.sleep(1)
      bat_n()

#Option B - New York Stock Exchange
def nyse():
    print("\nThe time machine lands in an alleyway next to the 'NYSE' you enter the building to see herds of people staring at screens waving frantically as the stocks rise and \nfall! You have money to spend, what do you invest in?")
    time.sleep(1)
    print("\nA) Rising computer tech brands.")
    print("\nB) Nothing, I'm saving up for present from me to me.\n")
    time.sleep(1)
    choice = input("A or B?: ").upper()
    if choice == "A":
        invest()
    elif choice == "B":
        pocket()
    else:
        print("Please enter A or B")
        time.sleep(1)
        nyse()

#If Player does invest
def invest():
    #points for being smart with money.
    print("\nYou approach the kiosk and put your investment into Microsoft™ and head back to the time machine\nWhat's next?")
    time.sleep(1)
    print("\nA) Continue exploring the past and future")
    print("\nB) I wanna go home and spend my millions!\n")
    time.sleep(1)
    choice = input("A or B?: ").upper()
    if choice == "A":
        check_years() #send to main(future or past)
        #remove 1980s from list of years to visit
    elif choice == "B":
        print("\nYou return home to 2019 and see that your investment pays off, you are now filthy rich...Don't spend it all at once!")
        print("\nThanks for playing!")
        exit
    else:
        print("Please enter A or B")
        time.sleep(1)
        invest()

#If Player decides not to invest
def pocket():
    #points for being smart with money (But less points than when you invest).
    print("\nYou decide to keep the money in your pocket, moments later chaos amongst the people ensues, today is the infamous Black Monday of the trading world. As investors \npanic trying to sell their stocks and shares you make your way back to your time machine and?")
    time.sleep(1)
    print("\nA) Continue exploring moments in time!")
    print("\nB) Go home, this time travelling isn't for me...")
    time.sleep(1)
    choice = input("A or B?: ").upper()

    if choice == "A":
        check_years() #send to main (future or past)
        #remove 1980s from list of years to visit

    elif choice == "B":
        print("\nYou're done with travelling through time today")
        print("\nThanks for playing!")
        exit

    else:
        print("Please enter A or B")
        time.sleep(1)
        pocket()



#YEAR 2100
def td31():
        print("\nThe World is in world war 3 for resources.")
        time.sleep(1)
        print("\nYou tried to start back up the Time Machine but it is broken.")
        time.sleep(1)
        print("\nYour only choices are:")
        time.sleep(1)
        print ("\nA) Live Underground")
        time.sleep(1)
        time.sleep(1)
        time_m_broken = input("\nB) Join the Army").lower()
        time.sleep(1)
        
        if time_m_broken == "underground":
            td32()

        elif time_m_broken == "army":
            td35()

        elif time_m_broken == "a":
            td32()

        elif time_m_broken == "b":
            td35()

def td32():
    print("\nYou decide to live underground.")
    time.sleep(1)
    print("\nAs soon as you arrive to the underground village.\nthe villagers tell you that you have to earn your stay.")
    time.sleep(2)
    print("\nYour options are:")
    time.sleep(1) 
    print("\nA) Mining")
    time.sleep(1)
    print("\nB) Chef")
    job_choice = input("A or B?: ").lower()
    if job_choice == "a":
        td33()

    elif job_choice == "b":
        td34()

    else:
        print("\nNot an option, please use A or B...")
        td32()

def td33():
    print("\nYou find water whilst mining.")
    time.sleep (1)
    print("\nYour options are:")
    print("\nA) Share")
    time.sleep(1)
    print("\nB) Keep for yourself")
    mining_water = input("A or B?: \n").lower()
    if mining_water == 'a':
        print("\nYou decide to share the water.")
        time.sleep(1)
        print("\nEventually dehydration catches up with you. End of game.")

    elif mining_water == 'b':
        print("\nYou are eternally praised within your home underground for the rest of your life until the war is over. Then you create a water company and make billions. ")

    else:
        print("\nNot an option, please use A or B...")
        td33()

def td34():
    print("\nAs you are working as a chef.\n\nyou notice theres enough cooking oil to use as a catalyst for your time travel fuel.")
    time.sleep(2)
    print("\nYour options are:")
    print("A) Stay and cook for the population till the war is over")
    time.sleep(1)
    print("B) Steal the cooking oil and leave.")
    time.sleep(1)
    chef_choice = input("A or B: \n").lower()
    if chef_choice == 'a':
        print("You have chosen to cook. and become the best chef in the village.\nEventually the food and water recourses run out and the village dies. ")
        time.sleep
        print("Game over")

    elif chef_choice == 'b':
        print("znYou have stolen the oil.")
        time.sleep(1)
        print("znWhat do you do?")
        time.sleep(1)
        print("\nA) another adventure?")
        time.sleep(1)
        print("\nB) go back home to 2019")
        time.sleep(1)
        refuel_machine_choice = input("\nA or B?: ").lower()
        if refuel_machine_choice == "a":
            check_years()
        elif refuel_machine_choice == "b":
            print("\nYou have gone back home. Game Over")

    else:
        print("\nNot an option, please use A or B...")
        td34()

def td35():
    print("\nYou decide to join the army")
    time.sleep(1)
    print("\nYou set out in squads on the battle field.")
    time.sleep(1)
    print("\nYou are now free to make a choice to either..")
    time.sleep(2)
    print("\nA) Fix Time machine")
    time.sleep(1)
    print("\nB) Save the village")
    time.sleep(1)
    army_choice = input("\nA or B?: ").lower()

    if army_choice == "a":
        print("\nYou have now fixed the time machine.")
        time.sleep(1)
        print("\nDo you want to on A) another adventure? or B) go back home to 2019 ")
        time.sleep(1)
        print("What do you do?:")
        time.sleep(1)
        print("A) Adventure")
        time.sleep(1)
        print("\nB) Home in 2019")
        time.sleep(1)
        fix_machine_choice = input("\nA or B: ").lower()
        if fix_machine_choice == "a":
            check_years()
        elif fix_machine_choice == "b":
            print("\nYou have gone back home. Game Over")

    elif army_choice == "b":
        print("\nYou Save the village and die a ware hero.")
        time.sleep(1)
        print("\nGame over")
        print("\nThanks for playing!")
        exit

    else:
        print("\nNot an option, please use A or B...")
        td35()

#YEAR 3000
def td41():
        print("\nWhat was once Earth is now underwater."),
        time.sleep(1)
        print("\nDolphins have taken over the planet"), 
        time.sleep(1)
        print("\nWhat do you do?\n")
        time.sleep(1)
        print("A) Join richest humans on Mars\n \nB) Create an army and revolt against the dolphin overlords")
        choice= input("\nA or B: ").lower()
        time.sleep(1)
        if choice == "a":
            td42()

        elif choice == "b":
            print("\nYou die in combat.")
            time.sleep(1)
            print("\nEventually both sides agree to an armistice.")
            time.sleep(1)
            print("\nFollowing the war very few humans or dolphins remain on Earth")

        else:
            print("\nNot an option, please use A or B...")
            td41()

def td42():
        print("\nUsing money from their cryogenics company X Æ A-12 is celebrating their father's lifelong mission making Mars habital for humans")
        time.sleep(2)
        print("\nDo you show Elon Musk Jr your time travel machine?")
        print("\nA) Yes!")
        print("\nB) No!")
        choice= input("\nA or B: ").lower()
        time.sleep(1)
        if choice == "a":
            print("\nX Æ A-12 helps get your time machine working")
            check_years()            
        elif choice == "b":
            td43()        
        else:
            print("\nNot an option, please use A or B...")
            td42()
            
def td43():
    print("\nYour time machine is broken.")
    time.sleep(1)
    print("\nYou have no choice but to work for X Æ A-12")
    time.sleep(1)
    print("\nDo you live out the rest of your days on Mars?\n")
    time.sleep(1)
    print("\nA) Yes")
    print("\nB) Ask X Æ A-12 for help")
    choice = input("\nA or B?: ").lower()
    time.sleep(1)

    if choice == "a":
        print("As it turns out, \nnewly populated Mars is boring")
        time.sleep(1)
        print("but thanks to your company health care plan") 
        time.sleep(1)
        print("you can choose when in the future you want to wake up.")
        time.sleep(1)
        td44()

    elif choice == "b":
        print("\nX Æ A-12 helps get your time machine working and you head off on another journey, where to?")
        check_years()   

    else:
        print("\nNot an option, please use A or B...")
        td43()  

def td44():
   choice = input("\nA)100 years \nor \nB)4000 years\n")
   choice
   if len(choice) >= 1: 
       print("\nsee you then!")
    
name_choosing()