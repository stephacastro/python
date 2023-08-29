import asyncio

# async transforma a função em uma corrotina (prog assincrona)

# função assincrona
async def diz_oi():
    print('Oii...')

el = asyncio.get_event_loop() # criando o event loop
el.run_until_complete(diz_oi()) # passando que se sera executado e a função
el.close() # fechando a conexao 