################################################################################
##############TOMASZ łOCHMANCZYK################################################
##################LANGUAGE RECOGNITION##########################################
######################PYTHON 3.7.3##############################################
#########################2019###################################################
################################################################################
languages = {'pl' : 0, 'eng' : 1, 'de' : 2, 'oc' : 3, 'lt' : 4, 'pt' : 5, 'es' : 6}
inverseLanguages = {val : key for key, val in languages.items()}

def scrap(webpage):
    r = requests.get(webpage)
    if(r.status_code == 200):
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.get_text()
    else:
        return r.status_code

def letterCounter(string):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
    return [string.count(letter) for letter in alphabet]

def csvIn(txt, file):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(txt)

def readInput(file):
    return np.genfromtxt(file, delimiter=',')
################################################################################
def prepareDataToLearn(learn_csv = 'dataToLearn.csv', target_csv = 'target.csv', data_csv = 'data.csv'):
    open(target_csv, 'w').close()
    open(data_csv, 'w').close()
    with open(learn_csv,'r') as file:
        learn = csv.reader(file, dialect='excel')
        for index in learn:
            webPage = str(scrap(index[0]))
            if webPage.isdigit():
                continue
            else:
                csvIn(str(languages[index[1]]), target_csv)
                csvIn(letterCounter(webPage), data_csv)

def makeModel(model_joblib = 'model.joblib', target_csv = 'target.csv', data_csv = 'data.csv'):
    gnb = GaussianNB()
    target = readInput(target_csv)
    data = readInput(data_csv)
    trainedModel = gnb.fit(data, target)
    dump(trainedModel, model_joblib)

def makePrediction(webpage, model_joblib = 'model.joblib'):
    model = load(model_joblib)
    wp = str(scrap(webpage))
    if wp.isdigit():
        return wp
    else:
        arr = (np.array(letterCounter(wp))).reshape(1,-1)
        prediction = model.predict(arr)
        return inverseLanguages[prediction[0]]
################################################################################
def create():
    prepareDataToLearn(e2.get() + '.csv')
    makeModel(e1.get() + '.joblib')
    updateDisplay(displayVar, 'success')

def pred():
    INFO = makePrediction(e3.get(), e1.get() + '.joblib')
    updateDisplay(displayVar,INFO)

def updateDisplay(var, myString):
    if myString.isdigit():
        var.set('ERR: ' + myString)
    elif myString.endswith('.csv') or myString.endswith('.joblib'):
        var.set(myString)
    else:
        var.set('PRED: ' + myString)

def fileSearch():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fileCont = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
             fileCont.append(str(file))
    return fileCont
##########################################################################################################
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv
from sklearn.naive_bayes import GaussianNB
from joblib import dump, load
import tkinter as tk
import os

root = tk.Tk()

tk.Label(root, text="Model name").grid(row=0)
tk.Label(root, text="File with data").grid(row=1)
tk.Label(root, text="Webpage").grid(row=2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

button = tk.Button(root, text="Create model", command = create).grid(row=3, column=0)
button2 = tk.Button(root, text="Predict", command = pred).grid(row=3, column=1, sticky='W')

msg = tk.Message(root)
displayVar = tk.StringVar()
updateDisplay(displayVar, 'none')
msg.config(textvariable = displayVar)
msg.grid(row=4, columnspan = 2)

r = 0
for file in fileSearch():
    if file.endswith('.csv') or file.endswith('.joblib'):
        msg = tk.Message(root)
        Var = tk.StringVar()
        updateDisplay(Var, str(file))
        msg.config(textvariable = Var)
        msg.grid(row=r, column = 2, columnspan = 2)
        r += 1

root.mainloop()


'''
print("welcome in program which recognize languages from webpages!")

while True:
    print("Would you like to make model or predict something?")
    a = int(input("1 - make model \n2 - predict\n0 - exit\n"))
    if a == 1:

        inDataToLearn = input("enter a file which consist data to learn from or leave it empty if you want to choose deflaut one\n\nADD ' .csv ' AT THE END!!!\n")
        if inDataToLearn != "":
            prepareDataToLearn(inDataToLearn)
        else:
            prepareDataToLearn()

        modelName = input("name the model which you are creating now or leave it empty\n\nADD ' .joblib ' AT THE END!!!\n")
        if modelName != "":
            makeModel(modelName)
        else:
            makeModel()
        print("Congratulations you have made your own model!")

    if a == 2:
        modelName = input("name the model which you want now or leave it empty\n\nADD ' .joblib ' AT THE END!!!\n")
        webpage = input("enter the website which you want to recognaize: \n")
        if modelName != "":
            print(makePrediction(webpage, modelName))
        else:
            print(makePrediction(webpage))

    if a == 0:
        break
'''
