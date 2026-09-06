import asyncio, requests
import aiohttp

async def get_twosecdelay(session, url):
    print(f"Start fetching data for {url.split('/')[-1]} sec...")
    async with session.get(url) as response:
        print(f"Fetching for url={url} and getting status data: ", {response.status})
        # data = await response.text()
        


async def main():
    urls=['https://httpbin.org/delay/2', 'https://httpbin.org/delay/3', 'https://httpbin.org/delay/5']
    async with aiohttp.ClientSession() as session:
        tasks = [get_twosecdelay(session, url)  for url in urls ]
        await asyncio.gather(*tasks)

    

asyncio.run(main())
    
    
    
    