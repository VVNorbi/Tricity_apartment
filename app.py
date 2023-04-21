import pyodbc
from flask import Flask, render_template, Response
import pandas as pd
from flask import request


# Tworzenie połączenia z bazą danych
server = 'DESKTOP-D8JAB2P'
database = 'lbs'
username = 'nk'
password = '123'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Tworzenie obiektu Flask
server = Flask(__name__)

# Routing w Flask
@server.route("/")
def home():
    return render_template("home.html")

@server.route("/sopot", methods=["GET", "POST"])
def sopot():
    if request.method == "POST":
        liczba_pokoi = request.form["liczba_pokoi"]
        powierzchnia = request.form["powierzchnia"]
    else:
        liczba_pokoi = "4"
        powierzchnia = "60"

    # Wykonanie zapytania SQL i zapisanie wyników do DataFrame
    query = f"SELECT Lokalizacja, ROUND(AVG(Cena / Powierzchnia), 2) AS SredniaCenaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Sopot%' AND Liczba_pokoi={liczba_pokoi} AND Powierzchnia > {powierzchnia} GROUP BY Lokalizacja ORDER BY SredniaCenaM2"
    data = pd.read_sql(query, conn)

    return render_template("sopot.html", data=data.to_dict("records"))

@server.route("/gdansk", methods=["GET", "POST"])
def gdansk():
    if request.method == "POST":
        liczba_pokoi = request.form["liczba_pokoi"]
        powierzchnia = request.form["powierzchnia"]
    else:
        liczba_pokoi = "4"
        powierzchnia = "60"

    # Wykonanie zapytania SQL i zapisanie wyników do DataFrame
    query = f"SELECT Lokalizacja, ROUND(AVG(Cena / Powierzchnia), 2) AS SredniaCenaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdańsk%' AND Liczba_pokoi={liczba_pokoi} AND Powierzchnia > {powierzchnia} GROUP BY Lokalizacja ORDER BY SredniaCenaM2"
    data = pd.read_sql(query, conn)

    return render_template("gdansk.html", data=data.to_dict("records"))

@server.route("/gdynia", methods=["GET", "POST"])
def gdynia():
    if request.method == "POST":
        liczba_pokoi = request.form["liczba_pokoi"]
        powierzchnia = request.form["powierzchnia"]
    else:
        liczba_pokoi = "4"
        powierzchnia = "60"

    # Wykonanie zapytania SQL i zapisanie wyników do DataFrame
    query = f"SELECT Lokalizacja, ROUND(AVG(Cena / Powierzchnia), 2) AS SredniaCenaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdynia%' AND Liczba_pokoi={liczba_pokoi} AND Powierzchnia > {powierzchnia} GROUP BY Lokalizacja ORDER BY SredniaCenaM2"
    data = pd.read_sql(query, conn)

    return render_template("gdynia.html", data=data.to_dict("records"))

@server.route("/trojmiasto")
def trojmiasto():
    query = "SELECT 'Sopot' AS Lokalizacja, ROUND(AVG(cena/powierzchnia), 2) AS SredniaCenaZaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Sopot%' UNION ALL SELECT 'Gdynia' AS Lokalizacja, ROUND(AVG(cena/powierzchnia), 2) AS SredniaCenaZaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdynia%' UNION ALL SELECT 'Gdańsk' AS Lokalizacja, ROUND(AVG(cena/powierzchnia), 2) AS SredniaCenaZaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdańsk%';"
    data = pd.read_sql(query, conn)
    
    return render_template("trojmiasto.html", data=data.to_dict('records'))

if __name__ == '__main__':
    server.run(debug=True)

    