coding = 1251

from tkinter import *

root = Tk()
root.title("Jewelry")

root.geometry("600x500")

# Глобальні змінні
jewelry = 0  # Тип украшения: 0 - не вибрано, 1 - кільце, 2 - намисто, 3 - браслет, 4 - сережки

# Початкова ціна
start_price = {
    'ring': 5000,
    'necklece': 10000,
    'bracelet': 4500,
    'earings': 6000
}

# Надбавка за метал
metal = {
    'rgold': 2000,
    'wgold': 3000,
    'silver': 4000
}

# Надбавка за додаткові опції
additional_options = {
    'diamond': 3500,
    'gold_plating': 1000,
    'engraving': 1245
}


# --------------------------------------------------
# Користувацькі функції

def jewelry1(event):
    global jewelry
    jewelry = 1


def jewelry2(event):
    global jewelry
    jewelry = 2


def jewelry3(event):
    global jewelry
    jewelry = 3


def jewelry4(event):
    global jewelry
    jewelry = 4


def show_info():
    s = ""
    if jewelry == 0:
        s = "Jewelry not selected\n"
    else:
        if jewelry == 1: s = "Ring\n"
        if jewelry == 2: s = "Necklece\n"
        if jewelry == 3: s = "Bracelet\n"
        if jewelry == 4: s = "Earrings\n"

        if rb_val.get() == metal['rgold']:
            s += "Rose gold metal\n"
        elif rb_val.get() == metal['wgold']:
            s += "White gold metal\n"
        else:
            s += "Silver metal\n"

        if cb1_val.get() == 1:
            s += "With diamonds\n"
        if cb2_val.get() == 1:
            s += "With gold plating\n"
        if cb3_val.get() == 1:
            s += "With engraving\n"

    jewelry_info_str.set(s)


def show_info():
    s = ""
    if jewelry == 0:
        s = "Jewelry not selected\n"
    else:
        if jewelry == 1: s = "Ring\n"
        if jewelry == 2: s = "Necklece\n"
        if jewelry == 3: s = "Bracelet\n"
        if jewelry == 4: s = "Earrings\n"

        if rb_val.get() == metal['rgold']:
            s += "Rose gold metal\n"
        elif rb_val.get() == metal['wgold']:
            s += "White gold metal\n"
        else:
            s += "Silver metal\n"

        if cb1_val.get() == 1:
            s += "With diamonds\n"
        if cb2_val.get() == 1:
            s += "With gold plating\n"
        if cb3_val.get() == 1:
            s += "With engraving\n"

    jewelry_info_str.set(s)


def calculator(event):
    show_info()

    if jewelry == 0:
        return 0

    price = 0

    if jewelry == 1:
        price = start_price['ring']
    if jewelry == 2:
        price = start_price['necklece']
    if jewelry == 3:
        price = start_price['bracelet']
    if jewelry == 4:
        price = start_price['earings']

    price += rb_val.get()

    if cb1_val.get() == 1:
        price += additional_options['diamond']
    if cb2_val.get() == 1:
        price += additional_options['gold_plating']
    if cb3_val.get() == 1:
        price += additional_options['engraving']

    s = str(jewelry_info_str.get())
    s = s + "\n" + str(price) + " UAH."
    jewelry_info_str.set(s)


def about_program(event):
    global jewelry
    s = "Лабораторна робота №1\n" \
        "Виконала: студентка 3 курсу гр. КНІТ-Б18-Б\n" \
        "Степанюк О.С."
    jewelry_info_str.set(s)
    jewelry = 0


# --------------------------------------------------
# Створення віджетів

# Мітка вибору прикраси
container_label1 = Label(root, text="L1")

# Кнопки вибору прикраси
b1 = Button(container_label1, text="Ring", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")
b2 = Button(container_label1, text="Necklece", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")
b3 = Button(container_label1, text="Bracelet", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")
b4 = Button(container_label1, text="Earings", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")

b1.bind("<Button-1>", jewelry1)
b2.bind("<Button-1>", jewelry2)
b3.bind("<Button-1>", jewelry3)
b4.bind("<Button-1>", jewelry4)

# Мітка "Оберіть метал"

container_label2 = Label(root)
title_label1 = Label(container_label2, text="Оберіть метал", font="Arial 16 bold")

# Створення радіокнопок для вибору металу
rb_val = IntVar()
rb_val.set(metal['rgold'])

r1 = Radiobutton(container_label2, text="Rose gold", font="Arial 14", bg="gold2", variable=rb_val, value=metal['rgold'])
r2 = Radiobutton(container_label2, text="White gold", font="Arial 14", bg="gold2", variable=rb_val,
                 value=metal['wgold'])
r3 = Radiobutton(container_label2, text="Silver", font="Arial 14", bg="gold2", variable=rb_val, value=metal['silver'])

# Мітка "Оберіть додаткові опції"

container_label3 = Label(root)
title_label2 = Label(container_label3, text="Оберіть додаткові опції", font="Arial 14 bold")

# Створення чекбоксів для вибору додаткових опцій
cb1_val = IntVar()
cb1_val.set(0)
c1 = Checkbutton(container_label3, text="Diamand", font="Arial 14", bg="ivory3", variable=cb1_val, onvalue=1,
                 offvalue=0)

cb2_val = IntVar()
cb2_val.set(0)
c2 = Checkbutton(container_label3, text="Gold plating", font="Arial 14", bg="ivory3", variable=cb2_val, onvalue=1,
                 offvalue=0)

cb3_val = IntVar()
cb3_val.set(0)
c3 = Checkbutton(container_label3, text="Engraving", font="Arial 14", bg="ivory3", variable=cb3_val, onvalue=1,
                 offvalue=0)

# Мітка для виводу інформації
jewelry_info_str = StringVar()
jewelry_info_str.set("")
info_label = Label(root, bg="white", font="Arial 14", height=10, width=40, textvariable=jewelry_info_str)

# Кнопка підрахунку загальної вартості виробу
calculation_button = Button(root, text="Calculate price", font="Arial 24 bold", bg="gold2", activebackground="gold3")

calculation_button.bind("<Button-1>", calculator)

# Кнопка виводу інформації про розробника
about_button = Button(root, text="About program", bg="light goldenrod", font="Arial 12")

about_button.bind("<Button-1>", about_program)

# --------------------------------------------------
# Упаковка віджетів
#
# container_label1.pack(side=LEFT, fill=BOTH, expand=1)
# b1.pack(side=TOP, fill=BOTH, expand=1)
# b2.pack(side=TOP, fill=BOTH, expand=1)
# b3.pack(side=TOP, fill=BOTH, expand=1)
# b4.pack(side=TOP, fill=BOTH, expand=1)
#
# title_label1.pack(side=TOP, fill=BOTH, expand=1)
# container_label2.pack(side=TOP, fill=BOTH, expand=1)
# r1.pack(side=LEFT, fill=X, expand=1)
# r2.pack(side=LEFT, fill=X, expand=1)
# r3.pack(side=LEFT, fill=X, expand=1)
#
# title_label2.pack(side=TOP, fill=BOTH, expand=1)
# container_label3.pack(side=TOP, fill=BOTH, expand=1)
# c1.pack(side=LEFT, fill=X, expand=1)
# c2.pack(side=LEFT, fill=X, expand=1)
# c3.pack(side=LEFT, fill=X, expand=1)
#
# info_label.pack(side=TOP, fill=BOTH, expand=1)
#
# calculation_button.pack(side=TOP, fill=BOTH, expand=1)
#
# about_button.pack(side=TOP, fill=BOTH, expand=1)

container_label1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
b1.place(relx=0, rely=0, relwidth=1, relheight=0.25)
b2.place(relx=0, rely=0.25, relwidth=1, relheight=0.25)
b3.place(relx=0, rely=0.50, relwidth=1, relheight=0.25)
b4.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

container_label2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.20)
title_label1.place(relx=0, rely=0, relwidth=1, relheight=0.25)
r1.place(relx=0, rely=0.25, relwidth=0.33, relheight=0.3)
r2.place(relx=0.33, rely=0.25, relwidth=0.33, relheight=0.3)
r3.place(relx=0.66, rely=0.25, relwidth=0.33, relheight=0.3)

container_label3.place(relx=0.3, rely=0.15, relwidth=0.7, relheight=0.20)
title_label2.place(relx=0, rely=0, relwidth=1, relheight=0.25)
c1.place(relx=0, rely=0.25, relwidth=0.33, relheight=0.3)
c2.place(relx=0.33, rely=0.25, relwidth=0.33, relheight=0.3)
c3.place(relx=0.66, rely=0.25, relwidth=0.33, relheight=0.3)

info_label.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.5)

calculation_button.place(relx=0.3, rely=0.70, relwidth=0.7, relheight=0.20)
about_button.place(relx=0.3, rely=0.89, relwidth=0.7, relheight=0.11)
root.mainloop()
