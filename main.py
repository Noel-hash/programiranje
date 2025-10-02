STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bio', 'bila', 'što', 'ga', 'mu', 'joj', 'ih']

def ucitaj_tekst(filepath):
    try:
    #ovdje ide logika za čitanje datoteke
        with open (filepath,'r',encoding='utf-8') as file:
         sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f'greška: Datoteka na putanji {filepath} ne postoji.')
        return None #vraća prazan skup podataka, ako ne nađe datoteku
 
#Funkcija koja prociscava tekst
def ocisti_tekst(tekst):
    #ovdje ide logika za pročišćavanje teksta
    tekst = tekst.lower()
    interpunkcija = ['.',',','!','?',':',';','"',"'",'(',')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci
    return tekst
#Funkcija za brojanje frekvencije riječi u tekstu
def broji_frekvenciju(lista_rijeci):
    # 1. Kreiramo prazan rječnik koji će čuvati rezultate
    rjecnik_frekvencija = {}
    # 2. Prolazimo kroz svaku riječ u primljenoj listi.
    for rijec in lista_rijeci:
        if rijec in rjecnik_frekvencija:
            rjecnik_frekvencija[rijec] +=1
        else:
            rjecnik_frekvencija[rijec] = 1
    return rjecnik_frekvencija
 
 #ciscen je teksta od veznika i slicnih "nebitnih" rijeci
def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):
    ocisceni_rjecnik = {}
    for rijec, frekvencija in rjecnik_frekvencija.items():
        if rijec not in stop_words_lista:
            ocisceni_rjecnik[rijec] = frekvencija
    return ocisceni_rjecnik
 
#glavni dio programa
if __name__ == '__main__':
    filepath = 'tekst.txt'
    print(f'učitavam tekst iz datoteke :{filepath}')
 
    ucitani_tekst = ucitaj_tekst(filepath)
 
    if ucitani_tekst:
        print('\ntekst uspješno učitan. slijedi ispis sadržaja:')
        print('-' * 40)
        print(ucitani_tekst)
        print('-' * 40)
    else:
        print('program se prekida jer tekst nije učitan.')
    procisceni_tekst = ocisti_tekst(ucitani_tekst)
    if procisceni_tekst:
        print ("Pročišćeni tekst je:")
        print('-' * 40)
        print(procisceni_tekst)
        print('-' * 40)
        #Novi dio - pozivamo novu funkciju
        print("Brojim frekvenciju riječi...")
        broj_rijeci = broji_frekvenciju(procisceni_tekst)
        print("Brojanje završeno!")
          
        #   Ispitivamo rezultat da vidimo šta smo dobili
        print("\n--- Riječnik frekvencija ---")
        print(broj_rijeci)
        print("----------------------------")

        #Faza 3: filtriranje i sortiranje
        ociscene_frekvenicje = ukloni_stop_words(broj_rijeci, STOP_WORDS)
        print("\n--- Očišćeni rječnik frekvencija ---")
        print  (ociscene_frekvenicje)
        print("-----------------------------")

    else:
        print("program se prekida jer tekst nije pročišćen")