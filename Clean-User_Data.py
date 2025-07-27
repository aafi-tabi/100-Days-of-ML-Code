raw_data = [
    "Name: Aafi, Email: aafi@gmail.com",
    "Name: Sana, Email: sana@gmail.com",
    "Name: Aafi, Email: aafi@gmail.com",  # duplicate
    "Name: Moiz, Email: moiz(at)gmail.com",  # invalid
    "Name: Zoya, Email: zoya@gmail.com",
    "Name: Aafi, Email: aafi123@gmail.com"
]

data = []
data_invalid =[]

for ch in raw_data:
    if "@" in ch:
        data.append(ch)
    else:
        data_invalid.append(ch)
        
        


print(data_invalid)      
print(data)


data_set = set(data)
print(data_set)

data_list = list(data_set)
print(data_list)
        
