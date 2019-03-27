# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json

PORT = 8089
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)

request = "/"
conn.request("GET", request)

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))


if request == "/":
    data1 = r1.read().decode("utf-8")
    print(data1)

elif request == "/listusers":

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Create a variable with the data,
    # -- form the JSON received

    person = json.loads(data1)

    print("CONTENT: ")

    # Print the information of all person in the data base

    termcolor.cprint("Total people in the data base: ", 'magenta', end='')
    print(len(person))

    for per in person["People"]:
        print()
        termcolor.cprint("Name: ", 'green', end="")
        print(per['Firstname'], per['Lastname'])

        termcolor.cprint("Age: ", 'green', end="")
        print(per['age'])

        # Get the phoneNumber list
        phoneNumbers = per['phoneNumber']

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

else:
    data1 = r1.read().decode("utf-8")
    print(data1)
