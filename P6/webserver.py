# This is the web server of Practice 6

import http.server
import socketserver
import termcolor
import Seq

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
            msg = options[0]
            if options[1][:3] == 'chk':
                chk = options[1]
                base = options[2]
                operation = options[3]
                file = open('form2.html', 'r')
                content = file.read()
                content = content.replace('---', msg[4:]).replace('--', chk).replace('-', base[5:]).replace('%', operation[10:])
            else:
                base = options[1]
                operation = options[2]
                file = open('form2.html', 'r')
                content = file.read()
                content = content.replace('---', msg[4:]).replace('--', 'not asked').replace('-', base[5:]).replace('%', operation[10:])

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
