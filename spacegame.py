import random
import pgzrun
WIDTH = 500
HEIGHT = 400
no_of_satellites=10
sats = []
for i in range(no_of_satellites):
    satellite = Actor("satellite")
    satellite.x = random.randint(50,WIDTH-50)
    satellite.y = random.randint(50,HEIGHT-50)
    sats.append(satellite)
def draw():
    screen.blit("background",(0,0))
    number = 1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+20))
        number += 1
pgzrun.go()