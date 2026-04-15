from flask import Flask, render_template
import json
import urllib.parse

app = Flask(__name__)

def generate_wikiwiki_link(task):
    if not isinstance(task, dict):
        return ""

    base = "https://wikiwiki.jp/eft"
    trader = task["trader"]
    name = task["task"]["name"]
    encoded_name = urllib.parse.quote(name)
    return f"{base}/{trader}/{encoded_name}"

# -------------------------
# Flask ルート
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hideout")
def hideout():
    return render_template("hideout.html")


@app.route("/task")
def task_page():
    return render_template("task.html")

# -------------------------
# Flask 起動
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)