import socket

ip = input("Digite o endereço IP: ")
port = int(input("Digite a porta a ser verificada: "))

# Cria um objeto socket para se conectar ao servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(1)

try:
    s.connect((ip, port))
     
    s.send(b"GET / HTTP/1.1\r\n\r\n")
    
    banner = s.recv(1024)
    
    print("Banner encontrado: ")
    print(banner.decode().strip())
    
    s.close()
    
except socket.timeout:
    print("Erro: tempo de conexão esgotado")
    
except ConnectionRefusedError:
    print("Erro: conexão recusada")
