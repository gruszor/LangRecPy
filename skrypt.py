Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> numpy.version.version
'1.16.3'
>>> import scipy
>>> scipy.version.version
'1.3.0'
>>> joblib.version.version
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    joblib.version.version
NameError: name 'joblib' is not defined
>>> import joblib
>>> joblib.version.version
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    joblib.version.version
AttributeError: module 'joblib' has no attribute 'version'
>>> joblib.version
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    joblib.version
AttributeError: module 'joblib' has no attribute 'version'
>>> import scikit-learn
SyntaxError: invalid syntax
>>> import scikitlearn
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import scikitlearn
ModuleNotFoundError: No module named 'scikitlearn'
>>> import sklearn
>>> 
================= RESTART: E:/Python projects/sklearntst.py =================
None
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
0.0064551850000000854
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 58, in <module>
    plik.write(stats)
TypeError: write() argument must be str, not dict
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
0.006625851999999988
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
0.007581677999999981
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
>>> plik
<_io.TextIOWrapper name='model1' mode='r' encoding='cp1252'>
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 60, in <module>
    b = dupsko
NameError: name 'dupsko' is not defined
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 64, in <module>
    csvin(a,'csvtst.csv')
  File "E:\Python projects\lngrec.py", line 15, in csvin
    sheet.write(txt)
TypeError: write() argument must be str, not list
>>> import csv
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 56, in <module>
    statss = [string.count(letter) for letter in alphabet]
  File "E:\Python projects\lngrec.py", line 56, in <listcomp>
    statss = [string.count(letter) for letter in alphabet]
NameError: name 'string' is not defined
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 56, in <module>
    statss = [string.count(letter) for letter in alphabet]
  File "E:\Python projects\lngrec.py", line 56, in <listcomp>
    statss = [string.count(letter) for letter in alphabet]
NameError: name 'string' is not defined
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 78, in <module>
    my_data = genfromtxt('my_file.csv', delimiter=',')
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\npyio.py", line 1744, in genfromtxt
    fhd = iter(np.lib._datasource.open(fname, 'rt', encoding=encoding))
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\_datasource.py", line 266, in open
    return ds.open(path, mode, encoding=encoding, newline=newline)
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\_datasource.py", line 624, in open
    raise IOError("%s not found." % path)
OSError: my_file.csv not found.
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 78, in <module>
    my_data = genfromtxt('csvtst.csv', delimiter=',')
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\npyio.py", line 2075, in genfromtxt
    raise ValueError(errmsg)
ValueError: Some errors were detected !
    Line #3 (got 6 columns instead of 4)
    Line #5 (got 8 columns instead of 4)
    Line #7 (got 25 columns instead of 4)
    Line #11 (got 6 columns instead of 4)
    Line #13 (got 8 columns instead of 4)
    Line #15 (got 25 columns instead of 4)
    Line #19 (got 6 columns instead of 4)
    Line #21 (got 8 columns instead of 4)
    Line #23 (got 25 columns instead of 4)
    Line #27 (got 6 columns instead of 4)
    Line #29 (got 8 columns instead of 4)
    Line #31 (got 25 columns instead of 4)
    Line #35 (got 6 columns instead of 4)
    Line #37 (got 8 columns instead of 4)
    Line #39 (got 25 columns instead of 4)
>>> my_data
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    my_data
NameError: name 'my_data' is not defined
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 78, in <module>
    my_data = np.genfromtxt('csvtst.csv', delimiter=',')
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\npyio.py", line 2075, in genfromtxt
    raise ValueError(errmsg)
ValueError: Some errors were detected !
    Line #3 (got 6 columns instead of 4)
    Line #5 (got 8 columns instead of 4)
    Line #7 (got 25 columns instead of 4)
    Line #11 (got 6 columns instead of 4)
    Line #13 (got 8 columns instead of 4)
    Line #15 (got 25 columns instead of 4)
    Line #19 (got 6 columns instead of 4)
    Line #21 (got 8 columns instead of 4)
    Line #23 (got 25 columns instead of 4)
    Line #27 (got 6 columns instead of 4)
    Line #29 (got 8 columns instead of 4)
    Line #31 (got 25 columns instead of 4)
    Line #35 (got 6 columns instead of 4)
    Line #37 (got 8 columns instead of 4)
    Line #39 (got 25 columns instead of 4)
    Line #43 (got 6 columns instead of 4)
    Line #45 (got 8 columns instead of 4)
    Line #47 (got 25 columns instead of 4)
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
>>> my_data
array([[1., 2., 3., 4.],
       [1., 2., 3., 4.]])
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 81, in <module>
    my_data = np.genfromtxt('csvtst2.csv', delimiter=',')
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\npyio.py", line 2075, in genfromtxt
    raise ValueError(errmsg)
ValueError: Some errors were detected !
    Line #5 (got 5 columns instead of 4)
    Line #7 (got 5 columns instead of 4)
>>> import sklearn
>>> a = sklearn.GaussianNB()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a = sklearn.GaussianNB()
AttributeError: module 'sklearn' has no attribute 'GaussianNB'
>>> gnb = sklearn.GaussianNB()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    gnb = sklearn.GaussianNB()
AttributeError: module 'sklearn' has no attribute 'GaussianNB'
>>> gnb = GaussianNB()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    gnb = GaussianNB()
NameError: name 'GaussianNB' is not defined
>>> from sklearn.naive_bayes import GaussianNB
>>> gnb = GaussianNB()
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 81, in <module>
    my_data = np.genfromtxt('csvtst2.csv', delimiter=',')
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\npyio.py", line 2075, in genfromtxt
    raise ValueError(errmsg)
ValueError: Some errors were detected !
    Line #5 (got 5 columns instead of 4)
    Line #7 (got 5 columns instead of 4)
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================

{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}
{'a': 692, 'b': 198, 'c': 348, 'd': 407, 'e': 1016, 'f': 267, 'g': 223, 'h': 294, 'i': 714, 'j': 42, 'k': 45, 'l': 419, 'm': 285, 'n': 718, 'o': 693, 'p': 391, 'q': 33, 'r': 570, 's': 683, 't': 1004, 'u': 398, 'w': 228, 'x': 35, 'y': 171, 'z': 0}cipsko
>>> my_data
array([[1., 2., 3., 4.],
       [1., 2., 3., 4.],
       [1., 2., 3., 4.],
       [1., 2., 3., 4.]])
>>> my_data[0][0]
1.0
>>> my_data[3][2]
3.0
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
<!DOCTYPE html>
<html class="client-nojs" lang="pl" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Primus Classic – Wikipedia, wolna encyklopedia</title>
<script>document.documentElement.className=document.documentElement.className.replace(/(^|\s)client-nojs(\s|$)/,"$1client-js$2");RLCONF={"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":!1,"wgNamespaceNumber":0,"wgPageName":"Primus_Classic","wgTitle":"Primus Classic","wgCurRevisionId":54847616,"wgRevisionId":54847616,"wgArticleId":4392428,"wgIsArticle":!0,"wgIsRedirect":!1,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Kolarstwo w Belgii","Brabancja Flamandzka","Wyścigi kolarskie jednodniowe"],"wgBreakFrames":!1,"wgPageContentLanguage":"pl","wgPageContentModel":"wikitext","wgSeparatorTransformTable":[",\t."," \t,"],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","styczeń","luty","marzec","kwiecień","maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","grudzień"],"wgMonthNamesShort":["","sty","lut","mar","kwi","maj","cze","lip","sie","wrz","paź","lis","gru"],"wgRelevantPageName":
"Primus_Classic","wgRelevantArticleId":4392428,"wgRequestId":"XOrbxgpAMFgAALK3XXcAAADW","wgCSPNonce":!1,"wgIsProbablyEditable":!0,"wgRelevantPageIsProbablyEditable":!0,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgFlaggedRevsParams":{"tags":{"accuracy":{"levels":1,"quality":2,"pristine":4}}},"wgStableRevisionId":54847616,"wgMediaViewerOnClick":!0,"wgMediaViewerEnabledByDefault":!0,"wgPopupsReferencePreviews":!1,"wgPopupsConflictsWithNavPopupGadget":!1,"wgVisualEditor":{"pageLanguageCode":"pl","pageLanguageDir":"ltr","pageVariantFallbacks":"pl"},"wgMFDisplayWikibaseDescriptions":{"search":!0,"nearby":!0,"watchlist":!0,"tagline":!0},"wgRelatedArticles":null,"wgRelatedArticlesUseCirrusSearch":!0,"wgRelatedArticlesOnlyUseCirrusSearch":!1,"wgWMESchemaEditAttemptStepOversample":!1,"wgPoweredByHHVM":!0,"wgULSCurrentAutonym":"polski","wgNoticeProject":"wikipedia","wgCentralNoticeCookiesToDelete":[],"wgCentralNoticeCategoriesUsingLegacy":["Fundraising",
"fundraising"],"wgWikibaseItemId":"Q3113739","wgCentralAuthMobileDomain":!1,"wgEditSubmitButtonLabelPublish":!0};RLSTATE={"ext.gadget.small-references":"ready","ext.gadget.main-page-css":"ready","ext.globalCssJs.user.styles":"ready","ext.globalCssJs.site.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","ext.globalCssJs.site":"ready","user":"ready","user.options":"loading","user.tokens":"loading","ext.cite.styles":"ready","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","mediawiki.toc.styles":"ready","wikibase.client.init":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready","ext.3d.styles":"ready","ext.flaggedRevs.basic":"ready","mediawiki.skinning.interface":"ready","skins.vector.styles":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","site","mediawiki.page.startup","mediawiki.page.ready","mediawiki.toc",
"mediawiki.searchSuggest","ext.gadget.ll-script-loader","ext.gadget.maps","ext.gadget.heading-icons","ext.gadget.refToolbar","ext.gadget.edit-buttons","ext.gadget.edit-summaries","ext.gadget.edit-first-section","ext.gadget.edit-summary-warning","ext.gadget.wikibugs","ext.gadget.nuxTBKeys","ext.gadget.enhanced-upload","ext.gadget.map-toggler","ext.gadget.ReferenceTooltips","ext.gadget.narrowFootnoteColumns","ext.gadget.WDsearch","ext.gadget.main-page-js","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.compactlinks","ext.uls.interface","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.flaggedRevs.advanced","skins.vector.js"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.implement("user.options@0i6mxc2",function($,jQuery,require,module){/*@nomin*/mw.user.options.set({"variant":"pl"});
});mw.loader.implement("user.tokens@0tffind",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});});</script>
<link rel="stylesheet" href="/w/load.php?lang=pl&amp;modules=ext.3d.styles%7Cext.cite.styles%7Cext.flaggedRevs.basic%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cmediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.skinning.interface%7Cmediawiki.toc.styles%7Cskins.vector.styles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector"/>
<script async="" src="/w/load.php?lang=pl&amp;modules=startup&amp;only=scripts&amp;skin=vector"></script>
<meta name="ResourceLoaderDynamicStyles" content=""/>
<link rel="stylesheet" href="/w/load.php?lang=pl&amp;modules=ext.gadget.main-page-css%2Csmall-references&amp;only=styles&amp;skin=vector"/>
<link rel="stylesheet" href="/w/load.php?lang=pl&amp;modules=site.styles&amp;only=styles&amp;skin=vector"/>
<meta name="generator" content="MediaWiki 1.34.0-wmf.6"/>
<meta name="referrer" content="origin"/>
<meta name="referrer" content="origin-when-crossorigin"/>
<meta name="referrer" content="origin-when-cross-origin"/>
<meta property="og:image" content="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG/1200px-Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG"/>
<link rel="alternate" href="android-app://org.wikipedia/http/pl.m.wikipedia.org/wiki/Primus_Classic"/>
<link rel="alternate" type="application/x-wiki" title="Edytuj" href="/w/index.php?title=Primus_Classic&amp;action=edit"/>
<link rel="edit" title="Edytuj" href="/w/index.php?title=Primus_Classic&amp;action=edit"/>
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png"/>
<link rel="shortcut icon" href="/static/favicon/wikipedia.ico"/>
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (pl)"/>
<link rel="EditURI" type="application/rsd+xml" href="//pl.wikipedia.org/w/api.php?action=rsd"/>
<link rel="license" href="//creativecommons.org/licenses/by-sa/3.0/"/>
<link rel="canonical" href="https://pl.wikipedia.org/wiki/Primus_Classic"/>
<link rel="dns-prefetch" href="//login.wikimedia.org"/>
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<!--[if lt IE 9]><script src="/w/load.php?lang=qqx&amp;modules=html5shiv&amp;only=scripts&amp;skin=fallback&amp;sync=1"></script><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Primus_Classic rootpage-Primus_Classic skin-vector action-view">
<div id="mw-page-base" class="noprint"></div>
<div id="mw-head-base" class="noprint"></div>
<div id="content" class="mw-body" role="main">
	<a id="top"></a>
	<div id="siteNotice" class="mw-body-content"><!-- CentralNotice --></div>
	<div class="mw-indicators mw-body-content">
</div>

	<h1 id="firstHeading" class="firstHeading" lang="pl">Primus Classic</h1>
	
	<div id="bodyContent" class="mw-body-content">
		<div id="siteSub" class="noprint">Z Wikipedii, wolnej encyklopedii</div>
		<div id="contentSub"></div>
		
		
		
		<div id="jump-to-nav"></div>
		<a class="mw-jump-link" href="#mw-head">Przejdź do nawigacji</a>
		<a class="mw-jump-link" href="#p-search">Przejdź do wyszukiwania</a>
		<div id="mw-content-text" lang="pl" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/Plik:Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem,_20_september_2014,_aankomst_(B32).JPG" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/07/Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG/220px-Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG" decoding="async" width="220" height="187" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/07/Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG/330px-Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/07/Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG/440px-Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG 2x" data-file-width="3942" data-file-height="3353" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/Plik:Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem,_20_september_2014,_aankomst_(B32).JPG" class="internal" title="Powiększ"></a></div>Podium w roku 2014: <a href="/wiki/Tosh_Van_der_Sande" title="Tosh Van der Sande">Tosh Van der Sande</a> (2), <a href="/wiki/Greg_Van_Avermaet" title="Greg Van Avermaet">Greg Van Avermaet</a> (1) i <a href="/wiki/Micha%C5%82_Go%C5%82a%C5%9B" title="Michał Gołaś">Michał Gołaś</a> (3)</div></div></div>
<p><b>Primus Classic</b> – <a href="/wiki/Kolarstwo_szosowe" title="Kolarstwo szosowe">kolarski</a> <a href="/wiki/Klasyk_(kolarstwo)" title="Klasyk (kolarstwo)">wyścig jednodniowy</a>, rozgrywany w <a href="/wiki/Belgia" title="Belgia">Belgii</a> w prowincji <a href="/wiki/Brabancja_Flamandzka" title="Brabancja Flamandzka">Brabancja Flamandzka</a> od 1982. Zaliczany jest do cyklu <a href="/wiki/UCI_Europe_Tour" title="UCI Europe Tour">UCI Europe Tour</a>, w którym posiada najwyższą kategorię 1.HC.
</p>
<div id="toc" class="toc"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none" /><div class="toctitle" lang="pl" dir="ltr"><h2>Spis treści</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Historia"><span class="tocnumber">1</span> <span class="toctext">Historia</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Lista_zwycięzców"><span class="tocnumber">2</span> <span class="toctext">Lista zwycięzców</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Uwagi"><span class="tocnumber">3</span> <span class="toctext">Uwagi</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Bibliografia"><span class="tocnumber">4</span> <span class="toctext">Bibliografia</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#Linki_zewnętrzne"><span class="tocnumber">5</span> <span class="toctext">Linki zewnętrzne</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Historia">Historia</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Primus_Classic&amp;veaction=edit&amp;section=1" class="mw-editsection-visualeditor" title="Edytuj sekcję: Historia">edytuj</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Primus_Classic&amp;action=edit&amp;section=1" title="Edytuj sekcję: Historia">edytuj kod</a><span class="mw-editsection-bracket">]</span></span></h2>
<p>Początkowo wyścig nosił nazwę <b>GP Impanis</b> (Grote Prijs Raymond Impanis). W latach 1995–2004 i 2007–2008 nie był organizowany. W 2005 był zawodami dla juniorów, w 2006 dla zawodników elity bez kontraktów, a w 2009 i 2010 dla amatorów. W 2011 ponownie stał się wyścigiem zawodowców gdy został przyłączony do <a href="/wiki/UCI_Europe_Tour" title="UCI Europe Tour">UCI Europe Tour</a> z kategorią 1.2. Rok później zyskał wyższą kategorię 1.1, a w 2015 1.HC. Zmieniała się również jego nazwa: w latach 2011-2013 był to <b>GP Impanis-Van Petegem</b>, w latach 2014-2016 <b>Primus Classic Impanis - Van Petegem</b>, a od 2017 Primus Classic.
</p><p>Rekordzistą pod względem zwycięstw jest Holender, Wiebren Veenstra, który dwukrotnie stawał na najwyższym stopniu podium. Najlepszym rezultatem osiągniętym w wyścigu przez Polaka było 3. miejsce zajęte przez <a href="/wiki/Micha%C5%82_Go%C5%82a%C5%9B" title="Michał Gołaś">Michała Gołasia</a> w 2014 roku.
</p>
<h2><span id="Lista_zwyci.C4.99zc.C3.B3w"></span><span class="mw-headline" id="Lista_zwycięzców">Lista zwycięzców</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Primus_Classic&amp;veaction=edit&amp;section=2" class="mw-editsection-visualeditor" title="Edytuj sekcję: Lista zwycięzców">edytuj</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Primus_Classic&amp;action=edit&amp;section=2" title="Edytuj sekcję: Lista zwycięzców">edytuj kod</a><span class="mw-editsection-bracket">]</span></span></h2>
<table id="toc" cellpadding="2" width="100%">

<tbody><tr>
<td valign="top">
<ul><li>2018  <a href="/w/index.php?title=Taco_Van_Der_Hoorn&amp;action=edit&amp;redlink=1" class="new" title="Taco Van Der Hoorn (strona nie istnieje)">Taco Van Der Hoorn</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/22px-Flag_of_the_Netherlands.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/33px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/44px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;</span><a href="/wiki/Holandia" title="Holandia">Holandia</a></li>
<li>2017	<a href="/wiki/Matteo_Trentin" title="Matteo Trentin">Matteo Trentin</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/22px-Flag_of_Italy.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/33px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/44px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" />&#160;</span><a href="/wiki/W%C5%82ochy" title="Włochy">Włochy</a></li>
<li>2016	<a href="/wiki/Fernando_Gaviria" title="Fernando Gaviria">Fernando Gaviria</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/22px-Flag_of_Colombia.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/33px-Flag_of_Colombia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/44px-Flag_of_Colombia.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;</span><a href="/wiki/Kolumbia" title="Kolumbia">Kolumbia</a></li>
<li>2015	<a href="/w/index.php?title=Sean_De_Bie&amp;action=edit&amp;redlink=1" class="new" title="Sean De Bie (strona nie istnieje)">Sean De Bie</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>2014	<a href="/wiki/Greg_Van_Avermaet" title="Greg Van Avermaet">Greg Van Avermaet</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>2013	<a href="/wiki/Sep_Vanmarcke" title="Sep Vanmarcke">Sep Vanmarcke</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>2012	<a href="/wiki/Andr%C3%A9_Greipel" title="André Greipel">André Greipel</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/22px-Flag_of_Germany.svg.png" decoding="async" width="22" height="13" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/33px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/44px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" />&#160;</span><a href="/wiki/Niemcy" title="Niemcy">Niemcy</a></li>
<li>2011	<a href="/w/index.php?title=Sander_Cordeel&amp;action=edit&amp;redlink=1" class="new" title="Sander Cordeel (strona nie istnieje)">Sander Cordeel</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>2010<sup id="cite_ref-uwaga1_1-0" class="reference"><a href="#cite_note-uwaga1-1">[a]</a></sup> <a href="/w/index.php?title=Joeri_Clauwaert&amp;action=edit&amp;redlink=1" class="new" title="Joeri Clauwaert (strona nie istnieje)">Joeri Clauwaert</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>2009<sup id="cite_ref-uwaga1_1-1" class="reference"><a href="#cite_note-uwaga1-1">[a]</a></sup> <a href="/w/index.php?title=Maxim_Debusschere&amp;action=edit&amp;redlink=1" class="new" title="Maxim Debusschere (strona nie istnieje)">Maxim Debusschere</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>2006<sup id="cite_ref-uwaga2_2-0" class="reference"><a href="#cite_note-uwaga2-2">[b]</a></sup> <a href="/w/index.php?title=Kevin_Peeters&amp;action=edit&amp;redlink=1" class="new" title="Kevin Peeters (strona nie istnieje)">Kevin Peeters</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>2005<sup id="cite_ref-uwaga3_3-0" class="reference"><a href="#cite_note-uwaga3-3">[c]</a></sup> <a href="/w/index.php?title=Thomas_Volckaert&amp;action=edit&amp;redlink=1" class="new" title="Thomas Volckaert (strona nie istnieje)">Thomas Volckaert</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>1994	<a href="/w/index.php?title=Carlo_Bomans&amp;action=edit&amp;redlink=1" class="new" title="Carlo Bomans (strona nie istnieje)">Carlo Bomans</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li></ul>
</td>
<td valign="top">
<ul><li>1993	<a href="/wiki/Phil_Anderson" title="Phil Anderson">Phil Anderson</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/22px-Flag_of_Australia.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/33px-Flag_of_Australia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/44px-Flag_of_Australia.svg.png 2x" data-file-width="1280" data-file-height="640" />&#160;</span><a href="/wiki/Australia" title="Australia">Australia</a></li>
<li>1992	<a href="/w/index.php?title=Louis_De_Koning&amp;action=edit&amp;redlink=1" class="new" title="Louis De Koning (strona nie istnieje)">Louis De Koning</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/22px-Flag_of_the_Netherlands.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/33px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/44px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;</span><a href="/wiki/Holandia" title="Holandia">Holandia</a></li>
<li>1991	<a href="/w/index.php?title=Wiebren_Veenstra&amp;action=edit&amp;redlink=1" class="new" title="Wiebren Veenstra (strona nie istnieje)">Wiebren Veenstra</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/22px-Flag_of_the_Netherlands.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/33px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/44px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;</span><a href="/wiki/Holandia" title="Holandia">Holandia</a></li>
<li>1990	<a href="/w/index.php?title=Wiebren_Veenstra&amp;action=edit&amp;redlink=1" class="new" title="Wiebren Veenstra (strona nie istnieje)">Wiebren Veenstra</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/22px-Flag_of_the_Netherlands.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/33px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/44px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;</span><a href="/wiki/Holandia" title="Holandia">Holandia</a></li>
<li>1989	<a href="/w/index.php?title=Eric_Vanderaerden&amp;action=edit&amp;redlink=1" class="new" title="Eric Vanderaerden (strona nie istnieje)">Eric Vanderaerden</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>1988	<a href="/w/index.php?title=Stephen_Hodge&amp;action=edit&amp;redlink=1" class="new" title="Stephen Hodge (strona nie istnieje)">Stephen Hodge</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/22px-Flag_of_Australia.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/33px-Flag_of_Australia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/44px-Flag_of_Australia.svg.png 2x" data-file-width="1280" data-file-height="640" />&#160;</span><a href="/wiki/Australia" title="Australia">Australia</a></li>
<li>1987	<a href="/w/index.php?title=Paul_Haghedooren&amp;action=edit&amp;redlink=1" class="new" title="Paul Haghedooren (strona nie istnieje)">Paul Haghedooren</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>1986	<a href="/w/index.php?title=Allan_Peiper&amp;action=edit&amp;redlink=1" class="new" title="Allan Peiper (strona nie istnieje)">Allan Peiper</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/22px-Flag_of_Australia.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/33px-Flag_of_Australia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/44px-Flag_of_Australia.svg.png 2x" data-file-width="1280" data-file-height="640" />&#160;</span><a href="/wiki/Australia" title="Australia">Australia</a></li>
<li>1985	<a href="/w/index.php?title=Jelle_Nijdam&amp;action=edit&amp;redlink=1" class="new" title="Jelle Nijdam (strona nie istnieje)">Jelle Nijdam</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/22px-Flag_of_the_Netherlands.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/33px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/44px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;</span><a href="/wiki/Holandia" title="Holandia">Holandia</a></li>
<li>1984	<a href="/w/index.php?title=Ad_Wijnands&amp;action=edit&amp;redlink=1" class="new" title="Ad Wijnands (strona nie istnieje)">Ad Wijnands</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/22px-Flag_of_the_Netherlands.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/33px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/44px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;</span><a href="/wiki/Holandia" title="Holandia">Holandia</a></li>
<li>1983	<a href="/w/index.php?title=Ludo_Peeters&amp;action=edit&amp;redlink=1" class="new" title="Ludo Peeters (strona nie istnieje)">Ludo Peeters</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li>
<li>1982	<a href="/w/index.php?title=Willem_Peeters&amp;action=edit&amp;redlink=1" class="new" title="Willem Peeters (strona nie istnieje)">Willem Peeters</a> <span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/22px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/33px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/44px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="450" data-file-height="300" />&#160;</span><a href="/wiki/Belgia" title="Belgia">Belgia</a></li></ul>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Uwagi">Uwagi</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Primus_Classic&amp;veaction=edit&amp;section=3" class="mw-editsection-visualeditor" title="Edytuj sekcję: Uwagi">edytuj</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Primus_Classic&amp;action=edit&amp;section=3" title="Edytuj sekcję: Uwagi">edytuj kod</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="do-not-make-smaller refsection refsection-uwagi ll-script ll-script-uwagi"><div class="mw-references-wrap"><ol class="references">
<li id="cite_note-uwaga1-1"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-uwaga1_1-0">a</a></sup> <sup><a href="#cite_ref-uwaga1_1-1">b</a></sup></span> <span class="reference-text">Wyścig amatorów.</span>
</li>
<li id="cite_note-uwaga2-2"><span class="mw-cite-backlink"><a href="#cite_ref-uwaga2_2-0">↑</a></span> <span class="reference-text">Wyścig kolarzy elity bez kontraktów.</span>
</li>
<li id="cite_note-uwaga3-3"><span class="mw-cite-backlink"><a href="#cite_ref-uwaga3_3-0">↑</a></span> <span class="reference-text">Wyścig juniorów.</span>
</li>
</ol></div></div>
<h2><span class="mw-headline" id="Bibliografia">Bibliografia</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Primus_Classic&amp;veaction=edit&amp;section=4" class="mw-editsection-visualeditor" title="Edytuj sekcję: Bibliografia">edytuj</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Primus_Classic&amp;action=edit&amp;section=4" title="Edytuj sekcję: Bibliografia">edytuj kod</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a rel="nofollow" class="external text" href="http://www.radsportseiten.net/wedstrijdfiche.php?wedstrijdid=1067">Wyścig w latach 1982-2006 na stronie <i>cyclingarchives.com</i></a></li>
<li><a rel="nofollow" class="external text" href="http://www.cyclingarchives.com/wedstrijdfiche.php?wedstrijdid=17939">Wyścig od 2009 na stronie <i>cyclingarchives.com</i></a></li>
<li><a rel="nofollow" class="external text" href="https://www.procyclingstats.com/race/gp-impanis-van-petegem/overview">Primus Classic na stronie <i>procyclingstats.com</i></a></li>
<li><a rel="nofollow" class="external text" href="http://www.bikeraceinfo.com/races/GP-Impanis-van-petegem/GP-Impanis-van-petegem-index.html">Historia wyścigu na stronie<i>bikeraceinfo.com</i></a></li></ul>
<h2><span id="Linki_zewn.C4.99trzne"></span><span class="mw-headline" id="Linki_zewnętrzne">Linki zewnętrzne</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Primus_Classic&amp;veaction=edit&amp;section=5" class="mw-editsection-visualeditor" title="Edytuj sekcję: Linki zewnętrzne">edytuj</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Primus_Classic&amp;action=edit&amp;section=5" title="Edytuj sekcję: Linki zewnętrzne">edytuj kod</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a rel="nofollow" class="external text" href="http://impanis-vanpetegem.be/">Oficjalna strona</a></li></ul>
<!-- 
NewPP limit report
Parsed by mw1266
Cached time: 20190518180447
Cache expiry: 2592000
Dynamic content: false
CPU time usage: 0.124 seconds
Real time usage: 0.173 seconds
Preprocessor visited node count: 2144/1000000
Preprocessor generated node count: 0/1500000
Post‐expand include size: 8555/2097152 bytes
Template argument size: 1781/2097152 bytes
Highest expansion depth: 7/40
Expensive parser function count: 0/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 1282/5000000 bytes
Number of Wikibase entities loaded: 0/400
Lua time usage: 0.008/10.000 seconds
Lua memory usage: 546 KB/50 MB
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  117.625      1 -total
 69.10%   81.284     25 Szablon:Państwo
 24.98%   29.387      1 Szablon:Uwagi
 15.53%   18.261      6 Szablon:Państwo_dane_NED
 14.46%   17.011     25 Szablon:Państwo/core
 13.78%   16.211     13 Szablon:Państwo_dane_BEL
  9.36%   11.011      3 Szablon:Państwo_dane_AUS
  8.67%   10.195      1 Szablon:Państwo_dane_GER
  7.89%    9.284      1 Szablon:Państwo_dane_ITA
  7.81%    9.189      1 Szablon:Państwo_dane_COL
-->

<!-- Saved in parser cache with key plwiki:stable-pcache:idhash:4392428-0!canonical and timestamp 20190518180447 and revision id 54847616
 -->
</div><noscript><img src="//pl.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" title="" width="1" height="1" style="border: none; position: absolute;" /></noscript></div>
		
		<div class="printfooter">Źródło: „<a dir="ltr" href="https://pl.wikipedia.org/w/index.php?title=Primus_Classic&amp;oldid=54847616">https://pl.wikipedia.org/w/index.php?title=Primus_Classic&amp;oldid=54847616</a>”</div>
		
		<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Specjalna:Kategorie" title="Specjalna:Kategorie">Kategorie</a>: <ul><li><a href="/wiki/Kategoria:Kolarstwo_w_Belgii" title="Kategoria:Kolarstwo w Belgii">Kolarstwo w Belgii</a></li><li><a href="/wiki/Kategoria:Brabancja_Flamandzka" title="Kategoria:Brabancja Flamandzka">Brabancja Flamandzka</a></li><li><a href="/wiki/Kategoria:Wy%C5%9Bcigi_kolarskie_jednodniowe" title="Kategoria:Wyścigi kolarskie jednodniowe">Wyścigi kolarskie jednodniowe</a></li></ul></div></div>
		
		<div class="visualClear"></div>
		
	</div>
</div>

		<div id="mw-navigation">
			<h2>Menu nawigacyjne</h2>
			<div id="mw-head">
									<div id="p-personal" role="navigation" aria-labelledby="p-personal-label">
						<h3 id="p-personal-label">Narzędzia osobiste</h3>
						<ul>
							<li id="pt-anonuserpage">Nie jesteś zalogowany</li><li id="pt-anontalk"><a href="/wiki/Specjalna:Moja_dyskusja" title="Dyskusja użytkownika dla tego adresu IP [n]" accesskey="n">Dyskusja</a></li><li id="pt-anoncontribs"><a href="/wiki/Specjalna:M%C3%B3j_wk%C5%82ad" title="Lista edycji wykonanych z tego adresu IP [y]" accesskey="y">Edycje</a></li><li id="pt-createaccount"><a href="/w/index.php?title=Specjalna:Utw%C3%B3rz_konto&amp;returnto=Primus+Classic" title="Zachęcamy do stworzenia konta i zalogowania, ale nie jest to obowiązkowe.">Utwórz konto</a></li><li id="pt-login"><a href="/w/index.php?title=Specjalna:Zaloguj&amp;returnto=Primus+Classic" title="Zachęcamy do zalogowania się, choć nie jest to obowiązkowe. [o]" accesskey="o">Zaloguj się</a></li>						</ul>
					</div>
									<div id="left-navigation">
										<div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label">
						<h3 id="p-namespaces-label">Przestrzenie nazw</h3>
						<ul>
							<li id="ca-nstab-main" class="selected"><span><a href="/wiki/Primus_Classic" title="Zobacz stronę treści [c]" accesskey="c">Artykuł</a></span></li><li id="ca-talk"><span><a href="/wiki/Dyskusja:Primus_Classic" rel="discussion" title="Dyskusja o zawartości tej strony [t]" accesskey="t">Dyskusja</a></span></li>						</ul>
					</div>
										<div id="p-variants" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-variants-label">
												<input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-variants-label" />
						<h3 id="p-variants-label">
							<span>Warianty</span>
						</h3>
						<ul class="menu">
													</ul>
					</div>
									</div>
				<div id="right-navigation">
										<div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label">
						<h3 id="p-views-label">Widok</h3>
						<ul>
							<li id="ca-view" class="collapsible selected"><span><a href="/wiki/Primus_Classic">Czytaj</a></span></li><li id="ca-ve-edit" class="collapsible"><span><a href="/w/index.php?title=Primus_Classic&amp;veaction=edit" title="Edytuj tę stronę [v]" accesskey="v">Edytuj</a></span></li><li id="ca-edit" class="collapsible"><span><a href="/w/index.php?title=Primus_Classic&amp;action=edit" title="Edytuj tę stronę [e]" accesskey="e">Edytuj kod źródłowy</a></span></li><li id="ca-history" class="collapsible"><span><a href="/w/index.php?title=Primus_Classic&amp;action=history" title="Starsze wersje tej strony. [h]" accesskey="h">Historia i autorzy</a></span></li>						</ul>
					</div>
										<div id="p-cactions" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-cactions-label">
						<input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-cactions-label" />
						<h3 id="p-cactions-label"><span>Więcej</span></h3>
						<ul class="menu">
													</ul>
					</div>
										<div id="p-search" role="search">
						<h3>
							<label for="searchInput">Szukaj</label>
						</h3>
						<form action="/w/index.php" id="searchform">
							<div id="simpleSearch">
								<input type="search" name="search" placeholder="Przeszukaj Wikipedię" title="Przeszukaj Wikipedię [f]" accesskey="f" id="searchInput"/><input type="hidden" value="Specjalna:Szukaj" name="title"/><input type="submit" name="fulltext" value="Szukaj" title="Szukaj wprowadzonego tekstu w treści stron" id="mw-searchButton" class="searchButton mw-fallbackSearchButton"/><input type="submit" name="go" value="Przejdź" title="Przejdź do strony o dokładnie takim tytule, o ile istnieje" id="searchButton" class="searchButton"/>							</div>
						</form>
					</div>
									</div>
			</div>
			<div id="mw-panel">
				<div id="p-logo" role="banner"><a class="mw-wiki-logo" href="/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna" title="Strona główna"></a></div>
						<div class="portal" role="navigation" id="p-navigation" aria-labelledby="p-navigation-label">
			<h3 id="p-navigation-label">Nawigacja</h3>
			<div class="body">
								<ul>
					<li id="n-mainpage-description"><a href="/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna" title="Przejdź na stronę główną [z]" accesskey="z">Strona główna</a></li><li id="n-randompage"><a href="/wiki/Specjalna:Losowa_strona" title="Załaduj losową stronę [x]" accesskey="x">Losuj artykuł</a></li><li id="n-Kategorie"><a href="/wiki/Portal:Kategorie_G%C5%82%C3%B3wne">Kategorie artykułów</a></li><li id="n-Featured-articles"><a href="/wiki/Wikipedia:Wyr%C3%B3%C5%BCniona_zawarto%C5%9B%C4%87_Wikipedii">Najlepsze artykuły</a></li><li id="n-FAQ"><a href="/wiki/Pomoc:FAQ">Częste pytania (FAQ)</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-zmiany" aria-labelledby="p-zmiany-label">
			<h3 id="p-zmiany-label">Dla czytelników</h3>
			<div class="body">
								<ul>
					<li id="n-czytelnicy"><a href="/wiki/Wikipedia:O_Wikipedii">O Wikipedii</a></li><li id="n-bug_in_article"><a href="/wiki/Wikipedia:Zg%C5%82o%C5%9B_b%C5%82%C4%85d_w_artykule">Zgłoś błąd</a></li><li id="n-bad-image"><a href="/wiki/Wikipedia:Zg%C5%82oszone_grafiki">Zgłoś błąd w pliku</a></li><li id="n-contact"><a href="/wiki/Wikipedia:Kontakt_z_wikipedystami">Kontakt</a></li><li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_pl.wikipedia.org&amp;uselang=pl" title="Pomóż nam">Wspomóż Wikipedię</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-edytorzy" aria-labelledby="p-edytorzy-label">
			<h3 id="p-edytorzy-label">Dla wikipedystów</h3>
			<div class="body">
								<ul>
					<li id="n-pierwsze-kroki"><a href="/wiki/Pomoc:Pierwsze_kroki">Pierwsze kroki</a></li><li id="n-portal"><a href="/wiki/Wikipedia:Portal_wikipedyst%C3%B3w" title="O projekcie - co możesz zrobić, gdzie możesz znaleźć informacje">Portal wikipedystów</a></li><li id="n-Noticeboard"><a href="/wiki/Wikipedia:Tablica_og%C5%82osze%C5%84">Ogłoszenia</a></li><li id="n-Guidelines"><a href="/wiki/Wikipedia:Zasady">Zasady</a></li><li id="n-helppage-name"><a href="/wiki/Pomoc:Spis_tre%C5%9Bci">Pomoc</a></li><li id="n-recentchanges"><a href="/wiki/Specjalna:Ostatnie_zmiany" title="Lista ostatnich zmian w Wikipedii. [r]" accesskey="r">Ostatnie zmiany</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-tb" aria-labelledby="p-tb-label">
			<h3 id="p-tb-label">Narzędzia</h3>
			<div class="body">
								<ul>
					<li id="t-whatlinkshere"><a href="/wiki/Specjalna:Linkuj%C4%85ce/Primus_Classic" title="Pokaż listę wszystkich stron linkujących do tej strony [j]" accesskey="j">Linkujące</a></li><li id="t-recentchangeslinked"><a href="/wiki/Specjalna:Zmiany_w_linkowanych/Primus_Classic" rel="nofollow" title="Ostatnie zmiany w stronach, do których ta strona linkuje [k]" accesskey="k">Zmiany w linkowanych</a></li><li id="t-upload"><a href="//pl.wikipedia.org/wiki/Wikipedia:Prześlij_plik" title="Prześlij pliki [u]" accesskey="u">Prześlij plik</a></li><li id="t-specialpages"><a href="/wiki/Specjalna:Strony_specjalne" title="Lista wszystkich stron specjalnych [q]" accesskey="q">Strony specjalne</a></li><li id="t-permalink"><a href="/w/index.php?title=Primus_Classic&amp;oldid=54847616" title="Stały link do tej wersji strony">Link do tej wersji</a></li><li id="t-info"><a href="/w/index.php?title=Primus_Classic&amp;action=info" title="Więcej informacji na temat tej strony">Informacje o tej stronie</a></li><li id="t-wikibase"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q3113739" title="Link do powiązanego elementu w repozytorium danych [g]" accesskey="g">Element Wikidanych</a></li><li id="t-cite"><a href="/w/index.php?title=Specjalna:Cytuj&amp;page=Primus_Classic&amp;id=54847616" title="Informacja o tym jak należy cytować tę stronę">Cytowanie tego artykułu</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-wikibase-otherprojects" aria-labelledby="p-wikibase-otherprojects-label">
			<h3 id="p-wikibase-otherprojects-label">W innych projektach</h3>
			<div class="body">
								<ul>
					<li class="wb-otherproject-link wb-otherproject-commons"><a href="https://commons.wikimedia.org/wiki/Category:Grote_Prijs_Impanis-Van_Petegem" hreflang="en">Wikimedia Commons</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-coll-print_export" aria-labelledby="p-coll-print_export-label">
			<h3 id="p-coll-print_export-label">Drukuj lub eksportuj</h3>
			<div class="body">
								<ul>
					<li id="coll-create_a_book"><a href="/w/index.php?title=Specjalna:Ksi%C4%85%C5%BCka&amp;bookcmd=book_creator&amp;referer=Primus+Classic">Utwórz książkę</a></li><li id="coll-download-as-rl"><a href="/w/index.php?title=Specjalna:ElectronPdf&amp;page=Primus+Classic&amp;action=show-download-screen">Pobierz jako PDF</a></li><li id="coll-download-as-rdf2latex"><a href="/w/index.php?title=Specjalna:Ksi%C4%85%C5%BCka&amp;bookcmd=render_article&amp;arttitle=Primus+Classic&amp;returnto=Primus+Classic&amp;oldid=54847616&amp;writer=rdf2latex">Pobierz jako PDF</a></li><li id="t-print"><a href="/w/index.php?title=Primus_Classic&amp;printable=yes" title="Wersja do wydruku [p]" accesskey="p">Wersja do druku</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-lang" aria-labelledby="p-lang-label">
			<h3 id="p-lang-label">W innych językach</h3>
			<div class="body">
								<ul>
					<li class="interlanguage-link interwiki-ca"><a href="https://ca.wikipedia.org/wiki/Gran_Premi_Impanis-Van_Petegem" title="Gran Premi Impanis-Van Petegem – kataloński" lang="ca" hreflang="ca" class="interlanguage-link-target">Català</a></li><li class="interlanguage-link interwiki-da"><a href="https://da.wikipedia.org/wiki/Grand_Prix_Impanis-Van_Petegem" title="Grand Prix Impanis-Van Petegem – duński" lang="da" hreflang="da" class="interlanguage-link-target">Dansk</a></li><li class="interlanguage-link interwiki-de"><a href="https://de.wikipedia.org/wiki/Primus_Classic" title="Primus Classic – niemiecki" lang="de" hreflang="de" class="interlanguage-link-target">Deutsch</a></li><li class="interlanguage-link interwiki-en"><a href="https://en.wikipedia.org/wiki/Grand_Prix_Impanis-Van_Petegem" title="Grand Prix Impanis-Van Petegem – angielski" lang="en" hreflang="en" class="interlanguage-link-target">English</a></li><li class="interlanguage-link interwiki-es"><a href="https://es.wikipedia.org/wiki/Gran_Premio_Impanis-Van_Petegem" title="Gran Premio Impanis-Van Petegem – hiszpański" lang="es" hreflang="es" class="interlanguage-link-target">Español</a></li><li class="interlanguage-link interwiki-fr"><a href="https://fr.wikipedia.org/wiki/Primus_Classic" title="Primus Classic – francuski" lang="fr" hreflang="fr" class="interlanguage-link-target">Français</a></li><li class="interlanguage-link interwiki-it"><a href="https://it.wikipedia.org/wiki/Primus_Classic" title="Primus Classic – włoski" lang="it" hreflang="it" class="interlanguage-link-target">Italiano</a></li><li class="interlanguage-link interwiki-nl"><a href="https://nl.wikipedia.org/wiki/Primus_Classic_Impanis-Van_Petegem" title="Primus Classic Impanis-Van Petegem – niderlandzki" lang="nl" hreflang="nl" class="interlanguage-link-target">Nederlands</a></li><li class="interlanguage-link interwiki-no"><a href="https://no.wikipedia.org/wiki/Grand_Prix_Impanis-Van_Petegem" title="Grand Prix Impanis-Van Petegem – norweski" lang="no" hreflang="no" class="interlanguage-link-target">Norsk</a></li><li class="interlanguage-link interwiki-pt"><a href="https://pt.wikipedia.org/wiki/Grande_Pr%C3%AAmio_Impanis-Van_Petegem" title="Grande Prêmio Impanis-Van Petegem – portugalski" lang="pt" hreflang="pt" class="interlanguage-link-target">Português</a></li><li class="interlanguage-link interwiki-ru"><a href="https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%BD-%D0%BF%D1%80%D0%B8_%D0%98%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%81%E2%80%93%D0%92%D0%B0%D0%BD_%D0%9F%D0%B5%D1%82%D0%B5%D0%B3%D0%B5%D0%BC" title="Гран-при Импанис–Ван Петегем – rosyjski" lang="ru" hreflang="ru" class="interlanguage-link-target">Русский</a></li>				</ul>
				<div class="after-portlet after-portlet-lang"><span class="wb-langlinks-edit wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q3113739#sitelinks-wikipedia" title="Edytuj linki pomiędzy wersjami językowymi" class="wbc-editpage">Edytuj linki</a></span></div>			</div>
		</div>
				</div>
		</div>
				<div id="footer" role="contentinfo">
						<ul id="footer-info">
								<li id="footer-info-lastmod"> Tę stronę ostatnio edytowano 26 paź 2018, 20:57.</li>
								<li id="footer-info-copyright">Tekst udostępniany na <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.pl">licencji Creative Commons: uznanie autorstwa, na tych samych warunkach</a>, z możliwością obowiązywania dodatkowych ograniczeń.
Zobacz szczegółowe informacje o <a href="https://foundation.wikimedia.org/wiki/Warunki_korzystania">warunkach korzystania</a>.</li>
							</ul>
						<ul id="footer-places">
								<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Privacy_policy" class="extiw" title="wmf:Privacy policy">Polityka ochrony prywatności</a></li>
								<li id="footer-places-about"><a href="/wiki/Wikipedia:O_Wikipedii" title="Wikipedia:O Wikipedii">O Wikipedii</a></li>
								<li id="footer-places-disclaimer"><a href="/wiki/Wikipedia:Korzystasz_z_Wikipedii_tylko_na_w%C5%82asn%C4%85_odpowiedzialno%C5%9B%C4%87" title="Wikipedia:Korzystasz z Wikipedii tylko na własną odpowiedzialność">Korzystasz z Wikipedii tylko na własną odpowiedzialność</a></li>
								<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Dla deweloperów</a></li>
								<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Cookie_statement">Komunikat na temat ciasteczek</a></li>
								<li id="footer-places-mobileview"><a href="//pl.m.wikipedia.org/w/index.php?title=Primus_Classic&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Wersja mobilna</a></li>
							</ul>
										<ul id="footer-icons" class="noprint">
										<li id="footer-copyrightico">
						<a href="https://wikimediafoundation.org/"><img src="/static/images/wikimedia-button.png" srcset="/static/images/wikimedia-button-1.5x.png 1.5x, /static/images/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation"/></a>					</li>
										<li id="footer-poweredbyico">
						<a href="https://www.mediawiki.org/"><img src="/static/images/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/poweredby_mediawiki_132x47.png 1.5x, /static/images/poweredby_mediawiki_176x62.png 2x" width="88" height="31"/></a>					</li>
									</ul>
						<div style="clear: both;"></div>
		</div>
		

<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.124","walltime":"0.173","ppvisitednodes":{"value":2144,"limit":1000000},"ppgeneratednodes":{"value":0,"limit":1500000},"postexpandincludesize":{"value":8555,"limit":2097152},"templateargumentsize":{"value":1781,"limit":2097152},"expansiondepth":{"value":7,"limit":40},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":1282,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  117.625      1 -total"," 69.10%   81.284     25 Szablon:Państwo"," 24.98%   29.387      1 Szablon:Uwagi"," 15.53%   18.261      6 Szablon:Państwo_dane_NED"," 14.46%   17.011     25 Szablon:Państwo/core"," 13.78%   16.211     13 Szablon:Państwo_dane_BEL","  9.36%   11.011      3 Szablon:Państwo_dane_AUS","  8.67%   10.195      1 Szablon:Państwo_dane_GER","  7.89%    9.284      1 Szablon:Państwo_dane_ITA","  7.81%    9.189      1 Szablon:Państwo_dane_COL"]},"scribunto":{"limitreport-timeusage":{"value":"0.008","limit":"10.000"},"limitreport-memusage":{"value":559259,"limit":52428800}},"cachereport":{"origin":"mw1266","timestamp":"20190518180447","ttl":2592000,"transientcontent":false}}});});</script>
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","name":"Primus Classic","url":"https:\/\/pl.wikipedia.org\/wiki\/Primus_Classic","sameAs":"http:\/\/www.wikidata.org\/entity\/Q3113739","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q3113739","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2018-10-26T18:57:43Z","image":"https:\/\/upload.wikimedia.org\/wikipedia\/commons\/0\/07\/Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG","headline":"Wy\u015bcig kolarski"}</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":126,"wgHostname":"mw1253"});});</script>
</body>
</html>

{'a': 645, 'b': 109, 'c': 277, 'd': 286, 'e': 737, 'f': 53, 'g': 267, 'h': 90, 'i': 610, 'j': 87, 'k': 157, 'l': 325, 'm': 211, 'n': 411, 'o': 413, 'p': 230, 'q': 16, 'r': 391, 's': 408, 't': 524, 'u': 209, 'w': 265, 'x': 55, 'y': 164, 'z': 112}
{'a': 645, 'b': 109, 'c': 277, 'd': 286, 'e': 737, 'f': 53, 'g': 267, 'h': 90, 'i': 610, 'j': 87, 'k': 157, 'l': 325, 'm': 211, 'n': 411, 'o': 413, 'p': 230, 'q': 16, 'r': 391, 's': 408, 't': 524, 'u': 209, 'w': 265, 'x': 55, 'y': 164, 'z': 112}cipsko
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================





Primus Classic – Wikipedia, wolna encyklopedia
document.documentElement.className=document.documentElement.className.replace(/(^|\s)client-nojs(\s|$)/,"$1client-js$2");RLCONF={"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":!1,"wgNamespaceNumber":0,"wgPageName":"Primus_Classic","wgTitle":"Primus Classic","wgCurRevisionId":54847616,"wgRevisionId":54847616,"wgArticleId":4392428,"wgIsArticle":!0,"wgIsRedirect":!1,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Kolarstwo w Belgii","Brabancja Flamandzka","Wyścigi kolarskie jednodniowe"],"wgBreakFrames":!1,"wgPageContentLanguage":"pl","wgPageContentModel":"wikitext","wgSeparatorTransformTable":[",\t."," \t,"],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","styczeń","luty","marzec","kwiecień","maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","grudzień"],"wgMonthNamesShort":["","sty","lut","mar","kwi","maj","cze","lip","sie","wrz","paź","lis","gru"],"wgRelevantPageName":
"Primus_Classic","wgRelevantArticleId":4392428,"wgRequestId":"XOrbxgpAMFgAALK3XXcAAADW","wgCSPNonce":!1,"wgIsProbablyEditable":!0,"wgRelevantPageIsProbablyEditable":!0,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgFlaggedRevsParams":{"tags":{"accuracy":{"levels":1,"quality":2,"pristine":4}}},"wgStableRevisionId":54847616,"wgMediaViewerOnClick":!0,"wgMediaViewerEnabledByDefault":!0,"wgPopupsReferencePreviews":!1,"wgPopupsConflictsWithNavPopupGadget":!1,"wgVisualEditor":{"pageLanguageCode":"pl","pageLanguageDir":"ltr","pageVariantFallbacks":"pl"},"wgMFDisplayWikibaseDescriptions":{"search":!0,"nearby":!0,"watchlist":!0,"tagline":!0},"wgRelatedArticles":null,"wgRelatedArticlesUseCirrusSearch":!0,"wgRelatedArticlesOnlyUseCirrusSearch":!1,"wgWMESchemaEditAttemptStepOversample":!1,"wgPoweredByHHVM":!0,"wgULSCurrentAutonym":"polski","wgNoticeProject":"wikipedia","wgCentralNoticeCookiesToDelete":[],"wgCentralNoticeCategoriesUsingLegacy":["Fundraising",
"fundraising"],"wgWikibaseItemId":"Q3113739","wgCentralAuthMobileDomain":!1,"wgEditSubmitButtonLabelPublish":!0};RLSTATE={"ext.gadget.small-references":"ready","ext.gadget.main-page-css":"ready","ext.globalCssJs.user.styles":"ready","ext.globalCssJs.site.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","ext.globalCssJs.site":"ready","user":"ready","user.options":"loading","user.tokens":"loading","ext.cite.styles":"ready","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","mediawiki.toc.styles":"ready","wikibase.client.init":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready","ext.3d.styles":"ready","ext.flaggedRevs.basic":"ready","mediawiki.skinning.interface":"ready","skins.vector.styles":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","site","mediawiki.page.startup","mediawiki.page.ready","mediawiki.toc",
"mediawiki.searchSuggest","ext.gadget.ll-script-loader","ext.gadget.maps","ext.gadget.heading-icons","ext.gadget.refToolbar","ext.gadget.edit-buttons","ext.gadget.edit-summaries","ext.gadget.edit-first-section","ext.gadget.edit-summary-warning","ext.gadget.wikibugs","ext.gadget.nuxTBKeys","ext.gadget.enhanced-upload","ext.gadget.map-toggler","ext.gadget.ReferenceTooltips","ext.gadget.narrowFootnoteColumns","ext.gadget.WDsearch","ext.gadget.main-page-js","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.compactlinks","ext.uls.interface","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.flaggedRevs.advanced","skins.vector.js"];
(RLQ=window.RLQ||[]).push(function(){mw.loader.implement("user.options@0i6mxc2",function($,jQuery,require,module){/*@nomin*/mw.user.options.set({"variant":"pl"});
});mw.loader.implement("user.tokens@0tffind",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});});































Primus Classic

Z Wikipedii, wolnej encyklopedii


Przejdź do nawigacji
Przejdź do wyszukiwania
 Podium w roku 2014: Tosh Van der Sande (2), Greg Van Avermaet (1) i Michał Gołaś (3)
Primus Classic – kolarski wyścig jednodniowy, rozgrywany w Belgii w prowincji Brabancja Flamandzka od 1982. Zaliczany jest do cyklu UCI Europe Tour, w którym posiada najwyższą kategorię 1.HC.

Spis treści

1 Historia
2 Lista zwycięzców
3 Uwagi
4 Bibliografia
5 Linki zewnętrzne


Historia[edytuj | edytuj kod]
Początkowo wyścig nosił nazwę GP Impanis (Grote Prijs Raymond Impanis). W latach 1995–2004 i 2007–2008 nie był organizowany. W 2005 był zawodami dla juniorów, w 2006 dla zawodników elity bez kontraktów, a w 2009 i 2010 dla amatorów. W 2011 ponownie stał się wyścigiem zawodowców gdy został przyłączony do UCI Europe Tour z kategorią 1.2. Rok później zyskał wyższą kategorię 1.1, a w 2015 1.HC. Zmieniała się również jego nazwa: w latach 2011-2013 był to GP Impanis-Van Petegem, w latach 2014-2016 Primus Classic Impanis - Van Petegem, a od 2017 Primus Classic.
Rekordzistą pod względem zwycięstw jest Holender, Wiebren Veenstra, który dwukrotnie stawał na najwyższym stopniu podium. Najlepszym rezultatem osiągniętym w wyścigu przez Polaka było 3. miejsce zajęte przez Michała Gołasia w 2014 roku.

Lista zwycięzców[edytuj | edytuj kod]



2018  Taco Van Der Hoorn  Holandia
2017	Matteo Trentin  Włochy
2016	Fernando Gaviria  Kolumbia
2015	Sean De Bie  Belgia
2014	Greg Van Avermaet  Belgia
2013	Sep Vanmarcke  Belgia
2012	André Greipel  Niemcy
2011	Sander Cordeel  Belgia
2010[a] Joeri Clauwaert  Belgia
2009[a] Maxim Debusschere  Belgia
2006[b] Kevin Peeters  Belgia
2005[c] Thomas Volckaert  Belgia
1994	Carlo Bomans  Belgia


1993	Phil Anderson  Australia
1992	Louis De Koning  Holandia
1991	Wiebren Veenstra  Holandia
1990	Wiebren Veenstra  Holandia
1989	Eric Vanderaerden  Belgia
1988	Stephen Hodge  Australia
1987	Paul Haghedooren  Belgia
1986	Allan Peiper  Australia
1985	Jelle Nijdam  Holandia
1984	Ad Wijnands  Holandia
1983	Ludo Peeters  Belgia
1982	Willem Peeters  Belgia

Uwagi[edytuj | edytuj kod]

↑ a b Wyścig amatorów.

↑ Wyścig kolarzy elity bez kontraktów.

↑ Wyścig juniorów.


Bibliografia[edytuj | edytuj kod]
Wyścig w latach 1982-2006 na stronie cyclingarchives.com
Wyścig od 2009 na stronie cyclingarchives.com
Primus Classic na stronie procyclingstats.com
Historia wyścigu na stroniebikeraceinfo.com
Linki zewnętrzne[edytuj | edytuj kod]
Oficjalna strona




Źródło: „https://pl.wikipedia.org/w/index.php?title=Primus_Classic&oldid=54847616”
Kategorie: Kolarstwo w BelgiiBrabancja FlamandzkaWyścigi kolarskie jednodniowe




Menu nawigacyjne


Narzędzia osobiste

Nie jesteś zalogowanyDyskusjaEdycjeUtwórz kontoZaloguj się 



Przestrzenie nazw

ArtykułDyskusja 




Warianty







Widok

CzytajEdytujEdytuj kod źródłowyHistoria i autorzy 



Więcej





Szukaj



 







Nawigacja


Strona głównaLosuj artykułKategorie artykułówNajlepsze artykułyCzęste pytania (FAQ) 



Dla czytelników


O WikipediiZgłoś błądZgłoś błąd w plikuKontaktWspomóż Wikipedię 



Dla wikipedystów


Pierwsze krokiPortal wikipedystówOgłoszeniaZasadyPomocOstatnie zmiany 



Narzędzia


LinkująceZmiany w linkowanychPrześlij plikStrony specjalneLink do tej wersjiInformacje o tej stronieElement WikidanychCytowanie tego artykułu 



W innych projektach


Wikimedia Commons 



Drukuj lub eksportuj


Utwórz książkęPobierz jako PDFPobierz jako PDFWersja do druku 



W innych językach


CatalàDanskDeutschEnglishEspañolFrançaisItalianoNederlandsNorskPortuguêsРусский 
Edytuj linki 





 Tę stronę ostatnio edytowano 26 paź 2018, 20:57.
Tekst udostępniany na licencji Creative Commons: uznanie autorstwa, na tych samych warunkach, z możliwością obowiązywania dodatkowych ograniczeń.
Zobacz szczegółowe informacje o warunkach korzystania.


Polityka ochrony prywatności
O Wikipedii
Korzystasz z Wikipedii tylko na własną odpowiedzialność
Dla deweloperów
Komunikat na temat ciasteczek
Wersja mobilna



 

 



(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.124","walltime":"0.173","ppvisitednodes":{"value":2144,"limit":1000000},"ppgeneratednodes":{"value":0,"limit":1500000},"postexpandincludesize":{"value":8555,"limit":2097152},"templateargumentsize":{"value":1781,"limit":2097152},"expansiondepth":{"value":7,"limit":40},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":1282,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  117.625      1 -total"," 69.10%   81.284     25 Szablon:Państwo"," 24.98%   29.387      1 Szablon:Uwagi"," 15.53%   18.261      6 Szablon:Państwo_dane_NED"," 14.46%   17.011     25 Szablon:Państwo/core"," 13.78%   16.211     13 Szablon:Państwo_dane_BEL","  9.36%   11.011      3 Szablon:Państwo_dane_AUS","  8.67%   10.195      1 Szablon:Państwo_dane_GER","  7.89%    9.284      1 Szablon:Państwo_dane_ITA","  7.81%    9.189      1 Szablon:Państwo_dane_COL"]},"scribunto":{"limitreport-timeusage":{"value":"0.008","limit":"10.000"},"limitreport-memusage":{"value":559259,"limit":52428800}},"cachereport":{"origin":"mw1266","timestamp":"20190518180447","ttl":2592000,"transientcontent":false}}});});
{"@context":"https:\/\/schema.org","@type":"Article","name":"Primus Classic","url":"https:\/\/pl.wikipedia.org\/wiki\/Primus_Classic","sameAs":"http:\/\/www.wikidata.org\/entity\/Q3113739","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q3113739","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2018-10-26T18:57:43Z","image":"https:\/\/upload.wikimedia.org\/wikipedia\/commons\/0\/07\/Boortmeerbeek_%26_Haacht_-_Grote_Prijs_Impanis-Van_Petegem%2C_20_september_2014%2C_aankomst_%28B32%29.JPG","headline":"Wy\u015bcig kolarski"}
(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":126,"wgHostname":"mw1253"});});



>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 34, in <module>
    learn = readInput('dataToLearn.csv')
  File "E:\Python projects\lngrec.py", line 20, in readInput
    return np.genfromtxt(file, delimiter=',')
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\npyio.py", line 2075, in genfromtxt
    raise ValueError(errmsg)
ValueError: Some errors were detected !
    Line #14 (got 3 columns instead of 2)
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 34, in <module>
    learn = np.genfromtxt('dataToLearn.csv', delimiter=',')
  File "C:\Users\tomek\AppData\Roaming\Python\Python37\site-packages\numpy\lib\npyio.py", line 2075, in genfromtxt
    raise ValueError(errmsg)
ValueError: Some errors were detected !
    Line #14 (got 3 columns instead of 2)
>>> learn
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    learn
NameError: name 'learn' is not defined
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 39, in <module>
    if learn[index][1] == 'pl':             #TEMP CONSTRUCTION ENUM with languages IN THE FUTURE
TypeError: '_csv.reader' object is not subscriptable
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 39, in <module>
    if learn[index][1] == 'pl':             #TEMP CONSTRUCTION ENUM with languages IN THE FUTURE
NameError: name 'learn' is not defined
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
>>> learn
<_csv.reader object at 0x10772EF0>
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
>>> learn
<_csv.reader object at 0x10CC2EF0>
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
>>> learn
<_csv.reader object at 0x111B2EF0>
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
>>> learn
<_csv.reader object at 0x110C2EF0>
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 39, in <module>
    for index in learn:
ValueError: I/O operation on closed file.
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
['https://pl.wikipedia.org/wiki/Filip_Alzacki', 'pl']
['https://pl.wikipedia.org/wiki/Diecezja_Cassano_all%E2%80%99Jonio', 'pl']
['https://pl.wikipedia.org/wiki/Andrij_Kaniuk', 'pl']
['https://pl.wikipedia.org/wiki/Chalton_(Bedfordshire)', 'pl']
['https://pl.wikipedia.org/wiki/Wiernadski', 'pl']
['https://pl.wikipedia.org/wiki/Dirk_Crois', 'pl']
['https://pl.wikipedia.org/wiki/U-576', 'pl']
['https://pl.wikipedia.org/wiki/Sarejn', 'pl']
['https://pl.wikipedia.org/wiki/Pedro_Segura_y_S%C3%A1enz', 'pl']
['https://en.wikipedia.org/wiki/Battling_Jane', 'eng']
['https://en.wikipedia.org/wiki/Kurzer_Prozess', 'eng']
['https://en.wikipedia.org/wiki/Apion_ervi', 'eng']
['https://en.wikipedia.org/wiki/St_Enghenedl%27s_Church', '_Llanynghenedl', 'eng']
['https://en.wikipedia.org/wiki/Sniperlite', 'eng']
['https://en.wikipedia.org/wiki/Telephone_numbers_in_Lesotho', 'eng']
['https://en.wikipedia.org/wiki/Abergarw', 'eng']
['https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia', 'eng']
['https://en.wikipedia.org/wiki/Stanton_College_Preparatory_School', 'eng']
['https://en.wikipedia.org/wiki/Mikhail_Petrenko', 'eng']
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 44, in <module>
    csvin(0,'target.csv')
  File "E:\Python projects\lngrec.py", line 17, in csvin
    writer.writerow(txt)
_csv.Error: iterable expected, not int
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 48, in <module>
    csvin(count(scrap(learn[index][0])),'data.csv')
TypeError: '_csv.reader' object is not subscriptable
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
['https://pl.wikipedia.org/wiki/Filip_Alzacki', 'pl']
['https://pl.wikipedia.org/wiki/Diecezja_Cassano_all%E2%80%99Jonio', 'pl']
['https://pl.wikipedia.org/wiki/Andrij_Kaniuk', 'pl']
['https://pl.wikipedia.org/wiki/Chalton_(Bedfordshire)', 'pl']
['https://pl.wikipedia.org/wiki/Wiernadski', 'pl']
['https://pl.wikipedia.org/wiki/Dirk_Crois', 'pl']
['https://pl.wikipedia.org/wiki/U-576', 'pl']
['https://pl.wikipedia.org/wiki/Sarejn', 'pl']
['https://pl.wikipedia.org/wiki/Pedro_Segura_y_S%C3%A1enz', 'pl']
['https://en.wikipedia.org/wiki/Battling_Jane', 'eng']
['https://en.wikipedia.org/wiki/Kurzer_Prozess', 'eng']
['https://en.wikipedia.org/wiki/Apion_ervi', 'eng']
['https://en.wikipedia.org/wiki/St_Enghenedl%27s_Church', '_Llanynghenedl', 'eng']
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 48, in <module>
    csvin(count(scrap(index[0])),'data.csv')
  File "E:\Python projects\lngrec.py", line 12, in count
    return [string.count(letter) for letter in alphabet]
  File "E:\Python projects\lngrec.py", line 12, in <listcomp>
    return [string.count(letter) for letter in alphabet]
AttributeError: 'NoneType' object has no attribute 'count'
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
['https://pl.wikipedia.org/wiki/Filip_Alzacki', 'pl']
['https://pl.wikipedia.org/wiki/Diecezja_Cassano_all%E2%80%99Jonio', 'pl']
['https://pl.wikipedia.org/wiki/Andrij_Kaniuk', 'pl']
['https://pl.wikipedia.org/wiki/Chalton_(Bedfordshire)', 'pl']
['https://pl.wikipedia.org/wiki/Wiernadski', 'pl']
['https://pl.wikipedia.org/wiki/Dirk_Crois', 'pl']
['https://pl.wikipedia.org/wiki/U-576', 'pl']
['https://pl.wikipedia.org/wiki/Sarejn', 'pl']
['https://pl.wikipedia.org/wiki/Pedro_Segura_y_S%C3%A1enz', 'pl']
['https://en.wikipedia.org/wiki/Battling_Jane', 'eng']
['https://en.wikipedia.org/wiki/Kurzer_Prozess', 'eng']
['https://en.wikipedia.org/wiki/Apion_ervi', 'eng']
['https://en.wikipedia.org/wiki/St_Enghenedl%27s_Church', '_Llanynghenedl', 'eng']
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 48, in <module>
    csvin(counter(scrap(index[0])),'data.csv')
  File "E:\Python projects\lngrec.py", line 12, in counter
    return [string.count(letter) for letter in alphabet]
  File "E:\Python projects\lngrec.py", line 12, in <listcomp>
    return [string.count(letter) for letter in alphabet]
AttributeError: 'NoneType' object has no attribute 'count'
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
['https://pl.wikipedia.org/wiki/Filip_Alzacki', 'pl']
['https://pl.wikipedia.org/wiki/Diecezja_Cassano_all%E2%80%99Jonio', 'pl']
['https://pl.wikipedia.org/wiki/Andrij_Kaniuk', 'pl']
['https://pl.wikipedia.org/wiki/Chalton_(Bedfordshire)', 'pl']
['https://pl.wikipedia.org/wiki/Wiernadski', 'pl']
['https://pl.wikipedia.org/wiki/Dirk_Crois', 'pl']
['https://pl.wikipedia.org/wiki/U-576', 'pl']
['https://pl.wikipedia.org/wiki/Sarejn', 'pl']
['https://pl.wikipedia.org/wiki/Pedro_Segura_y_S%C3%A1enz', 'pl']
['https://en.wikipedia.org/wiki/Battling_Jane', 'eng']
['https://en.wikipedia.org/wiki/Kurzer_Prozess', 'eng']
['https://en.wikipedia.org/wiki/Apion_ervi', 'eng']
['https://en.wikipedia.org/wiki/St_Enghenedl%27s_Church_Llanynghenedl', 'eng']
Traceback (most recent call last):
  File "E:\Python projects\lngrec.py", line 48, in <module>
    csvin(counter(scrap(index[0])),'data.csv')
  File "E:\Python projects\lngrec.py", line 12, in counter
    return [string.count(letter) for letter in alphabet]
  File "E:\Python projects\lngrec.py", line 12, in <listcomp>
    return [string.count(letter) for letter in alphabet]
AttributeError: 'NoneType' object has no attribute 'count'
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
['https://pl.wikipedia.org/wiki/Filip_Alzacki', 'pl']
['https://pl.wikipedia.org/wiki/Diecezja_Cassano_all%E2%80%99Jonio', 'pl']
['https://pl.wikipedia.org/wiki/Andrij_Kaniuk', 'pl']
['https://pl.wikipedia.org/wiki/Chalton_(Bedfordshire)', 'pl']
['https://pl.wikipedia.org/wiki/Wiernadski', 'pl']
['https://pl.wikipedia.org/wiki/Dirk_Crois', 'pl']
['https://pl.wikipedia.org/wiki/U-576', 'pl']
['https://pl.wikipedia.org/wiki/Sarejn', 'pl']
['https://pl.wikipedia.org/wiki/Pedro_Segura_y_S%C3%A1enz', 'pl']
['https://en.wikipedia.org/wiki/Battling_Jane', 'eng']
['https://en.wikipedia.org/wiki/Kurzer_Prozess', 'eng']
['https://en.wikipedia.org/wiki/Apion_ervi', 'eng']
['https://en.wikipedia.org/wiki/Sniperlite', 'eng']
['https://en.wikipedia.org/wiki/Telephone_numbers_in_Lesotho', 'eng']
['https://en.wikipedia.org/wiki/Abergarw', 'eng']
['https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia', 'eng']
['https://en.wikipedia.org/wiki/Stanton_College_Preparatory_School', 'eng']
['https://en.wikipedia.org/wiki/Mikhail_Petrenko', 'eng']
>>> from sklearn.naive_bayes import GaussianNB
>>> gnb = GaussianNB()
>>> tar = readInput('target.csv')
>>> dat = readInput('data.csv')]
SyntaxError: invalid syntax
>>> dat = readInput('data.csv')
>>> y_pred = gnb.fit(dat, tar)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    y_pred = gnb.fit(dat, tar)
  File "C:\Users\tomek\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\naive_bayes.py", line 189, in fit
    X, y = check_X_y(X, y)
  File "C:\Users\tomek\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\utils\validation.py", line 729, in check_X_y
    check_consistent_length(X, y)
  File "C:\Users\tomek\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\utils\validation.py", line 205, in check_consistent_length
    " samples: %r" % [int(l) for l in lengths])
ValueError: Found input variables with inconsistent numbers of samples: [32, 33]
>>> dat
array([[ 610.,   76.,  223.,  259.,  706.,   35.,  252.,   70.,  585.,
          80.,  145.,  295.,  194.,  381.,  398.,  157.,    4.,  358.,
         375.,  495.,  193.,  224.,   52.,  164.,  102.],
       [1086.,  190.,  344.,  458., 1051.,   52.,  296.,  117., 1126.,
         168.,  287.,  516.,  313.,  623.,  710.,  316.,    4.,  695.,
         547.,  640.,  294.,  393.,   56.,  337.,  339.],
       [ 577.,   82.,  217.,  220.,  631.,   46.,  216.,   74.,  524.,
          73.,  144.,  280.,  157.,  393.,  408.,  154.,    4.,  291.,
         334.,  448.,  166.,  188.,   62.,  139.,  109.],
       [ 628.,   89.,  201.,  259.,  682.,   43.,  214.,   64.,  619.,
          99.,  254.,  237.,  160.,  384.,  408.,  188.,    4.,  435.,
         326.,  496.,  233.,  260.,   62.,  187.,  151.],
       [ 517.,   71.,  174.,  260.,  655.,   62.,  225.,  108.,  507.,
          62.,  121.,  261.,  168.,  381.,  390.,  161.,    4.,  331.,
         315.,  479.,  169.,  183.,   60.,  141.,   72.],
       [ 986.,  113.,  320.,  371.,  915.,   52.,  279.,  111.,  775.,
         164.,  282.,  344.,  224.,  631.,  585.,  232.,    4.,  539.,
         476.,  644.,  280.,  267.,   60.,  303.,  235.],
       [ 443.,   67.,  182.,  213.,  605.,   36.,  216.,   60.,  499.,
          79.,  128.,  249.,  156.,  302.,  330.,  150.,    5.,  310.,
         318.,  427.,  155.,  189.,   53.,  139.,   89.],
       [ 746.,  122.,  274.,  355.,  849.,   58.,  246.,   92.,  713.,
         103.,  255.,  310.,  225.,  556.,  653.,  256.,    4.,  474.,
         410.,  643.,  269.,  325.,   55.,  265.,  245.],
       [ 483.,   74.,  171.,  208.,  581.,   41.,  202.,   56.,  456.,
          71.,  117.,  228.,  154.,  336.,  327.,  149.,    4.,  277.,
         289.,  427.,  161.,  180.,   62.,  124.,   79.],
       [ 707.,  117.,  251.,  288.,  709.,   41.,  255.,   84.,  619.,
          65.,  208.,  313.,  213.,  442.,  507.,  243.,    5.,  478.,
         354.,  563.,  265.,  270.,   55.,  200.,  132.],
       [ 736.,  120.,  302.,  318., 1040.,  116.,  289.,  201.,  753.,
          10.,  108.,  431.,  300.,  577.,  558.,  258.,    8.,  576.,
         539.,  808.,  267.,  181.,   53.,  147.,   12.],
       [ 524.,   98.,  233.,  226.,  833.,   74.,  244.,  104.,  578.,
           7.,  104.,  308.,  243.,  405.,  383.,  215.,    5.,  487.,
         415.,  599.,  250.,  143.,   53.,   83.,   39.],
       [ 425.,   67.,  168.,  186.,  670.,   50.,  179.,   78.,  482.,
           8.,   68.,  234.,  149.,  306.,  319.,  162.,    3.,  293.,
         296.,  466.,  146.,  115.,   56.,   78.,    7.],
       [ 610.,   76.,  223.,  259.,  706.,   35.,  252.,   70.,  585.,
          80.,  145.,  295.,  194.,  381.,  398.,  157.,    4.,  358.,
         375.,  495.,  193.,  224.,   52.,  164.,  102.],
       [1086.,  190.,  344.,  458., 1051.,   52.,  296.,  117., 1126.,
         168.,  287.,  516.,  313.,  623.,  710.,  316.,    4.,  695.,
         547.,  640.,  294.,  393.,   56.,  337.,  339.],
       [ 577.,   82.,  217.,  220.,  631.,   46.,  216.,   74.,  524.,
          73.,  144.,  280.,  157.,  393.,  408.,  154.,    4.,  291.,
         334.,  448.,  166.,  188.,   62.,  139.,  109.],
       [ 628.,   89.,  201.,  259.,  682.,   43.,  214.,   64.,  619.,
          99.,  254.,  237.,  160.,  384.,  408.,  188.,    4.,  435.,
         326.,  496.,  233.,  260.,   62.,  187.,  151.],
       [ 517.,   71.,  174.,  260.,  655.,   62.,  225.,  108.,  507.,
          62.,  121.,  261.,  168.,  381.,  390.,  161.,    4.,  331.,
         315.,  479.,  169.,  183.,   60.,  141.,   72.],
       [ 986.,  113.,  320.,  371.,  915.,   52.,  279.,  111.,  775.,
         164.,  282.,  344.,  224.,  631.,  585.,  232.,    4.,  539.,
         476.,  644.,  280.,  267.,   60.,  303.,  235.],
       [ 443.,   67.,  182.,  213.,  605.,   36.,  216.,   60.,  499.,
          79.,  128.,  249.,  156.,  302.,  330.,  150.,    5.,  310.,
         318.,  427.,  155.,  189.,   53.,  139.,   89.],
       [ 746.,  122.,  274.,  355.,  849.,   58.,  246.,   92.,  713.,
         103.,  255.,  310.,  225.,  556.,  653.,  256.,    4.,  474.,
         410.,  643.,  269.,  325.,   55.,  265.,  245.],
       [ 483.,   74.,  171.,  208.,  581.,   41.,  202.,   56.,  456.,
          71.,  117.,  228.,  154.,  336.,  327.,  149.,    4.,  277.,
         289.,  427.,  161.,  180.,   62.,  124.,   79.],
       [ 707.,  117.,  251.,  288.,  709.,   41.,  255.,   84.,  619.,
          65.,  208.,  313.,  213.,  442.,  507.,  243.,    5.,  478.,
         354.,  563.,  265.,  270.,   55.,  200.,  132.],
       [ 736.,  120.,  302.,  318., 1040.,  116.,  289.,  201.,  753.,
          10.,  108.,  431.,  300.,  577.,  558.,  258.,    8.,  576.,
         539.,  808.,  267.,  181.,   53.,  147.,   12.],
       [ 524.,   98.,  233.,  226.,  833.,   74.,  244.,  104.,  578.,
           7.,  104.,  308.,  243.,  405.,  383.,  215.,    5.,  487.,
         415.,  599.,  250.,  143.,   53.,   83.,   39.],
       [ 425.,   67.,  168.,  186.,  670.,   50.,  179.,   78.,  482.,
           8.,   68.,  234.,  149.,  306.,  319.,  162.,    3.,  293.,
         296.,  466.,  146.,  115.,   56.,   78.,    7.],
       [ 428.,   72.,  173.,  187.,  660.,   51.,  184.,  102.,  463.,
           9.,   70.,  284.,  163.,  298.,  314.,  157.,    3.,  314.,
         298.,  469.,  150.,  120.,   43.,   81.,    7.],
       [ 533.,  108.,  198.,  226.,  849.,   60.,  200.,  141.,  542.,
           9.,   69.,  296.,  188.,  421.,  417.,  171.,    5.,  377.,
         376.,  561.,  207.,  130.,   53.,   91.,   11.],
       [ 391.,   62.,  150.,  174.,  593.,   42.,  198.,   74.,  404.,
           7.,   66.,  219.,  134.,  278.,  270.,  119.,    3.,  285.,
         261.,  420.,  135.,  124.,   39.,   80.,    7.],
       [1885.,  274.,  683.,  861., 2541.,  444.,  546.,  795., 1808.,
          23.,  295.,  992.,  567., 1417., 1487.,  473.,   13., 1504.,
        1301., 1809.,  702.,  345.,   76.,  347.,   48.],
       [1616.,  251.,  788.,  761., 2213.,  259.,  506.,  668., 1471.,
          17.,  184., 1019.,  450., 1436., 1654.,  452.,   10., 1255.,
        1203., 1710.,  553.,  324.,   81.,  302.,   22.],
       [ 552.,   77.,  236.,  239.,  799.,   66.,  237.,  122.,  615.,
           7.,  127.,  286.,  215.,  444.,  423.,  227.,    5.,  434.,
         384.,  625.,  216.,  159.,   49.,   90.,   12.]])
>>> tar
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
>>> 
=================== RESTART: E:\Python projects\lngrec.py ===================
['https://pl.wikipedia.org/wiki/Primus_Classic', 'pl']
['https://pl.wikipedia.org/wiki/Filip_Alzacki', 'pl']
['https://pl.wikipedia.org/wiki/Diecezja_Cassano_all%E2%80%99Jonio', 'pl']
['https://pl.wikipedia.org/wiki/Andrij_Kaniuk', 'pl']
['https://pl.wikipedia.org/wiki/Chalton_(Bedfordshire)', 'pl']
['https://pl.wikipedia.org/wiki/Wiernadski', 'pl']
['https://pl.wikipedia.org/wiki/Dirk_Crois', 'pl']
['https://pl.wikipedia.org/wiki/U-576', 'pl']
['https://pl.wikipedia.org/wiki/Sarejn', 'pl']
['https://pl.wikipedia.org/wiki/Pedro_Segura_y_S%C3%A1enz', 'pl']
['https://en.wikipedia.org/wiki/Battling_Jane', 'eng']
['https://en.wikipedia.org/wiki/Kurzer_Prozess', 'eng']
['https://en.wikipedia.org/wiki/Apion_ervi', 'eng']
['https://en.wikipedia.org/wiki/Sniperlite', 'eng']
['https://en.wikipedia.org/wiki/Telephone_numbers_in_Lesotho', 'eng']
['https://en.wikipedia.org/wiki/Abergarw', 'eng']
['https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia', 'eng']
['https://en.wikipedia.org/wiki/Stanton_College_Preparatory_School', 'eng']
['https://en.wikipedia.org/wiki/Mikhail_Petrenko', 'eng']
>>> from sklearn.naive_bayes import GaussianNB
>>> gnb = GaussianNB()
>>> tar = readInput('target.csv')
>>> dat = readInput('data.csv')
>>> y_pred = gnb.fit(dat, tar)
>>> y_pred = y_pred.predict(np.array(counter(scrap(https://www.numpy.org/devdocs/user/basics.creation.html))))
SyntaxError: invalid syntax
>>> y_pred = y_pred.predict(np.array(counter(scrap('https://www.numpy.org/devdocs/user/basics.creation.html'))))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    y_pred = y_pred.predict(np.array(counter(scrap('https://www.numpy.org/devdocs/user/basics.creation.html'))))
  File "C:\Users\tomek\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\naive_bayes.py", line 65, in predict
    jll = self._joint_log_likelihood(X)
  File "C:\Users\tomek\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\naive_bayes.py", line 430, in _joint_log_likelihood
    X = check_array(X)
  File "C:\Users\tomek\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\utils\validation.py", line 521, in check_array
    "if it contains a single sample.".format(array))
ValueError: Expected 2D array, got 1D array instead:
array=[409  50 133 123 435  94  76 133 279  15  18 148 112 288 278  95   3 373
 261 328 116  46  21 129   4].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
>>> arr = np.array(counter(scrap('https://www.numpy.org/devdocs/user/basics.creation.html')))
>>> ar2 = arr.reshape(-1,1)
>>> y_pred = y_pred.predict(ar2)
>>> print(y_pred)
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
 1.]
>>> arr
array([409,  50, 133, 123, 435,  94,  76, 133, 279,  15,  18, 148, 112,
       288, 278,  95,   3, 373, 261, 328, 116,  46,  21, 129,   4])
>>> ar2
array([[409],
       [ 50],
       [133],
       [123],
       [435],
       [ 94],
       [ 76],
       [133],
       [279],
       [ 15],
       [ 18],
       [148],
       [112],
       [288],
       [278],
       [ 95],
       [  3],
       [373],
       [261],
       [328],
       [116],
       [ 46],
       [ 21],
       [129],
       [  4]])
>>> ar3 = ar2 + ar2
>>> ar3
array([[818],
       [100],
       [266],
       [246],
       [870],
       [188],
       [152],
       [266],
       [558],
       [ 30],
       [ 36],
       [296],
       [224],
       [576],
       [556],
       [190],
       [  6],
       [746],
       [522],
       [656],
       [232],
       [ 92],
       [ 42],
       [258],
       [  8]])
>>> ar2 = arr.reshape(1,-1)
>>> ar2
array([[409,  50, 133, 123, 435,  94,  76, 133, 279,  15,  18, 148, 112,
        288, 278,  95,   3, 373, 261, 328, 116,  46,  21, 129,   4]])
>>> y_pred = y_pred.predict(ar2)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    y_pred = y_pred.predict(ar2)
AttributeError: 'numpy.ndarray' object has no attribute 'predict'
>>> y_pred = gnb.fit(dat, tar)
>>> y_pred = y_pred.predict(ar2)
>>> print(y_pred)
[1.]
>>> y_pred = gnb.fit(dat, tar)
>>> arr = np.array(counter(scrap('https://pl.wikipedia.org/wiki/Okr%C4%99ty_podwodne_typu_Wilk')))
>>> ar2 = arr.reshape(1,-1)
>>> pred = y_pred.predict(ar2)
>>> print(pred)
[0.]
>>> 
