from flask import Flask, request, jsonify
import datetime
import requests
from datetime import datetime, date
app = Flask(__name__)


# @app.route("/")
# def home():
#     return "Home"
today = datetime.now()


@app.route("/ovidot", methods=['GET'],)
def get_user():
    args = request.args
    slack_name = args.get("slack_name")
    track = args.get("track")

    r = requests.get('http://127.0.0.1:5000/slack_name',)
    user_data = {
        "slack_name": slack_name,
        "current_day": today.strftime('%A'),
        "utc_time": datetime.utcnow(),
        "track": track,
        "github_file_url": "https://github.com/ovidot/Backend-task1/blob/main/main.py",
        "github_repo_url": "https://github.com/ovidot/Backend-task1",
        "Status_code": '200'
    }

# "ovidot?slack_name=Uzez Ovraiti?track=Backend"

    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)
