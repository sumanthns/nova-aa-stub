from flask import Flask, url_for
from flask import jsonify
import random
import uuid

app = Flask(__name__)
hypervisors = ['21-2-66-429063', '21-4-67-429065']
tenant_id = 1234

@app.route('/')
def api_root():
    return 'Welcome to nova admin api stub'

@app.route('/%s/rax-fg-migrations' % tenant_id, methods=['POST'])
def create_instance():
  message = {"instance_uuid": str(uuid.uuid4())}
  resp = jsonify(message)
  return resp

@app.route('/%s/rax-fg-migrations/<instance_id>/activate' % tenant_id, methods=['POST'])
def activate_instance(instance_id):
  message = {'status': 204, 'message': 'No content'}
  resp = jsonify(message)
  resp.status_code = 204
  return resp

@app.route('/%s/rax-fg-migrations/<instance_id>' % tenant_id, methods=['DELETE'])
def delete_instance(instance_id):
  message = {'status': 204, 'message': 'No content'}
  resp = jsonify(message)
  resp.status_code = 204
  return resp

@app.route('/%s/rax-fg-migrations/<instance_id>' % tenant_id)
def show_instance(instance_id):
  message = {'hypervisor_hostname': random.choice(hypervisors)}
  resp = jsonify(message)
  return resp

@app.route('/%s/flavors/<flavor_id>/action' % tenant_id, methods=['POST'])
def add_flavor_access(flavor_id):
  message = {"status": 204, "message":"No Content"}
  resp = jsonify(message)
  resp.status_code = 204
  return resp

if __name__ == '__main__':
    app.run()
