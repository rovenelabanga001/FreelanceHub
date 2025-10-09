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
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Authorization header missing"}), 401
        
        #Expect header in format: "Bearer <token>"
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return jsonify({"error" : "Invalid Authorization format"}), 401
        
        token = parts[1]

        if token in blacklisted_tokens:
            return jsonify({"error": "Token has been blackilisted. Please login again"}), 401
        
        decoded = decode_token(token)
        if "error" in decoded:
            return jsonify(decoded), 401
        
        #Attach user to request for access inside views
        request.user = decoded
        return f(*args, **kwargs)
    
    return decorated

def blacklist_token(token):
    """Add a token to the blacklist (used for logout)."""
    blacklisted_tokens.add(token)