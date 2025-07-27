word = input("enter a word(number of characters should be odd):")
if len(word)%2 == 0:
    lenght = len(word)//2
    word_1 = word[:lenght]
    word_1_ = word_1[::-1]
    word_2 = word[lenght:]
    print(word_1_ + word_2)
else:
    print("invalid number of characters")
    