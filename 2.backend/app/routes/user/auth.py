from flask import request, jsonify, make_response, current_app
from app.models.user import User
from app.utils.jwt_utils import generate_jwt, jwt_required, blacklist_token
from app.utils.validate_fields import validate_fields
from app import db
from . import user_bp


@user_bp.post("/signup")
def signup():
    data = request.get_json() or {}
    required_fields = ["username", "email", "password", "role"]

    #validate required fields
    error_response = validate_fields(data, required_fields)
    if error_response:
        return error_response
    
    username, email, password, role = (data.get(f) for f in required_fields)

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400
    
    user = User(username=username, email=email, role=role)
    user.password = password
    db.session.add(user)
    db.session.commit()

    # token = generate_jwt({"id": user.id, "email":user.email, "role": user.role})
    return jsonify({
        "message": "Signup successful",
        "user": user.to_dict(),
    }), 201

@user_bp.post("/signin")
def signin():
    data = request.get_json() or {}
    required_fields = ["email", "password"]

    error_response = validate_fields(data, required_fields)
    if error_response:
        return error_response
    
    email, password = (data.get(f) for f in required_fields)

    user = User.query.filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return jsonify({"error": "Invalid email or password"}), 401
    
    token = generate_jwt({"id": user.id, "email": user.email, "role": user.role})
    
    response = make_response(jsonify({
        "message": "Login Successful",
        "user": user.to_dict()
    }))

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,        # must be False for localhost, True in prod
        samesite="None",     # needed for cross-origin cookie
        max_age=60 * 60 * 24,
        path="/"
    )

    return response

@user_bp.get("/profile")
def get_profile():
    return jsonify({"message": "Welcome!", "user": request.user}), 200


@user_bp.post("/signout")
@jwt_required
def signout():
    token = request.cookies.get("access_token")
    # if token present, blacklist it
    if token:
        try:
            blacklist_token(token)
        except Exception:
            # swallow blacklist errors so logout still succeeds
            pass

    # create response and delete cookie (match attributes used when setting cookie)
    response = make_response(jsonify({"message": "Successfully logged out"}))
    response.delete_cookie(
        "access_token",
        path="/",
        httponly=True,
        secure=False,   # True in production with HTTPS
        samesite="None" # matches how you set it
    )
    return response
