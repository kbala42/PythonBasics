import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import folium
import requests
import json
import os

ROOT_URL="https://api.collectapi.com/health/"
baslik={"content-type":"application/json",
        "authorization":"apikey 1gxNgOb4fKCZq7OwFkabsF:20msAAW9A8ojeEQda3eel6"}
#Şehirleri listeler
#r=requests.get(ROOT_URL+"districtList?il=",headers=baslik).json()
#print(r)
sehirler=['İl seçiniz...','istanbul', 'ankara', 'izmir', 'adana', 'adıyaman', 'afyonkarahisar', 'ağrı', 'aksaray', 'amasya',
'antalya', 'ardahan', 'artvin', 'aydın', 'balıkesir', 'bartın', 'batman', 'bayburt', 'bilecik', 'bingöl', 'bitlis', 'bolu', 'burdur', 'bursa', 'çanakkale', 'çankırı', 'çorum', 'denizli', 'diyarbakır', 'düzce', 'edirne', 'elazığ', 'erzincan', 'erzurum', 'eskişehir', 'gaziantep', 'giresun', 'gümüşhane', 'hakkari', 'hatay', 'ığdır', 'ısparta', 'kahramanmaraş', 'karabük', 'karaman', 'kars', 'kastamonu', 'kayseri', 'kırıkkale', 'kırklareli', 'kırşehir', 'kilis', 'kocaeli', 'konya', 'kütahya', 'malatya', 'manisa', 'mardin', 'mersin', 'muğla', 'muş', 'nevşehir', 'niğde', 'ordu', 'osmaniye', 'rize', 'sakarya', 'samsun', 'siirt', 'sinop', 'sivas', 'şırnak', 'tekirdağ', 'tokat', 'trabzon', 'tunceli', 'şanlıurfa', 'uşak', 'van', 'yalova', 'yozgat', 'zonguldak']
ilceler=['İlçe seçiniz...']
il=""
ilce=""

def ilceSec(event):
    global ilce
    ilce = event.widget.get()

def ilceBul(event):
    ilceler=['İlçe seçiniz...']
    global il
    il = event.widget.get()
    r=requests.get(ROOT_URL+"districtList?il="+il,headers=baslik).json()
    if r['success']:
        for i in r['result']:
            ilceler.append(i['text'])
    else:
        print("İlçe bulunamadı")
    cmbIlce.configure(values=ilceler)
    cmbIlce.current(0)

def ara_click(event):
    if il!="" and ilce!="":
        r=requests.get(ROOT_URL+"dutyPharmacy?ilce="+ilce+"&il="+il,headers=baslik).json()
        if r['success']:
            eczane=r['result'][0]['address'].upper()+" "+r['result'][0]['name'].upper()+" ECZANESİ"
            messagebox.showinfo("Nöbetçi Eczane Bilgi", eczane)
            print(eczane,r['result'][0]["loc"])
            x=float(r['result'][0]["loc"].split(',')[0])
            y=float(r['result'][0]["loc"].split(',')[1])
            mappy = folium.Map(location=[x,y], zoom_start = 13)
            folium.Marker(location=[x,y],
            popup=r['result'][0]['name'].upper(),
            icon=folium.Icon(color="red"),).add_to(mappy)
            mappy.save('nobetcieczane.html')
            os.system('nobetcieczane.html')
        else:
            print("Nöbetçi eczane bulunamadı")
            messagebox.showerror("Uyarı", "Nöbetçi eczane bulunamadı")

window = tk.Tk(className='Nöbetçi Eczane Bulma Aracı')
window.geometry("500x200")
programBaslik = tk.Label(text="NÖBETÇİ ECZANE")
programBaslik.pack()
lblIl = tk.Label(text="İl:")
lblIl.pack()
cmbIl = ttk.Combobox()
cmbIl['values']=sehirler
cmbIl.current(0)
cmbIl.bind("<<ComboboxSelected>>", ilceBul)
cmbIl.pack()
lblIlce = tk.Label(text="İlçe:")
lblIlce.pack()
cmbIlce = ttk.Combobox()
cmbIlce['values']=ilceler
cmbIlce.current(0)
cmbIlce.bind("<<ComboboxSelected>>", ilceSec)
cmbIlce.pack()
btnAra = tk.Button(text="Ara")
btnAra.bind("<Button-1>", ara_click)
btnAra.pack()
window.mainloop()