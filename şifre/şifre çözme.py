import random
import math
import itertools

def şifre_oluşturma():
    uzunluk = int(input("şifre uzunluğunu giriniz: "))
    şifre = ""

    for i in range(uzunluk):
        şifre += str(random.randint(0, 9))
    return şifre

# Function to print all distinct combinations of length `k`, where the
# repetition of elements is allowed
def findCombinations(A, k, i=0, out=[]):
    # base case: if the combination size is `k`, print it
    if len(out) == k:
        print(out)
        return
    
    # start from the previous element in the current combination
    # till the last element
    j = i
    while j < len(A):
 
        # add current element `A[j]` to the solution and recur with the
        # same index `j` (as repeated elements are allowed in combinations)
        out.append(A[j])
        findCombinations(A, k, j, out)
 
        # backtrack: remove the current element from the solution
        out.pop()
 
        # code to handle duplicates – skip adjacent duplicates
        while j < len(A) - 1 and A[j] == A[j + 1]:
            j = j + 1
 
        j = j + 1

def şifre_çözme(şifre):
    şifre = str(şifre)
    #olasılıklar = list(itertools.combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(şifre)))
    olasılıklar = []
    olasılıklar.append(findCombinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ], len(şifre), i=0, out=[]))
    olasılıklar.sort()
    print(olasılıklar)
    deneme_sayısı = 0
    #n! / ((n – r)! r!) n
    #Number of permutations when ‘r’ elements are arranged out of a total of ‘n’ elements is n Pr = n! / (n – r)!. For example, let n = 4 (A, B, C and D) and r = 2 (All permutations of size 2). The answer is 4!/(4-2)! = 12. The twelve permutations are AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB and DC.
    for i in range(len(olasılıklar)):
        şifre_denemesi = ""
        deneme_sayısı += 1
        for j in range(len(olasılıklar[0])):
            şifre_denemesi = şifre_denemesi + str(olasılıklar[i][j])
        #print(str(deneme_sayısı) + "-" + şifre_denemesi)
        if str(şifre_denemesi) == şifre:
            print("Şifre " + str(deneme_sayısı) + " denemede bulundu.\n Şifre: " + str(şifre) + "\nBulunan şifre: " + str(şifre_denemesi))
            return

    

    print("Şifre bulunamadı. Şifre: " + str(şifre) + ". Deneme sayısı: " + str(deneme_sayısı))



while True:
    çözülecek_şifre = şifre_oluşturma()
    şifre_çözme(str(çözülecek_şifre))
