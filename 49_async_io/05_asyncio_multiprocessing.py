import asyncio
from concurrent.futures import ProcessPoolExecutor


def encrypt_data(data):
    print(f"Lock the data now..{data[::-1]}")
    return data[::-1]



async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        rsult = await loop.run_in_executor(pool, encrypt_data, "credit_card_1234")
        print(f"Result {rsult}")


if __name__ == "__main__":
    asyncio.run(main())
        
