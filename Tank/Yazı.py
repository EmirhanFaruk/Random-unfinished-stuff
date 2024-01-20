
# Modification date: Tue Dec 20 22:32:58 2022

# Production date: Sun Sep  3 15:44:14 2023

class Yazı:
    def __init__(self, x, y, yazı, boyut, renk, süre, değişken, hız = 0):
        self.x, self.y, self.boyut, self.renk, self.süre, self.hız = x, y, boyut, renk, süre, hız
        self.yazı = yazı
        self.değişken = değişken
        self.font = pygame.font.SysFont('Comic Sans MS', self.boyut)
        self.yazı_yüzey = self.font.render(self.yazı, False, self.renk)
        self.yazı_genişlik = self.yazı_yüzey.get_width()

    def draw(self, pencere, yazılar):
        if self.süre == 0:
            yazılar.remove(self)
        if self.süre != -1:
            self.süre -= 1
        self.yazı_yüzey = self.font.render(self.yazı + str(self.değişken), False, self.renk)
        self.yazı_genişlik = self.yazı_yüzey.get_width()
        pencere.blit(self.yazı_yüzey, (self.x - self.yazı_genişlik/2, self.y))
        self.y -= self.hız
        return