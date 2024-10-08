import aiohttp
import pandas as pd


async def fetch(url, method='GET', headers=None, json=None, body=None):
    async with aiohttp.ClientSession() as session:
        if body:
            async with session.request(method, url, headers=headers, data=body) as response:
                return await response.json()
        elif json:
            async with session.request(method, url, headers=headers, json=json) as response:
                return await response.json()
        async with session.request(method, url, headers=headers,) as response:
            return await response.json()
            
async def get_csv_data(url: str):
    return pd.read_csv(url, sep=';')
    