from selenium import webdriver
from selenium.webdriver.common.by import By 
import pyodbc

# Establishing a database connection.
server = 'DESKTOP-D8JAB2P'
database = 'lbs'
username = 'nk'
password = '123'

cnxn = pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
cursor = cnxn.cursor()

# Set up the Chrome driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Define the page URLs to scrape
links = [f'https://dom.trojmiasto.pl/nieruchomosci-rynek-wtorny/f1i,1_2_3,wi,100.html?strona=0{i}' for i in range(101)]

#For each element of the web page, it searches for the appropriate HTML elements on the page

for link in links:
    
    driver.get(link)

    apartment_price = driver.find_elements(By.CLASS_NAME, 'ogloszeniaList__price')
    location = driver.find_elements(By.CLASS_NAME, 'ogloszeniaList__location')
    apartment_size = driver.find_elements(By.XPATH, "//div[@class='ogloszeniaList__detail button button--label button--fourth'][1]")
    number_of_rooms = driver.find_elements(By.XPATH, "//div[@class='ogloszeniaList__detail button button--label button--fourth'][2]")

    # Loop through the elements and extract the data
    for price, location, size, rooms in zip(apartment_price, location, apartment_size, number_of_rooms):
               
        price = price.get_attribute('innerText')
        price = price.strip().replace("zł", "")
        price = int(price.replace(' ', '').strip())
        
        location = location.text
        
        size = size.get_attribute('innerText')
        size = size.strip().replace("m2", "")
        size = float(size.replace(' ', '').strip())
        
        rooms = rooms.get_attribute('innerText')
        rooms = int(rooms)
        
        # Insert the data into the database
        cursor.execute("INSERT INTO Nieruchomosci (Cena, Lokalizacja, Powierzchnia, Liczba_pokoi) VALUES (?, ?, ?, ?)", price, location, size, rooms)
        cnxn.commit()
        
cursor.close()
cnxn.close()
      
