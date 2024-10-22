import firebase_admin
from firebase_admin import credentials, auth, firestore
import pyrebase
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to serviceAccountKey.json
service_account_path = os.path.join(current_dir, 'config', 'serviceAccountKey.json')

# Initialize Firebase Admin SDK
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)

# Initialize Firestore with error handling
try:
    db = firestore.client()
except Exception as e:
    print(f"Error initializing Firestore: {e}")
    db = None

# Configure Pyrebase
firebase_config = {
    "apiKey": "AIzaSyCxMkhf-GXt4Ke54PGPD2O169Qm6DUPYUk",
    "authDomain": "sarah-chatbot-cdc75.firebaseapp.com",
    "databaseURL": "https://sarah-chatbot-cdc75.firebaseio.com",
    "projectId": "sarah-chatbot-cdc75",
    "storageBucket": "sarah-chatbot-cdc75.appspot.com",
    "messagingSenderId": "220334182905",
    "appId": "1:220334182905:web:b894ec2d2ff7bcb0feed28"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
