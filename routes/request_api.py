from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
REQUEST_API = Blueprint('request_api', __name__)


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
        return jsonify(ORDER_REQUESTS)
    else:
        print(request.get_json())
        return "ok"


@REQUEST_API.route('/orders/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_order(id):
    if request.method == "GET":
        return jsonify(ONE_ORDER), 200
    elif request.method == "POST":
        return "ok"
    elif request.method == "PUT":
        return "ok"
    elif request.method == "DELETE":
        return "ok"
    else:
        return "not ok"
