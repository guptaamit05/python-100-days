
import asyncio


async def prepare_tea():
    
    print("Making your tea...")
    await asyncio.sleep(3)
    print("Tea is ready...")
    


asyncio.run(prepare_tea())


print("okay lets run other code")