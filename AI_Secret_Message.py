message = "AIengineer@2025|Google"
separator = message.split("@")
print(separator)
year  = int(separator[1][:4])
print(year)
google = separator[1][5:].upper()
print(google)

title = separator[0]
reverse_ =title[::-1]
print(reverse_)


separator_copy = separator.copy()
print(separator_copy)

info = {
  "title": title,
  "year": year,
  "company": google
}
print(info)

info_tuple =(title,year,google)
print(info_tuple)
