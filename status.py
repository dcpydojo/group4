from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_status():
    url = 'https://www.opm.gov/json/operatingstatus.json'
    response = jsonify(requests.get(url).json())
    return response


if __name__ == "__main__":
    app.run()