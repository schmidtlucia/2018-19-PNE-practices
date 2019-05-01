# This is Exercise 2 of the session 15

import http.server
import socketserver
import termcolor

PORT = 8081


class TestHandler(http.server.BaseHTTPRequestHandler):  # We are creating objects that heritates the properties of the http.server library

    def do_GET(self):

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open('form4.html', 'r')
        contents = f.read()

        # -- creating a happy server response
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('  Content-Length', len(str.encode(contents)))
        self.end_headers()

        #  create a response different from happy server
        req_line = self.requestline.split(" ")[1]
        if req_line == '/' or req_line == '/form4.html' or req_line == '/echo?msg=':
            file = open('form4.html', 'r')
            content = file.read()
        else:
            msg = req_line.split('=')
            if msg[0] == '/echo?msg':
                file = open('form5.html', 'r')
                content = file.read()
                final_msg = msg[1]
                if final_msg[-4:] == '&chk':
                    final_msg = final_msg.replace('&chk', '').upper()
                content = content.replace('###', final_msg)

            else:
                file = open('error-ex2.html', 'r')
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
