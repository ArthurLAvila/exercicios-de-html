from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


@app.route("/empresa")
def empresa():
    return render_template("empresa.html")


@app.route("/tecnologia")
def tecnologia():
    return render_template("tecnologia.html")


@app.route("/documentacao")
def documentacao():
    return render_template("documentacao.html")


if __name__ == "__main__":
    app.run(debug=True)