import fandom 
fandom.set_wiki("Jojo") 
fandom.search("Dio") 
dio = fandom.page("Dio Brando")
print(dio.content)
with open("fanwiki.txt", "w") as file:
    file.write(str(dio.content))


