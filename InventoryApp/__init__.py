import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.DevelopmentConfig")
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    csfr = CSRFProtect(app)
    
    #from InventoryApp import (
    #    #tablascreadas
    #    )   
    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping("test_config")
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from InventoryApp.views.index import landingPage
    #from InventoryApp.views.portalTransaccional import zonaTransaccional
    app.register_blueprint(landingPage)
    #app.register_blueprint(zonaTransaccional)
    
    return app