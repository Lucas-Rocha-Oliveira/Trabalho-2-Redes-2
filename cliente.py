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

async def escrever_mensagens(websocket, nome_usuario):
    #Fica pedindo input do usuário e enviando para o servidor.
    while True:
        # Usamos to_thread para liberar o Event Loop enquanto o terminal espera a digitação do usuário
        mensagem = await asyncio.to_thread(input, "")
        
        # Envia a mensagem apenas se o usuário não digitou um texto vazio
        if mensagem.strip():
            # Junta o nome do usuário com a mensagem que ele digitou
            mensagem_formatada = f"{nome_usuario}: {mensagem}"
            await websocket.send(mensagem_formatada)

async def main():
    # Pede o nome do usuário antes de conectar
    nome_usuario = input("Digite seu nome para o chat: ")
    if not nome_usuario.strip():
        nome_usuario = "Anônimo"

    # Pede o IP antes de tentar conectar
    ip_servidor = input("Digite o IP do servidor (ou aperte Enter para localhost): ")
    
    # Se o usuário não digitar nada, usa localhost por padrão
    if not ip_servidor.strip():
        ip_servidor = "localhost"
        
    # Monta a URI com o IP digitado, mantendo a porta 8765
    uri = f"ws://{ip_servidor}:8765"
    print(f"\nTentando conectar em {uri}...")
    
    try:
        # Estabelece a conexão com o servidor
        async with websockets.connect(uri) as websocket:
            print(f"Conectado com sucesso! Bem-vindo(a), {nome_usuario}. Digite sua mensagem e aperte Enter.\n")
            
            # Coloca a função de escutar rodando no Event Loop em uma "esteira paralela"
            asyncio.create_task(escutar_servidor(websocket))
            
            # Trava o fluxo principal aqui, no loop infinito de pedir digitação, passando o nome junto
            await escrever_mensagens(websocket, nome_usuario)
            
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar. Verifique se o servidor está rodando.")

# Dá a partida no script do cliente
asyncio.run(main())