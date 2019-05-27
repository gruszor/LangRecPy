def scrap(webpage):
    r = requests.get(webpage)
    if(r.status_code == 200):
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.get_text()
    else:
        return None
    
def letterCounter(string):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
    return [string.count(letter) for letter in alphabet]

def csvIn(txt, file):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(txt)    

def readInput(file):
    return np.genfromtxt(file, delimiter=',')

def prepareDataToLearn(learn_csv = 'dataToLearn.csv', target_csv = 'target.csv', data_csv = 'data.csv'):
    languages = {'pl' : 0, 'eng' : 1}
    
    open(target_csv, 'w').close()
    open(data_csv, 'w').close()

    with open(learn_csv,'r') as file:
        
        learn = csv.reader(file, dialect='excel')
        for index in learn:
            csvIn(str(languages[index[1]]), target_csv)
            csvIn(letterCounter(scrap(index[0])), data_csv)
            
def makeModel(model_joblib = 'model.joblib', target_csv = 'target.csv', data_csv = 'data.csv'):
    gnb = GaussianNB()
    target = readInput(target_csv)
    data = readInput(data_csv)
    trainedModel = gnb.fit(data, target)
    dump(trainedModel, model_joblib)

def makePrediction(webpage, model_joblib = 'model.joblib'):
    languages = {0 : pl', 1 : 'eng'} 
    
    model = load(model_joblib)
    arr = (np.array(counter(scrap(webpage)))).reshape(1,-1)
    prediction = model.predict(arr)
    return languages[prediction]

##########################################################################################################    
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv
from sklearn.naive_bayes import GaussianNB
from joblib import dump, load

#prepareDataToLearn()
'''
#LERNING
#data format: webpage, language(acronym)
with open('dataToLearn.csv','r') as file:
    learn = csv.reader(file, dialect='excel')
    for index in learn:
        if index[1] == 'pl':             #TEMP CONSTRUCTION ENUM with languages IN THE FUTURE
            csvin('0','target.csv')
        else:
            csvin('1','target.csv')
        csvin(counter(scrap(index[0])),'data.csv')
'''
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
