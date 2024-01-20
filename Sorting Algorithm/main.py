
# Modification date: Wed Oct  4 14:13:19 2023

# Production date: Sun Sep  3 15:44:14 2023

from random import randint
import pygame

class Stick:
    sn = 0
    def __init__(self, number):
        self.number = number
        Stick.add_stick()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.colours = [(255, 0, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255)]
        self.colour = self.colours[2]
    
    def get_props(self, max):
        self.w = 600//Stick.sn
        tick = 600//max
        self.h = tick * self.number
        self.y = 700 - self.h
    
    def draw(self, win):
        pygame.draw.rect(win, self.colour, pygame.Rect(self.x, self.y, self.w, self.h))
    @classmethod
    def add_stick(cls):
        cls.sn += 1

w = 1000
h = 800
win = pygame.display.set_mode((w,h))
pygame.init()

da_length = int(input("Enter the number of elements(max 600): "))

used = []
sl = []
counter = 1
while counter < da_length + 1:
    danum = randint(1, da_length)
    if not danum in used:
        sl.append(Stick(danum))
                
        used.append(danum)
        counter += 1

"""
sl[0], sl[-1] = sl[-1], sl[0]
sl[31], sl[30] = sl[30], sl[31]
"""

for i in range(da_length):
    sl[i].get_props(da_length)
    sl[i].x = 200 + i * sl[i].w
    

# Font
font = pygame.font.Font("freesansbold.ttf", 15)


def show(x, y, value, sentence):
    da_result = font.render(sentence + str(value), True, (250, 250, 250))#(50, da_length, 250)
    win.blit(da_result, (x, y))
    
clock = pygame.time.Clock()
running = True
comparaisons = 0
index = 1
done = 0
si = 0
comparing = True
lci = 0
comparaisons = 0
switches = 0
thicc = 240
while running:
    #clock.tick(thicc)
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    if comparing:
        for i in range(da_length):
            sl[i].colour = sl[i].colours[2]
        if not done == da_length:
            if index != da_length:
                sl[index].colour = sl[index].colours[0]
                sl[si].colour = sl[si].colours[0]
                sl[done-1].colour = sl[done-1].colours[1]
                comparaisons += 1
                if sl[index].number < sl[si].number:
                    si = index
                index += 1
            else:
                sl[done], sl[si] = sl[si], sl[done]
                switches += 1
                for i in range(da_length):
                    sl[i].get_props(da_length)
                    sl[i].x = 200 + i * sl[i].w
                done += 1
                index = done + 1
                si = done
        else:
            comparing = False
    else:
        if lci >= da_length:
            if lci < da_length + thicc//10:
                lci += 1
            else:
                for i in range(da_length):
                    sl[i].colour = sl[i].colours[2]
        else:
            sl[lci].colour = sl[lci].colours[1]
            if lci < da_length:
                lci += 1
        
                


    show(10, 10, comparaisons, "Comparaisons: ")
    show(10, 35, switches, "Switches: ")
    show(10, 60, "Selection", "Sorting type: ")

    for i in sl:
        i.draw(win)
    
    pygame.display.flip()
