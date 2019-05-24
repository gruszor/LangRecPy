'''
re beatifulsoup

sklearn
numpy



'''
import requests
import time
from bs4 import BeautifulSoup
from collections import Counter

r = requests.get('https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python')
print (r.text)
soup = BeautifulSoup(r.text, 'html.parser')


'''

a = time.perf_counter()
print(Counter(soup.get_text())['a'])
b = time.perf_counter()
print(soup.get_text().count('a'))
c = time.perf_counter()

print(b-a,c-b)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']

for letter in alphabet:
    stats = {}
    stats[letter] = soup.get_text().count(letter)

print(stats)    
'''




alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']

stats = {letter: soup.get_text().count(letter) for letter in alphabet}

print(stats)  
