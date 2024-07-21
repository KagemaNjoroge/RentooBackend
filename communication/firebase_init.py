import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

FIREBASE_CONFIG_PATH = os.getenv("FIREBASE_CONFIG_PATH")


cred = credentials.Certificate(FIREBASE_CONFIG_PATH)
firebase_admin.initialize_app(cred)


db = firestore.client()
