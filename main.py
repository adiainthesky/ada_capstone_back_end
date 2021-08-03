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
    from app.routes import user_bp, trip_bp, photo_bp, journal_entry_bp

    app.register_blueprint(user_bp)    
    app.register_blueprint(trip_bp)    
    app.register_blueprint(photo_bp)    
    app.register_blueprint(journal_entry_bp)    

    return app





app = create_app()    



# dont need these if i do "flask run" instead of  "python main.py", otherwise
# we are just saying to load the function but we never actually call it (which we do with app = create_app())
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=8080, debug=True)

# if __name__ == "__main__":
#     app.run(debug=True)