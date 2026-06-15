import asyncio
import websockets
import socket

#Variável global para guardar os clientes conectados
clientes_conectados = set()

def obter_ip_local():
    """Descobre o IP principal da máquina na rede atual."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Tenta simular uma rota externa para descobrir qual placa de rede está ativa
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        # Se estiver sem internet nenhuma, cai pro localhost
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

# A função 'recepcionista' é a responsável por lidar com cada cliente que se conecta ao servidor. Ela é chamada toda vez que um novo cliente entra.
async def recepcionista(websocket):
    # Quando um cliente entra, adicionamos ele ao conjunto
    clientes_conectados.add(websocket)
    print(f"Novo usuário conectado! Total: {len(clientes_conectados)}")
    
    try:
        # Criamos um loop infinito para este cliente específico
        while True:
            # O 'await' aqui é reponssável por fazer o servidor esperar por uma mensagem do cliente, sem travar o resto do servidor"
            mensagem = await websocket.recv()
            
            print(f"Mensagem recebida: {mensagem}")
            
            # Agora, queremos enviar essa mensagem para todos os outros clientes conectados
            for cliente in clientes_conectados:
                await cliente.send(mensagem)
                
    except websockets.exceptions.ConnectionClosed:
        # Se o usuário fechar a janela ou cair, o Python joga ele aqui
        print("Usuário desconectado.")
    finally:
        # Remove o cliente do conjunto quando ele sair, para não tentar enviar mensagens para ele no futuro
        clientes_conectados.remove(websocket)
        print(f"Usuário removido. Restam: {len(clientes_conectados)}")

#Inicializar o servidor principal
async def main():
    # Chama a função para descobrir o IP antes de subir o servidor
    meu_ip = obter_ip_local()
    
    # Isso cria o servidor na porta 8765 ouvindo em todas as redes (0.0.0.0)
    async with websockets.serve(recepcionista, "0.0.0.0", 8765):
        print(f"Servidor de Chat rodando!")
        print(f"-> Para conectar na mesma máquina, aperte Enter no cliente.")
        print(f"-> Para conectar de outro computador, digite este IP: {meu_ip}")
        
        await asyncio.Future() # Mantém o servidor rodando para sempre

# Chave de ignição do código assíncrono
asyncio.run(main())