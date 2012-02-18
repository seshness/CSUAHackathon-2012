import socket, ssl

bindsocket = socket.socket()
bindsocket.bind(('0.0.0.0', 443))
bindsocket.listen(5)

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile="sesh-ca-cert.crt",
                                 keyfile="sesh-ca-private.key",
                                 ssl_version=ssl.PROTOCOL_TLSv1,
                                 suppress_ragged_eofs=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()

def deal_with_client(connstream):
    data = connstream.read()
    # null data means the client is finished with us
    while data:
        if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            break
        data = connstream.read()
    # finished with client

def do_something(connstream, data):
    print connstream, data
