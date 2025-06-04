import pygame as pg
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()
    timer = pg.time.Clock()
    dt = 0
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2   
    player1 = Player(x, y)
    while True:
        screen.fill((0,0,0))
        player1.draw(screen)
        pg.display.flip()
        dt = timer.tick(60)/1000
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
if __name__ == "__main__":
    main()