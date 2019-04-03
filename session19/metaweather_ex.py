# Example of accessing to the Chuck Norris Database service for getting an URL
# of a random joke of Chuck Norris. This clients just print it on the console
import http.client
import json
import termcolor

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
# -- we are making a loop, so that the program doesn't stop asking for cities

while True:

    # -- API information
    HOSTNAME = "www.metaweather.com"
    ENDPOINT = "/api/location/"
    SEARCH = 'search/?query='
    city = str(input('\n\nPlease enter here the name of a capital: '))
    METHOD = "GET"


    # -- this will be the argument for the function above for searching the woeid of the entered city
    get_woeid = ENDPOINT+SEARCH+city

    # -- this is the information we get by searching a city
    r1 = json.loads(endpoint(get_woeid)[0])

    # -- we have to be sure that the city entered is actually in our data base
    if r1 != []:

        # -- out of that information we take the value for the woeid of the searched city
        LOCATION_WOEID = str(r1[0]['woeid'])

        # -- this will be the argument for the function above for searching the weather information
        get_weather = ENDPOINT + LOCATION_WOEID + '/'
        termcolor.cprint('\nThis is the weather information for {}, with woeid {}:'.format(r1[0]['title'], r1[0]['woeid']), 'blue')

        # -- this is ALL the information ABOUT the given woeid/city
        r2 = json.loads(endpoint(get_weather)[0])

        # -- now we only want to know the current time, the temperature and the sunset time of that city
        time = r2['time']
        temp = r2['consolidated_weather'][0]['the_temp']
        sunset = r2['sun_set']

        termcolor.cprint('  Current time: {}'.format(time[11:19]), 'red')
        termcolor.cprint('  Current temperature: {} ºC'.format(temp), 'red')
        termcolor.cprint('  Sunset time: {}'.format(sunset[11:19]), 'red')

    else:

        # -- print error message
        termcolor.cprint('\nThe city entered was not found in our data base', 'red')
