import pygame as pg
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()
    timer = pg.time.Clock()
    dt = 0
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill((0,0,0))
        pg.display.flip()
        dt = timer.tick(60)/1000
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
if __name__ == "__main__":
    main()