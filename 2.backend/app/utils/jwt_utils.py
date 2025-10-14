import jwt
from datetime import datetime, timedelta
from flask import current_app, request, jsonify
from functools import wraps

blacklisted_tokens = set()
def generate_jwt(payload ,expires_in=3600):
    """Generate access token (default expires in 1 hour)."""
    payload_copy = payload.copy()
    payload_copy["exp"] = datetime.utcnow() + timedelta(seconds=expires_in)
    payload_copy["iat"] = datetime.utcnow()
    return jwt.encode(payload_copy, current_app.config["SECRET_KEY"])

def decode_token(token):
    """Decode JWT token and validate it."""
    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error":"Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    
def jwt_required(f):
    """Decorator to protect routes with JWT"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("access_token")
        if not token:
            return jsonify({"error": "Authentication required"}), 401

        if token in blacklisted_tokens:
            return jsonify({"error": "Token has been blacklisted. Please log in again"}), 401

        decoded = decode_token(token)
        if "error" in decoded:
            return jsonify(decoded), 401

        request.user = decoded

        return f(*args, **kwargs)

    return decorated
def blacklist_token(token):
    """Add a token to the blacklist (used for logout)."""
    blacklisted_tokens.add(token)