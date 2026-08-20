import string

def anagrams(string1, string2):
    '''
    Checks if two strings are anagrams.
    '''
    
    
    # Strip punctuation   
    string1_no_punct = string1.translate(str.maketrans("","", string.punctuation))
    string2_no_punct = string2.translate(str.maketrans("","", string.punctuation))
    
    # Strip lowercase and spaces
    text1 = string1_no_punct.lower().strip().replace(" ","")
    text2 = string2_no_punct.lower().strip().replace(" ","")

    # Make it a list and sort the lists
    text1, text2 = list(text1), list(text2)
    text1.sort()
    text2.sort()
    
    # Check if the lists are equal
    if text1 == text2:
        return True
    else:
        return False
    
print(anagrams("Hello, world", "worldhello"))
