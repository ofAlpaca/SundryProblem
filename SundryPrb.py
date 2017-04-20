import os
import math
'''
Problem:
    Suppose on a certain island there are 13 grey, 15 brown, and 17 crimson chameleons. If two chameleons
of different colour meet, they both change to the third colour 
(e.g.a brown and crimson pair would both change to grey). This is the only
time they change colour. Is it possible for all chameleons to eventually be the same colour?
'''
def Sundry(red, gre, blu):
    red = int(red)%3
    blu = int(blu)%3
    gre = int(gre)%3
    sum = str(red)+str(blu)+str(gre)
    if sum in '012 021 102 120 201 210'.split():
        return False
    else:
        return True

def main():
    r, g, b = input("Plz enter 3 number: ").split()
    print("{} {} {}".format(r,g,b))
    if Sundry(r,g,b):
        print("Yes")
    else:
        print("No")

while __name__ == '__main__':
    main()
    os.system('pause')
    os.system('cls')
   
