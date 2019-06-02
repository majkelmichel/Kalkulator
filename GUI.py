from tkinter import Tk, Label, Button, IntVar, Entry, W, E

class Kalkulator:
    def __init__(self, master):
        self.master = master

        self.znak = None
        self.wynik = 0
        self.wynik_text = IntVar()
        self.wynik_text.set(self.wynik)



        vcmd = master.register(self.validate)
        vcmd2 = master.register(self.validate2)

        self.dodaj = Button(master,text="+",command=lambda: self.zmien_znak("+"))
        self.odejmij = Button(master,text="-",command=lambda: self.zmien_znak("-"))
        self.mnoz = Button(master,text = "*",command=lambda: self.zmien_znak("*"))
        self.dziel = Button(master,text="/",command=lambda: self.zmien_znak("/"))
        self.wykonaj = Button(master,text="=", command=lambda: self.wykonaj_dzialanie(self.znak))
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry2 = Entry(master, validate="key", validatecommand=(vcmd2, "%P"))
        self.wynikwyswietl = Label(master,textvariable = self.wynik_text)




        self.dodaj.grid(row=0)
        self.odejmij.grid(row=1)
        self.mnoz.grid(row=0,column=1)
        self.dziel.grid(row=1,column=1)
        self.entry.grid(row=2, column=0, columnspan=10, sticky=W + E)
        self.entry2.grid(row=3,column=0,columnspan=10,sticky=W+E)
        self.wykonaj.grid(row=0,column=2)
        self.wynikwyswietl.grid(row=4,sticky=E)


        master.title("Kalkulator")


    def zmien_znak(self,znak):
        if znak == "+":
            self.znak = "+"
        elif znak == "-":
            self.znak="-"
        elif znak == "*":
            self.znak = "*"
        elif znak == "/":
            self.znak = "/"
        #print(self.znak)
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

    def wykonaj_dzialanie(self,znak):
        self.wynik=0
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
            else:
                raise ValueError
            #print(self.wynik)
            self.wynik_text.set(self.wynik)
            #return self.wynik
        except ValueError:
            print("Nie podano znaku")
            return "Nie podano znaku"
        except ZeroDivisionError:
            print("Nie dzieli się przez 0")
            return "Nie dzieli się przez 0"




root = Tk()
my_gui = Kalkulator(root)
root.mainloop()