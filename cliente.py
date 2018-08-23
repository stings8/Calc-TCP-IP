import socket
HOST = 'localhost'
PORT = 5656

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
pedido = input("Digite a operação desejada: ")
msg = pedido.encode('utf-8')

cliente.sendto(msg, (HOST, PORT))
modifiedMessage, serverAddress = cliente.recvfrom(2048)
print(modifiedMessage.decode('utf-8'))
cliente.close()