import socket

def soma(a, b):
    c = float(a) + float(b)
    return str(c)

def subtracao(a, b):
    c = float(a) - float(b)
    return str(c)

def multiplica(a, b):
    c = float(a) * float(b)
    return str(c)


def calculadora(operacao):
    operador = operacao.decode('utf-8').split()
    print(operador)
    if operador[1] == '+':
        if operador[0].isnumeric() and operador[2].isnumeric():
            return soma(operador[0], operador[2])
        else:
            erro = 'Os valores passados não são numéricos.'
            return erro
    elif operador[1] == '-':
        if operador[0].isnumeric():
            return subtracao(operador[0], operador[2])
        else:
            erro = 'Os valores passados não são numéricos.'
            return erro
    elif operador[1] == '*':
        if operador[0].isnumeric():
            return multiplica(operador[0], operador[2])
        else:
            erro = 'Os valores passados não são numéricos.'
            return erro
    else:
        erro = 'operacao invalida'
        return erro


HOST = 'localhost'
PORT = 5656

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn: 
        print('conectado a', addr)
        while True:
            data = conn.recv(1024)
            resp = calculadora(data)
            print("\n", resp)
            conn.send(resp.encode())





