from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get('name','World')
    return 'Hello ' + name + '!'



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

# if __name__ == "__main__":
#     app.run(debug=True)