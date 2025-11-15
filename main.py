from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Allowed frontend origins
ALLOWED_ORIGINS = [
    "http://localhost:3000",                     # local dev
    "https://vnit-hostel-grievances-frontend.onrender.com"   # production frontend
]

# Configure CORS for all routes
CORS(
    app,
    resources={r"/*": {"origins": ALLOWED_ORIGINS}},
    supports_credentials=True
)

# Import blueprints
from app.routes import auth, complaints, admin, worker

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(complaints.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(worker.bp)

# Basic routes
@app.route('/api')
def home():
    return {'message': 'Complaint Management System API', 'status': 'running'}

@app.route('/health')
def health():
    return {'status': 'healthy'}

# IMPORTANT:
# Do NOT use app.run() in production.
# Gunicorn will start the server using: gunicorn app:app
