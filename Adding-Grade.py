students = [
    {"name": "Aafi", "score": 50},
    {"name": "Lia", "score": 80},
    {"name": "Zoya", "score": 100},
    {"name": "Sara", "score": 60}
]

def normalized_score(scores,max_, min_):
    norm = (scores - min_)/(max_ - min_)
    return norm

def grading(score):
    if score >= 0.8:
        grade = "A"
        return grade
    elif 0.6 <= score < 0.8:
        grade = "B"
        return grade
    elif 0.4 <= score < 0.6:
        grade = "C"
        return grade
    else:
        grade = "D"
        return grade
    
    
scores = []

for student in students:
    scores.append(student["score"])

max_ = max(scores)
min_ = min(scores) 

for student in students:
    student["score"] = normalized_score(student["score"],max_,min_)
    student["grade"] = grading(student["score"])

    

print(students)
