# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json

PORT = 8900
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")
print(data1)

# -- Create a variable with the data,
# -- form the JSON received
people = json.loads(data1)

print("CONTENT: ")

# Print the information of all person in the data base

termcolor.cprint("Total people in the data base: ", 'magenta', end='')
print(len(people))

for per in people:
    print()
    per = str(per)
    people = (people[per][0])
    print(people)
    termcolor.cprint("Name: ", 'green', end="")
    print(people['Firstname'], people['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(people['age'])

    # Get the phoneNumber list
    phoneNumbers = people['phoneNumber']

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])

