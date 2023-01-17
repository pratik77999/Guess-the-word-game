'''Word guessing game using python'''

from random import *

words=['Actor','Gold','Painting','Advertisement','Grass','Parrot','Airport','Guitar','Piano','Afternoon','Greece','Pencil','Ambulance','Hair','Pillow','Animal','Hamburger','Pizza','Answer','Helicopter','Planet','Apple','Helmet','comb','Balloon','Horse','Queen','Banana','Hospital','Quill','Battery','House','Rain','Beach','Hydrogen','Rainbow','Beard','Raincoat','Bed','Insect','Refrigerator','Belgium','Insurance','Restaurant','Iron','River','Branch','Island','Rocket','Brother','Rose','Camera','Jewellery','Candle','Jordan','Sandwich','Juice','Carpet','King','Shampoo','Kitchen','Shoe','China','Kite','Church','Knife','Crayon','Lamp','Stone','Crowd','Lawyer','Sugar','Daughter','Leather','Death','Library','Teacher','Denmark','Lighter','Telephone','Diamond','Lion','Television','Lizard','Tent','Disease','Lock','Thailand','Tomato','Lunch','Toothbrush','Dream','Machine','Magazine','Train','Easter','Truck','Manchester','Uganda','Market','Egypt','Match','Elephant','Microphone','Vase','Energy','Monkey','Vegetable','Engine','Morning',]

def guess_the_word():

    random_word=choice(words).lower()
    len_word=len(random_word)

    blank_list=[]
    count=0
    for i in range(len_word):
        blank_list.append('-')
    n=len(random_word)
    blank_list[0]=random_word[0]
    blank_list[n-1]=random_word[n-1]
    print(''.join(blank_list))
    
    while True:
        input_letter=input("Guess another letter :").lower()
        
        for j in range(len(random_word)):
            if input_letter in random_word[j]:
                blank_list[j]=input_letter
        
        count=count+1

        join_blank_list=''.join(blank_list)
        print(join_blank_list)
        if random_word==join_blank_list:
            print('-'*40)    
            print("The correct answer is ",random_word)
            print(f"You find the correct word in {count} times")
            print('-'*40)
            break
        


guess_the_word()
while True:
    option=input("Do you wanna play again ? (yes/no) :").lower()
    if option=='no':
        break
    else:
        guess_the_word()
