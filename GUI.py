from tkinter import Tk, Label, Button, IntVar

class Kalkulator:
    def __init__(self, master):
        self.master = master

        master.title("Kalkulator")

        self.total = 0
        self.podany_numer = 0

        self.podany_numer_Var = IntVar()
        self.podany_numer_Var.set(self.podany_numer)
        self.podany_numer_label = Label(master, textvariable = self.podany_numer_Var)

        self.label = Label(master, text="To jest kalkulator")
        self.label1 = Label(master, textvariable = self.podany_numer_Var)

        self.button1 = Button(master, text = " 1 ", command = self.but_1())

        self.button2 = Button(master, text = " 2 ")
        """
        self.button3 = Button(master, text = " 3 ")
        self.button4 = Button(master, text = " 4 ")
        self.button5 = Button(master, text=" 5 ")
        self.button6= Button(master, text=" 6 ")
        self.button7= Button(master, text=" 7 ")
        self.button8= Button(master, text=" 8 ")
        self.button9= Button(master, text=" 9 ")
        """
        #self.label.grid(columnspan=5,sticky = W)
        self.label1.grid(row =0,column = 1)
        self.button1.grid(row=1,column = 0)
        self.button2.grid(row=1,column = 1)
        """
        self.button3.grid(row=1,column = 2)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button7.grid(row=3, column=0)
        self.button8.grid(row=3, column=1)
        self.button9.grid(row=3, column=2)
        """

        #self.button1.bind("<Button-1>", self.but_1())

    def but_1(self):
        self.podany_numer += 1

        self.podany_numer_Var.set(self.podany_numer)
    def but_2(self):
        self.podany_numer +=2

        self.podany_numer_Var.set(self.podany_numer)


root = Tk()
my_gui = Kalkulator(root)
root.mainloop()