from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate     # companion package to SQLAlchemy
import os   #needed to grab database url variable from .env file
from dotenv import load_dotenv     #is this also needed for the above?

# Sets up db and migrate, which are conventional variables that give us access to database operations
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

# Configures the app to include two new SQLAlchemy settings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
# Connects db and migrate to our Flask app
    db.init_app(app)
    migrate.init_app(app, db)

    #to do -- import models once created
    from app.routes import users_bp, trips_bp, photos_bp

    app.register_blueprint(users_bp)    
    app.register_blueprint(trips_bp)    
    app.register_blueprint(photos_bp)    
    # app.register_blueprint(journal_entries_bp)  

    return app


app = create_app()    


# dont need these if i do "flask run" instead of  "python main.py", otherwise
# we are just saying to load the function but we never actually call it (which we do with app = create_app())
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=8080, debug=True)

# if __name__ == "__main__":
#     app.run(debug=True)