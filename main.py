import pygame as pg
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()        
    asteroids = pg.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player1 = Player(x, y)
    AsteroidField()
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        screen.fill((0,0,0))
        updatable.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pg.display.flip()
        dt = timer.tick(60)/1000
        
        
        
if __name__ == "__main__":
    main()