import json

class Success:

    id = None
    version = None
    result = None

    json: str

    def __init__(self, text:str) -> None:
        
        self.json = text

        result = json.loads(text)
        self.id = result.get("id")
        self.version = result.get("jsonrpc")
        self.result = result.get("result")

class ErrorMessage:

    code: int
    message: str

    def __init__(self, code: int, message: str) -> None:

        self.code = code
        self.message = message

class Error:

    id = None
    version = None
    error: ErrorMessage

    json: str

    def __init__(self, text:str) -> None:
        
        self.json = text

        result = json.loads(text)
        self.id = result.get("id")
        self.version = result.get("jsonrpc")
        error = result.get("error")

        self.error = ErrorMessage(code=error.get("code"), message=error.get("message"))
