import re
from datetime import datetime
from flask import Flask, jsonify, render_template, request
import ee
import json

# from fastapi import FastAPI, Request, HTTPException
# from fastapi.middleware.wsgi import WSGIMiddleware
# import uvicorn

app = Flask(__name__)

# app = FastAPI()
# flaskapp = Flask(__name__)
# Mount Flask on Fastapi
# app.mount("/CarbonTrack", WSGIMiddleware(flaskapp))


@app.get("/api/hello")
def hello(name: str):
    return {"message": f"Hello {name}"}


incomes = [{"description": "salary", "amount": 5000}]


@app.route("/api/incomes")
def get_incomes():
    return jsonify(incomes)


@app.route("/api/incomes", methods=["POST"])
def add_income():
    incomes.append(request.get_json())
    return "", 204


# @app.get("/api/hello")
# def hello(name: str):
#     return {"message": f"Hello {name}"}


# @app.get("/api")
@app.get("/api")
def root():
    # 501 Not Implemented server error. Server does not support the functionality required to fulfill the request.
    # raise HTTPException(status_code=501, detail="Not Implemented")
    return {"text": "Fast API"}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/analysis/")
def analysis():
    return render_template("analysis.html")


@app.route("/carboncycle/")
def carboncycle():
    return render_template("carboncycle.html")


@app.route("/conclusion/")
def conclusion():
    return render_template("conclusion.html")


@app.route("/contract/")
def contract():
    return render_template("contract.html")


@app.route("/data/")
def data():
    return render_template("data.html")


@app.route("/datapolicy/")
def datapolicy():
    return render_template("datapolicy.html")


@app.route("/GPP/")
def GPP():
    return render_template("GPP.html")


@app.route("/GPPapp/")
def GPPapp():
    return render_template("GPPapp.html")


@app.route("/NEE/")
def NEE():
    return render_template("NEE.html")


# @app.route("/hello/<name>")
# def hello_there(name=None):
#     return render_template("hello_there.html", name=name, date=datetime.now())


# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("json/test.json")


if __name__ == "__main__":
    app.run()

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
