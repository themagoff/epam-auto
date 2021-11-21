import requests
from bs4 import BeautifulSoup
r = requests.get('http://epam.com')
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
div_amount = len(soup.find_all('div'))
print(f'Количество тегов div равно {div_amount}')


import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE names (number text, name text)")
c.execute("INSERT INTO names VALUES (1,'Иван')")
c.execute("INSERT INTO names VALUES (2,'Алексей')")
c.execute("INSERT INTO names VALUES (3,'Сергей')")
conn.commit()
for row in c.execute('SELECT * FROM names'):
    print(row)
conn.close()
