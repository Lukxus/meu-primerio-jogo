import time
import random
#Importações
#----------------------------------------------------------------------------------------------------------------
points=0
choice=str()
name=str()
score=[]
catch_counter=0
#Declarações básicas
#----------------------------------------------------------------------------------------------------------------
def gender():
    gender=""
    gender=input("Type [M] for male or [F] for female: ").strip().upper()
    while (gender) not in 'MF' or gender=="":
         gender=input("Type [M] for male or [F] for female: ").strip().upper()
    if gender=='M':
         return"Alan"
    else:
         return'Judith'
#Definição de personagem
#----------------------------------------------------------------------------------------------------------------
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
GREY = "\033[1;90m"
MAGENTA = "\033[1;35m"
DEFAULT='\033[1;97m'
BLACK = '\033[30m'
#EX: print(RED + "ERROR!" + RESET + "Something went wrong...")
#Cores para o terminal
#----------------------------------------------------------------------------------------------------------------
fundo_preto = '\033[40m'
fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'
fundo_magenta = '\033[45m'
fundo_ciano = '\033[46m'
fundo_branco = '\033[47m'
#EX: print(RED + "ERROR!" + RESET + "Something went wrong...")
#Cores de fundo para o terminal
#----------------------------------------------------------------------------------------------------------------
def text_choice(text_zero,text_One,text_Two=0,text_Three=0, text_Four=0,text_Five=0):
    param=[text_zero,text_One,text_Two,text_Three, text_Four,text_Five]
    counter=0
    for x in param:
        if x!=0:
            print(BOLD+"\n"+f"Type {counter} - {x}")
            counter+=1
 
def answer_choice(text_zero,text_One,text_Two=0,text_Three=0, text_Four=0,text_Five=0):
    param=[text_zero,text_One,text_Two,text_Three, text_Four,text_Five]
    counter=0
    for x in param:
        if x!=0:
            print(BOLD+"\n"+f"Type {counter} to answer '{x}'")
            counter+=1 
 
def choice(max, text=''):
    num=['0','1','2','3','4','5']
    tot=str()
    for ind in range(max): #Não pensar com os índices 
        tot=tot+num[ind]
    choice=input(BOLD+text+"Choice: ").strip()
    while choice=="" or choice not in tot or len(choice)!=1:
        choice=input(BOLD+text+"Choice: ").strip()
    return int(choice)
 
def report(text):
    print(fundo_branco+BLACK+f"\n{text}\n"+BLACK+fundo_branco)
    time.sleep(0.5)
 
def Jim(text):
    print(GREEN+f"\n{text}\n")
    time.sleep(0.5)
 
def Alis(text):
    print(MAGENTA+f"\n{text}")
    time.sleep(0.5)
 
def grey_skin(text):
    print(GREY+f"\n{text}\n")
    time.sleep(0.5)
 
def narrator(text):
    print(CYAN+f'\n{text}\n')
    time.sleep(0.5)
 
def vola(text):
    print(RED+ f"\n{text}\n")
    time.sleep(0.5)
 
def rider(text):
    print(BLUE+f"\n{text}\n")
    time.sleep(0.5)
 
def soma(x):
    global score
    score.append(x)
#Funções
#----------------------------------------------------------------------------------------------------------------
 
print("\n"*130)
rider("Each character will have a color for their sentences.")
narrator("The sentences in this color will indicate the sentences of the narrator telling the story.")
print("-"*70)
name=gender()
print("\n"*130)
narrator('You wake up in the passenger seat of a chariot.')
narrator('You feel tired, weak and cold.')
narrator('Some flashes of what happened last night come into your mind, but nothing makes sense yet.')
narrator(f'The only thing you remember for sure is your name, {name}.')
narrator('With your eyes barely open, you notice a tall man wearing a doublet. He is the person riding the chariot.')
narrator('He also notices you are awake and starts talking to you.')
rider("Hmm, you are finally awake. My name is O'brian, you probably don't remember that. You have been unconscious since you got in this chariot.")
text_choice("Stay silent.","Ask 'where are we?'.", "Ask 'where are we headed?'.", 'Try to run away.')
choice_one=choice(4)
while True:
    if choice_one==0:
        rider("...\n")
        break
    if choice_one==1:
        rider("We are in the middle of the Vola forest. ")
        text_choice("Stay silent.","Ask 'where are we?'.", "Ask 'where are we headed?'.", 'Try to run away.')
        choice_one=choice(4)
    if choice_one==2:
        rider("I was hired to take you to the Vola Castle.")
        text_choice("Stay silent.","Ask 'where are we?'.", "Ask 'where are we headed?'.", 'Try to run away.')
        choice_one=choice(4)
    if choice_one==3:
        narrator("You feel weak but still attempt to run away. ")
        narrator("As you try to get up O'brian says...", )
        rider("I will only receive my money if I get you in that castle. Then if try to run I will knock you out and you won't enjoy the beauty of this forest in our way to it.\n")
        text_choice("Stay silent.","Ask 'where are we?'.", "Ask 'where are we headed?'.", 'Try to run away.')
        choice_one=choice(4)
narrator("The way to the castle is simple but takes some time.")
time.sleep(5)
narrator("The night falls.")
narrator("Suddenly you start seeing the greatness of the castle appearing in the middle of the woods. ")
narrator("It's big, old and has some major cracks in it's structure. But it really is magnificent.")
time.sleep(4)
narrator("The chariot stops in front of the main gate, and a man with grey skin appears.")
narrator("He looks familiar to you. You put a lot effort in trying to remember.")
narrator("Unfortunately the only thing you can assure is that Gariot is his name.")
narrator("The man throws a bag of coins to the rider and asks you to leave the chariot.")
narrator("You don't seem to have much of a choice.")
narrator("As you get out, the man with grey skin welcomes you.")
grey_skin(f"Welcome {name}. I can see by your face that you haven't got much rest.")
grey_skin("Please follow me.")
narrator("You follow him and between the steps he speaks.")
grey_skin("I was being polite back there. You look horrible. Do you remember why you are here?")
text_choice("Stay silent.","No.", "Yes(Lie).","I don't care.")
choice_two=choice(4)
if choice_two==0:
    grey_skin("..... Okay, I will assume that you do.")
elif choice_two==1:
    grey_skin("I understand. You were pretty confuse that night.")
    grey_skin("You told me you liked challenges so I got you this one.")
    grey_skin("You agreed to come and have 3 dinners with the master of this castle.")
    grey_skin("He is a very nice person. He wants to help the world keeping knowledge and empathy in it.")
    soma(1)
elif choice_two==2:
    grey_skin("Great!! I hope you enjoy the game.")
elif choice_two==3:
    grey_skin("You were much more polite the day we met.")
    grey_skin("I wonder if this world still has someone good.")
    soma(-1)
grey_skin("I think that is enough chatting. I will show you your room.")
narrator("You keep walking and going up stairs... ")
time.sleep(2)
grey_skin("\nThis is your room. Please try to not break anything.")
grey_skin("Ohh, and one more thing. Do not go to rooms that you are not supposed to. The master does not like people who do not respect privacy.")
narrator("Gariot leaves before you can ask anything else.")
time.sleep(3)
narrator("A few moments latter, the door of the room opens...")
#Quartos dia 1
#----------------------------------------------------------------------------------------------------------------
text_choice("Stay in the room and wait for dinner.", "Go check other rooms.")
choice_three=choice(2)
if choice_three==1:
    narrator("You get out of the room and see five doors distributed by the lower floors.")
    text_choice("Go back to your room.","Check door 1.","Check door 2.","Check door 3.","Check door 4.", "Check door 5.")
    choice_four=choice(6)
    while True:
        if choice_four==0:
            narrator("Boring...")
            break
        elif choice_four==1:
            narrator("This door is locked!")
            text_choice("Go back to your room.","Check door 1.","Check door 2.","Check door 3.","Check door 4.", "Check door 5.")
            choice_four=choice(6)
        elif choice_four==2:
            narrator("You open the door and find a great library full of books about ethic and psychology.")
            narrator("It's weird because it is the only part of the castle that is not full of dust. Perhaps someone uses that room a lot.")
            text_choice("Go back to your room.","Check door 1.","Check door 2.","Check door 3.","Check door 4.", "Check door 5.")
            choice_four=choice(6)
        elif choice_four==3:
            narrator("This door is locked!")
            text_choice("Go back to your room.","Check door 1.","Check door 2.","Check door 3.","Check door 4.", "Check door 5.")
            choice_four=choice(6)
        elif choice_four==4:
            narrator("This door is locked!")
            text_choice("Go back to your room.","Check door 1.","Check door 2.","Check door 3.","Check door 4.", "Check door 5.")
            choice_four=choice(6)
        elif choice_four==5:
            narrator("As you touches the door you hear a voice...")
            grey_skin("Already disobeying the rules?")
            grey_skin("No wonder why I don't have much hope for people. Go back to your room and don't get out before dinner.")
            narrator("You do as he says.")
            catch_counter+=1
            soma(-2)
            break
else:
    narrator("Boring...")
#QUIZ dia 1
#----------------------------------------------------------------------------------------------------------------
time.sleep(3)
narrator("After an hour waiting in you room, Gariot appears.")
grey_skin(f"Follow me, {name}.")
narrator("You walk down all the stairs of the castle. There you find the dinner room and a old man sitting in one side of the dinner table.")
grey_skin("The game shall begin...")
narrator("Gariot leaves the place.\n")
vola(f"\nHmmm. You must be {name}.")
vola("I think our game will be interesting, don't you?")
vola("Well it will work like a quiz. Each day that passes the difficulty will increase. So... shall we start? ")
text_choice('Yes', "No")
choice_five=choice(2)
if choice_five!=0:
    vola("I'm not very patient. Let's start already.")
#1
vola("What is the difference between sadness and depression??")
answer_choice("Sadness is healthy and lasts for days, while depression is not healthy and can last for years or a lifetime.","Depression is healthy and sadness is not.","Both just mean bad feelings, so they are unhealthy. However, depression is far worse.","Depression comes from hard times only, while sadness is related to losing the will to do any kind of activity.", "Sadness comes from hard times only, while  depression is related to losing the will to do any kind of activity.")
answer_one=choice(5)
if answer_one==0:
    soma(4)
    vola("Well done!")
else:
    vola("What a bad way to start.")
    vola("Many people think that sadness and depression are the same thing, but that is wrong. Sadness is something healthy and natural related to hard times such as losing a job, divroce or losing someone important. On the other hand, depression is something that affects in a negative way the behaviour of the person. It can make them feel sad and lose their will to do any kind of activity. ")
#2
vola("What causes depression?")
answer_choice("Just troubles at school.", "Just family matters.", "Family matters and troubles at school only.","Depression is a disorder that doesn’t have a specific cause. There are many factors that can increase the chances of having it or not. Some of them are genetics and traumas.","Depression is a disease that can have many cases. The most important of them are stressful moments.")
answer_two=choice(5)
if answer_two==3:
    vola("You know a thing or two.")
    soma(4)
else:
    vola("Wrong!")
    vola("Each person is different, so each situation is unique. There is no cause that will always be seen in every case. However genetics and traumas increase the chance og havint it. ")
#3
vola("What are the symptoms of depression?")
answer_choice("Depression symptoms are just sadness and gain of weight.", "Depression symptoms are just sadness and oversleeping.", "Depression has only one symptom that is sadness.","Depression can have many symptoms. Some of them are insonia, feeling guilty and overthinking.", "Depression has many symptoms, some of them are sadness, loss of smell and feeling tired." )
answer_three=choice(5)
if answer_three==3:
    vola("Nice work.")
    soma(4)
else:
    vola("Have you ever tried to have empathy? ")
    vola("Nevermind...")
    vola("This disease has many symptoms. They always involve behavioral matters, which means that loss of smell is not one of them.")
#4
vola("Who are those that most suffer with depression?")
answer_choice("The kids.", "The teenagers.", "The young adults", "The older adults.", "The elders.")
answer_four=choice(5)
if answer_four==4:
    vola("Good...")
    soma(4)
else:
    vola("God...")
    vola("The ones that suffer the most with this disease are the elder ones. In most cases it is related to the lack of attention from the rest of the family or because they miss the activities they used to perform.")
if sum(score)>=9:
    vola("I'm impressed. It has been a long time since someone got such a good score.")
    vola("Now we should get some rest.")
else:
    vola("Go get some rest. I will delude myself believing you got such a bad score because you were tired.")
time.sleep(15)
print('\n'*60)
print(f"Points so far: {sum(score)}")
time.sleep(10)
print('\n'*60)
#Day Two
#----------------------------------------------------------------------------------------------------------------
narrator("DAY 2")
if sum(score)>8:
    narrator("A shiny day starts.")
    narrator("You feel well and motivated after a good night of rest.")
else:
    narrator("A cloudy day starts.")
    narrator("After a bad night of sleep, you wake up feeling a little dizzy.")
 
narrator("There is no one waiting for you.")
narrator("Therefore you can do anything you want...")
#Quartos dia 2
#----------------------------------------------------------------------------------------------------------------
narrator("After you leave your room you hear a noise coming from the downstairs. However you also notice that the 5 doors on the lower floors seem different... ")
text_choice("Chek door 1.","Chek door 2.","Chek door 3.", "Chek door 4.", "Chek door 5.", "Check the dinner room.")
choice_six=choice(6, "(Doors)")
while True:
        if choice_six==0:
            narrator("You open the door and sees a simple room with purple walls and a bed full of dust.")
            narrator("On The table there is a kid's journal and a doll.")
            text_choice("Check the doll","Read Journal", "Leave the room.")
            choice_room_one=choice(3, '(Room 1)')
            while True:
                if choice_room_one==0:
                    narrator("The doll is old and dirty, but it has it's beauty.")
                    text_choice("Check the doll","Read Journal", "Leave the room.")
                    choice_room_one=choice(3, '(Room 1)')
                    print("\n")
                if choice_room_one==1:
                    narrator("You open the journal and see that every page is as conserved as if it was written in the day before.")
                    narrator("It tells the story of a little girl that was on her limit due to never having friends.")
                    narrator("In the last page of the journal it was written...")
                    Alis("I can't stand to never met someone knew.")
                    Alis("The only friend I have is Mito, the doll.")
                    Alis("I begged to dad to live in a big city.")
                    Alis("He refused to listen to me again.")
                    Alis("He says the world is too dangerous for me.")
                    Alis("I can not do this anymore.")
                    text_choice("Check the doll","Read Journal", "Leave the room.")
                    choice_room_one=choice(3, '(Room 1)')
                if choice_room_one==2:
                    narrator("You leave the room.")
                    print("\n")
                    break
            text_choice("Chek door 1.","Chek door 2.","Chek door 3.", "Chek door 4.", "Chek door 5.", "Check the dinner room.")
            choice_six=choice(6, "(Doors)")
        elif choice_six==1:
            narrator("You open the door and find a great library full of books about ethic and psychology.")
            narrator("It feels weird because it is the only part of the castle that is not full of dust. Perhaps someone uses that room a lot.")
            narrator("You leave the room.")
            text_choice("Chek door 1.","Chek door 2.","Chek door 3.", "Chek door 4.", "Chek door 5.", "Check the dinner room.")
            choice_six=choice(6, "(Doors)")
        elif choice_six==2:
            narrator("You open the door and notice it is a big bedroom.")
            narrator("The walls are wood color and all the furniture is big.")
            narrator("On the desk you notice many mirrors")
            text_choice("Leave the room.", "Check the mirrors.")
            choice_room_three=choice(2, "(Room 3)")
            while True:
                if choice_room_three==0:
                    narrator("You leave the room.")
                    print("\n")
                    break
                if choice_room_three==1:
                    narrator("Suddenly you start feeling small in that room.... you feel lonely.")
                    narrator("You sit in front of the mirrors and stares at them for some moments.")
                    narrator("It feels like there are more people with you there.")
                    text_choice("Leave the room.", "Check the mirrors.")
                    choice_room_three=choice(2, "(Room 3)")
                    print("\n"*2)
            text_choice("Chek door 1.","Chek door 2.","Chek door 3.", "Chek door 4.", "Chek door 5.", "Check the dinner room.")
            choice_six=choice(6, "(Doors)")
        elif choice_six==3:
            narrator("You open the door and see a boy's bedroom.")
            narrator("The room is very organized and full of story books.")
            narrator("It seems that the person who used to sleep here, dreamed of travelling the world.")
            narrator("There is a note on the desk....")
            text_choice("Leave the room.", "Read the note.")
            choice_room_four=choice(2, "(Room 4)")
            while True:
                if choice_room_four==0:
                    narrator("You leave the room.")
                    break
                if choice_room_four==1:
                    narrator("The note says...")
                    Jim("One day I'll know at least one person from each city of these lands.")
                    text_choice("Leave the room.", "Read the note.")
                    choice_room_four=choice(2, "(Room 4)")
            text_choice("Chek door 1.","Chek door 2.","Chek door 3.", "Chek door 4.", "Chek door 5.", "Check the dinner room.")
            choice_six=choice(6, "(Doors)")
        elif choice_six==4:
            catch_counter+=1
            if catch_counter==1:
                soma(-2)
                grey_skin("What did I told about privacy?")
            elif catch_counter==2:
                soma(-4)
                grey_skin("I really want you to lose this game...")
                grey_skin("I can't stand people that don't do what they are told.")
            grey_skin("You represents the reason why people can not be trusted.")
            grey_skin("Ahhh, by the way the master wants to talk to you.")
            time.sleep(2)
            narrator("You walk downstairs, heading the dinner room.")
            narrator("There you find Vola")
            if sum(score)>9:
                vola("I just wanted to say...")
                vola("I can see the potential in you")
                vola("Good luck today")
            else:
                vola("I don't know what to think about you yet. However, our last quiz was not what I would call a good first impression.")
                vola("So at least, try harder.")
            vola("Oww, one more thing. Respect my privacy, I'll tell you my story. If you are worthy.")
            vola("Now go back to your room and wait for dinner.")
            narrator("After that short speech, Vola leaves.")
            break
        elif choice_six==5:
            narrator("You walk down to the dinner room and there you see Vola.")
            vola("Good, you heard me.")
            if sum(score)>9:
                vola("I just wanted to say...")
                vola("I can see the potential in you")
                vola("Good luck today")
            else:
                vola("I don't know what to think about you yet. However, our last quiz was not what I would call a good first impression.")
                vola("So at least, try harder.")
            if  catch_counter!=0:
                vola("Oww, one more thing. Respect my privacy, I'll tell you my story. If you are worthy.")
            vola("Now go back to your room and wait for dinner.")
            narrator("After that short speech, Vola leaves.")
            break
#Quiz dia 2
#----------------------------------------------------------------------------------------------------------------
time.sleep(10)
narrator('After 10 long hours thinking about what Vola told you, you go to the dinner room.')
narrator("Vola is already there, waiting for you.")
if sum(score)>9:
    vola("Can we start?")
    text_choice("Yes.", "No.")
    choice_seven=choice(2)
    if choice_seven==0:
        vola("Good...")
    else:
        vola("You know I'm just trying to be polite, right? ")
        vola("We are playing now!")
else:
    vola("Be better than yesterday.")
#5
vola("How many types of depression exist?")
answer_choice("3", "17", "10", "7", "9")
answer_five=choice(5)
if answer_five==4:
    vola("Well done.")
    soma(6)
else:
    vola("Actually, there are 9 types of depression. Those types are Major, Persistent, Bipolar, Seasonal, Phisicotic, Postpartum, Premenstrual, Situational and Atypical.")
#6
vola("What are the characteristics of Persistent Depressive Disorder?")
answer_choice("If you have depression that lasts for 2 years or longer it receives the name of persistent depression. It’s treatment involves psychotherapy, medication or a combination of both.", "If you have depression that lasts for 1 year or longer it is called persistent depression. It's treatment involves psychotherapy, medication or a combination of both.", "If you have depression that lasts for 6 months or longer it receives the name of persistent depression. It's treatment involves psychotherapy, medication or a combination of both.", "If you have depression that lasts for 2 years or longer it receives the name of persistent depression. It's treatment involves taking medications only.", "If you have depression that lasts for 1 years or longer it is called persistent depression. It’s treatment involves psychotherapy only.")
answer_six=choice(5)
if answer_six==0:
    vola("Exactly.")
    soma(6)
else:
    vola("The Persistent Depressive Disorder classifies a depression that lasts for 2 years or longer. Its symptoms are a change in appetite, feeling hopeless, low self-esteem, among others. It's treatment involves psychotherapy, medication or a combination of both.")
#7
vola("What is the Atypical Depression?")
answer_choice("This type of depression is quite different from the other types of depression. It is known for having different symptoms if compared to them. Some of these symptoms are increased appetite and sleeping more than usual.  People also can feel temporarily happy having this kind of depression.","It is known for having it’s symptoms increased in women when they are on their period.", "It is known for including symptoms of both major depression and psychotic depression.", "It is known for happening during specific seasons, like winter. During that period, people get to see less of the daylight, which affects how they feel.", "This type of depression is quite different from the Persistent Depressive Disorder. It is known for having different symptoms if compared to the other types of depression. Some of these symptoms are increased appetite  and sleeping more than usual. People never feel happy having this kind of depression.")
answer_seven=choice(5)
if answer_seven==0:
    vola("Perfect.")
    soma(6)
else:
    vola("Perfectly wrong...")
    vola("It is characterized for having specific symptoms, such as increased appetite, oversleeping, feeling of heaviness in your arms and legs and oversensitive to criticism. Another thing that also distinguishes this type of depression is that a positive event can temporarily improve your mood")
#8
vola("What are the main characteristics of major depression?")
answer_choice("Major depression is the rarest type of depression. It’s main symptoms are Loss of interest or pleasure in your activities, Feeling worthless or guilty and constantly feeling depressed.","Major depression is the most common and ordinary type of depression. It’s characterized by an increase during winter, when people are not able to get as much sunlight as they are used to in the rest of the year.", "Major depression is the most common and ordinary type of depression. It’s main symptoms are Loss of interest or pleasure in your activities, Feeling worthless or guilty and constantly feeling depressed.", "Major depression is not a technical term in psychiatry and it qualifies the most common and ordinary type of depression.", "Major depression is the rarest type of depression. It’s known for not having a treatment and only depending on the person to get better.")
answer_eight=choice(5)
if answer_eight==2:
    vola("Very good!")
    soma(6)
else:
    vola("Really?")
    vola("Major depression is the most common and ordinary type of depression. It’s main symptoms are Loss of interest or pleasure in your activities, Feeling worthless or guilty and constantly feeling depressed. Furthermore it is treatable just like the other types of depression.")
if sum(score)>=40:
    vola("I can not remember the last time someone got me so impressed.")
    vola("You are doing a great job.")
    vola("See you tomorrow, go get some rest.")
if sum(score)> 20 and sum(score)<=39:
    vola("You are doing good so far...")
    vola("It could be worse.")
    vola("Maybe you just need some rest... again.")
else:
    vola("I don't understand why you are still trying.")
    vola("Have never worried about others?")
    vola("Go to your room now.")
time.sleep(15)
print('\n'*50)
print(f"Points so far: {sum(score)}")
time.sleep(10)
print('\n'*50)
#Day 3
#----------------------------------------------------------------------------------------------------------------
if sum(score)> 20:
    narrator("A great day is shining.")
    narrator("You can hear some birds singing.")
else:
    narrator("A rainy day starts.")
narrator("You leave the bed and get of out of the room.")
narrator("You can't hear any sound and it feels scary.")
narrator("You get to the stairs and again see the doors distributed over the lower floors.")
#Quartos dia 3
#----------------------------------------------------------------------------------------------------------------
text_choice("Check door 1.","Check door 2.", "Check door 3.","Check door 4.","Check door 5.","Go back to your room.")
choice_eight=choice(6, "(Doors)")
while True:
    if choice_eight==0:
        if sum(score)>20:
            narrator("You open the door and sees a simple room with purple walls and a bed full of dust.")
            narrator("On The table there is a kid's journal and a doll.")
            text_choice("Check the doll","Read Journal", "Leave the room.")
            choice_room_one=choice(3, '(Room 1)')
            while True:
                if choice_room_one==0:
                    narrator("The doll is old and dirty, but it has it's beauty.")
                    text_choice("Check the doll","Read Journal", "Leave the room.")
                    choice_room_one=choice(3, '(Room 1)')
                    print("\n")
                if choice_room_one==1:
                    narrator("You open the journal and see that every page is as conserved as if it was written in the day before.")
                    narrator("It tells the story of a little girl that was on her limit due to never having friends.")
                    narrator("In the last page of the journal it was written...")
                    Alis("I can't stand to never met someone knew.")
                    Alis("The only friend I have is Mito, the doll.")
                    Alis("I begged to dad to live in a big city.")
                    Alis("He refused to listen to me again.")
                    Alis("He says the world is too dangerous for me.")
                    Alis("I can not do this anymore.")
                    text_choice("Check the doll","Read Journal", "Leave the room.")
                    choice_room_one=choice(3, '(Room 1)')
                if choice_room_one==2:
                    narrator("You leave the room.")
                    break
        else:
            narrator("The door is locked.")
        text_choice("Check door 1.","Check door 2.", "Check door 3.","Check door 4.","Check door 5.","Go back to your room.")
        choice_eight=choice(6, "(Doors)")
    elif choice_eight==1:
        narrator("You open the door and find a great library full of books about ethic and psychology.")
        narrator("It feels weird because it is the only part of the castle that is not full of dust. Perhaps someone uses that room a lot.")
        narrator("You leave the room.")
        text_choice("Check door 1.","Check door 2.", "Check door 3.","Check door 4.","Check door 5.","Go back to your room.")
        choice_eight=choice(6, "(Doors)")
    elif choice_eight==2:
        if sum(score)>20:
            narrator("You open the door and notice it is a big bedroom.")
            narrator("The walls are wood color and all the furniture is big.")
            narrator("On the desk you notice many mirrors")
            text_choice("Leave the room.", "Check the mirrors.")
            choice_room_three=choice(2, "(Room 3)")
            while True:
                if choice_room_three==0:
                    narrator("You leave the room.")
                    break
                if choice_room_three==1:
                    narrator("Suddenly you start feeling small in that room.... you feel lonely.")
                    narrator("You sit in front of the mirrors and stares at them for some moments.")
                    narrator("It feels like there are more people with you there.")
                    text_choice("Leave the room.", "Check the mirrors.")
                    choice_room_three=choice(2, "(Room 3)")
                    print("\n")
        else:
            narrator("The door is locked.")
        text_choice("Check door 1.","Check door 2.", "Check door 3.","Check door 4.","Check door 5.","Go back to your room.")
        choice_eight=choice(6, "(Doors)")
    elif choice_eight==3:
        if sum(score)>20:
            narrator("You open the door and see a boy's bedroom.")
            narrator("The room is very organized and full of story books.")
            narrator("It seems that the person who used to sleep here, dreamed of travelling the world.")
            narrator("There is note on the desk....")
            text_choice("Leave the room.", "Read the note.")
            choice_room_four=choice(2, "(Room 4)")
            while True:
                if choice_room_four==0:
                    narrator("You leave the room.")
                    break
                if choice_room_four==1:
                    narrator("The note says...")
                    Jim("One day I'll know at least one person from each city of these lands.")
                    text_choice("Leave the room.", "Read the note.")
                    choice_room_four=choice(2, "(Room 4)")
        else:
            narrator("The door is locked.")
        text_choice("Check door 1.","Check door 2.", "Check door 3.","Check door 4.","Check door 5.","Go back to your room.")
        choice_eight=choice(6, "(Doors)")
    elif choice_eight==4:
        if sum(score)>20:
            narrator("The door opens")
            narrator("It's a dark room full of dust.")
            narrator("There is a large double bed and paintings of cities.")
            narrator("On the desk there is two sickness reports.")
            text_choice("Read the sickness reports.", "Leave the room.")
            choice_room_five=choice(2, "(Room 5)")
            while True:
                if choice_room_five==0:
                    report("Official report- Winter's first moon.")
                    report("A new sickness is spreading and it is a risk for everyone.")
                    report("If you don't require any essential supplies, as food, water or medicine, do not leave your house!")
                    report("Please have some empathy and help those who can not protect themselves from this virus.")
                    report("We will provide more information as soon as possible.")
                    report("Good luck to all of you.")
                    print(fundo_preto+"\n"*2)
                    report("Official report- Summer's seventh moon.")
                    report("The mysterious sickness is still among us.")
                    report("The disrespect of the quarantine rules has caused thousands of deaths so far. ")
                    report("Uncountable lives have been destroyed. What a shame.")
                    report("A cure has been found but many still do not accept to take it")
                    report("Empathy is still the key for us to survive.")
                    report("Will us manage to get our old lives back?")
                    text_choice("Read the sickness reports.", "Leave the room.")
                    choice_room_five=choice(2, "(Room 5)")
                    print(fundo_preto)
                if choice_room_five==1:
                    narrator("You leave the room.")
                    break
        else:
            catch_counter+=1
            if catch_counter==3:
                grey_skin("That is unacceptable. How can you be so stubborn and disrespectful?")
                grey_skin("Go back to you room and do not leave until dinner.")
                grey_skin("I think I will like it's end.")
                break
            else:
                narrator("The door is locked.")
                text_choice("Check door 1.","Check door 2.", "Check door 3.","Check door 4.","Check door 5.","Go back to your room.")
                choice_eight=choice(6, "(Doors)")
    elif choice_eight==5:
        break
#QUIZ dia 3
#----------------------------------------------------------------------------------------------------------------
narrator("You go back to you room and wait for dinner.")
time.sleep(5)
narrator("You go to the dinner room after some hours. Vola is alredy there.")
narrator("He seems anxious.")
vola("Today it will be faster. I have only prepared 3 questions")
#9
vola("What is psychotherapy?")
answer_choice("Psychotherapy is not essential for everyone who suffers from depression. It’s objective is to stimulate the individual about it’s emotional insecurities and anguishes.", "Psychotherapy is essential for everyone who suffers from depression. It’s objective is to stimulate the individual about it’s emotional insecurities and anguishes. Therefore it is not one the most efficient methods to treat depression.","Psychotherapy is essential for everyone who suffers from depression. It’s main use is to determine what is the best medicine for the person.. Therefore it is one the most efficient methods to treat depression.", "Psychotherapy is essential for everyone who suffers from depression. It’s objective is to stimulate the individual about it’s emotional insecurities and anguishes. Therefore it is one the most efficient methods to treat depression.", "Psychotherapy is not essential for everyone who suffers from depression. Furthermore it only shows results alongside controlled medication.")
answer_nine=choice(5)
if answer_nine==3:
    vola("Nice.")
    soma(8)
else:
    vola("Wrong!!")
    vola("Psychotherapy is one of the most effective treatments for depression. Through self knowledge it incentivizes the person to think and analyze what emotionally bothers it. This kind of treatment can last months or years and can bring benefits to everyone, even those who do not suffer from depression.")
#10
vola("What are the main characteristics of Electroconvulsive therapy? ")
answer_choice("This kind of treatment involves passing electrical currents through the patient’s brain. It’s mainly used to affect the neurotransmitters so they are correctly grouped and found in the proper amounts. This way depression symptoms tend to be smoothed.", "This kind of treatment involves passing electrical currents through the patient’s brain. It’s mainly used to affect the neurotransmitters so they are correctly grouped and found in the proper amounts. In order of it’s positive results, people often treat any kind of depression with this method.", "This kind of treatment involves passing electrical currents through the patient’s body. It’s mainly used to cause pain and increase the body's resistance. It affects the muscles so the person feels stronger and overcomes depression.", "This kind of treatment involves passing electrical currents through the patient’s brain. It’s mainly used to affect the bad memories so they disappear and the patient does not suffer with them anymore.", "This kind of treatment involves passing electrical currents through the patient’s body. It’s mainly used to affect the enzymes inside the organs. This way the whole biological system is affected and depression disappears in most cases.")
answer_ten=choice(5)
if answer_ten== 0:
    vola("Good.. very good.")
    soma(8)
else:
    vola("Terrible answer!")
    vola("Electroconvulsive therapy is a treatment for depression mostly used for severe major depression and bipolar disease that is not responding to any other treatment. This treatment is not used for every kind of depression because of it’s side effects, such as short-term memory loss, nausea and headaches. It's application involves passing electrical currents through the patient’s brain while it’s under the effect of anesthesia. The electrical discharge helps the brain to organize the neurotransmitters. The results aren't always positive, but when they are depressed symptoms tend to be smoothed.")
#11
vola("How do pandemic and quarantine circumstances associate with depression?")
answer_choice("Information about past quarantines should not be considered. There is nothing that is more likely to happen during quarentines, because each person is unique and no pattern can be found.", "Considering the information about past quarantines, people usually tend to have problems with insomnia, low mood, stress, irritability and confusion. Furthermore, it is also usual for people to get addicted to alcohol after the quarantine. These factors make it easier for someone to suffer from depression.", "Considering the information about past quarantines, people usually tend to have problems with insomnia, low mood, stress, irritability and confusion. Furthermore, people often get addicted to alcohol after the quarantine. These factors make it easier for someone not to suffer from depression.", "Considering the information about past quarantines, people rarely tend to have problems with insomnia, low mood, stress, irritability and confusion. Furthermore, it is also usual for people to get addicted to alcohol after the quarantine. These factors make it easier for someone to suffer from depression.", "Considering the information about past quarantines, people usually tend to have problems with short-term memory loss, oversleeping, low mood, stress, irritability and confusion. Furthermore, it is also usual for people to get addicted to alcohol after the quarantine. These factors make it easier for someone to suffer from depression.")
answer_eleven=choice(5)
if answer_eleven==1:
    vola("Perfect!!")
    soma(8)
else:
    vola("Have you ever been in quarantine?")
    vola("Let me explain.")
    vola("Information about past quarantines is very important because it helps us understand the best ways to help people during hard times. According to them people usually tend to have problems with insomnia, low mood, stress, irritability and confusion. Unfortunately, the problems also go beyond the quetientime periods, since some people may not know how to handle the situation and become dependent on substances. The most likely of them is alcohol.")
#END
#----------------------------------------------------------------------------------------------------------------
if sum(score)>48:
    vola("It's finally over.")
    vola("It was a pleasure to know that someone like you lives in this world.")
    vola("More than just your freedom, I will tell you my story...")
    time.sleep(3)
    vola("Before living in this castle I used to live in the big city, Vendonzza.")
    vola("The city was beautiful and full of energy.")
    vola("Hundreds of travellers would arrive there everyday.")
    vola("I used to take a normal and happy life there.")
    vola("However, a plague spread")
    vola("The only name it received was the mysterious disease.")
    vola("Thousands of people started dying.")
    vola("The Duque of the city tried to establish some rules about social distancing and quarantine, but people wouldn't listen.")
    vola("The city ran out of resources and people got even more desperate")
    vola("Noone, except for some families like mine, would stay in their houses, and help the fight against that disease.")
    vola("Empathy was gone. Everyone had been consumed by selfishness and lies.")
    vola("One day, my wife left the house to try to get some food for our kids.")
    vola("Unfortunately, she got infected.")
    vola("In the end she didn't make it.")
    vola("That situation made me understand people can not be trusted.")
    vola("After that I came to this castle and isolated me and my kids from the rest of the world.")
    vola("My kids grew here.")
    vola("Alis was my younger child. I remember her running through these halls with her doll. She used to say it was her only friend, but I couldn't truly understand what she meant.")
    vola("She dreamed of having many friends and living in a big city.")
    vola("Jim was my middle child. He would always keep a mirror with him. He was afraid of being alone.")
    vola("He dreamed of being surrounded of people and never have to carry a mirror again.")
    vola("My older child was Todd. He was the smartest of us all.")
    vola("He loved to read and wanted to know at least one person from each city from these lands.")
    vola("Furthermore, he was only one capable of understanding what his siblings were going through.")
    vola("Alis and Jim were suffering from depression, and I wouldn't see it because of my fear of people.")
    vola("One day, Todd and I had a bad discussion about me not listening to Jim and Alis. It was bad.")
    vola("He wanted to help them accomplish their dreams but I said that we were not leaving the castle.")
    vola("In the next night, Tood took his siblings and left the castle without me knowing.")
    vola("It has been 17 years since that night.")
    vola("The one I trusted most to have empathy, myself, failed me that night.")
    vola("Since then, I have been bringing some individuals to this castle and killing them if they prove to be incapable of empathy.")
    vola("Luck or not, you passed.")
    vola("Do not forget what you have learned here!")
    vola("You should go now, the next player should be here soon.")
    time.sleep(20)
    narrator("You leave the castle alive and with a lot of knowledge to make the world a better place.")
    print("\n"*70)
    narrator(f"SCORE:{sum(score)}")
    narrator("THE END.")
elif sum(score)<48 and sum(score)>=30:
    vola("It's finally over!")
    vola("I wonder if I should kill you or not.")
    vola("You don't have the worst score but you are also far from the best.")
    vola("Hmm, I have an idea. You shall stay here me with me studying psychology until you are ready.")
    vola("I do not care if you like it or not. I have already made up my mind.")
    vola("The next player will be here soon. We should get some rest.")
    time.sleep(15)
    print("\n"*70)
    narrator("You may be alive but still has much to learn...")
    narrator(f"SCORE:{sum(score)}")
    narrator("THE END")
else:
    vola("It's finally over! Thanks god.")
    vola("T=It has been a long time since someone got such a bad score.")
    vola("You have no empathy or will to help others.")
    vola("You shall die here.")
    narrator("Master Vola quickly got out the chair and started walking towards you.")
    narrator("Each step closer is making the room darker.")
    text_choice('Accept that you have nothing good to offer to this world', "Try to run away.")
    choice_nine=choice(2)
    if choice_nine==0:
        narrator("Vola stops to take a knife from the table and before you notice he is behind you.")
        narrator("Now, everything is getting darker and darker.")
        time.sleep(10)
        print("\n"*70)
        narrator(f"SCORE:{sum(score)}")
        narrator("THE END.")
    elif choice_nine==1:
        survival_chance=random.randint(1,20)
        if (survival_chance-catch_counter)%2==0:
            narrator("As you start running you feel garriott behind you.")
            narrator("He tries to hold you but you manage to dodge him.")
            narrator("You keep running and leave by the same gate that you arrived.")
        else:
            narrator("As you start running you feel garriott behind you.")
            narrator("He tries to hold you but you manage to dodge him.")
            narrator("Unfortunately you trip over you own foot and falls.")
            narrator("Vola gets closer to you and everything turns dark.")
        time.sleep(10)
        print("\n"*70)
        narrator(f"SCORE:{sum(score)}")
        narrator("THE END.")