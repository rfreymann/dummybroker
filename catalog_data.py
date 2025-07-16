# catalog_data.py
from schemas import create_instance_schema, create_instance_ui

# create_instance_schema = {
#     "$schema": "http://json-schema.org/draft-07/schema",
#     "title": "Kreditkarteninformationen",
#     "type": "object",
#     "properties": {
#         "frei1": {
#             "type": "string",
#             "description": "Nummer der Kreditkarte, alle Dienstleister werden akzeptiert"
#         },
#         "frei2": {
#             "type": "string",
#             "description": "Ablaufdatum im Format MM/JJ"
#         },
#         "frei3": {
#             "type": "string",
#             "description": "Sicherheitscode (CVC) der Kreditkarte"
#         },
#         "frei4": {
#             "type": "string",
#             "description": "Name wie auf der Karte"
#         }
#     },
#     "required": ["frei1", "frei2", "frei3"],
#     "additionalProperties": False
# }

plans = [
    {
        "name": "default",
        "id": "plan-0001",
        "description": "Standardplan",
        "metadata": {
            "displayName": "Standard"
        }
    },
    {
        "name": "groß",
        "id": "plan-0002",
        "description": "großer Plan",
        "metadata": {
            "displayName": "groß",
            "service_instance_create_ui": create_instance_ui
        },
        "schemas": {
            "service_instance": {
                "create": {
                    "parameters": create_instance_schema
                }
            }
        }
    },
    {
        "name": "Spar-Abo",
        "id": "plan-0003",
        "description": "Spar-Abo",
        "metadata": {
            "displayName": "Spar-Abo",
            "service_instance_create_ui": create_instance_ui
        },
        "schemas": {
            "service_instance": {
                "create": {
                    "parameters": create_instance_schema
                }
            }
        }
    }
]

catalog = {
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
        "plans": plans
    }]
}
