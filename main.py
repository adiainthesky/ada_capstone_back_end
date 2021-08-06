from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate     # companion package to SQLAlchemy
import os   #needed to grab database url variable from .env file
from dotenv import load_dotenv     #is this also needed for the above?
import sqlalchemy as real_sqlalchemy

# Sets up db and migrate, which are conventional variables that give us access to database operations
db = SQLAlchemy()
migrate = Migrate()

# vars that i am getting from my environment (which here is app.yaml)
db_user = os.environ.get('CLOUD_SQL_USER')
db_pass = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
# db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
cloud_sql_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
db_socket_dir = os.environ.get('DB_SOCKET_DIR', '/cloudsql')

# def open_connection():
#     unix_socket = '/cloudsql/{}'.format(db_connection_name)
#     print
#     try:
#         print("$$$$$$$$$$$$$$$")
#         print(os.environ.get('GAE_ENV'))
#         if os.environ.get('GAE_ENV') == 'standard':
#             print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#             print(f'%%%%%%%%%%%{db}%%%%%%%%%%%%')
#             conn = db.connect(user=db_user, password=db_password,
#                                 unix_socket=unix_socket, db=db_name,
#                                 cursorclass=db.cursors.DictCursor
#                                 )
#             print(f'@@@@@@@@@{conn}@@@@@@@@') 
#             return conn
#     except Exception as e:
#     # except db.MySQLError as e:
#         print(f'*********{e}**********')

    



# pool = db.create_engine(
#     # Equivalent URL:
#     # postgresql+pg8000://postgres:postgresPW@/geo-photo-album-db?unix_sock=<socket_path>/geophotoalbum:us-central1:geo-photo-album-db/.s.PGSQL.5432
#     # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
#     db.engine.url.URL.create(
#         drivername="postgresql+pg8000",
#         username=db_user,  # e.g. "my-database-user"
#         password=db_pass,  # e.g. "my-database-password"
#         database=db_name,  # e.g. "my-database-name"
#         query={
#             "unix_sock": "{}/{}/.s.PGSQL.5432".format(
#                 db_socket_dir,  # e.g. "/cloudsql"
#                 cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
#         }
#     ),
# )



# if in dev use: env vars, else, use google cloud vars for prodcuton

def create_app(test_config=None):
    print(os.environ)
    app = Flask(__name__)

# Configures the app to include two new SQLAlchemy settings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # below was when storing in .env for local deployment -- do i need to change when using vars in app.yaml?
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # this is attempt to make it work for google app engine:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+pg8000://{db_user}:{db_pass}@/{db_name}?unix_sock={db_socket_dir}/{cloud_sql_connection_name}/.s.PGSQL.5432"
    print(f'this is the database string {app.config["SQLALCHEMY_DATABASE_URI"]}')
    postgresql+pg8000://None:postgresPW@/geo-photo-album-db?unix_sock=/cloudsql/geophotoalbum:us-central1:geo-photo-album-db/.s.PGSQL.5432
    # app.config["SQLALCHEMY_DATABASE_URI"] = real_sqlalchemy.engine.url.URL.create(
    #     drivername="postgresql+pg8000",
    #     username=db_user,  # e.g. "my-database-user"
    #     password=db_pass,  # e.g. "my-database-password"
    #     database=db_name,  # e.g. "my-database-name"
    #     query={
    #         "unix_sock": "{}/{}/.s.PGSQL.5432".format(
    #             db_socket_dir,  # e.g. "/cloudsql"
    #             cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
    #     }
    # )
# Connects db and migrate to our Flask app

    from app.models.trip import Trip
    from app.models.photo import Photo

    db.init_app(app)
    migrate.init_app(app, db)

    #to do -- import models once created
    from app.routes import users_bp, trips_bp, photos_bp

    app.register_blueprint(users_bp)    
    app.register_blueprint(trips_bp)    
    app.register_blueprint(photos_bp)    
    # app.register_blueprint(journal_entries_bp)  

    return app

# do i need this?
app = create_app()    


# dont need these if i do "flask run" instead of  "python main.py", otherwise
# we are just saying to load the function but we never actually call it (which we do with app = create_app())
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=8080, debug=True)

# if __name__ == "__main__":
#     app.run(debug=True)