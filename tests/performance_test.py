import time, requests, os, yaml
from test_suit import TestSuit
from calculate_time import CalculateTime

HOST = 'http://localhost:3000'
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def load_requests():
  with open(ROOT_PATH + '/tests/requests.yaml') as stream:
    return yaml.load(stream)

ct = CalculateTime(max_time=2)
with TestSuit(ROOT_PATH, ct.print_results, ct.print_slowest_results):
  @ct.register_time
  def make_request(method, url, data=None):
    getattr(requests, method)(url, data=data)

  for request in load_requests()['endpoints']:
    try:
      data = request['data']
    except KeyError:
      data = None

    make_request(request['method'], HOST + request['path'], data)