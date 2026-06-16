"""
Exercício 1 - TCP: Servidor
Lucas Rocha Oliveira
Luiz Felipe Melo Oliveira
Luiz Guilherme Oliveira Pires
Otávio Gomes Calazans"""

import socket
import threading
import os

host = '0.0.0.0'
porta = 5005

def atender_cliente(conn, endereco):
  try:
    print(f"Cliente {endereco} conectado.")
    #Loop para recebimento de mensagem até encerrar.
    while True:
      #Recebe a mensagem
      msg = conn.recv(1024)

      #Cliente encerrou conexão
      if not msg:
        break

      mensagem = msg.decode('utf-8')
      print(f"Mensagem de cliente: {endereco}: {mensagem}")

      resposta = "Mensagem recebida com sucesso!"
      #Envia uma confirmação (ACK) para o cliente
      conn.sendall(resposta.encode('utf-8'))

  finally:
    #Encerra conexão
    conn.close()
    print(f"Conexão encerrada pelo cliente: {endereco}")

def ligar_servidor():
  #Criação de um socket IPv4(AF_INET) e TCP(SOCK_STREAM)
  servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #Garantia que a porta posso ser reutilizada imediatamente após reinicio do servidor.
  servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  #Vincula o socket ao endereço
  servidor.bind((host, porta))

  #servidor fica esperando requisição
  servidor.listen()

  #capturando ip da máquina, para cliente inserir
  ip_real = os.popen('hostname -I').read().split()[0]

  print(f"Servidor iniciado no ip:{ip_real}, aguardando requisição.\n")

  try:
    while True:
      #Estabelece conexão com socket que está aguardando.
      conn, endereco = servidor.accept()

      #Uso de threads para receber múltiplos clientes.
      thread = threading.Thread(target=atender_cliente, args=(conn, endereco), daemon=True)
      thread.start()
  
  except KeyboardInterrupt:
    pass
  #Quando finaliza 
  finally:
    servidor.close()

if __name__ == "__main__":
  ligar_servidor()