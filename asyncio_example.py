import asyncio

async def clean():
    await asyncio.sleep(3)
    print("cleaning finished")
    
async def invite():
    await asyncio.sleep(2)
    print("inviting finished")
    
async def main():
    clean_task = asyncio.create_task(clean())
    invite_task = asyncio.create_task(invite())
    await clean_task
    await invite_task
    
asyncio.run(main())