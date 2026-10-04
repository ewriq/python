from http.server import HTTPServer, BaseHTTPRequestHandler

port = 3000

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        self.wfile.write(b"hello mf")

server = HTTPServer(("localhost", port), Server)

print("http://localhost:" + str(port))

server.serve_forever()