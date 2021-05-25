import socket
import codecs
target_host = "www.google.com" 
filepath = "dane.txt"
f = open(filepath, "w")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect((target_host,80))   
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
s.send(request.encode())  
response = s.recv(4096)  
http_response = codecs.decode(response)
print(http_response)
f.write(http_response)
f.close
