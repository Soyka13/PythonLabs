coding = 1251

from tkinter import *

root = Tk()
root.title("Jewelry")

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
b1 = Button(root, text="Ring", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1", height=3)
b2 = Button(root, text="Necklece", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1", height=3)
b3 = Button(root, text="Bracelet", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1", height=3)
b4 = Button(root, text="Earings", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1", height=3)

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

r1 = Radiobutton(container_label2, text="Rose gold", font="Arial 14", bg="gold2", variable=rb_val, value=metal['rgold'], width=12)
r2 = Radiobutton(container_label2, text="White gold", font="Arial 14", bg="gold2", variable=rb_val,
                 value=metal['wgold'], width=12)
r3 = Radiobutton(container_label2, text="Silver", font="Arial 14", bg="gold2", variable=rb_val, value=metal['silver'], width=12)

# Мітка "Оберіть додаткові опції"

container_label3 = Label(root)
title_label2 = Label(container_label3, text="Оберіть додаткові опції", font="Arial 14 bold")

# Створення чекбоксів для вибору додаткових опцій
cb1_val = IntVar()
cb1_val.set(0)
c1 = Checkbutton(container_label3, text="Diamand", font="Arial 14", bg="ivory3", variable=cb1_val, onvalue=1,
                 offvalue=0, width=12)

cb2_val = IntVar()
cb2_val.set(0)
c2 = Checkbutton(container_label3, text="Gold plating", font="Arial 14", bg="ivory3", variable=cb2_val, onvalue=1,
                 offvalue=0, width=12)

cb3_val = IntVar()
cb3_val.set(0)
c3 = Checkbutton(container_label3, text="Engraving", font="Arial 14", bg="ivory3", variable=cb3_val, onvalue=1,
                 offvalue=0, width=12)

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

b1.grid(row=0, column=0, sticky='NESW', rowspan=2)
b2.grid(row=2, column=0, sticky='NESW', rowspan=2)
b3.grid(row=4, column=0, sticky='NESW', rowspan=2)
b4.grid(row=6, column=0, sticky='NESW', rowspan=2)

container_label2.grid(row=0, column=1, sticky='NESW')
title_label1.grid(row=1, column=1, sticky='NESW', columnspan=3)
r1.grid(row=2, column=1, sticky='NESW')
r2.grid(row=2, column=2, sticky='NESW')
r3.grid(row=2, column=3, sticky='NESW')

container_label3.grid(row=1, column=1)
title_label2.grid(row=1, column=1, columnspan=3)
c1.grid(row=2, column=1, sticky='NESW')
c2.grid(row=2, column=2, sticky='NESW')
c3.grid(row=2, column=3, sticky='NESW')

info_label.grid(row=3, column=1, rowspan=2, sticky='NESW')

calculation_button.grid(row=6, column=1, sticky='NESW')
about_button.grid(row=7, column=1, sticky='NESW')

root.mainloop()
