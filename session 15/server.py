import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):  # We are creating objects that heritates the properties of the http.server library

    def do_GET(self):

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open('form2.html', 'r')
        contents = f.read()

        # -- creating a happy server response
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('  Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- sending the body of the response message
        self.wfile.write(str.encode(contents))


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
