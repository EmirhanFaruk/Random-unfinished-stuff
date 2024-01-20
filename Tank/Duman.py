
# Modification date: Tue Dec 20 22:35:34 2022

# Production date: Sun Sep  3 15:44:14 2023

import pygame

class Duman:
    def __init__(self, x, y, r, gri_tonu, süre):
        self.x, self.y, self.r, self.gri_tonu, self.süre = x, y, r, gri_tonu, süre
		self.azami_süre = süre

    def draw(self, pencere, dumanlar):
        if self.süre == 0:
            dumanlar.remove(self)
            return
        self.süre -= 1
		
        pygame.draw.circle(pencere, (self.gri_tonu + self.azami_süre - self.süre, self.gri_tonu + self.azami_süre - self.süre, self.gri_tonu + self.azami_süre - self.süre), (self.x, self.y), self.r + self.gri_tonu + (self.azami_süre - self.süre)//2)