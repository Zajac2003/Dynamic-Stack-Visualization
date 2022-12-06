import tkinter
from tkinter import *

#FUNKCJE#FUNKCJE#FUNKCJE#FUNKCJE#FUNKCJE

stos = [complex(22,-8),complex(20,00), complex(0,-422), complex(-20,-20)]

#Pozwala na wprowadzenie liczby urojonej na wierzch stosu
def Insert():
    a=e.get()
    b=f.get()

    if(a=='' or a=='0'):
        a=int(0)
    else:
        try:
            a=int(a)
        except Exception:
            respondLabel.config(text='Wprowadzono nieprawidłowe dane')

    if(b=='' or b=='0'):
        b=int(0)
    else:
        try:
            b=int(b)
        except Exception:
            respondLabel.config(text='Wprowadzono nieprawidłowe dane')

    if(a==0 and b==0):
        return

    try:
        stos.append( complex(a,b) )
    except Exception:
        respondLabel.config(text='Wprowadzono nieprawidłowe dane')

    showStack()
#Pozwala na usunięcie liczby urojonej ze stosu, wprowadzając jej wartość rzeczywistą i urojoną, lub indeks
def Delete():
    a=e.get()
    b=f.get()

    if(b=='' and a!=''):
        a=int(a)-1
        try:
            stos.pop(a)
        except Exception:
            respondLabel.config(text="Podano nieprawidlowe dane")
    elif(b!='' and a!=''):
        try:
            a=int(a)
            b=int(b)
            stos.remove(complex(a, b))
        except Exception:
            respondLabel.config(text="Podano nieprawidłowe dane")

    showStack()
#Wyświetla stos w Scrollbarze w oknie
def showStack():
    iList.delete(0, END)
    for i in range(len(stos)):
        iList.insert(END,str(i+1) +'. '+ str(stos[i]))
#Wyszukuje indeks liczby, znając jej wartość rzeczywistą i urojoną
def Seek():
    a = e.get()
    b = f.get()


    try:
        a=int(a)
        b=int(b)
        for i in range(len(stos)):
            if (stos[i] == complex(a, b)):
                respondLabel.config(text='Znaleziono liczbę na pozycji ' + str(i + 1))
                return
        respondLabel.config(text='Nie znaleziono takiej liczby')
    except Exception:
        respondLabel.config(text="Podano nieprawidłowe dane")
#Sumuje wszystkie liczby w stosie
def sumAll():
    suma=complex(0,0)
    if(len(stos)==0):
        respondLabel.config(text='Stos jest pusty')
    for i in range(len(stos)):
        suma += stos[i]
        respondLabel.config(text='Suma wszystkich elementów stosu wynosi '+ str(suma))
#Mnozy wszystkie liczby w stosie
def multipleEvery():
    suma=1
    if (len(stos) == 0):
        respondLabel.config(text='Stos jest pusty')
    for i in range(len(stos)):
        suma *= stos[i]
        respondLabel.config(text='Wynik mnozenia wszystkich elementów wynosi '+ str(suma))
#Usuwa całą zawartość stosu
def deleteStack():
    stos.clear()
    showStack()
#Wyświetla okno pomocy
def pomoc():

    root2 = tkinter.Tk()
    helpLabel = tkinter.Label(root2,
                              text='Dodaj liczbę na stos - Wpisz w górnym oknie część rzeczywistą, w dolnym część urojoną. Podana liczba zostanie dodana na stos.')
    helpLabel2 = tkinter.Label(root2,
                               text='Usuń liczbę ze stosu - W górnym oknie wpisz indeks usuwanej liczby LUB w górnym oknie wpisz jej część rzeczywistą, a w dolnym część urojoną. Liczba zostanie usunięta ze stosu.')
    helpLabel3 = tkinter.Label(root2,
                               text='Wyszukaj liczbę w stosie - W górnym oknie wpisz część rzeczywistą szukanej liczby, a w dolnym jej wartość urojoną. Wynikiem jest indeks szukanej liczby')
    helpLabel4 = tkinter.Label(root2,
                               text='Suma wszystkich liczb na stosie - Wyświetla sumę wszystkich liczb na stosie.')
    helpLabel5 = tkinter.Label(root2,
                               text='Pomnóż każdą liczbę na stosie - Wyświetla wynik mnożenia wszystkich składników stosu.')
    helpLabel6 = tkinter.Label(root2, text='Usuń stos - Usuwa całą zawartość stosu')
    helpLabel.pack()
    helpLabel2.pack()
    helpLabel3.pack()
    helpLabel4.pack()
    helpLabel5.pack()
    helpLabel6.pack()


#GUI#GUI#GUI#GUI#GUI#GUI#GUI#GUI#GUI#GUI

#tworzy główne okno
root = tkinter.Tk() #tworzy okno
root.geometry("400x400") #ustawia wymiary okna

#ELEMENTY GUI#ELEMENTY GUI#ELEMENTY GUI

respondLabel = tkinter.Label(root) #tworzy etykiete wyświetlającą komunikaty z różnych funkcji
respondLabel.pack(side=BOTTOM) #porządkuje respondLabel na sam dół

#wejścia
e = Entry(root) #tworzy okno na czesc rzeczywistą
e.pack() #wrzuca e do okna
f = Entry(root) #tworzy okno na czesc urojoną
f.pack() #wrzuca f do okna

#przyciski odpowiadajace za akcje
B1 = tkinter.Button(root, text='Dodaj liczbe na stos', command=Insert) #Wywołuje funkcję Insert(), gdy klinięty
B1.pack() #funkcja dodajaca przycisk do okna

B2 = tkinter.Button(root, text='Usuń liczbę ze stosu', command=Delete) #Wywołuje funkcję Delete(), gdy klinięty
B2.pack() #funkcja dodajaca przycisk do okna

B4 = tkinter.Button(root, text='Wyszukaj liczbę w stosie', command=Seek) #Wywołuje funkcję Seek(), gdy klinięty
B4.pack() #funkcja dodajaca przycisk do okna

B5 = tkinter.Button(root, text='Suma wszystkich liczb na stosie', command=sumAll) #Wywołuje funkcję sumaAll(), gdy klinięty
B5.pack() #funkcja dodajaca przycisk do okna

B6 = tkinter.Button(root, text='Pomnóż każdą liczbę w stosie', command=multipleEvery) #Wywołuje funkcję multiplyEvery(), gdy klinięty
B6.pack() #funkcja dodajaca przycisk do okna

B7 = tkinter.Button(root, text='Usuń stos', command=deleteStack) #Wywołuje funkcję deleteStack(), gdy klinięty
B7.pack() #funkcja dodajaca przycisk do okna

B8 = tkinter.Button(root,text='Pomoc', command=pomoc) #Wywołuje funkcję pomoc(), gdy klinięty
B8.pack()

#ustawienia listy ze scrollbarem
iList =Listbox(root,height=18, width=15) #wymiary listboxa
scroll = Scrollbar(root,command= iList.yview) #przypisanie scrollbara do listboxa
iList.configure(yscrollcommand=scroll.set) #synchronizuje scrollowanie z ruchem listboxa
iList.pack(side=LEFT) #przyporządkowanie do lewej krawędzi
scroll.pack(side=LEFT,fill=Y) #przyporządkowanie do lewej krawędzi

showStack()
root.mainloop() #odpowiada za nieustanne wyswietlanie okna