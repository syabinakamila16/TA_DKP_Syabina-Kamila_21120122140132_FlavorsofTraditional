from tkinter import *
# modul 5 Inheritance modul tk
class FlavorsOfTraditional:
    def __init__(self):
        self.root = Tk() 
        self.root.title("Program Flavors of Traditional")
        self.root.resizable(0, 0)
#modul 1 //variabel root, drinks, Harga, quote, change, dan moneys //
        # Layout Global
#modul 8 
        self.main_frame = Frame(self.root, relief=RAISED, bg="gray", bd=20)
        self.main_frame.grid(row=0, column=0, rowspan=2, columnspan=2)

        self.income_frame = Frame(self.main_frame, relief=RAISED, bg="white", bd=10)
        self.income_frame.grid(row=1, column=1, rowspan=2, columnspan=2)

        self.return_frame = Frame(self.main_frame, relief=SUNKEN, bg="gray", bd=5)
        self.return_frame.grid(row=2, column=1, rowspan=2, columnspan=2)

        self.select_frame = Frame(self.main_frame, relief=RAISED, bg="brown", bd=10)
        self.select_frame.grid(row=2, column=0, rowspan=2)

        self.title_label = Label(self.main_frame, text="\tFlavors of Traditional", bg="gray", font=("arial bold", 20))
        self.title_label.grid(row=0, column=0, columnspan=5)

        # Variables
        self.harga = IntVar()
        self.harga.set(1)
# modul 6 setter 
        self.drinks = [["Martabak Bangka Rp 30.000", 30000],
                       ["Getas Kepiting Rp 20.000", 20000],
                       ["Kerupuk Sambel Rp 35.000", 35000],
                       ["sirup Jeruk Nipis Rp 13.000", 13000],
                       ["Durian Kupas Rp 50.000", 50000],
                       ["selai nanas Rp 28.000", 28000],
                       ["lempuk Cempedak Rp 11.000", 11000],
                       ["Lempuk Durian Rp 12.000", 12000],
                       ["Pantiau Rp 10000", 10000],
                       ["mie kuah ikan Rp 15.000", 15000],
                       ["madu pelawan Rp 100.000", 100000],
                       ["Lempah Kuning Rp 10.000", 10000],
                       ["Rusip Rp 15.000", 15000],
                       ["EXIT", 0]]

    def create_widgets(self):
        # Frame Select
        for i in range(len(self.drinks) - 1):
            pilihan = Radiobutton(self.select_frame,
                                  text=self.drinks[i][0],
                                  bg="sky blue",
                                  font=("pixel", 10),
                                  indicatoron=0,
                                  width=20,
                                  padx=20,
                                  variable=self.harga,
                                  value=self.drinks[i][1])
            pilihan.pack(side=TOP)

        pilihan = Radiobutton(self.select_frame,
                              text=self.drinks[i + 1][0],
                              indicatoron=0,
                              bg="lime",
                              width=5,
                              padx=20,
                              variable=self.harga,
                              command=self.quit,
                              value=self.drinks[i + 1][1])
        pilihan.pack(side=TOP)

        # Frame Income
        pembayaran_lbl = Label(self.income_frame, text="Masukkan Uang", bg="white")
        pembayaran_lbl.grid(row=0, column=0, columnspan=2)
        self.bayar_entry = Entry(self.income_frame, bd=7)
        self.bayar_entry.grid(row=1, column=0)
        pay_btn = Button(self.income_frame, text='Pay', bd=5, command=self.show_paid)
        pay_btn.grid(row=1, column=1)

        # Frame Return
        s = Scrollbar(self.return_frame)
        s.pack(side=RIGHT, fill=Y)
        self.t = Text(self.return_frame, height=7, width=28, bg="black", fg="red", bd=10)
        self.t.pack(side=LEFT, fill=Y)
        s.config(command=self.t.yview)
        self.t.config(yscrollcommand=s.set)
        self.t.insert(END, "Perubahan\n")
# //modul 2 pengkondisian ifelse//
    def show_paid(self):
        quote = "Di Bayar : Rp " + str(self.bayar_entry.get()) + "\n"
        change = int(self.bayar_entry.get()) - self.harga.get()
        if int(self.bayar_entry.get()) > self.harga.get():
            quote = quote + "Uang Kembalian : Rp " + str(change) + "\n"
        else:
            quote = "Jumlah Tidak Valid!"
        moneys = [50000, 20000, 10000, 5000, 2000, 1000, 500]
        x = 0
# modul  3 perulangan While 
        while change > 0:
            while change >= moneys[x]:
                change = change - moneys[x]
                quote = quote + "Rp " + str(moneys[x]) + " dibagikan\n"
            x = x + 1
        self.t.insert(END, quote + "\n")
# modul 4 method
    def quit(self):
        self.root.destroy()

    def run(self):
        self.create_widgets()
        self.root.mainloop()


app = FlavorsOfTraditional()
app.run()
