import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase service account credentials JSON file
FIREBASE_SERVICE_ACCOUNT_KEY = "C:\\Users\\kaman\\Desktop\\Rentoo\\communication\\rentoo-rentals-management-firebase-adminsdk-l8c06-6a5314d56c.json"

# Initialize Firebase Admin SDK
cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_KEY)
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()
