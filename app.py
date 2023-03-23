import re
from datetime import datetime
from flask import Flask, render_template
import folium


app = Flask(__name__)


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

@app.route("/GPPapp2/")
def GPPapp2():
    map = folium.Map(location=[37.422, -122.084], zoom_start=12)
    return render_template("GPPapp2.html", map=map._repr_html_())


@app.route("/NEE/")
def NEE():
    return render_template("NEE.html")


@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template("hello_there.html", name=name, date=datetime.now())


@app.route("/api/data")
def get_data():
    return app.send_static_file("json/test.json")


if __name__ == "__main__":
    app.run()


# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def flaskapp():
#     file="about9.jpg"
#     return render_template("flaskapp.html",file=file)

# if __name__ == "__main__":
#     app.run()
