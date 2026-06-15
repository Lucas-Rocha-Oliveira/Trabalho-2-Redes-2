"""
Exercício 4 -Exercício 4: Servidor de Hora com Threads (TCP)
Lucas Rocha Oliveira
Luiz Felipe Melo Oliveira
Luiz Guilherme Oliveira Pires
Otávio Gomes Calazans"""


import socket
import threading
import datetime 

def atender_cliente(socket_cliente, endereco_cliente):
    print("\n===================================")
    print(f"Cliente conectado: {endereco_cliente}")
    print(f"Thread iniciada para {endereco_cliente}")
    
    try:
        socket_cliente.recv(1024).decode() #Recebe a mensagem do cliente e decodifica para string
        print(f"Solicitação de horário recebida de {endereco_cliente}")
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
        socket_cliente.send(hora_atual.encode()) #Envia a hora atual codificada para o cliente
        print(f"Solicitação atendida para {endereco_cliente}")
    except socket.error as e:
        print(f"Erro de comunicação com o cliente {endereco_cliente}: {e}")
    finally:        
        socket_cliente.close() #Fecha a conexão com o cliente
        print(f"Cliente desconectado: {endereco_cliente}")
        print(f"Thread finalizada para {endereco_cliente}")
        print("===================================\n\n")



servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um socket TCP/IP com IPv4

try:
    servidor_socket.bind(("127.0.0.1", 7000)) #Vincula o socket a um endereço IP e porta específicos"
    servidor_socket.listen(5) #O servidor começa a escutar por conexões, permitindo até 5 conexões pendentes
    print("Servidor esperando conexões...")

    while True:
        socket_cliente, endereco_cliente = servidor_socket.accept() #Aceita uma conexão entrante, bloqueando até que um cliente se conecte. Retorna um novo socket para comunicação com o cliente e o endereço do cliente
        thread = threading.Thread(
            target=atender_cliente,
            args=(socket_cliente, endereco_cliente)
        )
        thread.start() #Inicia a thread para atender o cliente

except KeyboardInterrupt:
    print("\nServidor encerrado.")

except socket.error as e:

    print(f"Erro de comunicação na rede: {e}")

finally:
    servidor_socket.close() #Fecha a conexão com o servidor
