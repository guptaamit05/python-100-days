import asyncio


async def brew_tea(name):
    print(f"Preparing your: {name}")
    await asyncio.sleep(3)
    print(f"Here is you favorite {name} tea. Have a nice day..")
    
    
async def coffee_make(name):
    print(f"Preparing your Coffee: {name}")
    await asyncio.sleep(2)
    print(f"Here is you favorite Coffee: {name} tea. Have a nice day..")
    
    
async def main():
    await asyncio.gather(brew_tea("Masala Wali"), coffee_make("Capaciiteoe"))
    

asyncio.run(main())