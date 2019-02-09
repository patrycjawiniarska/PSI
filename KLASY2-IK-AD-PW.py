#BIBLIOTEKA IZA KOSMAN ALEKSANDRA DMYTRASZ PATRYCJA WINIARSKA

#informacja od nas
#pracowałyśmy na diagramie Izy Kosman, niestety w trakcie tworzenia tego programu
#dokonane zostały zmiany, ze względu na brak logiczności samego diagramu ( co oczywiscie zauwazylysmy dopiero podczas pisania samego kodu)


# 1 KATALOG BIBLIOTECZNY
# 2. KATALOG UZYTKOWNIKOW
# 3. STAN EGZEMPLARZY
# 4. PRZYKLADOWE FUNKCJE
# 5. MAIN


import sys
from datetime import datetime
from datetime import timedelta





#                                                         1  KATALOG BIBLIOTECZNY
#________________________________________________________________________________
class  AUTOR:
    def __init__(self, imie, nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko

              
class ISBN:
    def __init__(self, ISBN):
        self.ISBN=ISBN
ISBN=[1,2,3]

class TYTUL:
    def __init__(self, tytul,autor,isbn):
        self.tytul=TYTUL
        self.autor=AUTOR(self, imie, nazwisko)
        self.isbn=ISBN(self, ISB)
        
class WYDAWNICTWO:
    def __init__(self, nazwa, rok, miejsce):
        self.nazwa=nazwa
        self.rok= rok
        self.miejsce= miejsce   


class KATALOG_BIBLIOTECZNY: 
    def  __init__(self, egzemplarz, liczba_egzemplarz, miejsce_egzemplarz, katalog_biblioteczny):        
        class EGZEMPLARZ:            
            def __init__(self, autor_egzemplarz, ISBN_egzemplarz, tytul_egzemplarz, wydawnictwo_egzemplarz, status , nr_egzemplarz):
                
                self.autor_egzemplarz=autor_egzemplarz
                self.ISBN_egzemplarz=ISBN_egzemplarz
                self.tytul_egzemplarz=tytul_egzemplarz
                self.wydawnictwo_egzemplarz=wydawnictwo_egzemplarz
                self.status=status
                self.nr_egzemplarz=nr_egzemplarz
                

            def AUTOR(self, imie, nazwisko):              
                self.autor_egzemplarz.AUTOR()
                

            def ISBN(self, ISBN):               
               self.ISBN_egzemplarz.ISBN()
               

            def TYTUL(self, tytul,autor,isbn):            
                self.tytul_egzemplarz.TYTUL()
                

            def WYDAWNICTWO(self, nazwa, rok, miejsce):
                self.wydawnictwo_egzemplarz.WYDAWNICTWO()

        class CZASOPISMOKASETA(EGZEMPLARZ):
            pass
        class KSIAZKA(EGZEMPLARZ):
            pass
        
        self.egzemplarz=EGZEMPLARZ(self, autor_egzemplarz, ISBN_egzemplarz, tytul_egzemplarz, wydawnictwo_egzemplarz, status , nr_egzemplarz)        
        self.liczba_egzemplarz=liczba_egzemplarz
        self.miejsce_egzemplarz=miejssce_egzemplarz
        self.katalog_biblioteczny=katalog_biblioteczny
        
#KATALOG_BIBLIOTECZNY((('1','1'),'1',('1',('imie1','nazwisko1'),'1'),'1',('1','1','1')),'1','1','1')




#                                                                    2  KATALOG UZYTKOWNIKOW
#____________________________________________________________________________________________

class KONTO_UZYTKOWNIKA:
    def __init__(self,wypozyczenia_konta, rezerwacje_konta, zwroty_konta):
        self.wypozyczenia_konta=WYPOZYCZENIE(self,katalog_biblioteczny, katalog_uzytkownikow, data)
        self.rezerwacje_konta=REZERWACJA(self,katalog_biblioteczny, katalog_uzytkownikow, data)
        self.zwroty_konta=ZWROT(self,katalog_biblioteczny, katalog_uzytkownikow, data)

   
class KATALOG_UZYTKOWNIKOW:
    def __init__(object):

        class OSOBA:
            def __init__(self, imie, nazwisko, adres, data_ur, PESEL, login, haslo, id_osoba, konto_uzytkownika, katalog_biblioteczny):                
                self.imie=imie
                self.nazwisko=nazwisko
                self.adres=adres
                self.data_ur=data_ur
                self.PESEL=PESEL
                self.login=login
                self.haslo=haslo
                self.id_osoba=id_osoba
                self.konto_uzytkownika=konto_uzytkownika
                self.kat_biblioteczny=kat_biblioteczny

            def KONTO_UZYTKOWNIKA(self,wypozyczenia_konta, rezerwacje_konta, zwroty_konta):
                self.konto_uzytkownika.KONTO_UZYTKOWNIKA()

            def KATALOG_BIBLIOTECZNY(self, egzemplarz, liczba_egzemplarz, miejsce_egzemplarz, katalog_biblioteczny):
                self.kat_biblioteczny.KATALOG_BIBLIOTECZNY()

                
        self.osoba=OSOBA(self, imie, nazwisko, adres, data_ur, PESEL, login, haslo, id_osoba, konto_uzytkownika, katalog_biblioteczny)
                     

class KLIENT(KATALOG_UZYTKOWNIKOW):
    def __init__(self,osoba):
        KATALOF_UZYTKOWNIKOW.__init__(self,osoba)
        self.numer_karty=numer_karty
    
class PRACOWNIK(KATALOG_UZYTKOWNIKOW):
    def __init__(self,osoba):
        KATALOF_UZYTKOWNIKOW.__init__(self,osoba)
        self.stanowisko=stanowisko    


#                                                                            3 STAN
#_______________________________________________________________________________________

class STAN:   
    def __init__(self,katalog_biblioteczny, katalog_uzytkownikow, data):
        self.katalog_biblioteczny=katalog_biblioteczny
        self.katalog_uzytkownikow=katalog_biblioteczny
        
    def KATALOG_BIBLIOTECZNY(self, egzemplarz, liczba_egzemplarz, miejsce_egzemplarz, katalog_biblioteczny):
        self.katalog_biblioteczny.KATALOG_BIBLIOTECZNY()
        
    def KATALOG_UZYTKOWNIKOW(self,osoba):
        self.katalog_uzytkownikow.KATALOG_UZYTKOWNIKOW()
        

class WYPOZYCZENIE(STAN):
    def __init__(self,katalog_biblioteczny, katalog_uzytkownikow, data):
        STAN.__init__(self,katalog_biblioteczny, katalog_uzytkownikow, data)
        self.od=od(datetime.now()).strftime('%Y-%m-%d')
        self.do=do(datetime.now() + timedelta(days=10) ).strftime('%Y-%m-%d')
        
class REZERWACJA(STAN):
    def __init__(self,katalog_biblioteczny, katalog_uzytkownikow, data):
        STAN.__init__(self,katalog_biblioteczny, katalog_uzytkownikow, data)
        self.od=od(datetime.now()).strftime('%Y-%m-%d')
     
class ZWROT(STAN):
    def __init__(self,katalog_biblioteczny, katalog_uzytkownikow, data):
        STAN.__init__(self,katalog_biblioteczny, katalog_uzytkownikow, data)
        self.kiedy=kiedy(datetime.now()).strftime('%Y-%m-%d')
                        



#                                                              4   PRZYKLADOWE FUNKCJE
#_______________________________________________________________________________________

        
def FUNKCJE_EGZEMPLARZ(object):
    def __init__(self,egzemplarz):
        egzemplarz=[]

    def wyszukaj_ISBN(self,egzemplarz):
        for egzemplarz in KATALOG_BIBLIOTECZNY.egzemplarz :
            if ISBN ==ISBN:
                return egzemplarz

    def wyszukaj_tytul(self, egzemplarz):
        for egzemplarz in KATALOG_BIBLIOTECZNY.egzemplarz:
            if tytul == TYTUL:
                return egzemplarz
        
    def wyszukaj_autor(self, egzemplarz):
        for egzemplarz in KATALOG_BIBLIOTECZNY.egzemplarz:
            if autor == AUTOR:
                return egzemplarz

    def dodaj_egzemplarz(egzemplarz):
        self.egzemplarz.append(KATALOG_BIBLIOTECZNY.egzemplarz)
        
    def usun_egzemplarz(egzemplarz):
        self.egzemplarz.remove(KATALOG_BIBLIOTECZNY.egzemplarz)

        

# z tymi trzema funkcjami nie jesteśmy pewne czy są poprawnie napisane.

    def rezerwacja(self, rezerwacja):
        for egzemplarz in KATALOG_BIBLIOTECZNY.egzemplarz:
            if stan == wypozyczenie:
                self.zarezerwuj.append(rezerwacja)

    def zwrot (self, zwrot):
        for egzemplarz in KATALOG_BIBLIOTECZNY.egzemplarz:
            if stan == wypozyczenie:
                self.remove(wypozyczenie)
                self.zwroc.append(zwrot)

    def wypozyczenie (self,wypozyczenie):
        for egzemplarz in KATALOG_BIBLIOTECZNY.egzemplarz:
            if stan == zwrocone:
                self.wypozycz.append(wypozyczenie)
                self.remove(rezerwacja)
                self.remove(zwrot)
            else:
                self.zarezerwuj.append(rezerwacja)
            
                


def FUNKCJE_UZYTKOWNIK(object):
    def __init__(self, osoba):
        osoba=[]

    def szukaj_osoba(self, osoba):
        for osoba in KATALOG_UZYTKOWNIKOW.osoba :
            if  login==login:
                return KATALOG_UZYTKOWNIKOW.osoba
    
    def usun_osoba(self,osoba):
        self.osoba.remove(KATALOG_UZYTKOWNIKOW.osoba)
       
            
              
#                                                                    5   FUNKCJA MAIN
#_______________________________________________________________________________________

def main():
    print("Witamy w naszej Bibliotece")
    while (True):
        print( '''Wybierz opcje:
            1 Zaloguj sie jako pracownik
            2 zaloguj sie jako klient
            3 Wyjdz''')

        opc1=int(input("Prosze sie zalogowac"))


        if opc1==1:
            loginpracbib=input("Podaj swoj login:")
            haslopracbib=input("Podaj swoje haslo:")

            if [loginpracbib,haslopracbib] in KATALOG_UZYTKOWNIKOW.osoba.login :
           # if 1==1:
                print("Dozwolone")
                while(True):
                    print(''' Wybierz opcje:
                     1 Dodaj egzemplarz
                     3 Dodaj uzytkownika
                     4 Usun uzytkownika
                     6 Wyjdz lub cofnij
                     tutaj powinny byc funkcje ktore mozliwe sa
                     dla klienta, jednak nie chcialysmy niepotrzebnie
                     wydluzac kodu''')
                    
                    opc2=int(input("Prosze wybrac opcje"))

                    if opc2==1:
                        tytul=input("Wprowadz tytul egzemplarza:")
                        autor=input("Wprowadz autora egzemplarza:")
                        ISBN=input("Wprowadz ISBN egzemplarza:")
                        FUKCJE_EGZEMPLARZ.dodaj_egzemplarz(tytul.capitalize(),autor.capitalize(),ISBN.capitalize())

                    elif opc2==3:
                        login=input("Wprowadz login uzytkownika:")
                        FUNKCJE_UZYTKOWNIK.dodaj_uzytkownika(login.capitalize())
                        
                    elif opc2==4:
                        loginuzytkownika=input("wprowadz login uzytkownika:")
                        if loginuzytkownika==KATALOG_UZYTKOWNIKOW.osoba.login:
                            FUKCJE_UZYTKOWNIK.usun_osoba(loginuzytkownika.capitalize())
                        

                    elif opc2==6:    
                        print("Wroc do MENU")
                        break
                    else:
                        print("Zle wprowadzone dane")
                        continue

                else:
                    print("Odmowa dostepu\n Zle wprowadzone dane")

        elif opc1==2:
            i=1
            while (i<4):
                loginkli=input("Prosze podac login")
                haslokli=input("Prosze podac haso")
    
                if [loginkli,haslokli] in KATALOG_UZYTKOWNIKOW.osoba.login :
                    print("Dozwolone")
                    i=5
                    while(True):
                        print('''Wybierz opcje:
                             1:WYSZUKAJ ksiazke
                             2:wyporzycz ksiazke
                             3:wyjdz, cofnij
                             ''')
                        opc3=int(input("Wybierz :"))
                        if opc3==1:
                            print("Dostepne egzemplarze:\n")
                            bib.szczegoly_egzemlarz()
                            tytul=input("podaj tytul:")
                            autor=input("podaj autora:")
                            ISBN=input("podaj ISBN:")
                            FUKCJE_EGZEMPLARZ.wyszukaj_ISBN(isbn.capitalize())# tutaj mozna wyszukac po tytule i autorze, dziala analogicznie do szukania po ISBN
                        elif opc3==2:
                            print("Dostepne egzemplarze:\n")
                            bib.szczegoly_egzemlarz()
                            tytul=input("podaj tytul:")
                            autor=input("podaj autora:")
                            ISBN=input("podaj ISBN:")
                            FUNKCJE_EGZEMPLARZ.wypozycz_egzemplarz(tytul.capitalize(),autor.capitalize(),ISBN)
                        elif opc3==3:
                            print("Wracam do MENU")
                            break

                        else:
                            print("Zle wprowadzone dane")
    

        elif opc1==3:
            print("Wychodze")
            break

        else:
            print("Zle wprowadzone dane, wybierz jeszcze raz")

main()     
        
