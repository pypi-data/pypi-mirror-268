# Jsonrpc Python Client Generator

## Installation

```bash
pip install jsonrpc-python-client-generator
```

## Getting started

For generate file with PHP JSON-RPC 2.0 client run script from command line
```bash
python ./script/generate.py --output ./output/client.php --schema ./schema/onenrpc.json 
```
where:
 * --schema is path to OpenRPC schema file
 * --output is output file

```
## Requirements
 * Python 3.10 and higher
 * PHP --with-curl installation