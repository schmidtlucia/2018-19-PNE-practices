import http.server
import socketserver

PORT = 8006

# a Handler is a class. We call it whenever there is a request from a client

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("     Cmd: "+self.command)
        print("     Path: "+self.path)

        req_line = self.requestline.split(" ")
        if req_line[1] == '/':
            file = open('index.html', 'r')
            content = file.read()
            file.close()
        elif req_line[1] == '/pink.html':
            file = open('pink.html', 'r')
            content = file.read()
            file.close()
        elif req_line[1] == '/blue.html':
            file = open('blue.html', 'r')
            content = file.read()
            file.close()
        elif req_line[1] == '/green.html':
            file = open('green.html', 'r')
            content = file.read()
            file.close()
        else:
            file = open('error.html', 'r')
            content = file.read()
            file.close()


        #  special code 200 means that everything is okay
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:  # with no content in between "", that means that we use our own
    print('Serving at PORT', PORT)

    httpd.serve_forever()
