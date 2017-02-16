from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def get_status():
    url = "https://www.opm.gov/json/operatingstatus.json"
    response = requests.get(url).json()
    long_status_message = response["LongStatusMessage"]
    return "Status: \n" + long_status_message

if __name__ == "__main__":
    app.run()