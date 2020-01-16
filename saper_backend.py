import random

ILOSC_BOMB = 10
ROZMIAR_PLANSZY = 8
plansza_gry = [[0 for _ in range(ROZMIAR_PLANSZY)] for _ in range(ROZMIAR_PLANSZY)]
plansza_gracza = [['*' for _ in range(ROZMIAR_PLANSZY)] for _ in range(ROZMIAR_PLANSZY)]


def losuj_bomby():
    for i in range(ILOSC_BOMB):

        wiersz = random.randint(0, ROZMIAR_PLANSZY - 1)
        kolumna = random.randint(0, ROZMIAR_PLANSZY - 1)
        while plansza_gry[wiersz][kolumna] == 'b':
            wiersz = random.randint(0, ROZMIAR_PLANSZY - 1)
            kolumna = random.randint(0, ROZMIAR_PLANSZY - 1)
        plansza_gry[wiersz][kolumna] = 'b'


def wypisz_plansze_gry():
    for i in range(ROZMIAR_PLANSZY):
        for j in range(ROZMIAR_PLANSZY):
            print(plansza_gry[i][j], end=' ')
        print()


def wypisz_plansze_gracza():
    for i in range(ROZMIAR_PLANSZY):
        for j in range(ROZMIAR_PLANSZY):
            print(plansza_gracza[i][j], end=' ')
        print()


def wylicz_sasiadow(wiersz, kolumna):
    liczba_sasiadow = 0
    if wiersz > 0 and kolumna > 0 and plansza_gry[wiersz - 1][kolumna - 1] == 'b':
        liczba_sasiadow += 1
    if wiersz > 0 and plansza_gry[wiersz - 1][kolumna] == 'b':
        liczba_sasiadow += 1
    if wiersz > 0 and kolumna < ROZMIAR_PLANSZY - 1 and plansza_gry[wiersz - 1][kolumna + 1] == 'b':
        liczba_sasiadow += 1
    if kolumna > 0 and plansza_gry[wiersz][kolumna - 1] == 'b':
        liczba_sasiadow += 1
    if kolumna < ROZMIAR_PLANSZY - 1 and plansza_gry[wiersz][kolumna + 1] == 'b':
        liczba_sasiadow += 1
    if wiersz < ROZMIAR_PLANSZY - 1 and kolumna > 0 and plansza_gry[wiersz + 1][kolumna - 1] == 'b':
        liczba_sasiadow += 1
    if wiersz < ROZMIAR_PLANSZY - 1 and plansza_gry[wiersz + 1][kolumna] == 'b':
        liczba_sasiadow += 1
    if wiersz < ROZMIAR_PLANSZY - 1 and kolumna < ROZMIAR_PLANSZY - 1 and plansza_gry[wiersz + 1][kolumna + 1] == 'b':
        liczba_sasiadow += 1
    return liczba_sasiadow


def wylicz_wszystkich_sasiadow():
    for wiersz in range(ROZMIAR_PLANSZY):
        for kolumna in range(ROZMIAR_PLANSZY):
            if plansza_gry[wiersz][kolumna] != 'b':
                plansza_gry[wiersz][kolumna] = wylicz_sasiadow(wiersz, kolumna)


def init_backend():
    losuj_bomby()
    wylicz_wszystkich_sasiadow()


def prawy_klik(w, k):
    if plansza_gracza[w][k] == '*':
        plansza_gracza[w][k] = 'f' # flaga
    elif plansza_gracza[w][k] == 'f':
        plansza_gracza[w][k] = '*'  # zakrywamy pole

def lewy_klik(w, k):
    if plansza_gracza[w][k] == '*':
        plansza_gracza[w][k] = 'o' # odsloniete pole

def sprawdz_czy_przegrana():
    for wiersz in range(ROZMIAR_PLANSZY):
        for kolumna in range(ROZMIAR_PLANSZY):
            if plansza_gracza[wiersz][kolumna] == 'o' and plansza_gry[wiersz][kolumna] == 'b':
                return True
    return False

def sprawdz_czy_wygrana():
    ilosc_flag = 0
    for wiersz in range(ROZMIAR_PLANSZY):
        for kolumna in range(ROZMIAR_PLANSZY):
            # if plansza_gracza[wiersz][kolumna] == '*':
            #     return False
            if plansza_gracza[wiersz][kolumna] == 'f':
                ilosc_flag += 1
            if plansza_gracza[wiersz][kolumna] == 'o' and plansza_gry[wiersz][kolumna] == 'b':
                return False
            if plansza_gracza[wiersz][kolumna] == 'f' and plansza_gry[wiersz][kolumna] != 'b':
                return False
    return ilosc_flag == ILOSC_BOMB
