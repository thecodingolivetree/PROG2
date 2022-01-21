from flask import Flask, request, render_template

import database_service

# Quelle: Video Reihe https://www.youtube.com/watch?v=GgS8-mn9zoM&list=PLNmsVeXQZj7otfP2zTa8AIiNIWVg0BRqs&index=13
app = Flask("Hello World")

def calculate_costs(surfboard, transport, insurance, beginnerdate, intermediatedate, advanceddate):  # Input Herr Odoni
    return calculate_optional_selection_cost(surfboard, transport, insurance) + calculate_costs_lessons(beginnerdate,intermediatedate,advanceddate)

def calculate_optional_selection_cost(surfboard, transport, insurance): #Zusammenrechnen der ausgewählten Exklusivleistungen
    cost_metrics = database_service.get_costs_dict()
    costs = 0
    if surfboard == "ja":
        costs += cost_metrics['surfboard']
    if transport == "ja":
        costs += cost_metrics['transport']
    if insurance == "ja":
        costs += cost_metrics['insurance']
    return costs

def calculate_costs_lessons(beginnerdate, intermediatedate, advanceddate): #Kosten der Lektionen
    cost_metrics = database_service.get_costs_dict()

    total_course_count = len(beginnerdate) + len(intermediatedate) + len(advanceddate)
    return total_course_count * cost_metrics['basic_lesson']


@app.route("/admin/page", methods=['GET'])
def ausgabe():
    kurse = database_service.get_course_summary()
    anmeldungen = database_service.get_all_subscriptions()  # greift auf die Datenbank mit Anmeldung zu, dinger sind die anmeldungen.
    total = get_total_of_all_courses(kurse)
    return render_template("admin_page.html", anmeldungen=anmeldungen, kurse=kurse, total=total)


def get_total_of_all_courses(kurse): #Zusammenrechnen des Totals der Kurse
    total = 0
    for course in kurse:
        total = total + course['money']
    return total


def auflisten(): #https://docs.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/addition-assignment-operator
    anmeldungen = ""
    for key, value in anmeldungen.items():
        zeile = str(key) + ": " + value + "<br>"
        anmeldungen_liste += zeile

    return anmeldungen_liste


@app.route("/", methods=['GET', 'POST'])  # "/" - rootet immer zurück auf die Landingpage
def hello():
    return render_template("index.html", name="Surfer:in!")


@app.route("/create/subscription", methods=['GET'])
def render_create_subscription_form():
    return render_template("create_subscription.html", name="Surfer:in!")


@app.route("/save/subscription", methods=['POST'])
def save_new_subscription():
    if request.method == "POST": # Bei Speichern des Formulars wird ein POST ausgegeben
        beginnerdate = request.form.getlist("beginnerdate")
        intermediatedate = request.form.getlist("intermediatedate")
        advanceddate = request.form.getlist("advanceddate")
        level = request.form.get('level')
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
        costs = calculate_costs(surfboard, transport, insurance, beginnerdate, intermediatedate, advanceddate)

        database_service.save_subscription(beginnerdate, intermediatedate, advanceddate, level, surfboard, insurance,
                                           transport, sex, name, vorname, adresse, geburi, tel, mail,
                                           calculate_costs(surfboard, transport, insurance, beginnerdate,
                                                           intermediatedate, advanceddate))

    return render_template("save_subscription.html", name=name, vorname=vorname, adresse=adresse, geburi=geburi,
                           mail=mail, tel=tel, sex=sex, level=level, beginnerdate=beginnerdate,
                           intermediatedate=intermediatedate, advanceddate=advanceddate, surfboard=surfboard,
                           insurance=insurance, transport=transport, costs=costs)
                            #Red Code = Ausgabe Buchungsdetails Variabel wird benannt und es kann im html File angesprochen werden

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # IP Adresse ist das Gebäude, Port ist die Tür "wo es klingelt"
