import asyncio
import time

# Usamos 'async def' para transformar a função em uma corrotina
async def fritar_carne():
    print("1. Colocou a carne na chapa...")
    # O 'await asyncio.sleep' simula uma operação de rede demorada.
    # É aqui que o Python PAUSA esta função e vai fazer outra coisa.
    await asyncio.sleep(3) 
    print("4. Carne está pronta!")

async def fritar_batata():
    print("2. Colocou a batata na fritadeira...")
    await asyncio.sleep(1) # Demora menos tempo que a carne
    print("3. Batata está pronta!")

async def cozinhar():
    inicio = time.time()
    
    # O asyncio.gather executa várias corrotinas ao mesmo tempo
    # e o 'await' aguarda até que todas terminem.
    await asyncio.gather(
        fritar_carne(),
        fritar_batata()
    )
    
    fim = time.time()
    print(f"\nTempo total: {fim - inicio:.1f} segundos")

# Para rodar um código assíncrono, precisamos iniciar o Event Loop
asyncio.run(cozinhar())