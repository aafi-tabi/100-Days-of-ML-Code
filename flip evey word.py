word = input("enter a 3 word string: ")
words = word.split()
if len(words) == 3:
    words[0] = words[0][::-1]
    words[1] = words[1][::-1]
    words[2] = words[2][::-1]
    print(words)
else:
    print("invalid number of words")
    