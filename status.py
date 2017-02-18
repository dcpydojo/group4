from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def get_status():
    url = "https://www.opm.gov/json/operatingstatus.json"
    response = requests.get(url).json()

    status_summary = response["StatusSummary"]
    long_status_message = response["LongStatusMessage"]
    date_of_status = response["AppliesTo"]

    return render_template('status.html', 
                            status_summary = status_summary,
                            long_status_message = long_status_message,
                            date_of_status = date_of_status)

if __name__ == "__main__":
    app.run()
