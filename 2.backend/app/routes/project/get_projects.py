from flask import jsonify
from app.models.project import Project
from app.utils.jwt_utils import jwt_required
from . import project_bp

@project_bp.route("/projects", methods=["GET"])
@jwt_required
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify({"data": [p.to_dict() for p in projects]}), 200
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return jsonify({"error": "Failed to fetch projects"}), 500