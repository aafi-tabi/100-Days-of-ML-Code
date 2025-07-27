motivation_scores = []
for i in range(6):
    motivation_scores_ = int(input("enter your motivation scores: "))
    motivation_scores.append(motivation_scores_)
    
double = list(map(lambda x: x**2, motivation_scores))
above_10 = list(filter(lambda x :x>10, double)) 
motivation_scores = sorted(double, key = lambda x:x, reverse = True)
print(double)
print(above_10)
print(motivation_scores)



list_ = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
even = [num**2 for num in list_ if 1 <= num <=20]
print(even)


words = ["dream", "AI", "coding", "soft", "goal", "engineer"]
words_ = [word.upper() for word in words if len(word)>5]
print(words_)

scores_ = input("enter a motivational score(1 to 10): ")

scores = scores_.split()
odd=  [score**3 for score in scores if score%2 !=0]
print(odd)
