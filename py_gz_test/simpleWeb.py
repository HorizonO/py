from http.server import *
class RequestHandler(BaseHTTPRequestHandler):
    Page='''\
    <html>
    <body>
    <p>Hello,web!</p>
    </body>
    </html>
    '''
    def do_GET(self):
        self.send_response(200);
        self.protocol_version="HTTP/1.1"
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Length",str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))
if __name__=='__main__':
    serverAddress=('127.0.0.1',8000)
    server=HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()