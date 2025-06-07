

def alphabets():
    global Lower_case_alphabets,Upper_case_alphabets
    Lower_case_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Upper_case_alphabets=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def inputs():
    global test_word,value,text,number
    text =input("Text your message✍️... \n")
    number = input("Enter your secret code number🙈🙈 > \n")
    test_word = text
    value=int(number)
    print("Don't worry Your secret will be safe👍")
def Encode():
    alphabets() 
    inputs()
    encoded_word =""
    for each_letter in test_word:
        
        if each_letter in Lower_case_alphabets:
            ind_of_each_letter = Lower_case_alphabets.index(each_letter)
            changed_index=ind_of_each_letter+value
            if changed_index < len(Lower_case_alphabets):
                letter = Lower_case_alphabets[changed_index]
                encoded_word+=letter
            else:
                letter = Lower_case_alphabets[(changed_index%len(Lower_case_alphabets))]
                encoded_word+=letter
            
        elif each_letter in  Upper_case_alphabets:
            ind_of_each_letter = Upper_case_alphabets.index(each_letter)
            changed_index=ind_of_each_letter+value
            if changed_index < len(Upper_case_alphabets):
                letter = Upper_case_alphabets[changed_index]
                encoded_word+=letter
            else:
                letter = Upper_case_alphabets[(changed_index%len(Upper_case_alphabets))]
                encoded_word+=letter
            
        else:
            encoded_word+=each_letter
    print(f'''Your encrption is successfully over😁.\n\n"{encoded_word}"\n''')
def Decode():
    alphabets() 
    inputs()
    decoded_word =""
    for each_letter in test_word:
        
        if each_letter in Lower_case_alphabets:
            ind_of_each_letter = Lower_case_alphabets.index(each_letter)
            changed_index=ind_of_each_letter-value
            if changed_index < 0:
                letter = Lower_case_alphabets[changed_index]
                decoded_word+=letter
            else:
                letter = Lower_case_alphabets[changed_index]
                decoded_word+=letter
            
        elif each_letter in  Upper_case_alphabets:
            ind_of_each_letter = Upper_case_alphabets.index(each_letter)
            changed_index=ind_of_each_letter-value
            if changed_index < 0:
                letter = Upper_case_alphabets[changed_index]
                decoded_word+=letter
            else:
                letter = Upper_case_alphabets[changed_index]
                decoded_word+=letter
            
        else:
            decoded_word+=each_letter
    print(f'''Congratulations your decrption was sucessfully over😁\n\n"{decoded_word}"''')  
button = True
while  button:
    x = input("""What task do you want me to do...🤔\n
🔸 'ENCODE' to Encode your data.
🔸 'DECODE' to Decode yout data.
🔸 'STOP' to End this program.\n\n""").lower()
    if x == "encode":
        Encode()
    elif x == "stop":
       button = False
       print("Your program was ended💀.")
    elif x == "decode":
        Decode()
    else:
        print("""\nYour input is Wrong🤦
Please follow the instructions😒\n""")
    
