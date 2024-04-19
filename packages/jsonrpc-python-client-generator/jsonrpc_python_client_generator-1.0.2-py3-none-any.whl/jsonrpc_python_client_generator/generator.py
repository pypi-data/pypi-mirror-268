import json

class ClientGenerator:

    schema = None
    output: str

    def __init__(self, schema: str, output: str) -> None:
        
        self.schema = json.loads(schema)
        self.output = output

    def run(self) -> None:
        if self.__verify() == False:
            raise SyntaxError("Invalid OpenRPC schema")
        text = "from jsonrpc_python_client_generator.client import HttpClient\n\
from jsonrpc_python_client_generator.response import Success, Error\n\
from typing import Union\n\n\
class JsonRpcClient:\n\
\n\
    client: HttpClient\n\
\n\
    def __init__(self) -> None:\n\
        self.client = HttpClient(url='" + self.schema.get("servers")[0].get("url") + "')\n\n"

        text += self.__methods(self.schema.get("methods"))

        with open(self.output, 'w', encoding='utf-8') as f_out:
            f_out.write(text)

    def __verify(self) -> bool:
        if len(self.schema.get("methods")) == 0:
            return False
        if len(self.schema.get("servers")) ==0:
            return False
        if len(self.schema.get("servers")[0].get("url")) ==0:
            return False
        return True
    
    def __methods(self, methods) -> str:
        items = []
        out = []
        for method in methods:
            item = {"params":[]}
            if len(method.get("name")) == 0:
                raise SyntaxError("Invalid method name")
            item["name"] = method["name"]
            if len(method["description"]) > 0:
                item["description"] = method["description"]
            if len(method.get("params")) > 0:
                for param in method["params"]:
                    if len(param.get("name")) == 0:
                        raise SyntaxError("Invalid parameter name")
                    if len(param.get("schema")) == 0:
                        raise SyntaxError("Invalid parameter schema")
                    ref = param["schema"].get('$ref')
                    if len(ref):
                        path = ref.replace("#/", "").split("/")
                        type = ""
                        index = self.schema
                        for key in path:
                            if index.get(key) is not None:
                                index = index[key]
                        if index.get("type"):
                            type = ""
                            type = "str" if index["type"] == "string" else type
                            type = "int" if index["type"] == "integer" else type
                            type = "bool" if index["type"] == "boolean" else type
                            type = "list" if index["type"] == "array" else type
                            type = "dict" if index["type"] == "objec" else type
                        param["type"] = type
                    else:
                        raise SyntaxError("Invalid parameter schema $ref")
                    item["params"].append(param)
            items.append(method)
        for method in items:
            code = ""
            param_in_method = []
            param_in_doc = []
            param_in_call = []
            for param in method["params"]:
                description = " -- " + param.get("description") if len(param.get("description")) else ""
                param_in_doc.append(param["name"] + description)
                param_in_call.append('"' + param["name"] + '":' + param["name"])
                if len(param["type"]):
                    if param.get("required"):
                        param_in_method.append(param["name"] + ": " + param["type"])
                    else:
                        param_in_method.append(param["name"] + ": " + param["type"] + " = None")
                else:
                    if param.get("required"):
                        param_in_method.append(param["name"])
                    else:
                        param_in_method.append(param["name"] + " = None")
            code = "    def " + method["name"] + "(self," + ", ".join(param_in_method) + ") -> Union[Success,Error]:\n\
        '''" + method.get("description") + "\n\
\n\
        Keyword arguments:\n\
        " + "\n        ".join(param_in_doc) + "\n\
        '''\n\
        return self.client.post(method='" + method["name"] + "',params={" + ",".join(param_in_call) + "})"
            out.append(code)
        return "\n\n".join(out)
    
    