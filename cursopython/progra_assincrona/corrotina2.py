import asyncio

async def diz_oi_demorado():
    print('Oii...')
    await asyncio.sleep(2) # utilizar await sempre que for executar uma função assincrona  
    print('todos...')

el = asyncio.get_event_loop()
el.run_until_complete(diz_oi_demorado())
el.close()