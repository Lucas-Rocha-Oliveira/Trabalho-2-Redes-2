import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente_socket.connect(("127.0.0.1", 7000)) #Conecta ao servidor na porta 7000 do localhost
    cliente_socket.send(b"Hora")
    resposta = cliente_socket.recv(1024).decode() #Recebe a resposta do servidor
    print(f"Resposta do servidor: {resposta}")

except socket.error as e:
    print(f"Erro de comunicação: {e}")

finally:
    cliente_socket.close() #Fecha a conexão com o servidor