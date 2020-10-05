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

# Проби
probs = {
    '375' : 1230,
    '585' : 1373,
    '875' : 2100,
    "925" : 3400
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
        if jewelry == 1 : s = "Ring\n"
        if jewelry == 2 : s = "Necklace\n"
        if jewelry == 3 : s = "Bracelet\n"
        if jewelry == 4 : s = "Earrings\n"

        if am_val.get() > 0: s += "Amount: " + str(am_val.get()) + "\n"

        if rb_val.get() == metal['rgold']:
            s += "Rose gold metal\n"
        elif rb_val.get() == metal['wgold']:
            s += "White gold metal\n"
        else:
            s += "Silver metal\n"

        if cb1_val.get() == 1:
            s += "With diamond\n"
        if cb2_val.get() == 1:
            s += "With gold plating\n"
        if cb3_val.get() == 1:
            s += "With engraving\n"

        if gems_val.get() == 1:
            s += "With " + str(gems_val.get()) + " gemstone\n"
        elif gems_val.get() == 0:
            s += "No gemstones\n"
        else:
            s += "With " + str(gems_val.get()) + " gemstones\n"

        if len(prob_list.curselection()) != 0:
            if prob_list.curselection()[0] == 0:
                s += "Prob: 375\n"
            elif prob_list.curselection()[0] == 1:
                s += "Prob: 585\n"
            elif prob_list.curselection()[0] == 2:
                s += "Prob: 875\n"
            elif prob_list.curselection()[0] == 3:
                s += "Prob: 925\n"


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

    if len(prob_list.curselection()) != 0:
        if prob_list.curselection()[0] == 0 : price += probs['375']
        elif prob_list.curselection()[0] == 1 : price += probs['585']
        elif prob_list.curselection()[0] == 2 : price += probs['875']
        elif prob_list.curselection()[0] == 3 : price += probs['925']

    if am_val.get() > 0 : price *= am_val.get()

    price += gems_val.get()*1000

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

# Мітка-контейнер вибору прикраси L
container_label1 = Frame(root)

# Кнопки вибору прикраси
b1 = Button(container_label1, text="Ring", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")
b2 = Button(container_label1, text="Necklace", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")
b3 = Button(container_label1, text="Bracelet", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")
b4 = Button(container_label1, text="Earrings", font="Arial 18 bold", bg="Goldenrod3", activebackground="Goldenrod1")

b1.bind("<Button-1>", jewelry1)
b2.bind("<Button-1>", jewelry2)
b3.bind("<Button-1>", jewelry3)
b4.bind("<Button-1>", jewelry4)

# Мітка "Оберіть метал"
title_label1 = Label(root, text="Оберіть метал", font="Arial 16 bold")
# Контейнер L1
container_label2 = Frame(root)

# Створення радіокнопок для вибору металу
rb_val = IntVar()
rb_val.set(metal['rgold'])

r1 = Radiobutton(container_label2, text="Rose gold", font="Arial 14", bg="gold2", variable=rb_val, value=metal['rgold'])
r2 = Radiobutton(container_label2, text="White gold", font="Arial 14", bg="gold2", variable=rb_val,
                 value=metal['wgold'])
r3 = Radiobutton(container_label2, text="Silver", font="Arial 14", bg="gold2", variable=rb_val, value=metal['silver'])

# Мітка "Оберіть додаткові опції"
title_label2 = Label(root, text="Оберіть додаткові опції", font="Arial 14 bold")
# Контейнер L2
container_label3 = Frame(root)

# Створення чекбоксів для вибору додаткових опцій
cb1_val = IntVar()
cb1_val.set(0)
c1 = Checkbutton(container_label3, text="Faceting", font="Arial 14", bg="ivory3", variable=cb1_val, onvalue=1,
                 offvalue=0)

cb2_val = IntVar()
cb2_val.set(0)
c2 = Checkbutton(container_label3, text="Gold plating", font="Arial 14", bg="ivory3", variable=cb2_val, onvalue=1,
                 offvalue=0)

cb3_val = IntVar()
cb3_val.set(0)
c3 = Checkbutton(container_label3, text="Engraving", font="Arial 14", bg="ivory3", variable=cb3_val, onvalue=1,
                 offvalue=0)

# Мітка "Введіть кількість прикрас"
title_label3 = Label(root, text="Введіть кількість прикрас", font="Arial 14 bold")

# Поле для вводу кількості прикрас
am_val = IntVar()
am_val.set(1)
amount_entry = Entry(root, textvariable=am_val)

# Мітка "Оберіть пробу"
title_label4 = Label(root, text="Оберіть пробу", font="Arial 14 bold")

# Список проб
prob_list = Listbox(height=4, selectmode=SINGLE)
prob_list.selectedindex = 1

for prob in probs.keys():
    prob_list.insert(END, prob)

# Мітка "Виберіть кількість каменів в огранці"
title_label5 = Label(root, text="Виберіть кількість каменів в огранці(0-10)", font="Arial 14 bold")

# Спінбокс для вибору кількості каменів в огранці
gems_val = IntVar()
gems_val.set(1)
gems_spinbox = Spinbox(root, from_=0, to=10, textvariable=gems_val)

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

container_label1.pack(side=LEFT, fill=BOTH, expand=1)
b1.pack(side=TOP, fill=BOTH, expand=1)
b2.pack(side=TOP, fill=BOTH, expand=1)
b3.pack(side=TOP, fill=BOTH, expand=1)
b4.pack(side=TOP, fill=BOTH, expand=1)

title_label1.pack(side=TOP, fill=BOTH, expand=1)
container_label2.pack(side=TOP, fill=BOTH, expand=1)
r1.pack(side=LEFT, fill=X, expand=1)
r2.pack(side=LEFT, fill=X, expand=1)
r3.pack(side=LEFT, fill=X, expand=1)

title_label2.pack(side=TOP, fill=BOTH, expand=1)
container_label3.pack(side=TOP, fill=BOTH, expand=1)
c1.pack(side=LEFT, fill=X, expand=1)
c2.pack(side=LEFT, fill=X, expand=1)
c3.pack(side=LEFT, fill=X, expand=1)

title_label3.pack(side=TOP, fill=BOTH, expand=1)
amount_entry.pack(side=TOP, fill=BOTH, expand=1)

title_label4.pack(side=TOP, fill=BOTH, expand=1)
prob_list.pack(side=TOP, fill=BOTH, expand=1)

title_label5.pack(side=TOP, fill=BOTH, expand=1)
gems_spinbox.pack(side=TOP, fill=BOTH, expand=1)

info_label.pack(side=TOP, fill=BOTH, expand=1)

calculation_button.pack(side=TOP, fill=BOTH, expand=1)

about_button.pack(side=TOP, fill=BOTH, expand=1)
root.mainloop()