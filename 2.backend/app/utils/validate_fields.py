from flask import jsonify

def validate_fields(data, required_fields):
    missing = [field for field in required_fields if not data.get(field)]
    if missing:
        return jsonify({"error": f"Missing field(s): {', '.join(missing)}"}), 401
    return None