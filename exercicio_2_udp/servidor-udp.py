"""
Exercício 2 - UDP: Servidor
Lucas Rocha Oliveira
Luiz Felipe Melo Oliveira
Luiz Guilherme Oliveira Pires
Otávio Gomes Calazans"""

import socket
import os

host = '0.0.0.0'
porta = 6005

#Criação de um socket IPv4(AF_INET) e UDP(SOCK_DGRAM)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Garantia que a porta posso ser reutilizada imediatamente após reinicio do servidor.
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Inicializa o servidor
servidor.bind((host, porta))

#capturando ip da máquina, para cliente inserir
ip_real = os.popen('hostname -I').read().split()[0]

print(f"Servidor inicializado no ip: {ip_real}\n")

try:
  while True:
    msg, endereco_cliente = servidor.recvfrom(65535)
    mensagem = msg.decode('utf-8')

    #Imprimir a mensagem recebida
    print(f"Mensagem de {endereco_cliente} recebida: {mensagem}\n")

    #Eco da mensagem
    servidor.sendto(msg, endereco_cliente)
  
except KeyboardInterrupt:
  pass
#Quando finaliza 
finally:
  servidor.close()