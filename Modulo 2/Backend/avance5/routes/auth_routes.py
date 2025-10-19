# auth_routes.py
from flask import Blueprint, request, jsonify
from jwebt import create_access_token
from db.db_operations import get_user_by_email_db, get_user_roles_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    e_mail = request.json.get("e_mail", None)
    password = request.json.get("password", None)

    if not e_mail or not password:
        return jsonify({"msg": "Missing credentials"}), 400

    try:
        user_data = get_user_by_email_db(e_mail)

        if not user_data:
            return jsonify({"msg": "Incorrect email or password"}), 401

        if user_data['password'] != password: # In a real app, use hashed passwords
            return jsonify({"msg": "Incorrect email or password"}), 401

        rol_result = get_user_roles_db(user_data['id'])

        if not rol_result:
            return jsonify({"msg": "User has no role assigned"}), 403

        final_role = "admin" if "admin" in rol_result else rol_result[0]

        additional_claims = {"role": final_role}
        access_token = create_access_token(identity=e_mail, additional_claims=additional_claims)

        return jsonify(access_token=access_token)

    except Exception as e:
        return jsonify({"error": str(e)}), 500