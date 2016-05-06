import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import time
import netifaces as nif

class DoorHW():

    def __init__(self):
        pass

    def open(self):
        return True

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def __init__(self,request, client_address, server):
        self.door = DoorHW()
        self.client_add = client_address
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)
        

    def do_GET(self):
        path = self.path
        resp = ''
	
	#print self.ip2mac(self.client_add)
        #print dir(self)
        if path == '/ON':
            resp = "DoorOpened by " + str(self.client_add)
            self.door.open() 
        else:
            resp = "NADA"
        self.send_response(200)         
        self.send_header("Content-type",'text/plain')
        self.send_header("Content-Length",len(resp))
        self.end_headers()
        self.wfile.write(resp)

    def do_POST(self):
        self.do_GET()

    def ip2mac(self,ip):
	for i in nif.interfaces():
	    addrs = nif.ifaddresses(i)
	    try:
		if_mac = addrs[nif.AF_LINK][0]['addr']
		if_ip = addrs[nif.AF_INET][0]['addr']
	    except IndexError, KeyError:
		if_mac = if_ip = None
	    if if_ip == ip:
		return if_mac

	return None


if __name__ == '__main__':
    PORT = 8000

    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    try:
        httpd = SocketServer.TCPServer(("192.168.0.12", PORT), Handler)
        print "serving at port", PORT
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.shutdown()
        httpd.server_close()
