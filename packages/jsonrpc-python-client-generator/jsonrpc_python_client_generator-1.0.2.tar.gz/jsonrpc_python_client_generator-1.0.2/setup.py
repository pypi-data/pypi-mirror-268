from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='jsonrpc_python_client_generator',
  version='1.0.2',
  author='vk1511work',
  author_email='vk1511work@gmail.com',
  description='Jsonrpc Python Client Generator',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/vk1511work/jsonrpc-python-client-generator',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='jsonrpc 2.0 python client generator',
#   project_urls={
#     'Documentation': 'link'
#   },
  python_requires='>=3.10'
)