docker_compose_device_schema = {
    "type": "object",
    "additionalProperties": False,
    "required": ["x-config"],
    "properties": {
        "args": {"type": "object"},
        "x-config": {"type": "string"},
        "image": {"type": "string"},
        "build": {"type": "string"},
        "ports": {
            "type": "array",
            "minItems": 0,
            "items": {"type": "string"},
        },
        "volumes": {
            "type": "array",
            "minItems": 0,
            "items": {"type": "string"},
        },
        "environment": {
            "type": "array",
            "minItems": 0,
            "items": {"type": "string"},
        },
        "command": {"type": "string"},
        "x-cpu": {"type": "number"},
        "x-ram": {"type": "string"},
        "x-commit-user-image": {"type": "boolean"},
        "x-views": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["name", "url", "port"],
                "properties": {
                    "name": {"type": "string"},
                    "url": {"type": "string"},
                    "port": {"type": "string"},
                },
            },
        },
        "x-envvars": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["name", "value"],
                "properties": {
                    "name": {"type": "string"},
                    "value": {"type": ["string", "number", "boolean"]},
                },
            },
        },
    },
}
