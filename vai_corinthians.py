from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def perfil():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/sair")
def sair():
    return render_template("sair.html")


if __name__ == "__main__":
    app.run(debug=True)