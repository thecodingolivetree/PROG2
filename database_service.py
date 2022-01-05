from flask import Flask, request, render_template
import json
# class Subscription:
#     def __init__(self, beginnerdate, intermediatedate, advanceddate,
#                  level, surfboard, insurance, transport, sex, name, vorname,
#                  adresse, geburi, mail, tel, costs):
#         self.beginnerdate = beginnerdate
#         self.intermediatedate = intermediatedate
#         self.advanceddate = advanceddate
#         self.level = level
#         self.surfboard = surfboard
#         self.insurance = insurance
#         self.transport = transport
#         self.sex = sex
#         self.name = name
#         self.vorname = vorname
#         self.adresse = adresse
#         self.geburi = geburi
#         self.mail = mail
#         self.tel = tel
#         self.costs = costs


def save_subscription(beginnerdate, intermediatedate, advanceddate,
                 level, surfboard, insurance, transport, sex, name, vorname,
                 adresse, geburi, mail, tel, costs):
    get_costs_dict()
    d = open("data/subscriptions.json")
    datenspeicher_list = json.load(d)

    datenspeicher_list.append({"level": level, "datumBeginner": beginnerdate,"datumIntermediate": intermediatedate, "datumAdvanced": advanceddate, "surfboard": surfboard, "versicherung": insurance, "geschlecht": sex,"name": name, "vorname": vorname,"adresse": adresse, "geburtstag": geburi, "mail": mail, "telefon": tel, "transport": transport, "costs": costs})

    with open('data/subscriptions.json', 'w') as f:
        json.dump(datenspeicher_list, f, indent=4, sort_keys=True, separators=(",", ":")) #https://docs.python.org/3/library/json.html

def get_costs_dict():
    d = open("data/costs.json")
    costs = json.load(d)
    return costs

def get_all_subscriptions():
    d = open("data/subscriptions.json")
    datenspeicher_list = json.load(d)
    return datenspeicher_list