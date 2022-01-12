import json

def save_subscription(beginnerdate, intermediatedate, advanceddate,
                      level, surfboard, insurance, transport, sex, name, vorname,
                      adresse, geburi, mail, tel, costs):
    get_costs_dict()
    d = open("data/subscriptions.json")
    datenspeicher_list = json.load(d)

    datenspeicher_list.append({"level": level, "datumBeginner": beginnerdate, "datumIntermediate": intermediatedate,
                               "datumAdvanced": advanceddate, "surfboard": surfboard, "versicherung": insurance,
                               "geschlecht": sex, "name": name, "vorname": vorname, "adresse": adresse,
                               "geburtstag": geburi, "mail": mail, "telefon": tel, "transport": transport,
                               "costs": costs})

    with open('data/subscriptions.json', 'w') as f:
        json.dump(datenspeicher_list, f, indent=4, sort_keys=True,
                  separators=(",", ":"))  # https://docs.python.org/3/library/json.html


def get_costs_dict():
    d = open("data/costs.json")
    costs = json.load(d)
    return costs


def get_all_subscriptions():
    d = open("data/subscriptions.json")
    datenspeicher_list = json.load(d)
    return datenspeicher_list


def calculate_optional_selection_cost(surfboard, transport, insurance):
    cost_metrics = get_costs_dict()
    costs = 0
    if surfboard == "ja":
        costs += cost_metrics['surfboard']
    if transport == "ja":
        costs += cost_metrics['transport']
    if insurance == "ja":
        costs += cost_metrics['insurance']
    return costs


def get_course_summary():
    # Beginnercourses
    course1 = {
        "date": "10:00 Uhr, 22.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }

    course2 = {
        "date": "14:00 Uhr, 22.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }

    course3 = {
        "date": "08:00 Uhr, 23.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }

    # Intermediate courses
    course4 = {
        "date": "07:00 Uhr, 26.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }
    course5 = {
        "date": "15:00 Uhr, 26.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }
    course6 = {
        "date": "09:00 Uhr, 27.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }
    # Advanced courses
    course7 = {
        "date": "07:00 Uhr, 12.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }
    course8 = {
        "date": "07:00 Uhr, 13.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }
    course9 = {
        "date": "16:00 Uhr, 13.02.2022",
        "numberOfParticipants": 0,
        "money": 0
    }

    d = open("data/subscriptions.json")
    datenspeicher_list = json.load(d)
    print(datenspeicher_list)

    d = open("data/costs.json")
    costs = json.load(d)

    for entry in datenspeicher_list:
        print(entry)
        if course1['date'] in entry['datumBeginner']:
            course1['numberOfParticipants'] = course1['numberOfParticipants'] + 1
            course1['money'] = course1['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50
        if course2['date'] in entry['datumBeginner']:
            course2['numberOfParticipants'] = course2['numberOfParticipants'] + 1
            course2['money'] = course2['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50
        if course3['date'] in entry['datumBeginner']:
            course3['numberOfParticipants'] = course3['numberOfParticipants'] + 1
            course3['money'] = course3['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50

        if course4['date'] in entry['datumIntermediate']:
            course4['numberOfParticipants'] = course4['numberOfParticipants'] + 1
            course4['money'] = course4['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50

        if course5['date'] in entry['datumIntermediate']:
            course5['numberOfParticipants'] = course5['numberOfParticipants'] + 1
            course5['money'] = course5['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50

        if course6['date'] in entry['datumIntermediate']:
            course6['numberOfParticipants'] = course6['numberOfParticipants'] + 1
            course6['money'] = course6['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50

        if course7['date'] in entry['datumAdvanced']:
            course7['numberOfParticipants'] = course7['numberOfParticipants'] + 1
            course7['money'] = course7['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50

        if course8['date'] in entry['datumAdvanced']:
            course8['numberOfParticipants'] = course8['numberOfParticipants'] + 1
            course8['money'] = course8['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50

        if course9['date'] in entry['datumAdvanced']:
            course9['numberOfParticipants'] = course9['numberOfParticipants'] + 1
            course9['money'] = course9['money'] + calculate_optional_selection_cost(entry['surfboard'],
                                                                                    entry['transport'],
                                                                                    entry['versicherung']) + 50

    courses = []
    courses.append(course1)
    courses.append(course2)
    courses.append(course3)
    courses.append(course4)
    courses.append(course5)
    courses.append(course6)
    courses.append(course7)
    courses.append(course8)
    courses.append(course9)
    return courses


