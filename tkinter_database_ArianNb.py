import requests
from bs4 import BeautifulSoup
import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'SERVER=localhost;'
                          'DATABASE=ArianNb;'
                          'Trusted_Connection=yes;')
cursor = conn.cursor()
query = """INSERT INTO articles VALUES(?, ?)
"""
url = "https://maktabkhoone.org/mag/category/artifical-intelligence-articles/"
response = requests.get(url)
html_code = BeautifulSoup(response.content, "html.parser")
titles = html_code.find_all("h2", class_="elementor-heading-title elementor-size-default")
dates = html_code.find_all("span", class_="elementor-icon-list-text")
articles = dict(zip(titles, dates))

for title, date in articles.items():
    cursor.execute(query, (title.string, dates.string))
    cursor.commit()

cursor.close()