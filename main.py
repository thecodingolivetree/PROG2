from flask import Flask, request, render_template

app = Flask("Hello World")


@app.route("/", methods=['GET', 'POST'])  # "/" bedeutet es rootet immer zurück auf die Landingpage
def hello():
    return render_template("index.html", name="Du Schönheit!")


@app.route("/create/subscription", methods=['GET'])
def render_create_subscription_form():
    return render_template("create_subscription.html", name="Du Schönheit!")


@app.route("/save/subscription", methods=['POST'])
def save_new_subscription():
    print(request.form.get('sex1'))  # Bei Speichern des Formulars wird ein POST ausgegeben
    print("new form submitted")
    return render_template("index.html", name="Du Schönheit!")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
