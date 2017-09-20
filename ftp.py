from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/pi/ftp", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.1.163", 2123), handler)
server.serve_forever()
