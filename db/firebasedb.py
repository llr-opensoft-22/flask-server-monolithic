import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("config/firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://llr-library-backend-default-rtdb.firebaseio.com/'})


orders_ref = db.reference("/orders")
deliveries_ref = db.reference("/deliveries")
customer_loyalty_ref = db.reference("/customer-loyalty")

def get_one_order(id):
    data = orders_ref.child(id).get()
    return data

def add_one_order(data):
    key = orders_ref.push(data).key
    orders_ref.child(key).child("key").set(key)
    return key

def get_all_orders():
    data = orders_ref.get()
    return data
