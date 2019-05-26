def scrap(webpage):
    r = requests.get(webpage)
    if(r.status_code == 200):
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.get_text()
    else:
        return None
    
def counter(string):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
    #return {letter: string.count(letter) for letter in alphabet}
    return [string.count(letter) for letter in alphabet]

def csvin(txt, file):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(txt)    

def readInput(file):
    return np.genfromtxt(file, delimiter=',')



              
##########################################################################################################    
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv
from enum import IntEnum

#LERNING
#data format: webpage, language(acronym)
with open('dataToLearn.csv','r') as file:
    learn = csv.reader(file, dialect='excel')
#learn = np.genfromtxt('dataToLearn.csv', delimiter=',')
#learn = readInput('dataToLearn.csv')

    for index in learn:
        print(index)
  
#for index in csv.reader('dataToLearn'):    
        if index[1] == 'pl':             #TEMP CONSTRUCTION ENUM with languages IN THE FUTURE
            csvin('0','target.csv')
        else:
            csvin('1','target.csv')

        csvin(counter(scrap(index[0])),'data.csv')

'''
r = requests.get('https://pl.wikipedia.org/wiki/Primus_Classic')
print (r.text)
soup = BeautifulSoup(r.text, 'html.parser')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
stats = {letter: (soup.get_text().lower()).count(letter) for letter in alphabet}
statss = [(soup.get_text().lower()).count(letter) for letter in alphabet]
print(soup.get_text())

with open('model1','w') as plik:
    plik.write(str(stats))
    plik.write('sko')

with open('model1','r') as plik:
    print(plik.read())

a = [1,2,3,4]
b = 'duko'
c = ' no nwm '

csvin(a,'csvtst.csv')
csvin(b,'csvtst.csv')
csvin(c,'csvtst.csv')
csvin(statss,'csvtst.csv')

csvin(a,'csvtst2.csv')
csvin(a,'csvtst2.csv')

my_data = np.genfromtxt('csvtst2.csv', delimiter=',')
'''
