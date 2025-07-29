import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/principalapis/api/car-data'

mcp = FastMCP('car-data')

@mcp.tool()
def cars(limit: Annotated[str, Field(description='')],
         page: Annotated[str, Field(description='')],
         year: Annotated[Union[str, None], Field(description='')] = None,
         make: Annotated[Union[str, None], Field(description='')] = None,
         model: Annotated[Union[str, None], Field(description='')] = None,
         type: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Retrieve and filter lists of cars'''
    url = 'https://car-data.p.rapidapi.com/cars'
    headers = {'x-rapidapi-host': 'car-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'page': page,
        'year': year,
        'make': make,
        'model': model,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def types() -> dict: 
    '''get a list of supported types'''
    url = 'https://car-data.p.rapidapi.com/cars/types'
    headers = {'x-rapidapi-host': 'car-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def makes() -> dict: 
    '''get a list of supported makes'''
    url = 'https://car-data.p.rapidapi.com/cars/makes'
    headers = {'x-rapidapi-host': 'car-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def years() -> dict: 
    '''get a list of supported years'''
    url = 'https://car-data.p.rapidapi.com/cars/years'
    headers = {'x-rapidapi-host': 'car-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
