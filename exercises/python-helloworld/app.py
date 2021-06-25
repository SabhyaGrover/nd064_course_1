from flask import Flask,make_response
import json
import logging
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
    ## log line
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def metrics():
    ## log line
    app.logger.info('Metrics request successfull')
    return make_response(
        'data: {UserCount: 140, UserCountActive: 23}',
        200
    )

if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')
