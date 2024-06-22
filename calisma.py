#SORU 1  #Dikdörtgenin çevresi ve alanı
""" kisa = input("Kısa girin: ")
uzun = input("Uzun girin: ")

alan = int(kisa) * int(uzun)
cevre = (int(kisa)*2)+(int(uzun)*2) 

print("Dikdörtgen alanı :",alan)
print("Dikdörtgen çevresi : ",cevre) """

#SORU 2  #Girilen metnin harflerini alt alta yazma
"""metin = input("Metin girin: ")
sayac = 0
while sayac < len(metin):
    print(metin[sayac])
    sayac += 1""" 

#SORU 3 #Girilen aralıktaki sayıların toplamı
""" toplam = 0
bas = int(input("Küçük: "))
son = int(input("Büyük : "))

for i in range(bas+1,son):
    toplam = toplam + i
print(bas,"ile",son,"arasındaki sayıların toplamı: ",toplam) """


#SORU 4 #Girilen aralıktaki sayılardan 7'nin katı olanların toplamı
"""while True:
    kucuk = int(input("Küçük sayı: "))
    buyuk = int(input("Büyük sayı: "))
    if buyuk <= kucuk:
        print("Yanlış girdiniz. Tekrar girin.")
    else:
        break    

toplam = 0 
for i in range(kucuk,buyuk):
    if i%7==0:
        toplam = toplam + i
print("Sayıların toplamı : ",toplam) """



#SORU 5  #Girilen kelimeyi tersten yazma
"""x = input("Kelime girin: ")
x = x[::-1]
print(x)"""

#SORU 6  #Girilen ifadedeki sesli harf sayısı
"""kelime = input("Kelimeniz: ")
sesli = "aeıioöuü"
sayac = 0

for i in kelime:
    if i in sesli:
        sayac = sayac + 1

print("Sesli harf sayısı: ",sayac)"""

#SORU 7 #Girilen sayıya kadar Fibonacci serisi
"""a = 1
b = 1
c = 0

print(a)
while c<1000:
    print(b)        #fibonacci
    c = a + b
    a = b
    b = c    """


#SORU 8  #Girilen sayı asal mı? değil mi? 1 değeri girilerse program sonlanır
"""while True:
    n = int(input("Sayı girin: "))
    if n == 1:
        break
    sayac = 0
    for i in range(2,n):
        if (n % i == 0):
            sayac = sayac + 1

    if sayac == 0:
        print("ASAL")
    else:
        print("DEĞİL")"""



#SORU 9  #Girilen sayı adedi kadar sayı isteniyor ve o sayıların toplamı,ortalaması
"""adet = int(input("Adet: "))
dizi = []

for i in range(adet):
    dizi.append(int(input("Sayı girin: ")))
print(dizi)

toplam = 0
for j in dizi:
    toplam = toplam + j
print(toplam)
print(toplam/adet)"""



#SORU 10  #Girilen sayının yazıyla ekrana bastırılması. 1 değeri girilerse program sonlanır.
"""while True:
    
    birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    yuzler = ["","yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyüz","dokuzyüz"]
    binler = ["","bin","ikibin","üçbin","dörtbin","beşbin","altıbin","yedibin","sekizbin","dokuzbin"]
    sayi = int(input("Sayı giriniz: "))
    
    
    if sayi == 1:
        break
    else:
        s = str(sayi)
        print(binler[int(s[0])],yuzler[int(s[1])],onlar[int(s[2])],birler[int(s[3])])"""
        


#SORU 11  #1000 ile 30000 arasındaki Palindrom sayıların sayısı
"""sayac = 0
for i in range(1000,30000):
    s = str(i)
    t = s[::-1]             #palindrom(tersi aynı olan sayılar)
    if s == t: 
        sayac = sayac + 1
print(sayac)"""        


#SORU 12  #Girilen cümledeki harf ve kelime sayısı
"""cumle = input("Cümle giriniz: ")
sayac = 0
for k in cumle:
    if k == " ":
        sayac = sayac + 1
print("Kelime sayısı : ",sayac + 1)
print("Harf sayısı : ",len(cumle)-sayac)"""      




#SORU 13  #Girilen değere kadar olan sayıların toplamı
"""toplam = 0
while True:
    sayi = int(input("Sayı girin : "))
    toplam = toplam + sayi
    if sayi == 0:
        break
print("Sayıların toplamı : ",toplam)  """  




#SORU 14  #Basit hesap makinesi
def Topla(a,b):
    return a+b

def Cikar(a,b):
    return a-b

def Carp(a,b):
    return a*b

def Bol(a,b):
    return round(a/b)

print("Bir seçim giriniz")
print("+")
print("-")
print("*")
print("/")

while True:
    
    secim = input("Seçiminiz: ")
    
    if secim == 5:
        break
    sayi1 = int(input("Birinci sayi : "))
    sayi2 = int(input("İkinci sayi: "))
    
    if secim == "+":  
        print("Sonuç",Topla(sayi1,sayi2))
    elif secim == "-":  
        print("Sonuç",Cikar(sayi1,sayi2))
    elif secim == "*":  
        print("Sonuç",Carp(sayi1,sayi2))
    elif secim == "/":
        print("Sonuç",Bol(sayi1,sayi2))
    else:
        print("Hatalı seçim yaptınız !!!")

"""import random

#SORU 15 #Atılan zarların gelme olasılığı
zarlar = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(10000):
    zar = random.randint(1,6)
    zarlar[zar] += 1

for zar in zarlar:
    print(f"{zar} gelme olasılığı {zarlar[zar]/100000}")"""     

#SORU 16 #Girilen cümleyi dizi elemanları yapma
"""msg = input("Cümle girin: ")
sonuc = msg.split()
print(sonuc)""" 





