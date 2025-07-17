create_instance_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "title": "Kreditkarteninformationen",
    "type": "object",
    "properties": {
        "Kartennummer": {
            "type": "string",
            "description": "Nummer der Kreditkarte, alle Dienstleister werden akzeptiert"
        },
        "Ablaufdatum": {
            "type": "string",
            "description": "Ablaufdatum im Format MM/JJ"
        },
        "CVC": {
            "type": "string",
            "description": "Sicherheitscode (CVC) der Kreditkarte"
        },
        "Name des Karteninhabers": {
            "type": "string",
            "description": "Name wie auf der Karte"
        }
    },
    "required": ["frei1", "frei2", "frei3"],
    "additionalProperties": False
}
