keys = "user_id:105,name:Aafi_Tabii,level:Intermediate"
extra = "lang:Python|AI,year:2025"

keyslist_ = keys.split(",")
extrallist_ = extra.split(",")
print(keyslist_)
print(extrallist_)

user_id_ = keyslist_[0].split(":")
print(user_id_)
user_id = int(user_id_[1])

name__ =keyslist_[1].split(":")
name_ = name__[1].split("_")
print(name_)
name = " ".join(name_)
print(name)

level_ = keyslist_[2].split(":")
level =str(level_[1])
print(level)


keys_ ={
  "user_id": user_id,
  "name": name,
  "level": level
}

lang = extrallist_[0].split(":")
language_ = lang[1].split("|")
language__ = (",".join(language_))
language = language__.split(",")
print(language)


year_  =extrallist_[1].split(":")
year = int(year_[1])
print(year)

extra_ ={
  "lang": language,
  "year": year
}
data = keys_ | extra_

print(data)

data_ =(user_id, name, level, language, year)
print(data_)
