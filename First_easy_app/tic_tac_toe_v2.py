# Gra w kółko i krzyzyk

tab1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    #tab for player 1 moves - hiden
tab2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    #tab for player 2 moves - hiden
tab = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]     #tab for presentation

#possible wins
gra1 = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
gra2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
gra3 = [[0, 0, 1], [0, 0, 1], [0, 0, 1]]
gra4 = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
gra5 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
gra6 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
gra7 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
gra8 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

def showTab():      #show whole tab with results
    for i in tab:
        print(i)

showTab()
check = True
max = 0
while (check):
    check = False
    graczX = (input("Podaj pozycję gracza 1: "))
    tab1[int(graczX[0])][int(graczX[1])] = 1
    tab[int(graczX[0])][int(graczX[1])] = 1
    showTab()
    max = max + 1
    #checking option for winner 1
    if ((tab1[0][0] == gra1[0][0] and tab1[1][0] == gra1[1][0] and tab1[2][0] == gra1[2][0]) or
        (tab1[0][1] == gra2[0][1] and tab1[1][1] == gra2[1][1] and tab1[2][1] == gra2[2][1]) or
        (tab1[0][2] == gra3[0][2] and tab1[1][2] == gra3[1][2] and tab1[2][2] == gra3[2][2]) or
        (tab1[0][0] == gra4[0][0] and tab1[0][1] == gra4[0][1] and tab1[0][2] == gra4[0][2]) or
        (tab1[1][0] == gra5[1][0] and tab1[1][1] == gra5[1][1] and tab1[1][2] == gra5[1][2]) or
        (tab1[2][0] == gra6[2][0] and tab1[2][1] == gra6[2][1] and tab1[2][2] == gra6[2][2]) or
        (tab1[0][0] == gra7[0][0] and tab1[1][1] == gra7[1][1] and tab1[2][2] == gra7[2][2]) or
        (tab1[0][2] == gra8[0][2] and tab1[1][1] == gra8[1][1] and tab1[2][0] == gra8[2][0])) :
        print("Wygrał gracz 1")
        break
    else:
        check = True
    if (max == 9):
        print("Brak możłiwości ruchu")
        break
    graczY = (input("Podaj pozycję graca 2: "))
    tab2[int(graczY[0])][int(graczY[1])] = 1
    tab[int(graczY[0])][int(graczY[1])] = 2
    showTab()
    max = max + 1
    #checking option for winner 2
    if ((tab2[0][0] == gra1[0][0] and tab2[1][0] == gra1[1][0] and tab2[2][0] == gra1[2][0]) or
        (tab2[0][1] == gra2[0][1] and tab2[1][1] == gra2[1][1] and tab2[2][1] == gra2[2][1]) or
        (tab2[0][2] == gra3[0][2] and tab2[1][2] == gra3[1][2] and tab2[2][2] == gra3[2][2]) or
        (tab2[0][0] == gra4[0][0] and tab2[0][1] == gra4[0][1] and tab2[0][2] == gra4[0][2]) or
        (tab2[1][0] == gra5[1][0] and tab2[1][1] == gra5[1][1] and tab2[1][2] == gra5[1][2]) or
        (tab2[2][0] == gra6[2][0] and tab2[2][1] == gra6[2][1] and tab2[2][2] == gra6[2][2]) or
        (tab2[0][0] == gra7[0][0] and tab2[1][1] == gra7[1][1] and tab2[2][2] == gra7[2][2]) or
        (tab2[0][2] == gra8[0][2] and tab2[1][1] == gra8[1][1] and tab2[2][0] == gra8[2][0])):
        print("Wygrał gracz 2")
        break
    else:
        check = True
    if (max == 9):
        print("Brak możłiwości ruchu")
        break
print("Koniec gry")




