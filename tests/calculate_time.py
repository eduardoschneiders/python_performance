import time

class CalculateTime():
  def __init__(self):
    self.results = []

  def register_time(self, function):
    def wrapper(*args):
      t = time.time()
      result = function(*args)
      total_time = round(time.time() - t, 3)
      method, url = args
      self.results.append({'method': method, 'url': url, 'time': total_time})
      return result

    return wrapper

  def print_results(self):
    for r in self.results:
      print('%-15s%-4s%-40s' % (
        ' Time: ' + str(r['time']),
        r['method'].upper(),
        r['url']))