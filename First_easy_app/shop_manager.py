class Koszyk:
    def __init__(self):
        self.produktyKoszyk = {} #koszyk niech będzie slownikiem


    def showall(self):
        for i in self.produktyKoszyk:
            print(f"Produkt: {i}, ilość: {self.produktyKoszyk[i]}")

class KoszykController:
    def __init__(self):
        self.obj = Koszyk()

    def dodajProdukt(self, produkt, ilosc):
        znalezione = False
        for key in self.obj.produktyKoszyk:
            if (key == produkt):
                znalezione = True
                ile = self.obj.produktyKoszyk[produkt]
                self.obj.produktyKoszyk[produkt] = ile + ilosc
                break
        if (znalezione == False):
            self.obj.produktyKoszyk[produkt] = ilosc

    def usunProdukt(self, nazwaProduktu, ilosc):
        #sprawdzenie czy produkt istnieje w koszyku
        if (nazwaProduktu in self.obj.produktyKoszyk):
            aktualnaIloscWKoszyku = self.obj.produktyKoszyk[nazwaProduktu]
            if (aktualnaIloscWKoszyku - ilosc < 0):
                print("Zbyt duża ilość do usunięcia")
            elif (aktualnaIloscWKoszyku - ilosc == 0):
                self.obj.produktyKoszyk.pop(nazwaProduktu)
            else:
                tmp = aktualnaIloscWKoszyku - ilosc
                self.obj.produktyKoszyk[nazwaProduktu] = tmp
                #jeżeli liczba usuwanych produktów będzie mniejsza od liczby aktualnych produktów
        else:
            print("Brak produktu do usunięcia")

class Sklep(KoszykController):

    def __init__(self, nazwaSklepu):
        self.nazwaSklepu = nazwaSklepu
        self.koszyki = []
        super().__init__()
        #super to konstruktor nadklasy - buduje koszyk, odwołąnie do klasy wyżej

        self.asortyment = {"chleb":3.50, "sok":6.00, "woda":1.80, "cukier":4.25}
        self.menu()


    def menu(self):
        while(True):
            print("Asortyment sklepu")
            print(self.asortyment)

            dec = input(
                "PA-pokaż asortyment sklepu, PK - pokaż zawartość koszyka, DT - Dotaj towar, UT- usuń towar, aby zakończyć kliknij Enter ").upper()
            if (dec == "DT"):
                towar = input("Podaj towar do dodania: ")
                ilosc = int(input("Podaj ilość: "))
                for ki in self.asortyment:
                    if (towar in self.asortyment):
                        self.dodajProdukt(towar, ilosc)
                        self.obj.showall()
                        break
                    else:
                        print("Towaru nie ma w asortymencie sklepu!!!")
                        break
            elif (dec =="PK"):
                self.obj.showall()

            elif(dec == "UT"):
                towar = input("Podaj towar do usunięcia: ")
                ilosc = int(input("Podaj ilość produktu: "))
                self.usunProdukt(towar, ilosc)
            elif (dec ==""):
                czyNowe = input("Czy chcesz kończyć zakupy? jeśli nie weźmiesz nowy koszyk: y/n").upper()
                if (czyNowe == "N"):
                    self.koszyki.append(self.obj.produktyKoszyk)
                    self.obj = Koszyk()
                elif (czyNowe == "Y"):
                    print("-" * 20 + "Podsumowanie zakupów" + "-" * 20)
                    self.koszyki.append(self.obj.produktyKoszyk)
                    for kosz in self.koszyki:
                        suma = 0
                        print(f"Koszyk {self.koszyki.index(kosz)}")
                        for produkt in kosz:
                            wartosc = kosz[produkt]*self.asortyment[produkt]
                            suma = suma+wartosc
                            print(f"Produkt: {produkt}, ilość: {kosz[produkt]}, cena : {self.asortyment[produkt]}zł, wartość: {wartosc}zł")
                        print(f"Wartość zamówienia: {suma}zł")
                        if (suma > 10):
                            print(f"Otrzymałeś 10% rabatu - {round(suma * 0.1, 2)}")
                            suma = suma * 0.9
                            print(f"Do zapłaty: {round(suma, 2)}zł")
                        else:
                            print(f"Do zapłaty: {round(suma, 2)}zł")
                    break
                else:
                    print("Wybrałeś złą opcję!!!")

market = Sklep("ABC")
