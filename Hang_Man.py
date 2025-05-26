#for random number
import random
Given_num_list = ["one", "two", "three", "four"]
random_num = random.choice(Given_num_list)
Hang_man_status=['''
       _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / \\
     |
     |______________''',
      '''
       _______
     |/      |
     |      (_)
     |      \\|/
     |       
     |      
     |
     |_______________''',
     
     '''
       _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
     |______________''',
     '''
       _______
     |/      |
     |      
     |      
     |       
     |      
     |
     |______________ ''' 
     ]
     

print(f' {(len(random_num))* "_ "} fill the blanks with letters \n')

switch = False
guessed_word = []
total_lifes = 3
while  not switch:
    guessed_letter = input("Guess a letter🙈> ")
    dummy=""
    for random_letter in random_num:
        if guessed_letter == random_letter:
            dummy+=random_letter
            guessed_word.append(guessed_letter)
        elif random_letter in guessed_word:
            dummy += random_letter
        else:
            dummy+="_ "
    print(dummy)
    if "_" not in dummy:
        switch = True
        print("You Win😊")
    if guessed_letter not in random_num:
        total_lifes -=1
        if total_lifes == 0:
            switch = True
            print("You Loose😒")
    print(Hang_man_status[total_lifes])    
        
