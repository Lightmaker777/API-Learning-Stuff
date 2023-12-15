import aiohttp # pip install aiohttp
import asyncio

async def get_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.json())


async def hello():
    print('Hello ...')
    await asyncio.sleep(2)
    print('... World!')

async def get_response_with_key(url,headers={'X-API-KEY':'test_wSJAzw1HB4xDxw5QObiJCaKXOupQCxAfi5gjif0N'}
):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            print(await response.json())

async def main():
    # without API key
    url = 'https://api.breakingbadquotes.xyz/v1/quotes' 

    # with API key
    url1 = 'https://api.nettoolkit.com/v1/account/test-api-keys'
    headers = {'X-API-KEY':'test_wSJAzw1HB4xDxw5QObiJCaKXOupQCxAfi5gjif0N'}     
    tasks = [
        hello(),
        get_response(url),
        get_response_with_key(url1),
    ]
    # Wait for all processes to complete
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Run the main asynchronous program
    asyncio.run(main())






