from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/enviar", methods=["POST"])
def enviar():
    return render_template("sucesso.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form["nome"]
    email = request.form["email"]

    return f"Nome: {nome}<br>E-mail: {email}"

if __name__ == "__main__":
    app.run(debug=True)