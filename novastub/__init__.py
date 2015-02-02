from flask import Flask, url_for
from flask import jsonify
import random
import uuid

app = Flask(__name__)
hypervisors = ['21-2-66-429063', '21-4-67-429065']

@app.route('/')
def api_root():
    return 'Welcome to nova admin api stub'

@app.route('/<tenant_id>/rax-fg-migrations', methods=['POST'])
def create_instance(tenant_id):
  message = {"instance_uuid": str(uuid.uuid4())}
  resp = jsonify(message)
  return resp

@app.route('/<tenant_id>/rax-fg-migrations/<instance_id>/activate', methods=['POST'])
def activate_instance(tenant_id, instance_id):
  message = {'status': 204, 'message': 'No content'}
  resp = jsonify(message)
  resp.status_code = 204
  return resp

@app.route('/<tenant_id>/rax-fg-migrations/<instance_id>', methods=['DELETE'])
def delete_instance(tenant_id, instance_id):
  message = {'status': 204, 'message': 'No content'}
  resp = jsonify(message)
  resp.status_code = 204
  return resp

@app.route('/<tenant_id>/rax-fg-migrations/<instance_id>')
def show_instance(tenant_id, instance_id):
  message = {'hypervisor_hostname': random.choice(hypervisors)}
  resp = jsonify(message)
  return resp

@app.route('/<tenant_id>/flavors/<flavor_id>/action', methods=['POST'])
def add_flavor_access(tenant_id, flavor_id):
  message = {"status": 204, "message":"No Content"}
  resp = jsonify(message)
  resp.status_code = 204
  return resp

if __name__ == '__main__':
    app.run()
