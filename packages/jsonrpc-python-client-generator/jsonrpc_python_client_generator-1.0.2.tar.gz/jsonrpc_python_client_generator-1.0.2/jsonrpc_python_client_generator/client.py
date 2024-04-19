import requests
import json
from jsonrpc_python_client_generator.response import Success, Error
from typing import Union

class HttpClient:

    headers = {
        'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json'
    }

    url: str

    def __init__(self, url: str) -> None:
        self.url = url
        return
    
    def post(self, method: str, params) -> Union[Success,Error]:
        data = {
            'jsonrpc':'2.0',
            'method':method,
            'params':params
            }
        response = requests.post(self.url, json=data, headers=self.headers)
        result = json.loads(response.text)

        # пример вызова метода API с полученным токеном
        if 'result' in result:
            return Success(text=response.text)
        elif 'error' in result:
            return Error(text=response.text)
        else:
            raise ValueError("InvalidJsonResponse")