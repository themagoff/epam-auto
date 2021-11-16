import requests


def download_site():
    r = requests.get('http://epam.com')
    html = r.text
    with open('task04.html', 'w', encoding='utf-8') as file:
        file.write(html)
