"""
Exercício 3 - chat TCP: Servidor
Grupo:
Lucas Rocha Oliveira
Luiz Felipe Melo Oliveira
Luiz Guilherme Oliveira Pires
Otávio Gomes Calazans"""

import socket
import threading
import os

host = '0.0.0.0'
porta = 7005

def retransmitir(user_remetente, user_destinatario):
  try:
    while True:
      msg = user_remetente.recv(1024)
      if not msg: break

      user_destinatario.sendall(msg)
    
  except Exception:
    pass
  finally:
    #Quando os dois encerram a conexão. A conexão é finalizada.
    user_remetente.close()
    user_destinatario.close()
    print("Uma conexão foi encerrada.")

def ligar_servidor_chat():
  #Criação de um socket IPv4(AF_INET) e TCP(SOCK_STREAM)
  servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #Garantia que a porta posso ser reutilizada imediatamente após reinicio do servidor.
  servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  #Vicula o endereço ao socket
  servidor.bind((host, porta))

  #Servidor fica aguardando por requisições de 2 clientes.
  servidor.listen(2)

  #capturando ip da máquina, para cliente inserir
  ip_real = os.popen('hostname -I').read().split()[0]

  print(f"Servidor de chat inicializado no ip: {ip_real}.")

  #Aguarda conexão do primeiro usuário
  conn1, endereco1 = servidor.accept()
  print(f"Usuário 1 conectado: {endereco1}")
  conn1.sendall("Aguardando o segundo usuário entrar...\n".encode('utf-8'))

  #Aguarda conexão do segundo usuário
  conn2, endereco2 = servidor.accept()
  print(f"Usuário 2 conectado: {endereco2}")

  conn1.sendall("Ambos usuários conectados. Chat iniciado!\n".encode('utf-8'))
  conn2.sendall("Ambos usuários conectados. Chat iniciado!\n".encode('utf-8'))

  #Criação de duas threads para o full-duplex
  t1 = threading.Thread(target=retransmitir, args=(conn1, conn2), daemon=True)
  t2 = threading.Thread(target=retransmitir, args=(conn2, conn1), daemon=True)

  t1.start()
  t2.start()

  #Pausa a thread e espera ela terminar.
  t1.join()
  t2.join()

  servidor.close()
  print("Servidor encerrado.")

if __name__ == '__main__':
  ligar_servidor_chat()