import json
import termcolor

f = open("person.json", "r")

person = json.load(f)  # this function will analyze, read and create the variable person with the information we have in the file

print()

termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end='')
print(person['age'])

for i, num in enumerate(person['phoneNumber']):
    termcolor.cprint(" Phone {}: ".format(i), 'blue')

    termcolor.cprint("      Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("      Number: ", 'red', end='')
    print(num['number'])
