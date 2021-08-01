from flask import Flask, request

def create_app(test_config=None):
    app = Flask(__name__)

    from app.models.routes import hello_world_bp
    app.register_blueprint(hello_world_bp)    

    return app

app = create_app()    

# dont need these if i do "flask run" instead of  "python main.py", otherwise
# we are just saying to load the function but we never actually call it (which we do with app = create_app())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

# if __name__ == "__main__":
#     app.run(debug=True)