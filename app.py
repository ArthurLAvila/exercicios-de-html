from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    return render_template("login.html", erro=erro)


@app.route("/divs-spans")
def divs_spans():
    return render_template("divs_spans.html")


@app.route("/listas")
def listas():
    return render_template("listas.html")


@app.route("/tabelas")
def tabelas():
    return render_template("tabelas.html")

