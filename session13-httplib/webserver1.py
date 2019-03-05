import http.server
import socketserver

PORT = 8001

# a Handler is a class. We call it whenever there is a request from a client

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("     Cmd: "+self.command)
        print("     Path: "+self.path)

        # Create a message, in this case, the happy server
        content = "I am the happy server! :-)"

        #  special code 200 means that everything is okay
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:  # with no content in between "", that means that we use our own
    print('Serving at PORT', PORT)

    httpd.serve_forever()
