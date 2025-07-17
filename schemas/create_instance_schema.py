create_instance_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "title": "Kreditkarteninformationen",
    "type": "object",
    "properties": {
        "frei1": {
            "type": "string",
            "description": "Nummer der Kreditkarte, alle Dienstleister werden akzeptiert"
        },
        "frei2": {
            "type": "string",
            "description": "Ablaufdatum im Format MM/JJ"
        },
        "frei3": {
            "type": "string",
            "description": "Sicherheitscode (CVC) der Kreditkarte"
        },
        "frei4": {
            "type": "string",
            "description": "Name wie auf der Karte"
        }
    },
    "required": ["frei1", "frei2", "frei3"],
    "additionalProperties": False
}
