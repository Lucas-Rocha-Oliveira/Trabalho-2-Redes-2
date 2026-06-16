"""
Exercício 2 - UDP: Cliente
Grupo:
Lucas Rocha Oliveira
Luiz Felipe Melo Oliveira
Luiz Guilherme Oliveira Pires
Otávio Gomes Calazans"""

import socket
import sys

host = input("Digite o ip do servidor: ")
porta = 6005

#Tamanho máximo da mensagem permitido pelo UDP
TAM_MAX_MSG = 65507

#Criação de um socket IPv4(AF_INET) e UDP(SOCK_DGRAM)
cliente_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Tratamenteo de erro para perda de pacote. (Caso 2 segundos sem receber nada)
cliente_soc.settimeout(2.0)

print("Cliente pronto para enviar mensagens.\n")
print("Digite 'sair' para encerrar.\n")
try:
  while True:
    mensagem = input("Envie uma mensagem para o servidor: ")
    msg = mensagem.encode('utf-8')

    while not mensagem.strip():
      print("Mensagem vazia!\n")
      mensagem = input("Envie uma mensagem para o servidor: ")

    #Saída manual do Usuário
    if mensagem.lower() == "sair":
      break

    tamanho_msg = len(msg)

    if tamanho_msg > TAM_MAX_MSG:
      print(f"[ERRO] Mensagem muito grande! Tamanho: {tamanho_msg} bytes.")
      print(f"O limite máximo permitido é de {TAM_MAX_MSG} bytes.")
      continue

    try:
      #Envio da mensagem para o servidor
      cliente_soc.sendto(msg, (host, porta))

      #Aguarda o recebimento do ECO
      msg_eco, endereco_cliente_eco = cliente_soc.recvfrom(65535)
      print(f"Mensagem envia pelo cliente: {endereco_cliente_eco} ecoada do servidor: {msg_eco.decode('utf-8')}")

    except socket.timeout:
      #Perda de pacote ou servidor desligado.
      print("Tempo limite excedido! O pacote foi perdido ou o servidor está offline.")

    except ConnectionResetError:
      #Servidor desligado
      print("Servidor offline! O sistema recusou a entrega do pacote.")

except KeyboardInterrupt:
  pass
finally:
  cliente_soc.close()
  print("\nCliente udp Encerrado.")