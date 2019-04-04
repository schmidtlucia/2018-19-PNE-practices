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

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = "luciaschmidt"
REPOS = '/repos'
METHOD = "GET"

print()
# -- Get some data

# -- here we want to know the real name of the user & the number of repos
# we create the endpoint
endpt1 = ENDPOINT + GITHUB_ID

# we call the function and print the information given
user = json.loads(endpoint(endpt1)[0])

name = user['name']
nrepos = user['public_repos']
termcolor.cprint("Name: {}".format(name), 'cyan')
termcolor.cprint("Repos: {}".format(nrepos), 'cyan')

# -- here we want to know the names of the different repositories
# we create the endpoint
endpt2 = ENDPOINT + GITHUB_ID + REPOS

# we call the function and print the information given
user_repos = json.loads(endpoint(endpt2)[0])

# -- we create a function to print the names of the different repos
def repos(num):
    repos_name = user_repos[num]['name']
    return repos_name

num = int(nrepos)

# if the user has more than 0 repos then it should print the names of the repos
if num > 0:
    for i in range(num):
        termcolor.cprint('This are the names of the different repositories: {}'.format(repos(i)), 'magenta')
else:
    termcolor.cprint('The user has no repositories.', 'magenta')