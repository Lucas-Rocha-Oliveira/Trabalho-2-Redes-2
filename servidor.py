import asyncio
import websockets

#Variável global para guardar os clientes conectados
clientes_conectados = set()


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
    # Isso cria o servidor na porta 8765 na máquina local (localhost)
    async with websockets.serve(recepcionista, "localhost", 8765):
        print("Servidor de Chat rodando na porta 8765...")
        await asyncio.Future() # Mantém o servidor rodando para sempre

# Chave de ignição do código assíncrono
asyncio.run(main())