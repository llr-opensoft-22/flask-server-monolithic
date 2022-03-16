from crypt import methods
from flask import Blueprint, jsonify, request, abort
from datetime import datetime, timedelta
REQUEST_API = Blueprint('request_api', __name__)
from db.firebasedb import *
import psycopg2
# user=postgres password="kamal" host=db.tlagwlowvabyydvzipai.supabase.co port=5432 database=postgres


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


ONE_ORDER = {
    'title': u'Good Book',
    'email': u'testuser1@test.com',
    'timestamp': (datetime.today() - timedelta(1)).timestamp()
}

ORDER_REQUESTS = {
    "8c36e86c-13b9-4102-a44f-646015dfd981": {
        'title': u'Good Book',
        'email': u'testuser1@test.com',
        'timestamp': (datetime.today() - timedelta(1)).timestamp()
    },
    "04cfc704-acb2-40af-a8d3-4611fab54ada": {
        'title': u'Bad Book',
        'email': u'testuser2@test.com',
        'timestamp': (datetime.today() - timedelta(2)).timestamp()
    }
}


@REQUEST_API.route('/orders', methods=['GET', 'POST'])
def get_records():
    """Return all book requests
    @return: 200: an array of all known BOOK_REQUESTS as a \
    flask/response object with application/json mimetype.
    """
    if request.method == 'GET':
        return jsonify(get_all_orders())
    else:
        print(request.get_json())
        return "ok"


@REQUEST_API.route('/orders/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_order(id):
    if request.method == "GET":
        return jsonify(get_one_order()), 200
    elif request.method == "POST":
        return "ok"
    elif request.method == "PUT":
        return "ok"
    elif request.method == "DELETE":
        if id not in ["temp", "test", "1"]:
            abort(404)
        return "ok"
    else:
        return "not ok"

@REQUEST_API.route('/user',methods=['POST'])
def handle_create_user():
    if request.method=="POST":
        return "ok"


@REQUEST_API.route('/user/login',methods=['GET'])
def handle_login():
    if request.method=="POST":
        return "ok"

@REQUEST_API.route('/user/logout',methods=['GET'])
def handle_logout():
    if request.method=="POST":
        return "ok"


@REQUEST_API.route('/user/<userid>',methods=['GET', 'PUT', 'DELETE'])
def handle_user(userid):
    if request.method=="GET":
        return "ok"
    elif request.method=="PUT":
        return "ok"
    elif request.method=="DELETE":
        return "ok"