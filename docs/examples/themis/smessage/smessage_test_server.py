#echo server on handmade secure socket (see smessage_socket.py)

import smessage_ssocket;
import socket;

client_pub = str('\x55\x45\x43\x32\x00\x00\x00\x2d\x13\x8b\xdf\x0c\x02\x1f\x09\x88\x39\xd9\x73\x3a\x84\x8f\xa8\x50\xd9\x2b\xed\x3d\x38\xcf\x1d\xd0\xce\xf4\xae\xdb\xcf\xaf\xcb\x6b\xa5\x4a\x08\x11\x21');

server_priv= str('\x52\x45\x43\x32\x00\x00\x00\x2d\x49\x87\x04\x6b\x00\xf2\x06\x07\x7d\xc7\x1c\x59\xa1\x8f\x39\xfc\x94\x81\x3f\x9e\xc5\xba\x70\x6f\x93\x08\x8d\xe3\x85\x82\x5b\xf8\x3f\xc6\x9f\x0b\xdf');

conn=smessage_ssocket.ssocket(priv_key=server_priv);
conn.bind(("127.0.0.1", 26260));
conn.listen(1);
accepted, addr = conn.accept();

accepted.set_peer_pub_key(client_pub);

while True:
    try:
        message = accepted.recv(1024); #receive message
        print message;
        if message == "finish": #"finish" - last message
            break;
        accepted.sendall(message); #send message
    except Exception as e:
        e;        
conn.close();
