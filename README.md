Comflat - Porównywarka cen za m2 w dzielnicach trójmiasta (Python Web Application)
Oprogramowanie Comflat, którego głównym zadaniem jest porównywanie cen za m2 mieszkań na rynku wtórnym w trójmieście przy pomocy filtrów. Przy pomocy Web Scraping pobraliśmy potrzebne informacje ze strony https://dom.trojmiasto.pl/, aby umożliwić porówannie cen.
Aplikacja internetowa pozwala również na wgląd średniej ceny za m2 mieszkań w Gdyni, Sopocie lub Gdańsku jak i liczb ogłoszeń w dzielnicach trójmiasta.

Technologies Used
Frontend: HTML, CSS, Bootstrap, JavaScript
Backend: Python(Flask,Pandas,Plotly), MSSQL(Database)
Webservices: Selenium with Python

Workflow (Functionalities)

Odpalając skrypt tricity_apartment.py ściągamy dane do bazy danych.
Włączając aplikację webową mam 6 zakładek (Home, Sopot, Gdynia, Gdańsk, Trójmiasto, Liczba ogłoszeń)
W zakładce Sopot, Gdynia, Gdańsk przy użyciu formularza możemy zfiltrować mieszkania pod względem liczby pokoi i powierzchni.
W zakładce Trójmiasto mamy możliwość sprawdzenia średniej ceny za m2 wszystkich mieszkań w trójmieście.
W zakładce Liczba ogłoszeń mamy możliwość sprawdzenia ilości ogłoszeń we wszystkich dzielnicach trójmiasta.
