from tkinter import Tk, Label, Button, IntVar, Entry, W, E, StringVar
from math import sqrt


class Kalkulator:
    def __init__(self, master):
        self.master = master

        self.znak = None
        self.wynik = 0
        self.blad = ""
        self.wynik_text = IntVar()
        self.wynik_text.set(self.wynik)
        self.blad_text = StringVar()
        self.blad_text.set(self.blad)

        vcmd = master.register(self.validate)
        vcmd2 = master.register(self.validate2)

        # definiowanie przycisków akcji
        self.dodaj = Button(master, text="x+y", command=lambda: self.zmien_znak("+"))
        self.odejmij = Button(master, text="x-y", command=lambda: self.zmien_znak("-"))
        self.mnoz = Button(master, text="x*y", command=lambda: self.zmien_znak("*"))
        self.dziel = Button(master, text="x/y", command=lambda: self.zmien_znak("/"))
        self.potega = Button(master, text="x**y", command=lambda: self.zmien_znak("**"))
        self.pierwiastek = Button(master, text="√x", command=lambda: self.zmien_znak("√"))
        self.porownaj = Button(master, text="Porównaj liczby", command=lambda: self.zmien_znak("porownaj"))
        self.zamiana_bin_na_10 = Button(master, text="Zamień binarną na dziesiętną", command=lambda: self.zmien_znak("bin_na_10"))

        # definiowanie przycisku wykonującego liczenie
        self.wykonaj = Button(master, text="=", command=lambda: self.wykonaj_dzialanie(self.znak))

        # definiowanie pól do wprowadzania zmiennych
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry2 = Entry(master, validate="key", validatecommand=(vcmd2, "%P"))
        self.wynikwyswietl = Label(master, textvariable=self.wynik_text)
        self.bladwyswietl = Label(master, textvariable=self.blad_text)
        self.bladwyswietl_1 = Label(master, text="Wystąpił błąd:")

        # definiowanie labelow z podpisami
        self.x = Label(master, text="x:")
        self.y = Label(master, text="y:")
        self.wynik = Label(master, text = "Wynik:")

        # wstawienie przycisków akcji do okna aplikacji
        self.dodaj.grid(row=0)
        self.odejmij.grid(row=1)
        self.mnoz.grid(row=0, column=1)
        self.dziel.grid(row=1, column=1)
        self.potega.grid(row=0, column=2)
        self.pierwiastek.grid(row=1, column=2)
        self.porownaj.grid(row=2,columnspan=3)
        self.zamiana_bin_na_10.grid(row=3, columnspan=5)

        # wstawienie przycisku wykonującego liczenie do okna aplikacji
        self.wykonaj.grid(row=0, column=3)

        self.wynik.grid(row=10)
        self.wynikwyswietl.grid(row=10, column=1, sticky=E, columnspan=10)


        # nazwa okna aplikacji
        master.title("Kalkulator")

    def zmien_znak(self, znak):
        if znak == "+":
            self.znak = "+"
            self.x.grid(row=5)
            self.y.grid(row=6)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid(row=6, column=1, columnspan=10, sticky=W + E)
        elif znak == "-":
            self.znak = "-"
            self.x.grid(row=5)
            self.y.grid(row=6)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid(row=6, column=1, columnspan=10, sticky=W + E)
        elif znak == "*":
            self.znak = "*"
            self.x.grid(row=5)
            self.y.grid(row=6)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid(row=6, column=1, columnspan=10, sticky=W + E)
        elif znak == "/":
            self.znak = "/"
            self.x.grid(row=5)
            self.y.grid(row=6)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid(row=6, column=1, columnspan=10, sticky=W + E)
        elif znak == "**":
            self.znak = "**"
            self.x.grid(row=5)
            self.y.grid(row=6)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid(row=6, column=1, columnspan=10, sticky=W + E)
        elif znak == "√":
            self.znak = "√"
            self.x.grid(row=5)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid_remove()
            self.y.grid_remove()
        elif znak == "porownaj":
            self.znak = "porownaj"
            self.x.grid(row=5)
            self.y.grid(row=6)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid(row=6, column=1, columnspan=10, sticky=W + E)
        elif znak == "bin_na_10":
            self.znak = "bin_na_10"
            self.x.grid(row=5)
            self.entry.grid(row=5, column=1, columnspan=10, sticky=W + E)
            self.entry2.grid_remove()
            self.y.grid_remove()


        # print(self.znak)
        return self.znak

    def validate(self, new_text):
        if not new_text:
            self.num1 = 0
            return True

        try:
            self.num1 = int(new_text)
            return self.num1
        except ValueError:
            return False

    def validate2(self, new_text):
        if not new_text:
            self.num2 = 0
            return True

        try:
            self.num2 = int(new_text)
            return self.num2
        except ValueError:
            return False

    def porownanie(self,n1,n2):
        if n1 > n2:
            wynik = "jest większa od liczby"
        elif n1 < n2:
            wynik = "jest mniejsza od liczby"
        elif n1 == n2:
            wynik = "jest równa liczbie"
        n1 = str(n1)
        n2 = str(n2)
        self.wynik = "Liczba %s %s %s." % (n1,wynik,n2)
        return self.wynik

    def zamiana_bin_na_10_func(self,liczba):
        liczba = str(liczba)
        lista=[]
        wynik=0
        for i in liczba:
            if i not in ["1", "0"]:
                raise ArithmeticError
            lista.append(i)
        lista.reverse()
        a=0
        for i in lista:
            i = int(i)
            wynik += 2**a * i
            a+=1
        self.wynik = wynik
        return self.wynik

    def wykonaj_dzialanie(self, znak):
        self.wynik = 0
        try:
            if znak == "+":
                self.wynik = self.num1 + self.num2
            elif znak == "-":
                self.wynik = self.num1 - self.num2
            elif znak == "*":
                self.wynik = self.num1 * self.num2
            elif znak == "/":
                if self.num2 == 0:
                    raise ZeroDivisionError
                else:
                    self.wynik = self.num1 / self.num2
            elif znak == "**":
                self.wynik = self.num1 ** self.num2
            elif znak == "√":
                self.wynik = sqrt(self.num1)
            elif znak == "porownaj":
                self.porownanie(self.num1, self.num2)
            elif znak == "bin_na_10":
                self.zamiana_bin_na_10_func(self.num1)
            else:
                raise ValueError
            # print(self.wynik)
            self.wynik_text.set(self.wynik)
            self.bladwyswietl.grid_remove()
            self.bladwyswietl_1.grid_remove()
            # return self.wynik
        except ValueError:
            self.blad = "Nie podano znaku"
            self.blad_text.set(self.blad)
            self.bladwyswietl.grid(row=11, column=1, sticky=E, columnspan=10)
            self.bladwyswietl_1.grid(row=11)
        except ZeroDivisionError:
            self.blad = "Nie dzieli się przez 0"
            self.blad_text.set(self.blad)
            self.bladwyswietl.grid(row=11, column=1, sticky=E, columnspan=10)
            self.bladwyswietl_1.grid(row=11)
        except AttributeError:
            self.blad = "Nie podano liczb"
            self.blad_text.set(self.blad)
            self.bladwyswietl.grid(row=11, column=1, sticky=E, columnspan=10)
            self.bladwyswietl_1.grid(row=11)
        except ArithmeticError:
            self.blad = "Nieprawidłowa liczba binarna"
            self.blad_text.set(self.blad)
            self.bladwyswietl.grid(row=11, column=1, sticky=E, columnspan=10)
            self.bladwyswietl_1.grid(row=11)


root = Tk()
my_gui = Kalkulator(root)
root.mainloop()