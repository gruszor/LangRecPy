'''
re beatifulsoup

sklearn
numpy



'''
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python')
print (r.text)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.get_text())
