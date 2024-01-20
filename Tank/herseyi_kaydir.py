
# Modification date: Tue Dec 20 22:13:06 2022

# Production date: Sun Sep  3 15:44:14 2023

def herseyi_kaydir(merkez, monitor_buyuklugu, obje_listesi_listesi):
    if merkez.x != monitor_buyuklugu[0]/2 or merkez.y - merkez.yerden_yukseklik/2 != monitor_buyuklugu[1]/2:
        #if merkez.x < monitor_buyuklugu[0]/4:
        x_farki = -(merkez.x - monitor_buyuklugu[0]/2)
        y_farki = -(merkez.y - merkez.yerden_yukseklik/2 - monitor_buyuklugu[1]/2)
        
        merkez.x += x_farki*0.1
        merkez.y += y_farki*0.1
        for obje_listesi_sayaci in range(len(obje_listesi_listesi)):
            for obje_sayaci in range(len(obje_listesi_listesi[obje_listesi_sayaci])):
            	obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].x += x_farki*0.1
            	obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].y += y_farki*0.1

    return merkez, obje_listesi_listesi