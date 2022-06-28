from flask import Flask, jsonify, request
from data import data
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,
        "status":"success"
    }),200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(i for i in data if i["name"] == name)
    return jsonify({
        "data":"star_data",
        "status":"success"
    }),200

if __name__=="__main__":
    app.run(debug=True)

