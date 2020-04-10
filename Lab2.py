# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

# Zadanie 2 -------------------------------------------------------------------------------
from array import *

def zad2():
    myarr = array('b', [ord(input("Podaj element")) for _ in range(int(input("Podaj długość")))])
    for i in reversed(myarr):
        print(chr(i))
    
zad2()


# Zadanie 3 -------------------------------------------------------------------------------
from array import *
import numpy as np

def zad3():
    myarr = array('f', np.random.uniform(-5,5,int(input("Podaj dlugosc"))))
    print(myarr)
    try:
        file = open("result.txt", "w")
        file.write(str(myarr))
        print("Zapisano do pliku")
    finally:
        file.close()
    
zad3()


# Zadanie 4 -------------------------------------------------------------------------------
import numpy as np

def zad4():
    myarr = np.array([2,4,5,6,7], dtype="int64")
    
    for i in range(4):
        myarr = np.append(myarr, np.power(myarr[-5:],2))
    
    #myarr = np.append(myarr, np.power(myarr,2)).reshape(2,5)
    
    myarr = myarr.reshape(5,5)
    print(myarr)
    return myarr
          
zad4()


# Zadanie 5 -------------------------------------------------------------------------------

def zad5(loc):
    line = ""
    try:
        file = open(loc, "r")
        line = file.readline()
    finally:
        file.close()
        
    dictionary = {}
    
    for L in line:
        if (L in dictionary):
            dictionary[L] += 1
        else:
            dictionary[L] = 1
        
    print(dictionary)
    
zad5("result.txt")


# Zadanie 6 -------------------------------------------------------------------------------
import numpy as np

def deck():
    deck = []
    values = ['c', 'd', 'h', 's']
    ranks = np.append(np.arange(2,11), ['J', 'D', 'K', 'A'])
    for i in ranks:
        for v in values:
            deck.append((i, v))
    return tuple(deck)


def shuffle_deck(deck):
    deck = list(deck)
    np.random.shuffle(deck)
    return tuple(deck)


def deal(deck, n):
    deck = list(deck)
    decks = []
    for x in range(n):
        decks.append(tuple(deck[5*x:5*(x+1)])) 
    return tuple(decks)
    
    
print(deck())
print("--------------")
print(shuffle_deck(deck()))
print("--------------")
deal(shuffle_deck(deck()),5)
