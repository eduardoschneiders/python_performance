from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)

if os.environ['FLASK_ENV'] == 'test':
  logging.getLogger('werkzeug').disabled = True

@app.route('/')
def root():
  return jsonify({'message': 'root'})

@app.route('/test')
def test():
  return jsonify({'message': 'testing'})