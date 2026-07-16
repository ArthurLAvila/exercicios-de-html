from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = []

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        usuario = request.form["usuario"]
        email = request.form["email"]
        senha = request.form["senha"]
        nascimento = request.form["nascimento"]

        usuarios.append({
            "usuario": usuario,
            "email": email,
            "senha": senha,
            "nascimento": nascimento
        })

        return render_template(
            "login.html",
            mensagem="Usuário cadastrado com sucesso! Faça seu login."
        )

    return render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        for pessoa in usuarios:

            if pessoa["usuario"] == usuario and pessoa["senha"] == senha:
                return render_template("home.html")

        return render_template(
            "login.html",
            mensagem="Usuário ou senha inválidos!"
        )

    return render_template("login.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    return render_template("sucesso.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)