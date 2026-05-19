from flask import Flask, render_template, abort
from data.programas import PROGRAMAS, PROGRAMAS_BY_ID

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", programas=PROGRAMAS)


@app.route("/programa/<id>")
def programa(id):
    p = PROGRAMAS_BY_ID.get(id)
    if p is None:
        abort(404)
    return render_template("programa.html", programa=p)


if __name__ == "__main__":
    app.run(debug=True)
