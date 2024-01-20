import random

def şifre_oluşturma():
    uzunluk = int(input("şifre uzunluğunu giriniz: "))
    şifre = ""

    for i in range(uzunluk):
        şifre += str(random.randint(0, 9))
    return "oluşturulan şifre: " + şifre

while True:
    input(şifre_oluşturma())
