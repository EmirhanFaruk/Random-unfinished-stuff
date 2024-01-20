import time, sys
from time import sleep

def enter():
	input("Geçmek için Enter e basınız... ")

def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.06)
  print()

#kodlar alıntıdır. kaynak: https://repl.it/talk/learn/Python-Essentials-Made-EZ/52048
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Tüm hakları bana aittir. Olaylar ve kişiler gerçek değildir.")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

#örnek: "feşmekan" + red + "falan filan"

reset = "\u001b[0m"
underline = "\033[4m"
italic = "\033[3m"

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sen(x):
    x = "\n " + x
    for letter in x:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
    sleep(0.09)

def diğer(x):
    x = "\n   " + x
    for letter in x:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print()
    sleep(0.09)

def diğerk(x):
    x = "\n   " + x
    for letter in x:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)
    print()
    sleep(0.12)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ikitelefonarama():
    print("\n\n")
    print("Kimi arayacaksın?(telefondaki - li konuimalar karşı kişi, + lı konuşmalar sana ait.)")
    r = int(input(" 1- Kardeşim \n 2- Nibba Emir \n 0- Çık \n: "))
    if r == 1:
        input("Çalıyor...")
        input("Cevap yok.")
        print("-----------------------------------------------------------------------------\n\n")           
        print(ikiemirlitellibom())
    elif r == 2:
        input("Çalıyor...")
        input("Meşgule attı.")
        print("-----------------------------------------------------------------------------\n\n")
        print(ikiemirlitellibom())
    if r == 0:
       print(ikitelefon())



def telefonarama():
    print("\n\n")
    print("Kimi arayacaksın?(telefondaki - li konuimalar karşı kişi, + lı konuşmalar sana ait.)")
    r = int(input(" 1- Kardeşim \n 2- Nibba Emir \n 0- Çık \n: "))
    if r == 1:
        input("Çalıyor...")
        input("Cevap yok.")
        print("-----------------------------------------------------------------------------\n\n")           
        print(tellibom())
    elif r == 2:
        input("+Alo?")
        input("-Efendim kanka.")
        input("+Kanka acil yardımın lazım. Kardeşim evden kaçtı ve baya uzaklaşmış. Erzak falan ne bulursan çantana koyup getirebilir misin? Benim için de getir.")
        input("-Ne demek knk birkaç dakikaya oradayım.")
        input("Arama bitti.")
        print("-----------------------------------------------------------------------------\n\n")
        print(ikiemirlitellibom())
    if r == 0:
       print(telefon())
       
       
       
def tellibom():
    print(telefonarama())
    
    
def ikiemirlitellibom():
    emirhaberi = 2
    print(ikitelefonarama())

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def telefongps():
    print("\n\n")
    print("Kimin gps'sine bakacaksın?")
    g = int(input(" 1- Kardeşim \n 2- Nibba Emir \n 0- Çık\n: "))
    if g == 1:
        input(".....Ormanda.")
        print("-----------------------------------------------------------------------------\n\n")
        print(telefongpsdönüşü())
    elif g == 2:
        input(".....Evinde.")
        print("-----------------------------------------------------------------------------\n\n")
        print(telefongpsdönüşü())
    if g == 0:
        print(telefon())
            
def telefongpsdönüşü():
    print(telefongps())
    
    
def ikitelefongps():
    print("\n\n")
    print("Kimin gps'sine bakacaksın?")
    g = int(input(" 1- Kardeşim \n 2- Nibba Emir \n 0- Çık\n: "))
    if g == 1:
        input(".....Ormanda.")
        print("-----------------------------------------------------------------------------\n\n")
        print(ikitelefongpsdönüşü())
    elif g == 2:
        input(".....Sana yaklaşıyor.")
        print("-----------------------------------------------------------------------------\n\n")
        print(ikitelefongpsdönüşü())
    if g == 0:
        print(ikitelefon())
            
def ikitelefongpsdönüşü():
    print(ikitelefongps())

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

input("\n Arkadaşlarınla geçirdiğin harkika bir günün akşamındasın.")
telefonn = "\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nAramak, kişi bulmak, mesaj atmak gibi işlevleri yerine getirir. Aramak için telefonarama, kişi bulmak için telefongps yazabilirsin.\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
input("\n Elindeki telefonla Nibba Emir ile sohbet ederken, salondan bağırışmalar duyuyorsun.")
input("\n Hemen telefonu bırakıp salona koştun.")
input("\n Ama olaya biraz geç kalmıştın. Kardeşin, sertçe kapıyı kapatıp dışarı çıkmıştı.")
input("\n   Olay, babanla kardeşin arasındaydı. Babası, kardeşinin hayali arkadaşlarına kendisinden daha çok saygı göstermesini doğru bulmamıştı. Kardeşin ise, böyle birşey ile karşılaşınca hazmedememiş, iyice sinirlenip kapıyı çarpıp çıkmıştı.")
input("\n Sen zaten kardeşinin bu \"Hayali arkadaş\" olaylarından haberdardın. Kendisi sık sık onunla konuşurdu. Ama henüz kendi gözlerinle varlığını görememiştin.")
input("\n   Baban sinirli bir şekilde \"Git şu kardeşini çabuk bul gel! Ormanlık alan kaybolacak falan şimdi. Bir sorun daha istemiyorum. \"")
input("\n Babanın sinirini üstüne çekmemek için hemen yanına telefonu alıp dışarı çıktın. Kardeşinin sinyali nasıl olduysa çok uzakta gözüküyor.")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hikayeninkalani():
    input("\n Ormana doğru baktın. Çok karanlık gözüküyor.")
    input("\n Kardeşin aklına geldi. ")
    input("\n O da bu kadar korkmuş muydu?")
    input("\n Yoksa \"Hayali arkadaşı\"yla mı birlikteydi?")
    input("\n Daha fazla vakit kaybetmemek için yola çıktın.")
    input("\n Bir saatten biraz daha sonra...")
    input("\n Hala yürüyorsun. Artık yorulmaya başladın.")
    input("\n Gece karanlığında yolunu sadece yukarıda ışıl ışıl parlayan ay ışığı aydınlatıyor.")
    input("\n Telefonundan kardeşinin konumunu kontrol ediyorsun.")
    input("\n Bir hayli uzakta.")
    input("\n Eğer dinlenmek için ara verirsen, sinyali kaybetmekten korkuyorsun.")
    input("\n \"Devam etmeliyim.\"")
    input("\n Birden, bir araba sesi duyuyorsun.")
    input("\n Arkana baktığında, sana hızla yaklaşan bir araba görüyorsun.")
    input("\n İçinden bir ses, bunun sonunun kötü olacağını söylüyor.")
    input("\n Hemen yolun yanındaki ağaçların arasına doğru koşmaya başlıyorsun.")
    input("\n Ama senden daha dinç olan 2 adam, arabadan inip yorgun olan sana kolaylıkla yetişiyor.")
    input("\n Yüzüne garip kokulu bir bez bastırıyorlar.")
    input("\n Kendinden geçiyorsun.")
    input("\n ...")
    input("\n   \"Vay be! Bir taşla iki kuş vurduk. Aferin!\"")
    input("\n Yavaşça kendine gelirken biraz karanlık bir odada olduğunu farkediyorsun.")
    input("\n Etrafına bakındın.")
    input("\n Buradan kaçman gerekiyordu.")
    input("\n Ama kardeşini de bulman lazımdı ki, o da buradaydı büyük ihtimalle. Buradan direk kaçarsan, kardeşinin burada olma ihtimalinin büyük olmasını düşünürsek onu burada bırakmış oluyorsun.")
    input("\n Etrafına bakınmaya devam ederken, bir havalandırma borusu görüyorsun.")
    sen("Kapağını kaldırmaya karar veriyorsun.")
    sen("Kolaylıkla yerinden çıkıyor. Çıkarırken bir çivisi elinde kalıyor.")
    return print("\n------------Bölümün sonu-----------")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def emirarandi():
    input("\n   Ormana doğru baktın. Çok karanlık gözüküyor.")
    input("\n   Kardeşin aklına geldi. ")
    input("\n   O da bu kadar korkmuş muydu?")
    input("\n   Yoksa \"Hayali arkadaşı\"yla mı birlikteydi?")
    input("\n\"Resul!\"")
    input("\n   Wtf?")
    input("\n   Arkana baktığında Emir\'in elinde ve sırtında çanta ile sana koştuğunu görüyorsun.")
    input("\n   \"Korkuttun beni. Hem sen nasıl o kadar hızlı geldin?\"")
    input("\n\"Olm evim hemen şurası zaten koşunca 2 dk sürmüyor. Hadi başına kötü birşey gelmeden kardeşini bulalım.\"")
    input("\n   Daha fazla vakit kaybetmemek için yola çıktınız.")
    input("\n Bir süre sonra...")
    input("\n Kardeşini bulmak için biraz genişçe olan yoldan Nibba Emir ile yürüyorsun.")
    input("\n \"Sağol knk hemen geldin.\" ")
    input("\n	\"Önemli değil knk. Hem macera oluyor uzun süredir hep bi macera istemiştim. Ama kardeşin için değil, ona üzüldüm baya.\"")
    input("\n Yaklaşık 1 saattir yürüyorsunuz.")
    input("\n	\"Knk ne kadar yolumuz var? Ben hafiften yorulmaya başladım.\"")
    input("\n \"Hiç bilmiyorum knk. Biz gittikçe o uzaklaşıyor. Ara vermek isterdim ama aradaki mesafe artarsa kaybedebiliriz.\"")
    input("\n   \"Neyse, en azından yanımda biraz yiyecek ve içecek de vardı. Al biraz iç.\"")
    input("\n \"Eyw.\"")
    input("\n Nibba Emir'in verdiği meyve suyundan içerken enerjinin yerine geldiğini hissediyorsun.")
    input("\n Meyve suyunun dibini \"Hüüüüfpffpfp\" diye çekerken, elindeki fener ışığının büyüdüğünü ve önünde kendi gölgenin olduğunu farkediyorsun.")
    input("\n Aniden, hayal sandığın aracın sesi hızla yakınlaşıyor.")
    input("\n İçinden bir ses, hiçbir şeyin yolunda olmadığını söylüyor.")
    input("\n \"EMİR KOŞ!\"")
    input("\n Harekete geçene kadar, araçtan 2 adam gelip yüzünüze garip kokulu bir bez bastırıyor.")
    input("\n Yavaşça kendinden geçiyorsun.")
    input("\n ...")
    input("\n	\"Vay canına! bu kadar becerikli olduğunuzu bilmiyordum. Aferin, 1 taşla 3 kuş vurduk!\"")
    input("\n Yavaşça kendine gelirken bu yabancı sesle uyanıyorsun.")
    input("\n Hemen Emir'i kontrol ediyorsun.")
    input("\n Hala baygın.")
    input("\n Bir süre sarsıldıktan sonra uyanıyor.")
    input("\n	\"Ne oldu bize?\"")
    input("\n \"Kaçırıldık.\"")
    input("\n	\"Bir planın var mı kaçmak için?\"")
    input("\n \"Bilmiyorum. Ben de yeni kendime geldim.\"")
    input("\n Biraz etrafa bakındıktan sonra bir havalandırma borusu görüyorsun.")
    input("\n	\"Çok iyi gördün knk. İnş sığabiliriz oraya. Biraz dar gibi.\"")
    input("\n Ancak 1 kişi geçebilir gibi gözüküyor. Diğeri odada kalmalı ki nöbetçi falan gelirse oyalasın ve diğerinin de orada olduğunu düşünsün.")
    input("\n Düşündüğünden daha bir basit şekilde, havalandırma kapağı hemen çıkıyor. Kapağı çıkarırken çivisi eline geliyor. Çiviyi cebine attın.")
    input("\n Şimdi sıra gidecek olan kişiyi seçmeye gelmişti.")
    gidecek_kişi = int(input("\n***Kim gitmeli?\n(1-Sen, 2-Emir)\n: "))

    if gidecek_kişi == 1:
        input("\n \"Ben buradan geçeceğim ve yol varsa kapıyı da açarım. Birisi gelip kapının penceresinden bakarsa, şuradaki yığacağın şu kıyafetleri benmişim gibi uyandırmaya çalış. İnş işe yarar da o yığını ben sanar.\"")
        input("\n	\"Tamam knk çıkar montunu.\"")
        input("\n Montunu çıkardıktan sonra yavaşça havalandırma borusuna giriyorsun. HL3\'ü belki burada sen yapacaksın, sadece levyen eksik.")
    elif gidecek_kişi == 2:
        input("\n Nöbetçiler gelir de Emir numara yapamaz diye korkuyorsun.")
        input("\n \"Knk sen buradan geçebilir misin?\"")
        input("\n	\"Eee yani geçerim. Biraz küçük ama kayar geçerim diye düşünüyorum.\"")
        input("\n \"Güzel. Yalnız montunu rica edeceğim.\"")
        input("\n	\"Neden?\"")
        input("\n \"Nöbetçi gelirse oluşturacağım yığına ekleyeceğim, inş sen sanar yığını. Bu çiviyi de al, belki işine yarar.\"")
        input("\n \"Ok knk al montu.\"")
        input("\n	Montunu sana verdikten sonra, sessizce havalandırma borusuna giriyor.")
    return input()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def telefon():
    a = "telefon()"
    if a == "telefon()":
        a = "bruh"
        a = input("Bir telefon fonksiyonu girebilirsin, örnek olarak telefon yazarsan tanımı görürsün. Çıkmak için çık yaz.\n\n: ")
        if a == "telefon":
            print(telefonn)
            a = "bruh"
            print(telefon())
        elif a == "telefonarama":
            a = "bruh"
            print(telefonarama())
        elif a == "telefongps":
            a = "bruh"
            print(telefongps())
        elif a == "çık":
            return hikayeninkalani()
            
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
def ikitelefon():
    a = "telefon()"
    if a == "telefon()":
        a = "bruh"
        a = input("Bir telefon fonksiyonu girebilirsin, örnek olarak telefon yazarsan tanımı görürsün. Çıkmak için çık yaz.\n\n: ")
        if a == "telefon":
            print(telefonn)
            a = "bruh"
            print(telefon())
        elif a == "telefonarama":
            a = "bruh"
            print(ikitelefonarama())
        elif a == "telefongps":
            a = "bruh"
            print(ikitelefongps())
        elif a == "çık":
            return emirarandi()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
b = str(input("\n***Telefonunu telefon() yazarak inceleyebilir veya kullanabilirsin.\n: "))
if b == "telefon()":
    print(telefon())
    b = "bruh"
else:
    print(hikayeninkalani())
