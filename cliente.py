import asyncio
import websockets

async def escutar_servidor(websocket):
    #Fica ouvindo a rede em segundo plano e imprimindo as mensagens.
    try:
        while True:
            mensagem = await websocket.recv()
            # O \n antes ajuda a limpar a linha caso a mensagem chegue enquanto o usuários está digitando
            print(f"\n[Nova Mensagem]: {mensagem}")
    except websockets.exceptions.ConnectionClosed:
        print("\nConexão com o servidor foi encerrada.")

async def escrever_mensagens(websocket):
    #Fica pedindo input do usuário e enviando para o servidor.
    while True:
        # Usamos to_thread para liberar o Event Loop enquanto o terminal espera a digitação do usuário, evitando que o cliente trave e perca mensagens do servidor.
        mensagem = await asyncio.to_thread(input, "")
        
        # Envia a mensagem apenas se o usuário não digitou um texto vazio
        if mensagem.strip():
            await websocket.send(mensagem)

async def main():
    uri = "ws://localhost:8765"
    print(f"Tentando conectar em {uri}...")
    
    try:
        # Estabelece a conexão com o servidor
        async with websockets.connect(uri) as websocket:
            print("Conectado com sucesso! Digite sua mensagem e aperte Enter.\n")
            
            # Coloca a função de escutar rodando no Event Loop em uma "esteira paralela"
            asyncio.create_task(escutar_servidor(websocket))
            
            # Trava o fluxo principal aqui, no loop infinito de pedir digitação
            await escrever_mensagens(websocket)
            
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar. Verifique se o servidor está rodando.")

# Dá a partida no script do cliente
asyncio.run(main())