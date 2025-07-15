from flask import Flask, request, jsonify
from functools import wraps
import os

app = Flask(__name__)

# Basic Auth
def check_auth(username, password):
    return username == os.getenv("BROKER_USER") and password == os.getenv("BROKER_PASSWORD")

def authenticate():
    return jsonify({'error': 'Unauthorized'}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# /v2/catalog
@app.route('/v2/catalog', methods=['GET'])
@requires_auth
def catalog():
    return jsonify({
        "services": [{
            "name": "dummy-service",
            "id": "service-1234",
            "description": "Ein Dummy-Service für Tests",
            "bindable": False,
            "plans": [{
                "name": "default",
                "id": "plan-0001",
                "description": "Standardplan"
            }]
        }]
    })

# /v2/service_instances/<id>
@app.route('/v2/service_instances/<instance_id>', methods=['PUT', 'DELETE'])
@requires_auth
def manage_instance(instance_id):
    if request.method == 'PUT':
        print(f"[Broker] Provisioniere Instance {instance_id}")
        return jsonify({}), 201
    elif request.method == 'DELETE':
        print(f"[Broker] Lösche Instance {instance_id}")
        return jsonify({}), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
