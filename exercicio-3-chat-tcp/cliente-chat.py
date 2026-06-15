"""
Exercício 3 - chat TCP: Cliente
Grupo:
Lucas Rocha Oliveira
Luiz Felipe Melo Oliveira
Luiz Guilherme Oliveira Pires
Otávio Gomes Calazans"""

import socket
import threading

host = input("Digite o ip do servidor: ")
porta = 7005

def recebe_mensagens(cliente_soc):
  try:
    while True:
      msg = cliente_soc.recv(1024)
      if not msg:
        print("Ligação fechada pelo outro usuário ou servidor.")
        break
      
      mensagem = msg.decode('utf-8')
      print(f"Outro usuário: {mensagem}")

  except Exception:
    pass

#Inicializa o cliente
def ligar_cliente_chat():
  #Criação de um socket IPv4(AF_INET) e TCP(SOCK_STREAM)
  cliente_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    cliente_soc.connect((host, porta))

    #Recebimento em paralelo com uso das threads.
    thread_receber = threading.Thread(target=recebe_mensagens, args=(cliente_soc,), daemon=True)
    thread_receber.start()

    print("Converse pelo chat com o outro usuário. Se quiser encerrar, digite 'sair'.\n")

    #Envio das mensagens
    while True:
      #Thread em pausa, a espera do teclado.
      mensagem = input("")

      #Caso mensagem vazia, loop reinicia e continua aguardando.
      if not mensagem.strip():
        continue

      #"sair" para encerrar conexão
      if mensagem.lower() == 'sair':
        break
          
      #Envio da mensagem
      cliente_soc.sendall(mensagem.encode('utf-8'))

  except ConnectionRefusedError:
    print("Servidor está desligado.")
  finally:
    cliente_soc.close()
    print("\nVocê saiu do chat.")

if __name__ == "__main__":
  ligar_cliente_chat()