import time

class CalculateTime():
  def __init__(self, max_time):
    self.results = []
    self.max_time = max_time

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
    s = self.results.sort(key=lambda r: int(r['time'] * 100))
    for result in self.results:
      self.print_result(result)

  def print_slowest_results(self):
    results = [x for x in self.results if int(x['time']) >= self.max_time]

    if len(results) > 0:
      print('Slowest results: ' + 30 * '-')
      for result in results:
        self.print_result(result)

  def print_result(self, result):
    print('%-15s%-4s%-40s' % (
        ' Time: ' + str(result['time']),
        result['method'].upper(),
        result['url']))