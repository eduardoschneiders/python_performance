import time
import requests
import os
from server_manager import RunningServer
from calculate_time import CalculateTime

HOST = 'http://localhost:3000'
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with RunningServer(ROOT_PATH):
  ct = CalculateTime(max_time=2)

  @ct.register_time
  def request(method, url, data=None):
    eval('requests.' + method)(url, data=data)

  request('get', HOST + '/')
  request('get', HOST + '/test')
  request('get', HOST + '/superslow/2')
  request('post', HOST + '/post/create/', {'username': 'eduardo'})

  ct.print_results()
  ct.print_slowest_results()