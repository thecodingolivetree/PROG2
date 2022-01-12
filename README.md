**Anmeldetool: Surflektion**

**Ausgangslage**

Im Modul Programmierung 2 erhielten wird die Möglichkeit, eine eigene Webapplikation zu entwickeln.
Dabei sollte der Umgang mit verschiedenen Tools wie Pycharms und Github erlernt werden. Im Rahmen dieses Projekts, erstellte ich ein
Anmeldungstool für Surflektionen mit mir.

**Funktion und Projektidee**

In diesem Projekt handelt es sich um ein Anmeldetool für Surflektionen. 
Der/Die User:in wird von der Landingpage direkt zum Anmeldeformular geführt.
Im Anmeldeformular kann das Level, die gewünschten Lektions-Daten und persönliche Daten angegeben werden.
Dazu können Zusatzleistungen wie Surfboard, Transport oder Versicherung dazugebucht werden.
Nach der Sendung des Anmeldeformulars, werden dem/der User:in eine Informationsübersicht sowie der Gesamtpreis
ausgegeben.

Zusätzlich hat der Admin die Möglichkeit, alle bisher gebuchten Kurse auf der Admin-Page
einzusehen. Dort sieht er auch die bisher generierten Einnahmen pro Kurs sowie die Gesamteinnahmen ansehen.

**Workflow**

Die Dateneingabe erfolgt wie Formular. Es beinhaltet verschiedene Eingabeelemente
wie Freie Textfelder, Dropdown und Checkboxen. 

**Datenverarbeitung und Speicherung**
- Nach dem Senden des Anmeldeformulars, werden die verschiedenen Eckdaten des Surf-Schülers in einem Json-File 
in Form eines Dictionarys abgespeichert.
- Die Preise für die Zusatzleistungen (Surfboard, Transport und Versicherung) sind in einem Dictionary abgespeichert
und können laufend angepasst werden. Die Preise für die Lektionen bleibt stets der Gleiche.

**Datenausgabe**

- Nutzersicht: Die Daten können inklusive Endpreis für der/die User:in nach Anmeldung eingesehen werden.
- Adminsicht: Der Admin kann die Anzahl Anmeldungen und Einnahmen pro Kurs auf seiner persönlichen
Admin-Page ansehen. Dort findet er auch die Gesamteinnahmen.
- 
**Status**

In Bearbeitung

