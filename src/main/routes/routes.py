from flask import Blueprint, request, jsonify

#import adapters
from src.main.adapters.request_adapter import request_adapter

#import composers
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

#import error handler
from src.errors.error_handler import handle_errors

user_route_bq = Blueprint("user_routes", __name__)

@user_route_bq.route("/user/finder", methods=["GET"])
def find_user():
    http_reponse = None
    
    try:
        http_reponse = request_adapter(request=request, controller=user_finder_composer())
    except Exception as e:
        http_reponse = handle_errors(error=e)
    
    return jsonify(http_reponse.body), http_reponse.status_code

@user_route_bq.route("/user/register", methods=["POST"])
def register_user():
    http_reponse = None
    
    try:
        http_reponse = request_adapter(request=request, controller=user_register_composer())    
    except Exception as e:
        http_reponse = handle_errors(error=e)
    
    return jsonify(http_reponse.body), http_reponse.status_code