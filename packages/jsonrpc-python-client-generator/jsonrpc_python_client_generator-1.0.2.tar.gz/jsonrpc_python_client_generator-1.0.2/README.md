# Jsonrpc Python Client Generator

## Installation

```bash
pip install jsonrpc-python-client-generator
```

## Getting started

Create file `generate.py` with code:
```python
import sys, os

from jsonrpc_python_client_generator.generator import ClientGenerator

openRpcFile = '';
clientFile = '';

for i in range(len(sys.argv)):
    if sys.argv[i] == "--schema":
        openRpcFile = sys.argv[(i+1)]
    if sys.argv[i] == "--output":
        clientFile = sys.argv[(i+1)]

if (os.path.isfile(clientFile)):
    raise SystemExit("Output file is already exists: " + clientFile)

if (os.path.isfile(openRpcFile) == False):
    raise SystemExit("OpenRpc file does not exist: " + openRpcFile)

with open(openRpcFile) as f: schema = f.read()

generator = ClientGenerator(schema=schema,output=os.path.abspath(clientFile))
generator.run()
```

Than run script from command line:
```bash
python ./generate.py --output ./output/client.py --schema ./schema/onenrpc.json 
```
where:
 * --schema is path to OpenRPC schema file
 * --output is output file

 ## How to use client class

Put output file with client class in your project. Make import and than use the instance of this class.
For example:
```pyton
from client import JsonRpcClient

client = JsonRpcClient()
client.checkLogin(login="your_login")
```

## Requirements
 * Python 3.10 and higher