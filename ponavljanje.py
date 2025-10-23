"""
Ovo je višeredni komentar
"""
# -*- coding: utf-8 -*-

#Ovo je jednolinijski komentar

#1. Tipovi podataka

broj = 10 # int (integer - cijeli broj
tekst = "Ovo je rečenica." # string (tekst) - niz znakova
znak = 'a' # char (caracter - znak)
cijena=1.5 # float - Decimalni broj
istina = True # bool (boolean) - True/False                     



# Grananje (if/elif/else)
""""
if broj > 5:
    print("Broj je veći od 5")
elif broj == 5:
    print("Broj je jednak 5.")
else:
    print("Broj je manji 5.")

if not istina:
    print("False")
else:
    print("True")

""" 
#Zadatak 

"""
#print("Upiši trenutnu temperaturu:")
#temperatura = input()
#temperatura = int(temperatura)

temperatura = int(input("Upiši trenutnu temperaturu: "))

if temperatura <= 0:
    print("Ledenica")
elif temperatura >=0 and temperatura <=15:
    print("Hladno")
elif temperatura >15 and temperatura <=25:
    print("Ugodno")
else:
    print("Vruće")

"""
#Petlje

for i in range(0, 10, 3):
    print(i)