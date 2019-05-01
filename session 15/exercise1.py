# This is Exercise 1 of the session 15

import http.server
import socketserver
import termcolor

PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):  # We are creating objects that heritates the properties of the http.server library

    def do_GET(self):

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open('form1.html', 'r')
        contents = f.read()

        # -- creating a happy server response
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('  Content-Length', len(str.encode(contents)))
        self.end_headers()

        #  create a response different from happy server
        req_line = self.requestline.split(" ")[1]
        if req_line == '/' or req_line == '/form1.html' or req_line == '/echo?msg=':
            file = open('form1.html', 'r')
            content = file.read()
        else:
            msg = req_line.partition('=')
            if msg[0] == '/echo?msg':
                file = open('form3.html', 'r')
                content = file.read()
                content = content.replace('###', msg[2])

            else:
                file = open('error-ex1.html', 'r')
                content = file.read()
        self.wfile.write(str.encode(content))

# -- MAIN PROGRAM


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:  # an empty IP adress means: 'use your own IP'
    print('Serving at PORT {}'.format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
