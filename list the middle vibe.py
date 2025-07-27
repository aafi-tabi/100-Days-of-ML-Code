words = input("enter a 3 word sentence: ")
word = words.split()
if len(word) == 3:
    if(len(word[0])%2 != 0 and len(word[1])%2 != 0 and len(word[2])%2 != 0):
        a = len(word[0])//2
        b = len(word[1])//2
        c = len(word[2])//2
        word[0] = word[a]
        word[1] = word[b]
        word[2] = word[c]
        
        print(word)