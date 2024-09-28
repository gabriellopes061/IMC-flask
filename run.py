from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    imc = None
    peso = None
    altura = None

    if request.method == 'POST':
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        if altura > 0:
            imc = peso / (altura ** 2)

        return render_template("index.html", peso=peso, altura=altura, imc=imc)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
