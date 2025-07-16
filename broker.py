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

@app.route('/v2/catalog', methods=['GET'])
@requires_auth
def catalog():
    common_schemas = {
        "service_instance": {
            "create": {
                "parameters": {
                    "type": "object",
                    "properties": {
                        "frei1": {
                            "type": "string",
                            "title": "Kartennummer",
                            "description": "Nummer der Kreditkarte, alle Dienstleister werden akzeptiert"
                        },
                        "frei2": {
                            "type": "string",
                            "title": "Ablaufdatum",
                            "description": "Form MM/JJ"
                        },
                        "frei3": {
                            "type": "string",
                            "title": "CVC",
                            "description": "Sicherheitscode der Kreditkarte"
                        },
                        "frei4": {
                            "type": "string",
                            "title": "Name des Karteninhabers",
                            "description": "Name, wie auf der Kreditkarte angegeben"
                        }
                    }
                }
            }
        }
    }

    return jsonify({
        "services": [{
            "name": "dummy-service",
            "id": "service-1234",
            "description": "Ein Dummy-Service für Tests",
            "bindable": True,
            "metadata": {
                "displayName": "Dummy Service",
                "imageUrl": "https://example.com/logo.png",
                "longDescription": "Ein OSB für Tests mit der GeoPlattform",
                "providerDisplayName": "R. Freymann",
                "documentationUrl": "https://example.com/docs",
                "supportUrl": "https://example.com/support",
                "eulaUrl": "https://example.com/eula"
            },
            "plans": [
                {
                    "name": "default",
                    "id": "plan-0001",
                    "description": "Standardplan",
                    "metadata": {
                        "displayName": "Standard"
                    },
                    "schemas": common_schemas
                },
                {
                    "name": "groß",
                    "id": "plan-0002",
                    "description": "großer Plan",
                    "metadata": {
                        "displayName": "groß"
                    },
                    "schemas": common_schemas
                },
                {
                    "name": "Spar-Abo",
                    "id": "plan-0003",
                    "description": "Spar-Abo",
                    "metadata": {
                        "displayName": "Spar-Abo"
                    },
                    "schemas": common_schemas
                }
            ]
        }]
    })


@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['PUT', 'DELETE'])
@requires_auth
def service_binding(instance_id, binding_id):
    if request.method == 'PUT':
        print(f"[Broker] Binde Service {instance_id}, Binding {binding_id}")
        return jsonify({
            "credentials": {
                "url": f"https://dummy-{instance_id}.rafrey.com/api",
                "token": f"token-{binding_id}",
                "username": "demo",
                "password": "demo123",
                "notes": "Dies ist ein reines Dummy-Binding ohne echte Funktion."
            }
        }), 201

    elif request.method == 'DELETE':
        print(f"[Broker] Entferne Binding {binding_id} von Instance {instance_id}")
        return jsonify({}), 200


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
