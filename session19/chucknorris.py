# Example of accessing to the Chuck Norris Database service for getting an URL
# of a random joke of Chuck Norris. This clients just print it on the console
import http.client
import json
import termcolor

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT1 = "/jokes/count"
ENDPOINT2 = "/categories"
ENDPOINT3 = "/jokes/random"
METHOD = "GET"

# -- create a function to simplify the coding
def endpoint(enpt):

    """ This is a function to get the information asked when using different endpoints. We recieve a tuple with first
     the information given by the endpoint ans second the status line of the connection."""

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection! If we do not specify the port, the standard one will be used
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, enpt, None, headers)
    r1 = conn.getresponse()
    text_json = r1.read().decode("utf-8")

    # -- print status line
    status = "\nResponse received: {}{}".format(r1.status, r1.reason)
    conn.close()

    return text_json, status

# -- MAIN PROGRAM --

# -- Here we print it the information calling the function with the different endpoints
termcolor.cprint(endpoint(ENDPOINT1)[1], 'green')
num = json.loads(endpoint(ENDPOINT1)[0])
termcolor.cprint('The number of total jokes about Chuck Norris is: {}'.format(num['value']), 'red')

termcolor.cprint(endpoint(ENDPOINT2)[1], 'green')
cat = json.loads(endpoint(ENDPOINT2)[0])
termcolor.cprint('The number and names of the different categories is: {}, {}'.format(len(cat['value']), cat['value']), 'red')

termcolor.cprint(endpoint(ENDPOINT3)[1], 'green')
joke = json.loads(endpoint(ENDPOINT3)[0])
termcolor.cprint('This is a random joke about Chuck Norris: {}'.format(joke['value']['joke']), 'red')
