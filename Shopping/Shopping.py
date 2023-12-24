import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from numpy import random
import re

bgColour = "#F37A10"
def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()
def TrendyolDatabase(): #ÜRÜNLERİ RASTGELE DEĞİŞTİRME
    connection = sqlite3.connect("data/trendyol.db")
    cursor = connection.cursor()

    cursor.execute("select Urun.urunAdi,Urun.urunKodu,Urun.urunFiyat, UrunOzellik.kumasTipi,UrunOzellik.urunDesen from Urun inner join UrunOzellik on Urun.urunId = UrunOzellik.urunId;")
    data = cursor.fetchall()
    idx = random.randint(0, len(data) - 1)
    data = data[idx]
    print(data)
    return data

#Sadece 1 kez çalıştırılır
    """
    cursor.execute("Create Table Urun(urunId Integer Primary Key AUTOINCREMENT, urunAdi Text, urunKodu Int, urunFiyat Real, urunBeden Char[4]);")
    cursor.execute("Create Table UrunOzellik(urunOzellikId Integer Primary Key AUTOINCREMENT, kumasTipi Text, renk Text, urunId Int, urunStok Boolean Not Null, urunBoy Real, urunDesen Text,urunYas Text, urunMateryal Text, Foreign Key(urunId) References Urun(urunId));")
    cursor.execute("Create Table UrunYorum(yorumId Integer Primary Key AUTOINCREMENT, urunId Int, yorum Text, yorumDurum Boolean Not Null, Foreign Key(urunId) References Urun(urunId));")
    cursor.execute("Create Table Musteri(musteriId Integer Primary Key AUTOINCREMENT, yorumId Int, adi Text, soyadi Text, Foreign Key(yorumId) References UrunYorum(yorumId));")
    #URUN
    """

    connection.commit()
    connection.close()

def Insert(entry_urunAdi,entry_urunKodu,entry_urunFiyat,entry_urunBeden,entry_kumasTipi,entry_renk,entry_urunStok,entry_urunBoy,entry_urunDesen,entry_urunYas,entry_urunMateryal):
    connection = sqlite3.connect("data/trendyol.db")
    cursor = connection.cursor()

    urunAdi=entry_urunAdi.get()
    urunKodu=entry_urunKodu.get()
    urunFiyat=entry_urunFiyat.get()
    urunBeden=entry_urunBeden.get()
    urunKumasTipi=entry_kumasTipi.get()
    urunRenk=entry_renk.get()
    urunStok=entry_urunStok.get()
    urunBoy=entry_urunBoy.get()
    urunDesen=entry_urunDesen.get()
    urunYas=entry_urunYas.get()
    urunMateryal=entry_urunMateryal.get()

    sql= 'Insert Into Urun(urunAdi,urunKodu,urunFiyat,urunBeden) values (?,?,?,?);'
    values = (urunAdi,urunKodu,urunFiyat,urunBeden)
    cursor.execute(sql,values)
    urunId = cursor.lastrowid

    sql2='Insert Into UrunOzellik(kumasTipi, renk, urunId, urunStok, urunBoy, urunDesen,urunYas, urunMateryal) values (?,?,?,?,?,?,?,?)'
    values2=(urunKumasTipi,urunRenk,urunId,urunStok,urunBoy,urunDesen,urunYas,urunMateryal)
    cursor.execute(sql2,values2)

    connection.commit()
    connection.close()
    print("EKLEME İŞLEMİ BAŞARILI!")

def Update(id,entry_urunAdi,entry_urunKodu,entry_urunFiyat,entry_urunBeden,entry_kumasTipi,entry_renk,entry_urunStok,entry_urunBoy,entry_urunDesen,entry_urunYas,entry_urunMateryal):
    connection = sqlite3.connect("data/trendyol.db")
    cursor = connection.cursor()
    id = id;
    urunAdi = entry_urunAdi.get()
    urunKodu = entry_urunKodu.get()
    urunFiyat = entry_urunFiyat.get()
    urunBeden = entry_urunBeden.get()
    urunKumasTipi = entry_kumasTipi.get()
    urunRenk = entry_renk.get()
    urunStok = entry_urunStok.get()
    urunBoy = entry_urunBoy.get()
    urunDesen = entry_urunDesen.get()
    urunYas = entry_urunYas.get()
    urunMateryal = entry_urunMateryal.get()

    sql = 'Update Urun Set urunAdi= ?,urunKodu=?,urunFiyat=?,urunBeden= ? where urunID=?'
    values=(urunAdi,urunKodu,urunFiyat,urunBeden,id)
    cursor.execute(sql,values)

    sql2 = 'Update  UrunOzellik Set kumasTipi= ?, renk=?, urunId=?, urunStok=?, urunBoy=?, urunDesen=?,urunYas=?, urunMateryal=? where urunId=?'
    values2 = (urunKumasTipi, urunRenk, id, urunStok, urunBoy, urunDesen, urunYas, urunMateryal,id)
    cursor.execute(sql2, values2)

    connection.commit()
    connection.close()
    LoadFrame4()

    print("DEĞİŞTİRME İŞLEMİ BAŞARILI!")

def Delete(urunId):
    connection = sqlite3.connect("data/trendyol.db")
    cursor = connection.cursor()

    sql = 'Delete from Urun where urunId=?'
    values = (urunId,) # [urunId]
    cursor.execute(sql, values)

    sql2 = 'Delete from UrunOzellik where urunId=?'
    values2 = (urunId,)
    cursor.execute(sql2, values2)

    connection.commit()
    connection.close()

    LoadFrame5()

    print("SİLME İŞLEMİ BAŞARILI!")

def Select():
    connection = sqlite3.connect("data/trendyol.db")
    cursor = connection.cursor()

    cursor.execute('select urun.urunId,urun.urunAdi,urun.urunKodu,urun.urunFiyat,urun.urunBeden,UrunOzellik.kumasTipi,UrunOzellik.renk,UrunOzellik.urunStok,UrunOzellik.urunBoy,UrunOzellik.urunDesen,UrunOzellik.urunYas,UrunOzellik.urunMateryal from Urun inner join UrunOzellik on Urun.urunId=UrunOzellik.urunId')
    data= cursor.fetchall()

    connection.commit()
    connection.close()
    return data
    print("EKLEME İŞLEMİ BAŞARILI!")

def Select2():
    connection = sqlite3.connect("data/trendyol.db")
    cursor = connection.cursor()

    cursor.execute('select urun.urunId,urun.urunAdi,urun.urunKodu,urun.urunFiyat,urun.urunBeden,UrunOzellik.kumasTipi,UrunOzellik.renk,UrunOzellik.urunStok,UrunOzellik.urunBoy,UrunOzellik.urunDesen,UrunOzellik.urunYas,UrunOzellik.urunMateryal from Urun inner join UrunOzellik on Urun.urunId=UrunOzellik.urunId where UrunOzellik.renk="Mavi" AND UrunOzellik.kumasTipi="Pamuk" ')
    data= cursor.fetchall()

    connection.commit()
    connection.close()
    return data
    print("EKLEME İŞLEMİ BAŞARILI!")

def IndexChangedUpdate(event):
    selected_item = event.widget.get()
    print("düzensiz değerler",selected_item)
    selected_item = re.sub('\{(.*?)\}','', selected_item).split()


    print("Dizi Olarak Değerler:", selected_item)
    # urun adi
    urunAdi = tk.Label(frameMain4, text="Ürün Adı:")
    urunAdi.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunAdi = tk.Entry(frameMain4)
    entry_urunAdi.insert(0, selected_item[1])
    entry_urunAdi.grid(row=1, column=1, padx=5, pady=5)

    # urun kodu
    label_urunKodu = tk.Label(frameMain4, text="Ürün Kodu:")
    label_urunKodu.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunKodu = tk.Entry(frameMain4)
    entry_urunKodu.insert(1, selected_item[2])
    entry_urunKodu.grid(row=2, column=1, padx=5, pady=5)

    # urunFiyat
    label_urunFiyat = tk.Label(frameMain4, text="Ürün Fiyatı:")
    label_urunFiyat.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunFiyat = tk.Entry(frameMain4)
    entry_urunFiyat.insert(0, selected_item[3])
    entry_urunFiyat.grid(row=3, column=1, padx=5, pady=5)

    # urunBeden
    label_urunBeden = tk.Label(frameMain4, text="Ürün Beden:")
    label_urunBeden.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunBeden = tk.Entry(frameMain4)
    entry_urunBeden.insert(0, selected_item[4])
    entry_urunBeden.grid(row=4, column=1, padx=5, pady=5)

    ##########################################################################

    # urunKumasTipi
    label_kumasTipi = tk.Label(frameMain4, text="Kumaş Tipi:")
    label_kumasTipi.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    entry_kumasTipi = tk.Entry(frameMain4)
    entry_kumasTipi.insert(0, selected_item[5])
    entry_kumasTipi.grid(row=5, column=1, padx=5, pady=5)

    # urunRenk
    label_renk = tk.Label(frameMain4, text="Renk:")
    label_renk.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    entry_renk = tk.Entry(frameMain4)
    entry_renk.insert(0, selected_item[6])
    entry_renk.grid(row=6, column=1, padx=5, pady=5)

    # urunStok
    label_urunStok = tk.Label(frameMain4, text="Stok:")
    label_urunStok.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunStok = tk.Entry(frameMain4)
    entry_urunStok.insert(0, selected_item[7])
    entry_urunStok.grid(row=7, column=1, padx=5, pady=5)

    # urunBoy
    label_urunBoy = tk.Label(frameMain4, text="Boy:")
    label_urunBoy.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunBoy = tk.Entry(frameMain4)
    entry_urunBoy.insert(0, selected_item[8])
    entry_urunBoy.grid(row=8, column=1, padx=5, pady=5)

    # urunDesen
    label_urunDesen = tk.Label(frameMain4, text="Desen:")
    label_urunDesen.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunDesen = tk.Entry(frameMain4)
    entry_urunDesen.insert(0, selected_item[9])
    entry_urunDesen.grid(row=9, column=1, padx=5, pady=5)

    # urunYas
    label_urunYas = tk.Label(frameMain4, text="Yaş:")
    label_urunYas.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunYas = tk.Entry(frameMain4)
    entry_urunYas.insert(0, selected_item[10])
    entry_urunYas.grid(row=10, column=1, padx=5, pady=5)

    # urunMateryal
    label_urunMateryal = tk.Label(frameMain4, text="Materyal:")
    label_urunMateryal.grid(row=11, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunMateryal = tk.Entry(frameMain4)
    entry_urunMateryal.insert(0, selected_item[11])
    entry_urunMateryal.grid(row=11, column=1, padx=5, pady=5)

    #########################################################################
    # değiştir düğmesi
    tk.Button(
        frameMain4,
        text="ÜRÜNÜ DEĞİŞTİR",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: Update(selected_item[0],entry_urunAdi, entry_urunKodu, entry_urunFiyat, entry_urunBeden, entry_kumasTipi,
                               entry_renk, entry_urunStok, entry_urunBoy, entry_urunDesen, entry_urunYas,
                               entry_urunMateryal)).grid(row=12, column=0, columnspan=2, pady=10)

def IndexChangedDelete(event):
    selected_item = event.widget.get()
    selected_item = re.sub('\{(.*?)\}', '', selected_item).split()
    id=selected_item[0] #silinecek urunId
    print(id)

    # silme butonu
    tk.Button(
        frameMain5,
        text="ÜRÜNÜ SİL",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: Delete(id)).grid(row=12, column=0, columnspan=2, pady=10)

# Renk ve kumaş türüne göre filtreleme sorgusu
def Filtrele(renk, kumas_tipi):
    connection = sqlite3.connect("data/trendyol.db")
    cursor = connection.cursor()

    cursor.execute(
        'select urun.urunId,urun.urunAdi,urun.urunKodu,urun.urunFiyat,urun.urunBeden,UrunOzellik.kumasTipi,UrunOzellik.renk,UrunOzellik.urunStok,UrunOzellik.urunBoy,UrunOzellik.urunDesen,UrunOzellik.urunYas,UrunOzellik.urunMateryal from Urun inner join UrunOzellik on Urun.urunId=UrunOzellik.urunId')
    data = cursor.fetchall()

    connection.commit()
    connection.close()

    # Filtrelenen veriyi gösteren frame
    clear_widgets(frameMain6)
    tk.Label(
        frameMain6,
        text="Filtrelenen Ürünler",
        bg=bgColour,
        fg="white",
        font=("TkHeadingFont", 16)
    ).pack(pady=20)

    for i in data:
        tk.Label(
            frameMain6,
            text=i,
            bg=bgColour,
            fg="white",
            font=("Shanti", 12)
        ).pack(fill="both", padx=25)


def LoadFrame1(): #ANASAYFA
    clear_widgets(frameMain2)
    frameMain.tkraise() #ana frame'i en önde tutma
    frameMain.pack_propagate(False) #frame boyutunu sabit tutma
    # logo widget
    imge = Image.open("assets/commerce.png").resize((128, 128))
    imgLogo = ImageTk.PhotoImage(imge)
    logoWidget = tk.Label(frameMain, image=imgLogo, bg=bgColour)
    logoWidget.image = imgLogo
    logoWidget.pack() #ortalama

    tk.Label(
        frameMain,
        text="ALIŞVERİŞ",
        bg=bgColour,
        fg="white",  # text colour
        font=("TkMenuFont", 14)
    ).pack()

    # button widget
    tk.Button(
        frameMain,
        text="KEŞFET",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame2()
    ).pack(pady=20)

    # button widget
    ekle=tk.Button(
        frameMain,
        text="EKLE",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame3()
    ).pack( pady=20)


    # button widget
    duzenle=tk.Button(
        frameMain,
        text="DÜZENLE",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame4()
    ).pack( pady=20)


    sil=tk.Button(
        frameMain,
        text="SİL",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame5()
    ).pack( pady=20)

    # Filtreleme butonu
    tk.Button(
        frameMain,
        text="GETİR",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame6()
    ).pack(pady=20)


def LoadFrame2(): #ürünleri değiştirme (KEŞFET BUTONU)
    clear_widgets(frameMain2)
    clear_widgets(frameMain)
    frameMain2.tkraise()

    data =TrendyolDatabase()

    # logo widget
    imgLogo = ImageTk.PhotoImage(file="assets/online-shop-128.png")
    logoWidget = tk.Label(frameMain2, image=imgLogo, bg=bgColour)
    logoWidget.image = imgLogo
    logoWidget.pack(pady=20)

    tk.Label(
        frameMain2,
        text=data[0],
        bg=bgColour,
        fg="white",  # text colour
        font=("TkHeadingFont", 20)
    ).pack(pady=25)

    data= data[1:]
    for i in data:
        tk.Label(
            frameMain2,
            text=i,
            bg=bgColour,
            fg="white",  # text colour
            font=("Shanti", 12)
        ).pack(fill="both", padx=25)

    # button widget
    tk.Button(
        frameMain2,
        text="DEĞİŞTİR",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame2()
    ).pack(pady=20)

    tk.Button(
        frameMain2,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame1()
    ).pack(pady=20)
def LoadFrame3(): #EKLE BUTONU
    clear_widgets(frameMain)
    frameMain3.tkraise()
    #urun adi
    urunAdi = tk.Label(frameMain3, text="Ürün Adı:")
    urunAdi.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunAdi = tk.Entry(frameMain3)
    entry_urunAdi.grid(row=0, column=1, padx=5, pady=5)

    #urun kodu
    label_urunKodu = tk.Label(frameMain3, text="Ürün Kodu:")
    label_urunKodu.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W) #widget hizalama
    entry_urunKodu = tk.Entry(frameMain3)
    entry_urunKodu.grid(row=1, column=1, padx=5, pady=5)

    # urunFiyat
    label_urunFiyat = tk.Label(frameMain3, text="Ürün Fiyatı:")
    label_urunFiyat.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunFiyat = tk.Entry(frameMain3)
    entry_urunFiyat.grid(row=2, column=1, padx=5, pady=5)

    # urunBeden
    label_urunBeden = tk.Label(frameMain3, text="Ürün Beden:")
    label_urunBeden.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunBeden = tk.Entry(frameMain3)
    entry_urunBeden.grid(row=3, column=1, padx=5, pady=5)

    ##########################################################################

    # urunKumasTipi
    label_kumasTipi = tk.Label(frameMain3, text="Kumaş Tipi:")
    label_kumasTipi.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_kumasTipi = tk.Entry(frameMain3)
    entry_kumasTipi.grid(row=4, column=1, padx=5, pady=5)

    # urunRenk
    label_renk = tk.Label(frameMain3, text="Renk:")
    label_renk.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    entry_renk = tk.Entry(frameMain3)
    entry_renk.grid(row=5, column=1, padx=5, pady=5)

    # urunStok
    label_urunStok = tk.Label(frameMain3, text="Stok:")
    label_urunStok.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunStok = tk.Entry(frameMain3)
    entry_urunStok.grid(row=6, column=1, padx=5, pady=5)

    # urunBoy
    label_urunBoy= tk.Label(frameMain3, text="Boy:")
    label_urunBoy.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunBoy = tk.Entry(frameMain3)
    entry_urunBoy.grid(row=7, column=1, padx=5, pady=5)

    # urunDesen
    label_urunDesen= tk.Label(frameMain3, text="Desen:")
    label_urunDesen.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunDesen = tk.Entry(frameMain3)
    entry_urunDesen.grid(row=8, column=1, padx=5, pady=5)

    # urunYas
    label_urunYas= tk.Label(frameMain3, text="Yaş:")
    label_urunYas.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunYas = tk.Entry(frameMain3)
    entry_urunYas.grid(row=9, column=1, padx=5, pady=5)

    # urunMateryal
    label_urunMateryal = tk.Label(frameMain3, text="Materyal:")
    label_urunMateryal.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)
    entry_urunMateryal = tk.Entry(frameMain3)
    entry_urunMateryal.grid(row=10, column=1, padx=5, pady=5)

    #########################################################################
    # Ekle düğmesi
    button_ekle = tk.Button(
     frameMain3,
     text="ÜRÜN EKLE",
    font=("TkHeadingFont", 16),
    bg="#FF7700",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:Insert(entry_urunAdi,entry_urunKodu,entry_urunFiyat,entry_urunBeden,entry_kumasTipi,entry_renk,entry_urunStok,entry_urunBoy,entry_urunDesen,entry_urunYas,entry_urunMateryal))
    button_ekle.grid(row=11, column=0, columnspan=2, pady=10)

    btn_geri=tk.Button(
        frameMain3,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1())
    btn_geri.grid(row=12, column=0, columnspan=2, pady=10)
def LoadFrame4(): #GÜNCELLE BUTONU
    clear_widgets(frameMain)
    frameMain4.tkraise()

    listObjects= Select()

    # Combobox
    combo_var = tk.StringVar()

    combo = tk.Label(frameMain4, text="Ürün seç")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    combo = ttk.Combobox(frameMain4, values= listObjects)
    combo.grid(row=0, column=1, padx=5, pady=15)

    # Seçim değiştiğinde tetiklenecek olay işleyicisi ekleniyor
    combo.bind('<<ComboboxSelected>>', IndexChangedUpdate)


    btn_geri = tk.Button(
        frameMain4,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()).grid(row=13, column=0, columnspan=2, pady=10)
def LoadFrame5(): #SİL BUTONU
    clear_widgets(frameMain)
    frameMain5.tkraise()

    listObjects = Select()

    # Combobox
    combo_var = tk.StringVar()

    combo = tk.Label(frameMain5, text="Ürün seç")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    combo = ttk.Combobox(frameMain5, values=listObjects)
    combo.grid(row=0, column=1, padx=5, pady=15)

    # Seçim değiştiğinde tetiklenecek
    combo.bind('<<ComboboxSelected>>', IndexChangedDelete)

    btn_geri = tk.Button(
        frameMain5,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()).grid(row=13, column=0, columnspan=2, pady=10)

# Silme işlemi başarılı mesajını içeren fonksiyon
def LoadFrame6():
        clear_widgets(frameMain)
        frameMain6.tkraise()

        listObjects = Select2()

        # urun kodu
        label_urunKodu1 = tk.Label(frameMain6, text=listObjects[0])
        label_urunKodu2 = tk.Label(frameMain6, text=listObjects[1])
        label_urunKodu3 = tk.Label(frameMain6, text=listObjects[2])
        label_urunKodu1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)  # widget hizalama
        label_urunKodu2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)  # widget hizalama
        label_urunKodu3.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)  # widget hizalama


        # Geri butonu
        btn_geri = tk.Button(
            frameMain6,
            text="GERİ",
            font=("TkHeadingFont", 16),
            bg="#FF7700",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: LoadFrame1()).grid(row=13, column=0, columnspan=2, pady=10)




root = tk.Tk() #window object
root.title("ALIŞVERİŞ")


#frame widgets
frameMain = tk.Frame(root, width=500, height=600, bg=bgColour)
frameMain2 = tk.Frame(root, bg=bgColour)
frameMain3 = tk.Frame(root, bg=bgColour)
frameMain4 = tk.Frame(root, bg=bgColour)
frameMain5 = tk.Frame(root, bg=bgColour)
frameMain6 = tk.Frame(root, bg=bgColour)

for frame in (frameMain,frameMain2,frameMain3,frameMain4,frameMain5,frameMain6):
    frame.grid(row=0, column=0)

LoadFrame1()
#TrendyolDatabase()
# run app
root.mainloop()