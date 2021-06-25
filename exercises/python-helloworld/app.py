from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route("/metrics")
def metrics():
    return make_response(
        'data: {UserCount: 140, UserCountActive: 23}',
        200
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
