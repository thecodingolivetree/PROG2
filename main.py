from flask import Flask, request, render_template
import json
app = Flask("Hello World")

def calculate_costs(surfboard, transport,insurance): #Input Herr Odoni
    costs=0
    if surfboard=="ja":
        costs += 20
    if transport =="ja":
        costs += 30
    if insurance =="ja":
        costs += 50
    return costs

def calculate_costs_lessons(beginnerdate, intermediatedate, advanceddate):
    lesson_costs=50
    beginner_date_anzahl = len(beginnderdate)
   if beginner_date_anzahl => 1:
       costs = beginnerdate_anzahl + lesson_costs
        print(lesson_costs)


@app.route("/", methods=['GET', 'POST'])  # "/" bedeutet es rootet immer zurück auf die Landingpage
def hello():
    return render_template("index.html", name="Du Schönheit!")


@app.route("/create/subscription", methods=['GET'])
def render_create_subscription_form():
    return render_template("create_subscription.html", name="Du Schönheit!")

@app.route("/save/subscription", methods=['POST'])
def save_new_subscription():

    d = open("datenspeicher.json")
    datenspeicher_list = json.load(d)

    # Quelle: https://www.youtube.com/watch?v=_sgVt16Q4O4
    if request.method == "POST":
        beginnerdate = request.form.getlist("beginnerdate")
        intermediatedate = request.form.getlist("intermediatedate")
        advanceddate = request.form.getlist("advanceddate")
        level = request.form.get('level')  #Bei Speichern des Formulars wird ein POST ausgegeben
        surfboard = request.form.get("surfboard")
        insurance = request.form.get("insurance")
        transport = request.form.get("transport")
        sex = request.form.get("sex")
        name = request.form.get("name")
        vorname = request.form.get("vorname")
        adresse = request.form.get("adresse")
        geburi = request.form.get("geburi")
        mail = request.form.get("mail")
        tel = request.form.get("tel")
        costs=calculate_costs(surfboard, transport, insurance)

        # print("Beginnerdate: ", beginnerdate)
        # print("intermediatedate: ", intermediatedate)
        # print("Beginnerdate: ", beginnerdate)

        datenspeicher_list.append({"level": level, "datumBeginner": beginnerdate,"datumIntermediate": intermediatedate, "datumAdvanced": advanceddate, "surfboard": surfboard, "versicherung": insurance, "geschlecht": sex,"name": name, "vorname": vorname,"adresse": adresse, "geburtstag": geburi, "mail": mail, "telefon": tel, "transport": transport})

        with open('datenspeicher.json', 'w') as f:
            json.dump(datenspeicher_list, f, indent=4, sort_keys=True, separators=(",", ":")) #https://docs.python.org/3/library/json.html

    return render_template("save_subscription.html", name=name, vorname=vorname, adresse=adresse, geburi=geburi, mail=mail, tel=tel, sex=sex,level=level, beginnerdate=beginnerdate, intermediatedate=intermediatedate, advanceddate=advanceddate,surfboard=surfboard, insurance=insurance, transport=transport, costs=costs)

    return render_template("index.html", name="Du Schönheit!")


if __name__ == "__main__":
    app.run(debug=True, port=5000) #IP Adresse ist das Gebäude, Port ist die Tür "wo es klingelt"
