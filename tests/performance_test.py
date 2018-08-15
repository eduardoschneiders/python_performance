import time
import requests
import os
from server import Server

HOST = 'http://localhost:3000'
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def expect(expected, current):
  if expected != current:
    raise StandardError

server = Server(ROOT_PATH)
server.start()

response = requests.get(HOST + '/')
print(response.status_code)
print(response.json())

t = time.time()
response = requests.get(HOST + '/test')
print(response.status_code)
print(response.json())

print(round(time.time() - t, 3))

server.stop()