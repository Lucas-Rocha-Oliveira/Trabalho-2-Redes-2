"""
Exercício 1 - TCP: Cliente
Lucas Rocha Oliveira
Luiz Felipe Melo Oliveira
Luiz Guilherme Oliveira Pires
Otávio Gomes Calazans"""

import socket

host = input("Digite o ip do servidor: ")
porta = 5005

#Criação de um socket IPv4(AF_INET) e TCP(SOCK_STREAM)
cliente_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  #conectar cliente ao servidor
  cliente_soc.connect((host, porta))

  #Envia mensagem até sair.
  print("Pronto para o envio de mensagens. 'sair' para encerrar.")
  while True:
    mensagem = input("Envie uma mensagem para o servidor: ")
    
    while not mensagem.strip():
      print("Mensagem vazia!\n")
      mensagem = input("Envie uma mensagem para o servidor: ")

    #Saída manual do Usuário
    if mensagem.lower() == "sair":
      break

    #Envia a mensagem para o servidor.
    cliente_soc.sendall(mensagem.encode('utf-8'))

    #Resposta do servidor
    resposta = cliente_soc.recv(1024)
    print(f"Resposta: {resposta.decode('utf-8')}")

finally:
  #Encerra conexão
  cliente_soc.close()