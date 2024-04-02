from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)


from src.main.routes.event_routes import event_routes
app.register_blueprint(event_routes)