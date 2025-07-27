data = "name:Sana_Kim;year:2023;skills:Python,AI,ML"
list_ = data.split(";")
print(list_)
name = " ".join((list_[0][5:].split("_")))
print(name)
first_name =name[:4]
last_name = name[5:]
print(first_name)
print(last_name)

year = int(list_[1][5:])
print(year)
skills = list_[2][7:].split(",")
print(skills)
skills_ = skills[1:]
print(skills_)

bio = {
  "first_name": first_name,
  "last_name": last_name,
  "year": year,
  "skills": skills_
}

print(bio)

data_ =(first_name, last_name,year,skills)
