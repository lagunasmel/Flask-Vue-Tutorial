from flask import Flask, jsonify, request, render_template
import urllib.request, json

app = Flask(__name__)

api_url = "http://localhost:3000/db"


SAMPLE_DATA = []
@app.route("/", methods = ['GET'])
def get_articles():
    response = urllib.request.urlopen(api_url)
    data = response.read()
    result = json.loads(data)
    return render_template("index.html", data=data)

@app.route("/add", methods = ['POST'])
def add_article():
    sample_data = {

        "title": "This is the title",
        "body": "this is the body"
    }
    return jsonify(sample_data)


if __name__=="__main__":
    app.run(debug=True)