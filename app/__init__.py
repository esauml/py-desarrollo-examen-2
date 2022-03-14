from flask import Flask
from app.Examen.routes import examen
from app.Site.routes import site

def create_app():
    app = Flask(__name__)
    app.register_blueprint(examen)
    app.register_blueprint(site)
    
    return app