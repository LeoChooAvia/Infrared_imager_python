import tkinter
import csv
import numpy as np
import time
import sys

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageColor
from tkinter import messagebox
from tkinter import ttk
from sys import exit



metod = "BOX"
mas = []
palette = "Iron"
imax = 1
jmax = 1
imin = 1
jmin = 1
pozx = 0
pozy = 0
k = 0
temp = float(1000)

def trig():
    MAX()
    MIN()
    get_imadge(mas)
    global metod
    metod = combometod.get()

def on_wasd(event):
    global pozy, pozx
    pozx = int(event.x)
    pozy = int(event.y)
    print(pozx, " ", pozy)

def MAX():
    a=e_max.get()
    if a == '':
        return 1000
    else:
        return a

def MIN():
    b = e_min.get()
    if b == '':
        return 1000
    else:
        return b

def Max_t(arr):
    global imax, imin, jmax, jmin
    min_t = float(500)
    max_t = float(-100)
    a = MAX()
    for i in range(0, 24):
        for j in range(0, 32):
            if float(arr[i][j]) < min_t:
                min_t = float(arr[i][j])
                imin = i
                jmin = j
            if float(arr[i][j]) > max_t:
                max_t = float(arr[i][j])
                imax = i
                jmax = j
    if a==1000:
        return float(max_t)
    else:
        return float(a)

def Min_t(arr):
    global imax, imin, jmax, jmin
    min_t = float(500)
    max_t = float(-100)
    a = MIN()
    for i in range(0, 24):
        for j in range(0, 32):
            if float(arr[i][j]) < min_t:
                min_t = float(arr[i][j])
                imin = i
                jmin = j
            if float(arr[i][j]) > max_t:
                max_t = float(arr[i][j])
                imax = i
                jmax = j
    if a == 1000:
        return float(min_t)
    else:
        return float(a)

def on_closing():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        app.destroy()

def get_path():
    file_menu.entryconfig("Открыть", state = DISABLED)

    path = filedialog.askopenfilename()
    print("\n", path, "\n")
    open_arr(path, mas)

def open_arr(path, mas):
    with open(path, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            mas.append(row)

        for i in range(0, 24):
            for j in range(0, 32):
                print(float(mas[i][j]), end=' ,')
            print()

        print()

        get_imadge(mas)

def get_imadge(arr):
    global metod, temp, k
    metod = combometod.get()

    global palette
    palette = combopalette.get()

    color_black_and_white = [[tuple()]*32 for i in range(0, 24)] # Ч/Б палитра
    color_iron = [[tuple()] * 32 for i in range(0, 24)] # Iron палитра

    min = float(-1000)
    max = float(1000)

    print("Max temp = ", Max_t(arr), ", Min temp = ", Min_t(arr))
    print("Old_Max temp = ", Max_t(arr), ", Old_Min temp = ", Min_t(arr), "\n")

    OldMax = round(Max_t(arr), 2)
    OldMin = round(Min_t(arr), 2)

    NewMax = float(255)
    NewMin = float(0)
    OldRange = float(OldMax - OldMin)
    NewRange = float(NewMax - NewMin)

    iron_palette = ["#00000a","#000014","#00001e","#000025","#00002a","#00002e","#000032","#000036","#00003a","#00003e","#000042","#000046","#00004a","#00004f","#000052","#010055","#010057","#020059","#02005c","#03005e","#040061","#040063","#050065","#060067","#070069","#08006b","#09006e","#0a0070","#0b0073","#0c0074","#0d0075","#0d0076","#0e0077","#100078","#120079","#13007b","#15007c","#17007d","#19007e","#1b0080","#1c0081","#1e0083","#200084","#220085","#240086","#260087","#280089","#2a0089","#2c008a","#2e008b","#30008c","#32008d","#34008e","#36008e","#38008f","#390090","#3b0091","#3c0092","#3e0093","#3f0093","#410094","#420095","#440095","#450096","#470096","#490096","#4a0096","#4c0097","#4e0097","#4f0097","#510097","#520098","#540098","#560098","#580099","#5a0099","#5c0099","#5d009a","#5f009a","#61009b","#63009b","#64009b","#66009b","#68009b","#6a009b","#6c009c","#6d009c","#6f009c","#70009c","#71009d","#73009d","#75009d","#77009d","#78009d","#7a009d","#7c009d","#7e009d","#7f009d","#81009d","#83009d","#84009d","#86009d","#87009d","#89009d","#8a009d","#8b009d","#8d009d","#8f009c","#91009c","#93009c","#95009c","#96009b","#98009b","#99009b","#9b009b","#9c009b","#9d009b","#9f009b","#a0009b","#a2009b","#a3009b","#a4009b","#a6009a","#a7009a","#a8009a","#a90099","#aa0099","#ab0099","#ad0099","#ae0198","#af0198","#b00198","#b00198","#b10197","#b20197","#b30196","#b40296","#b50295","#b60295","#b70395","#b80395","#b90495","#ba0495","#ba0494","#bb0593","#bc0593","#bd0593","#be0692","#bf0692","#bf0692","#c00791","#c00791","#c10890","#c10990","#c20a8f","#c30a8e","#c30b8e","#c40c8d","#c50c8c","#c60d8b","#c60e8a","#c70f89","#c81088","#c91187","#ca1286","#ca1385","#cb1385","#cb1484","#cc1582","#cd1681","#ce1780","#ce187e","#cf187c","#cf197b","#d01a79","#d11b78","#d11c76","#d21c75","#d21d74","#d31e72","#d32071","#d4216f","#d4226e","#d5236b","#d52469","#d62567","#d72665","#d82764","#d82862","#d92a60","#da2b5e","#da2c5c","#db2e5a","#db2f57","#dc2f54","#dd3051","#dd314e","#de324a","#de3347","#df3444","#df3541","#df363d","#e0373a","#e03837","#e03933","#e13a30","#e23b2d","#e23c2a","#e33d26","#e33e23","#e43f20","#e4411d","#e4421c","#e5431b","#e54419","#e54518","#e64616","#e74715","#e74814","#e74913","#e84a12","#e84c10","#e84c0f","#e94d0e","#e94d0d","#ea4e0c","#ea4f0c","#eb500b","#eb510a","#eb520a","#eb5309","#ec5409","#ec5608","#ec5708","#ec5808","#ed5907","#ed5a07","#ed5b06","#ee5c06","#ee5c05","#ee5d05","#ee5e05","#ef5f04","#ef6004","#ef6104","#ef6204","#f06303","#f06403","#f06503","#f16603","#f16603","#f16703","#f16803","#f16902","#f16a02","#f16b02","#f16b02","#f26c01","#f26d01","#f26e01","#f36f01","#f37001","#f37101","#f37201","#f47300","#f47400","#f47500","#f47600","#f47700","#f47800","#f47a00","#f57b00","#f57c00","#f57e00","#f57f00","#f68000","#f68100","#f68200","#f78300","#f78400","#f78500","#f78600","#f88700","#f88800","#f88800","#f88900","#f88a00","#f88b00","#f88c00","#f98d00","#f98d00","#f98e00","#f98f00","#f99000","#f99100","#f99200","#f99300","#fa9400","#fa9500","#fa9600","#fb9800","#fb9900","#fb9a00","#fb9c00","#fc9d00","#fc9f00","#fca000","#fca100","#fda200","#fda300","#fda400","#fda600","#fda700","#fda800","#fdaa00","#fdab00","#fdac00","#fdad00","#fdae00","#feaf00","#feb000","#feb100","#feb200","#feb300","#feb400","#feb500","#feb600","#feb800","#feb900","#feb900","#feba00","#febb00","#febc00","#febd00","#febe00","#fec000","#fec100","#fec200","#fec300","#fec400","#fec500","#fec600","#fec700","#fec800","#fec901","#feca01","#feca01","#fecb01","#fecc02","#fecd02","#fece03","#fecf04","#fecf04","#fed005","#fed106","#fed308","#fed409","#fed50a","#fed60a","#fed70b","#fed80c","#fed90d","#ffda0e","#ffda0e","#ffdb10","#ffdc12","#ffdc14","#ffdd16","#ffde19","#ffde1b","#ffdf1e","#ffe020","#ffe122","#ffe224","#ffe226","#ffe328","#ffe42b","#ffe42e","#ffe531","#ffe635","#ffe638","#ffe73c","#ffe83f","#ffe943","#ffea46","#ffeb49","#ffeb4d","#ffec50","#ffed54","#ffee57","#ffee5b","#ffee5f","#ffef63","#ffef67","#fff06a","#fff06e","#fff172","#fff177","#fff17b","#fff280","#fff285","#fff28a","#fff38e","#fff492","#fff496","#fff49a","#fff59e","#fff5a2","#fff5a6","#fff6aa","#fff6af","#fff7b3","#fff7b6","#fff8ba","#fff8bd","#fff8c1","#fff8c4","#fff9c7","#fff9ca","#fff9cd","#fffad1","#fffad4","#fffbd8","#fffcdb","#fffcdf","#fffde2","#fffde5","#fffde8","#fffeeb","#fffeee","#fffef1","#fffef4","#fffff6"]
    print(len(iron_palette), "\n")
    iron = OldRange / 433
    for i in range(0, 433):
        iron_palette[i] = ImageColor.getcolor(iron_palette[i], "RGB")

    for i in range(0, 24):
        for j in range(0, 32):
            ind = int((float(arr[i][j]) - Min_t(arr)) / iron) - 1
            if ind >= 433:
                ind = 432
            if ind < 0:
                ind = 0
            color_iron[i][j] = iron_palette[ind]



    for i in range(0, 24):
        for j in range(0, 32):
            color_black_and_white[i][j] = tuple([int((((float(arr[i][j]) - float(OldMin)) * NewRange) / OldRange) + NewMin), int((((float(arr[i][j]) - float(OldMin)) * NewRange) / OldRange) + NewMin), int((((float(arr[i][j]) - float(OldMin)) * NewRange) / OldRange) + NewMin)])
            if int(color_black_and_white[i][j][1]) > 255:
                color_black_and_white[i][j] = tuple([255, 255, 255])
            if int(color_black_and_white[i][j][1]) < 0:
                color_black_and_white[i][j] = tuple([0, 0, 0])

    if palette == "Iron":
        array = np.array(color_iron, dtype=np.uint8) # Палитра
        for row in color_iron:
            print(row)
    elif palette == "black and white":
        array = np.array(color_black_and_white, dtype=np.uint8)  # Палитра
        for row in color_black_and_white:
            print(row)

    img = Image.fromarray(array)

    print()
    if metod == "BOX":
        img = img.resize((576, 432), Image.BOX)
    elif metod == "LINEAR":
        img = img.resize((576, 432), Image.LINEAR)
    elif metod == "BILINEAR":
        img = img.resize((576, 432), Image.BILINEAR)
    elif metod == "CUBIC":
        img = img.resize((576, 432), Image.CUBIC)
    elif metod == "BICUBIC":
        img = img.resize((576, 432), Image.BICUBIC)
    elif metod == "LANCZOS":
        img = img.resize((576, 432), Image.LANCZOS)
    elif metod == "ANTIALIAS":
        img = img.resize((576, 432), Image.ANTIALIAS)
    elif metod == "NEAREST":
        img = img.resize((576, 432), Image.NEAREST)
    elif metod == "HAMMING":
        img = img.resize((576, 432), Image.HAMMING)

    img.save('new.png')
    pixels = list(img.getdata())
    pixels_value = []
    buf = [tuple()]
    j = 0
    i2 = 0
    for i in range(0, len(pixels)):
        if j < 433:
            buf.append(pixels[i*j])
            pixels_value.append(buf)
        else:
            j=0
            buf = [tuple()]
    #print(pixels_value[190][207])

    #for i in pixels_value:
        #print(i)

    img = ImageTk.PhotoImage(img)
    label = Label(app, image=img)
    label.image = img
    label.place(x=255, y=0)

    label.bind_all("<Button-3>", on_wasd)
    print("pozition = ", pozx, "", pozy)
    iron_color_ind = 0

    img2 = Image.open('new.png')
    pix = img2.load()
    print(pix[pozx, pozy])

    for i in range(0, 433):
        if pix[pozx, pozy] == iron_palette[i]:
            iron_color_ind = i
            print("color_index = ", iron_color_ind)
            temp = float(iron_color_ind) / 4.33 / 100
            temp = (OldMax - OldMin) * temp + OldMin
            print("temp = ", temp)


    btn['state'] = 'normal'
    e_min['state'] = 'normal'
    e_max['state'] = 'normal'

    e_max.delete(0, END)
    e_max.insert(0, str(OldMax))
    e_min.delete(0, END)
    e_min.insert(0, str(OldMin))

    if f.get() == 1:
        canvas2 = Canvas(app, bg="white", width=9, height=9)
        canvas2.create_rectangle(2, 2, 10, 10, fill="#ff0000")
        canvas2.place(x=jmax*18+255-13, y=imax*18-13)

        canvas3 = Canvas(app, bg="white", width=9, height=9)
        canvas3.create_rectangle(2, 2, 10, 10, fill="#0000ff")
        canvas3.place(x=jmin * 18 + 255 + 5, y=imin * 18 + 5)

    if k!=0 and metod == "BOX":
        e_temp['state'] = 'normal'
        e_temp.delete(0, END)
        e_temp.insert(0, str(round(temp, 2)))
        e_temp['state'] = 'disabled'
    else:
        e_temp['state'] = 'normal'
        e_temp.delete(0, END)
        e_temp.insert(0, "None")
        e_temp['state'] = 'disabled'
    k+=1



app = Tk()

app.geometry("840x440")
app.resizable(False, False)
app.title("Termal Imadger 1.0")

menu_bar = Menu(app)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=get_path)
file_menu.add_separator()
file_menu.add_command(label="Выйти", command=exit)

reference_menu = Menu(menu_bar, tearoff=0)
reference_menu.add_command(label="Я ничего здесь не придумал")

menu_bar.add_cascade(label="Файл", menu=file_menu)
menu_bar.add_cascade(label="Справка", menu=reference_menu)
app.configure(menu=menu_bar)

canvas = Canvas(app, bg="white", width=577, height=433)
canvas.place(anchor=NW, x=255, y=0)
canvas.create_rectangle(2, 2, 578, 434, outline="#80CBC4")

app.protocol("WM_DELETE_WINDOW", on_closing)

e_min = Entry(app)
e_max = Entry(app)
e_min['state'] = 'disabled'
e_max['state'] = 'disabled'
e_min.place(anchor=NW, x=170, y=5, width=80)
e_max.place(anchor=NW, x=170, y=30, width=80)

btn = tkinter.Button(text="Применить", command=trig)
btn['state'] = 'disabled'
btn.place(anchor=NW, x=5, y=400, height=25, width=245)

text_min_t = Label(app, text="Минимальная температура:")
text_max_t = Label(app, text="Максимальная температура:")
text_min_t.place(x=5, y=5)
text_max_t.place(x=5, y=30)

text_metod = Label(app, text="Алгоритм интерполяции:")
text_metod.place(x=45, y=55)

combometod = ttk.Combobox(app, values=[
                                    "BOX",
                                    "LINEAR",
                                    "BILINEAR",
                                    "CUBIC",
                                    "BICUBIC",
                                    "LANCZOS",
                                    "ANTIALIAS",
                                    "NEAREST",
                                    "HAMMING"])
combometod.current(0)
combometod.place(anchor=NW, x=5, y=80, height=20, width=245)

text_palette = Label(app, text="Цветовая палитра:")
text_palette.place(x=65, y=105)

combopalette = ttk.Combobox(app, values=[
                                    "Iron",
                                    "black and white"])
combopalette.current(0)
combopalette.place(anchor=NW, x=5, y=130, height=20, width=245)

f = tkinter.IntVar()
f.set(1)
flags = Checkbutton(app, text='Маркеры максимальной и \n минимальной температуры',variable=f, onvalue=1, offvalue=0)
flags.place(x = 30, y = 155)

text_temp = Label(app, text="Температура в указанной точке:\n(клик правой кнопкой мыши и применить)\n(*работает только в методе BOX)")
text_temp.place(x=5, y=195)

e_temp = Entry(app, justify=CENTER, font=60)
e_temp.insert(0, "None")
e_temp['state'] = 'disabled'
e_temp.place(anchor=NW, x=5, y=255, width=245, height=50)



app.mainloop()