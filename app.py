from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Allowed origins
ALLOWED_ORIGINS = [
    "http://localhost:3000",  # local frontend
    "https://vnit-hostel-grievances-36cw.vercel.app"  # deployed frontend
]

# Configure CORS
CORS(app, resources={r"/*": {"origins": ALLOWED_ORIGINS}}, supports_credentials=True)

# Import routes
from app.routes import auth, complaints, admin, worker

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(complaints.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(worker.bp)

@app.route('/')
def home():
    return {'message': 'Complaint Management System API', 'status': 'running'}

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)
