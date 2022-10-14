import socket
import threading

def do(conn):
    conn.sendall(bytes(response_success(), encoding="utf-8"))
    pass
def response_success():
    return "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{result:success}\r\n"



max_connection = 5
port = 5800
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', port))
sock.listen(max_connection)
print("Server is listening port %s , with max connection %s" % (port, max_connection))
while True:
    connection, address = sock.accept()
    threading.Thread(target=do,args=[connection,]).start()