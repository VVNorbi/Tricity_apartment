import pyodbc
from flask import Flask, render_template, Response
import pandas as pd
from flask import request


# create the database engine using the appropriate database driver and connection information
server = 'DESKTOP-D8JAB2P'
database = 'lbs'
username = 'nk'
password = '123'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


server = Flask(__name__)

@server.route("/")
def home():
    return render_template("home.html")


#This is a Flask route decorator that defines a route for the "/sopot" endpoint. When a GET or POST request is received at this endpoint, it triggers the function "sopot".
@server.route("/sopot", methods=["GET", "POST"])
def sopot():
    if request.method == "POST":
        liczba_pokoi = request.form["liczba_pokoi"]
        liczba_pokoi1 = request.form["liczba_pokoi1"]
        powierzchnia = request.form["powierzchnia"]
    else:
        liczba_pokoi = "1"
        liczba_pokoi1 = "10"
        powierzchnia = "60"

    # This code fragment executes an SQL query to the database, which returns a result set. 
    query = f"SELECT Lokalizacja, ROUND(AVG(Cena / Powierzchnia), 2) AS SredniaCenaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Sopot%' AND Liczba_pokoi BETWEEN {liczba_pokoi} and {liczba_pokoi1} AND Powierzchnia > {powierzchnia} GROUP BY Lokalizacja ORDER BY SredniaCenaM2"
    data = pd.read_sql(query, conn)

    return render_template("sopot.html", data=data.to_dict("records"))

#This is a Flask route decorator that defines a route for the "/gdansk" endpoint. When a GET or POST request is received at this endpoint, it triggers the function "gdansk".
@server.route("/gdansk", methods=["GET", "POST"])
def gdansk():
    if request.method == "POST":
        liczba_pokoi = request.form["liczba_pokoi"]
        liczba_pokoi1 = request.form["liczba_pokoi1"]
        powierzchnia = request.form["powierzchnia"]
    else:
        liczba_pokoi = "1"
        liczba_pokoi1 = "10"
        powierzchnia = "60"

    # This code fragment executes an SQL query to the database, which returns a result set. 
    query = f"SELECT Lokalizacja, ROUND(AVG(Cena / Powierzchnia), 2) AS SredniaCenaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdańsk%' AND Liczba_pokoi BETWEEN {liczba_pokoi} and {liczba_pokoi1} AND Powierzchnia > {powierzchnia} GROUP BY Lokalizacja ORDER BY SredniaCenaM2"
    data = pd.read_sql(query, conn)

    return render_template("gdansk.html", data=data.to_dict("records"))

#This is a Flask route decorator that defines a route for the "/gdynia" endpoint. When a GET or POST request is received at this endpoint, it triggers the function "gdynia".
@server.route("/gdynia", methods=["GET", "POST"])
def gdynia():
    if request.method == "POST":
        liczba_pokoi = request.form["liczba_pokoi"]
        liczba_pokoi1 = request.form["liczba_pokoi1"]
        powierzchnia = request.form["powierzchnia"]
    else:
        liczba_pokoi = "1"
        liczba_pokoi1 = "10"
        powierzchnia = "60"

    # This code fragment executes an SQL query to the database, which returns a result set. 
    query = f"SELECT Lokalizacja, ROUND(AVG(Cena / Powierzchnia), 2) AS SredniaCenaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdynia%' AND Liczba_pokoi BETWEEN {liczba_pokoi} and {liczba_pokoi1} AND Powierzchnia > {powierzchnia} GROUP BY Lokalizacja ORDER BY SredniaCenaM2"
    data = pd.read_sql(query, conn)

    return render_template("gdynia.html", data=data.to_dict("records"))

# This code fragment executes an SQL query to the database, which returns a result set. 
@server.route("/trojmiasto")
def trojmiasto():
    query = "SELECT 'Sopot' AS Lokalizacja, ROUND(AVG(cena/powierzchnia), 2) AS SredniaCenaZaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Sopot%' UNION ALL SELECT 'Gdynia' AS Lokalizacja, ROUND(AVG(cena/powierzchnia), 2) AS SredniaCenaZaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdynia%' UNION ALL SELECT 'Gdańsk' AS Lokalizacja, ROUND(AVG(cena/powierzchnia), 2) AS SredniaCenaZaM2 FROM Nieruchomosci WHERE Lokalizacja LIKE 'Gdańsk%';"
    data = pd.read_sql(query, conn)
    
    return render_template("trojmiasto.html", data=data.to_dict('records'))



# This code fragment executes an SQL query to the database, which returns a result set. 
@server.route("/liczba_ogloszen")
def liczba_ogloszen():
    query = "SELECT COUNT(*) as 'Liczba_ogłoszeń', Lokalizacja FROM Nieruchomosci GROUP BY Lokalizacja ORDER BY 'Liczba_ogłoszeń' DESC;"

    data = pd.read_sql(query, conn)
    
    return render_template("liczba_ogloszen.html", data=data.to_dict('records'))

#This code starts the Flask server in debug mode.
if __name__ == '__main__':
    server.run(debug=True)


#method used to close the connection to a database
conn.close()
    