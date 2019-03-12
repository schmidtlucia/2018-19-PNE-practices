# This is Exercise 1 of the session 15

import http.server
import socketserver
import termcolor

PORT = 8089


class TestHandler(http.server.BaseHTTPRequestHandler):  # We are creating objects that heritates the properties of the http.server library

    def do_GET(self):

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open('form-server1.html', 'r')
        contents = f.read()

        # -- creating a happy server response
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('  Content-Length', len(str.encode(contents)))
        self.end_headers()

        #  create a response different from happy server
        req_line = self.requestline.split(" ")[1]
        if req_line != '':
            if req_line == '/':
                file = open('form-server1.html', 'r')
                content = file.read()
            elif req_line == '/form-server1.html':
                file = open('form-server1.html', 'r')
                content = file.read()
            elif req_line == '/echo?msg=':
                file = open('form-server1.html', 'r')
                content = file.read()
            else:
                msg = req_line.partition('=')
                if msg[0] == '/echo?msg':
                    file = open('form3.html', 'r')
                    content = file.read()
                else:
                    file = open('error.html', 'r')
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
