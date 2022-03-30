import random

a = open("Chuck.txt", "r")
a1 = open("newChuck.txt", "w")

a2 = a.read()

list = a2.split('.')

for n in list:
    print(n)

def jk(word):
    return a1.write(new_name(word))

def new_name(word):
    return a2.replace("Chuck Norris", word)

def cik_doesnt():
    return a2.count("doesnt")

def randomam_joka():
    return print(list[random.randint(0,14)])

word = input("Replace Chuck Norris with new name")
new_name(word)

jk(word)
randomam_joka()
