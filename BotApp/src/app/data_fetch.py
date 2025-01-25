import aiohttp
from .settings import API_URL


class ResponseMethod:
    def __init__(self):
        self.api_url = API_URL

    async def get_response(self, url, token=None):
        headers = {}
        # Если токен предоставлен, добавляем его в заголовки
        if token is not None:
            headers['Authorization'] = f'Bearer {token}'

        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url + "/" + url, headers=headers) as response:
                if 'application/json' in response.headers.get('content-type', ''):
                    response_json = await response.json()
                    return response_json
                else:
                    response_text = await response.text()
                    return response_text

    async def post_response(self, url, data, token=None):
        headers = {}
        if token is not None:
            headers['Authorization'] = f'Bearer {token}'
            headers['Content-Type'] = 'application/json'

        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url + "/" + url, headers=headers,  json=data) as response:
                if 'application/json' in response.headers.get('content-type', ''):
                    response_json = await response.json()
                    return response_json
                else:
                    response_text = await response.text()
                    return response_text