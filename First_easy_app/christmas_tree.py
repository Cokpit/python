# generowanie choinki

wiersze = int(input("Podaj wysokość choinki w piętrach: "))
y = 1
for i in range(0, wiersze):
    choinka = i + y
    przerwa = wiersze - y
    print(" " * przerwa, end= "")
    print("*" * choinka)
    y = y + 1
