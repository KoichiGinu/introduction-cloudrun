import os

from flask import Flask
import math
import requests
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello CloudRun"

# ランダムな数字を返す(0-100)
@app.route('/rand')
def rand():
    num = math.floor(random.uniform(0, 100))
    return str(num)

# 猫画像を返す
# The Cat API (https://thecatapi.com/)
@app.route('/cats')
def cats():
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {'x-api-key': 'hogehoge'}
    result = requests.get(url, headers=headers)
    jsonData = result.json()
    return "<img src=" + jsonData[0]["url"] + " width=500>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
