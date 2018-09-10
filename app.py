from flask import Flask, request, jsonify
import logging
import os
import time
import json


app = Flask(__name__)

try:
  environment = os.environ['FLASK_ENV']
except KeyError:
  environment = 'development'

if environment == 'test':
  logging.getLogger('werkzeug').disabled = True

@app.route('/')
def root():
  return jsonify({'message': 'root'})

@app.route('/test')
def test():
  return jsonify({'message': 'testing'})

@app.route('/<name>/<number>')
def random(name, number):
  time.sleep(int(number))
  return jsonify({'message': 'testing'})

@app.route('/post/create/', methods=['POST'])
def create_post():
  print(request.json)
  return jsonify({'a': 'a'})

def custom_func(data=None):
  def custom_response(**args):
    data.update({'a': 'a', 'name': 'asdf', 'n': args['name'] })
    return json.dumps(data)

  return custom_response

routes = [
  { 'path': '/index/<name>', 'function_name': 'index', 'data': { 'name': 'eduardo'}}
]

for route in routes:
  app.add_url_rule(route['path'], route['function_name'])
  app.view_functions[route['function_name']] = custom_func(route['data'])

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
