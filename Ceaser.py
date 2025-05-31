def alphabets():
    Lower_case_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Upper_case_alphabets=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return Lower_case_alphabets
    
def encode():
    
    Lower_case_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Upper_case_alphabets=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    skipping_letters_count= 1
    test_word ="abc.....!"
    encoded_word =""


    for letters in test_word:
        if letters in Lower_case_alphabets:
            skipped_letter_index = Lower_case_alphabets.index(letters)+skipping_letters_count
            if skipped_letter_index > 26:
                skipped_letter=Lower_case_alphabets[skipped_letter_index%26]
                encoded_word+=skipped_letter
            else:    
                skipped_letter=Lower_case_alphabets[skipped_letter_index]
                
                encoded_word+=skipped_letter
        elif letters in Upper_case_alphabets:
            skipped_letter_index = Upper_case_alphabets.index(letters)+skipping_letters_count
            skipped_letter=Upper_case_alphabets[skipped_letter_index]
            encoded_word+=skipped_letter    
        else:
            encoded_word+=letters
        
    print (encoded_word)

encode()
