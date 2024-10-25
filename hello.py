
from time import sleep
import random
from os import system

abc = list(' abcdefghijklmnopqrstuvwxyz ')
result = 'pull rqst'
txt = ''
for i in range(len(result)):
    for j in range(len(abc)):
        ch = abc[j]
        for a in range(10):
            print(txt + ch)
        sleep(0.05)
        system('clear')
        if ch == result[i]:
            txt += ch
            break
print((result+'\n')*10)
=======
print("Hello this is my PR!!!")

print("DONE!!")
word = "kingpin616"
for letter in word:
    print(letter)
=======


// I am using GeneratorExit

//I am writing this line.


