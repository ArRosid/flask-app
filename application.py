from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
flask_app = Flask(__name__)

# Get the name from environment variable
name = os.getenv("NAME")
if not name:
    raise ValueError("Environment variable 'NAME' not found. Use .env file to set environment variable!")

# Get the port from environment variable or default to 5000
port = int(os.getenv("PORT", 4321))

@flask_app.route('/')
def index():
    return render_template('index.html', name=name)

if __name__ == '__main__':
    flask_app.run(debug=True, port=port)
