# This is the web server of Practice 6

import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8000


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
        if req_line == '/' or req_line == '/form1.html':
            file = open('form1.html', 'r')
            content = file.read()
        else:
            path = req_line.partition('?')[2]
            options = path.split('&')
            msg = Seq(options[0][4:])
            mensaje = str(options[0][4:])
            if mensaje.strip('ACGT') == '':
                if options[1] == 'chk=on':
                    length = msg.len()
                    base = str(options[2][5:])
                    operation = options[3]
                    if operation == 'operation=count':
                        operation = msg.count(base)
                    else:
                        operation = msg.perc(base)

                    file = open('form2.html', 'r')
                    content = file.read()
                    content = content.replace('----',mensaje).replace('--', str(length)).replace('-', base).replace('%', str(operation))
                else:
                    base = str(options[1][5:])
                    operation = options[2]
                    if operation == 'operation=count':
                        operation = msg.count(base)
                    else:
                        operation = msg.perc(base)

                    file = open('form2.html', 'r')
                    content = file.read()
                    content = content.replace('----', mensaje).replace('--', 'not asked').replace('-', base).replace('%', str(operation))
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
