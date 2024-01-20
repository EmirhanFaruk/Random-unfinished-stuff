
# Modification date: Sat Mar 27 18:37:20 2021

# Production date: Sun Sep  3 15:44:14 2023

#Enjoy playing TicTacToe!!!
#les imports
#Pour les chaines des charactères colorées
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#Pour faire attendre
import time

#Pour l'IA
import random 

#Pour effacer les vieux trucs dans la console
from clear_screen import clear


#IA Contre Joueur
def IAContrePlayer():
  def the_game():
    clear()
    J1 = input(Fore.RESET + "Quel est votre nom?\n: ")
    clear()
    print(Fore.RED + J1 + " (X)" + Fore.WHITE + " CONTRE " + Fore.GREEN + "Bobby (O).")
    time.sleep(2)
    print(Fore.BLUE + Style.BRIGHT + "Prêt!")
    time.sleep(1)
    clear()
    n = [[" ", " ", " "], [" ", " ", " "], [" ", " "," "]]
    coloredn = []


    #les tableaux
    def tableau():
        pre = f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)

    def Ogagnanttableau():
        pre = f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)


    def Xgagnanttableau():
        pre = f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)

    def egalitetableau():
        pre = f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)



    #verifier si toutes les places sont remplies
    def cest_tout(n):
      pootis = 0
      sandwich = 0
      for i in range(3):
        for joe in range(3):
          sandwich += 1
          if n[i][joe] != " ":
            pootis += 1
          if pootis == 9:
            
            return True
          elif sandwich == 9:
            return False


    #verifier les lignes(une partie de tout_verifier(symbole)
    def verifier(symbole, ligne):
      if n[ligne] == [symbole, symbole, symbole]:
        return True
      return False

    def verifier2(symbole, ligne):
      a = 0
      counteur = 0
      for m in range(3):
        if n[a][ligne] == symbole:
          counteur += 1
        if counteur == 3:
          return True
        a += 1
      return False

    #verifier les lignes si qqn a gagne
    def tout_verifier(symbole):
      for i in range(3):
        if verifier(symbole, i) or verifier2(symbole, i):
          clear()
          if symbole == "X":
            Xgagnanttableau()
            print(Fore.RED + J1 + " a gagné!")
            return False
          if symbole == "O":
            Ogagnanttableau()
            print(Fore.GREEN + "Bobby a gagné!")
            return False        
      return True   


    joueur = 1

    ingame = True

    while ingame:
      #verifier s'il n'y a pas de place
      if cest_tout(n):
        ingame = cest_tout(n)
        egalitetableau()
        print(Fore.GREEN + Back.RED + Style.BRIGHT + "Il n'y a pas de place vide. Égalité!")
        break
      elif not cest_tout(n):#s'il y a place
        #Tour de X
        if joueur == 1:     
          tableau()
          try:
            lefunny = int(input("À quelle place vous voulez jouer?(Tour de " + J1 + ")(Utilises 1-9) \n: ")) - 1
          except ValueError:
            clear()
            print(Fore.YELLOW + "Erreur: Nombre attendu, mais des  lettres ont été reçu, ou rien.")
            continue
          if lefunny > 9:
            clear()
            print(Fore.YELLOW + "Erreur: Nombre invalide.")
            continue    
          if n[lefunny//3][lefunny%3] == " ":
            n[lefunny//3][lefunny%3] = "X"
            
            #Si X gagne diagonalement
            if n[0][0] == "X" and n[1][1] == "X" and n[2][2] == "X":
              ingame = False
              if ingame == False:
                clear()
                Xgagnanttableau()
                print(Fore.RED + J1 + " a gagné!!!")
                break

            elif n[0][2] == "X" and n[1][1] == "X" and n[2][0] == "X":
              ingame = False
              if ingame == False:
                clear()
                Xgagnanttableau()
                print(Fore.RED + J1 + " a gagné!!!")
                break

            ingame = tout_verifier("X")
            if ingame == False:
              break
            else:
              joueur = "LeIA"
            joueur = "LeIA"

          else:
            clear()
            print(Fore.YELLOW + "Erreur: Cette place est occupé.")
            continue
          
          clear()



        #Tour de O
        elif joueur == "LeIA":
          tableau()
          choixia = random.randint(0,8)
          if n[choixia//3][choixia%3] == " ":
            time.sleep(1)
            n[choixia//3][choixia%3] = "O"

            #Si L'IA gagne diagonalement
            if n[0][0] == "O" and n[1][1] == "O" and n[2][2] == "O":
              ingame = False
              if ingame == False:
                clear()
                Ogagnanttableau()
                print(Fore.GREEN + "Bobby a gagné!!!")
                break

            elif n[0][2] == "O" and n[1][1] == "O" and n[2][0] == "O":
              ingame = False
              if ingame == False:
                clear()
                Ogagnanttableau()
                print(Fore.GREEN + "Bobby a gagné!!!")
                break

            ingame = tout_verifier("O")
            if ingame == False:
              break
            else:
              joueur = 1
            joueur = 1
            clear()

          else:
            clear()
            continue


  play = True

  while play:
    the_game()
    a = input("Rejouer?(y/n)")
    if a == "n":
      play = False

#Joueur contre Joueur
def PlayerContrePlayer():
  def the_game():
    clear()
    J1 = input(Fore.RESET + "Quel est le nom de Joueur 1?\n: ")
    clear()
    J2 = input("Quel est le nom de Joueur 2?\n: ")
    clear()
    print(Fore.RED + J1 + " (X)" + Fore.WHITE + " CONTRE " + Fore.GREEN + J2 + " (O).")
    time.sleep(2)
    print(Fore.BLUE + Style.BRIGHT + "Prêt!")
    time.sleep(1)
    clear()
    n = [[" ", " ", " "], [" ", " ", " "], [" ", " "," "]]
    coloredn = []


    #les tableaux
    def tableau():
        pre = f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.WHITE}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)

    def Ogagnanttableau():
        pre = f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)


    def Xgagnanttableau():
        pre = f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.RED}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)

    def egalitetableau():
        pre = f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[0][0] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[0][1] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[0][2] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|     |1|2|3|"
        sec = f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[1][0] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[1][1] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[1][2] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|     |4|5|6|"
        tro = f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[2][0] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[2][1] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|" + n[2][2] + f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}|     |7|8|9|"
        print(pre)
        print(sec)
        print(tro)



    #verifier si toutes les places sont remplies
    def cest_tout(n):
      pootis = 0
      sandwich = 0
      for i in range(3):
        for joe in range(3):
          sandwich += 1
          if n[i][joe] != " ":
            pootis += 1
          if pootis == 9:
            
            return True
          elif sandwich == 9:
            return False


    #verifier les lignes(une partie de tout_verifier(symbole)
    def verifier(symbole, ligne):
      if n[ligne] == [symbole, symbole, symbole]:
        return True
      return False

    def verifier2(symbole, ligne):
      a = 0
      counteur = 0
      for m in range(3):
        if n[a][ligne] == symbole:
          counteur += 1
        if counteur == 3:
          return True
        a += 1
      return False

    #verifier les lignes si qqn a gagne
    def tout_verifier(symbole):
      for i in range(3):
        if verifier(symbole, i) or verifier2(symbole, i):
          clear()
          if symbole == "X":
            Xgagnanttableau()
            print(Fore.RED + J1 + " a gagné!")
            return False
          if symbole == "O":
            Ogagnanttableau()
            print(Fore.GREEN + J2 + " a gagné!")
            return False        
      return True   


    joueur = 1

    ingame = True

    while ingame:
      #verifier s'il n'y a pas de place
      if cest_tout(n):
        ingame = cest_tout(n)
        egalitetableau()
        print(Fore.GREEN + Back.RED + Style.BRIGHT + "Il n'y a pas de place vide. Égalité!")
        break
      elif not cest_tout(n):#s'il y a place
        #Tour de X
        if joueur == 1:          
          tableau()
          try:
            lefunny = int(input("À quelle place vous voulez jouer?(Tour de " + J1 + ")(Utilises 1-9) \n: ")) - 1
          except ValueError:
            clear()
            print(Fore.YELLOW + "Erreur: Nombre attendu, mais des  lettres ont été reçu, ou rien.")
            continue
          if lefunny > 9:
            clear()
            print(Fore.YELLOW + "Erreur: Nombre invalide.")
            continue    
          if n[lefunny//3][lefunny%3] == " ":
            n[lefunny//3][lefunny%3] = "X"
            
            #Si X gagne diagonalement
            if n[0][0] == "X" and n[1][1] == "X" and n[2][2] == "X":
              ingame = False
              if ingame == False:
                clear()
                Xgagnanttableau()
                print(Fore.RED + J1 + " a gagné!!!")
                break

            elif n[0][2] == "X" and n[1][1] == "X" and n[2][0] == "X":
              ingame = False
              if ingame == False:
                clear()
                Xgagnanttableau()
                print(Fore.RED + J1 + " a gagné!!!")
                break

            ingame = tout_verifier("X")
            if ingame == False:
              break
            else:
              joueur = 2
            joueur = 2

          else:
            clear()
            print(Fore.YELLOW + "Erreur: Cette place est occupé.")
            continue
          
          clear()



        #Tour de O
        elif joueur == 2:
          tableau()
          try:
            lefunny = int(input("À quelle place vous voulez jouer?(Tour de " + J2 + ")(Utilises 1-9) \n: ")) - 1
          except ValueError:
            clear()
            print(Fore.YELLOW + "Erreur: Nombre attendu, mais des lettres ont été reçu, ou rien.")
            continue
          if lefunny > 9:
            clear()
            print(Fore.YELLOW + "Erreur: Nombre invalide.")
            continue    
          if n[lefunny//3][lefunny%3] == " ":
            n[lefunny//3][lefunny%3] = "O"
            

            #Si O gagne diagonalement
            if n[0][0] == "O" and n[1][1] == "O" and n[2][2] == "O":
              ingame = False
              if ingame == False:
                clear()
                Ogagnanttableau()
                print(Fore.GREEN + J2 + " a gagné!!!")
                break

            elif n[0][2] == "O" and n[1][1] == "O" and n[2][0] == "O":
              ingame = False
              if ingame == False:
                clear()
                Ogagnanttableau()
                print(Fore.GREEN + J2 + " a gagné!!!")
                break

            ingame = tout_verifier("O")
            if ingame == False:
              break
            else:
              joueur = 1
            joueur = 1

          else:
            clear()
            print(Fore.YELLOW + "Erreur: Cette place est occupé.")
            continue
          
          clear()



  play = True
  while play:
    the_game()
    a = input("Rejouer?(y/n)")
    if a == "n":
      play = False

#Loop de Jeu
playing = True
while playing:
  clear()
  try:
    choice = int(input(Fore.GREEN + "Bienvenu(e) à TicTacToe!!! Vous voulez jouer contre l'ordi(1) ou contre un autre personne(2)?\n" + Fore.YELLOW + "Pour quitter, tapper sur Entrée sans rien écrire." + Fore.CYAN + "\n: "))


    if choice == 1:
      IAContrePlayer()
    elif choice == 2:
      PlayerContrePlayer()
  except Exception as i:
    clear()
    #print(i) montre l'exception
    #print(i)
    playing = False

    print(Fore.CYAN + "Au Revoir!")
    break
