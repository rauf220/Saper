import pygame, sys, random
from pygame.locals import *

import saper_backend

print(saper_backend.ROZMIAR_PLANSZY)
print(saper_backend.ILOSC_BOMB)

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255,0)

ROZMIAR_POLA = 100  # pixele
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(
    (ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY, ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY))
pygame.font.init()
GAME_FONT = pygame.font.SysFont('Comic Sans MS', ROZMIAR_POLA-ROZMIAR_POLA//4)

def init_game():
    pygame.init()
    pygame.display.set_caption("Saper")
    saper_backend.init_backend()
    saper_backend.wypisz_plansze_gry()


def ktore_pole(x, y):
    for wiersz in range(saper_backend.ROZMIAR_PLANSZY):
        for kolumna in range(saper_backend.ROZMIAR_PLANSZY):
            if kolumna * ROZMIAR_POLA <= x <= (kolumna + 1) * ROZMIAR_POLA and wiersz * ROZMIAR_POLA <= y <= (
                    wiersz + 1) * ROZMIAR_POLA:
                return wiersz, kolumna


def process_events(events):
    for event in events:
        # print(event)
        if event.type == QUIT:
            print("quited")
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            w, k = ktore_pole(event.pos[0], event.pos[1])
            saper_backend.lewy_klik(w, k)
            saper_backend.wypisz_plansze_gracza()
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            w, k = ktore_pole(event.pos[0], event.pos[1])
            saper_backend.prawy_klik(w, k)
            saper_backend.wypisz_plansze_gracza()


def rysyj_pole(wiersz, kolumna):
    lewy_gorny_x = kolumna * ROZMIAR_POLA
    lewy_gorny_y = wiersz * ROZMIAR_POLA
    pygame.draw.line(DISPLAYSURF, WHITE, (kolumna * ROZMIAR_POLA, wiersz * ROZMIAR_POLA),
                     ((kolumna + 1) * ROZMIAR_POLA, wiersz * ROZMIAR_POLA))
    pygame.draw.line(DISPLAYSURF, WHITE, (kolumna * ROZMIAR_POLA, (wiersz + 1) * ROZMIAR_POLA),
                     ((kolumna + 1) * ROZMIAR_POLA, (wiersz + 1) * ROZMIAR_POLA))
    pygame.draw.line(DISPLAYSURF, WHITE, (kolumna * ROZMIAR_POLA, (wiersz) * ROZMIAR_POLA),
                     ((kolumna) * ROZMIAR_POLA, (wiersz + 1) * ROZMIAR_POLA))
    pygame.draw.line(DISPLAYSURF, WHITE, ((kolumna + 1) * ROZMIAR_POLA, (wiersz) * ROZMIAR_POLA),
                     ((kolumna + 1) * ROZMIAR_POLA, (wiersz + 1) * ROZMIAR_POLA))
    if saper_backend.plansza_gracza[wiersz][kolumna] == 'f':
        pygame.draw.rect(DISPLAYSURF, WHITE, (lewy_gorny_x + ROZMIAR_POLA/4, lewy_gorny_y + ROZMIAR_POLA/8, ROZMIAR_POLA/20, ROZMIAR_POLA - ROZMIAR_POLA/4  ))
        pygame.draw.rect(DISPLAYSURF, RED, (lewy_gorny_x + ROZMIAR_POLA/4, lewy_gorny_y+ ROZMIAR_POLA/6, ROZMIAR_POLA/2, ROZMIAR_POLA/3))
    elif saper_backend.plansza_gracza[wiersz][kolumna] == 'o':
        if saper_backend.plansza_gry[wiersz][kolumna] == 'b':
            pygame.draw.circle(DISPLAYSURF, WHITE, (int(lewy_gorny_x + ROZMIAR_POLA / 2), int(lewy_gorny_y + ROZMIAR_POLA / 2)), ROZMIAR_POLA//2 - ROZMIAR_POLA//4)
            pygame.draw.circle(DISPLAYSURF, BLACK, (int(lewy_gorny_x + ROZMIAR_POLA / 2), int(lewy_gorny_y + ROZMIAR_POLA / 2)), ROZMIAR_POLA//2 - ROZMIAR_POLA//4 - 1)
            pygame.draw.line(DISPLAYSURF, WHITE, (lewy_gorny_x  + ROZMIAR_POLA / 2, lewy_gorny_y +  ROZMIAR_POLA//4), (lewy_gorny_x  + ROZMIAR_POLA / 2, lewy_gorny_y +  ROZMIAR_POLA//4 - 10))
            pygame.draw.line(DISPLAYSURF, WHITE, (lewy_gorny_x  + ROZMIAR_POLA / 2, lewy_gorny_y +  ROZMIAR_POLA//4 - 10), (lewy_gorny_x  + ROZMIAR_POLA / 2 + 10, lewy_gorny_y +  ROZMIAR_POLA//4 - 10))
            pygame.draw.rect(DISPLAYSURF, RED, (lewy_gorny_x  + + 10 + ROZMIAR_POLA / 2 - 5, lewy_gorny_y +  ROZMIAR_POLA//4 - 15, 10, 10))
        else:
            textsurface = GAME_FONT.render(str(saper_backend.plansza_gry[wiersz][kolumna]), False, WHITE)
            DISPLAYSURF.blit(textsurface, (lewy_gorny_x+ROZMIAR_POLA/4, lewy_gorny_y))
#         prawy dolny rog (kolumna + 1) * ROZMIAR_POLA,
#                          (wiersz + 1) * ROZMIAR_POLA)



def rysyj_pola():
    for wiersz in range(saper_backend.ROZMIAR_PLANSZY):
        for kolumna in range(saper_backend.ROZMIAR_PLANSZY):
            rysyj_pole(wiersz, kolumna)


def draw_objects():
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY,
                                          ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY))  # zamaluj ekran na czarno
    rysyj_pola()
    if saper_backend.sprawdz_czy_przegrana():
        textsurface = GAME_FONT.render("GAME OVER :(((", False, RED)
        DISPLAYSURF.blit(textsurface, ( ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY/8, ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY/2))
    if saper_backend.sprawdz_czy_wygrana():
        textsurface = GAME_FONT.render("WYGRAŁEŚ", False, GREEN)
        DISPLAYSURF.blit(textsurface, ( ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY/8, ROZMIAR_POLA * saper_backend.ROZMIAR_PLANSZY/2))
    pygame.display.update()


def game_loop():
    while True:
        process_events(pygame.event.get())
        # obliczenia
        draw_objects()
        fpsClock.tick(FPS)


def main():
    init_game()
    game_loop()


if __name__ == "__main__":
    main()
