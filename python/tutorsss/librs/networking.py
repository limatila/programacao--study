import socket #is a program to connect peer-to-peer, stablishing a two-part simoutaneous connection
import os

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #config padrão
mysock.connect(('data.pr4e.org', 80)) #connected to server

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() 
mysock.send(cmd) #connect to file address

while True:
    data = mysock.recv(512) #stablishing receiver for the file
    if len(data) < 1: #if i received the package, stop receiving.
        break
    print(type(data))
    print(data.decode())
    print(type(data))
mysock.close()

#text processing:
import urllib.request, urllib.parse, urllib.error 
filehandler = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Nuclear_fission.svg/309px-Nuclear_fission.svg.png')#request connection and open it
print(type(filehandler))
for line in filehandler:
    print(line.decode().strip()) #decode only text
