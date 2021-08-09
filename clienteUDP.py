import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso!")

host = 'localhost'
port = 5433

mensagem = "Olá servidor, beleza??"

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('A informação recebida é: Cliente: ' + dados)

finally:
        print("Cliente fechando a conexão!")
        s.close()
