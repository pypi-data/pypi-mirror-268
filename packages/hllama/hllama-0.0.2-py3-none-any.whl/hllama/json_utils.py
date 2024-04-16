from typing import Dict, Any

def match_structure(schema: Dict[str, Any], data: Dict[str, Any]) -> bool:
    for key, expected_type in schema.items():
        if key not in data:
            print(f"Missing key: {key}")
            return False

        if isinstance(expected_type, dict):
            # If the expected type is a dictionary, recursively check the structure
            if not isinstance(data[key], dict):
                print(f"Expected a dictionary for key: {key}, got {type(data[key])}")
                return False
            if not match_structure(expected_type, data[key]):
                return False
        elif isinstance(expected_type, type):
            # Direct type checking
            if not isinstance(data[key], expected_type):
                print(f"Key '{key}' expected {expected_type}, got {type(data[key])}")
                return False
        else:
            print(f"Unsupported type specification: {expected_type}")
            return False

    return True