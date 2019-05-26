def scrap(webpage):
    r = requests.get(webpage)
    if(r.status_code == 200):
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.get_text()
    else:
        return None
    
def count(string):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
    #return {letter: string.count(letter) for letter in alphabet}
    return [string.count(letter) for letter in alphabet]

def csvin(txt, file):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(txt)    

    
    #with open(file, 'a') as sheet:
     #   sheet.write(txt)



              
##########################################################################################################    
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv

#from numpy import genfromtxt

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
stats = {letter: (soup.get_text().lower()).count(letter) for letter in alphabet}
statss = [(soup.get_text().lower()).count(letter) for letter in alphabet]
print(stats)  

with open('model1','w') as plik:
    plik.write(str(stats))
    plik.write('cipsko')

with open('model1','r') as plik:
    print(plik.read())

a = ['ang',1,2,3,4]
b = 'dupsko'
c = ' no nwm '


csvin(a,'csvtst.csv')
csvin(b,'csvtst.csv')
csvin(c,'csvtst.csv')
csvin(statss,'csvtst.csv')

csvin(a,'csvtst2.csv')
csvin(a,'csvtst2.csv')

my_data = np.genfromtxt('csvtst2.csv', delimiter=',')
