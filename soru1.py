#Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.
"""degisken1=20
string='22'
degisken2=22.3
yeni=int(string)
yeni2=int(degisken2)
print(type(yeni)) """
#İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. 
#Bu karşılaştırmalara mantıksal operatörler de eklenir.
"""yas1=22
yas2=45
yas3=46
if(yas1>yas2 and yas1>yas3):
    print("Yaşı en büyük olan kişi ",yas1," Dir ")
elif(yas2>yas1 and yas2>yas3):
    print("Yaşı en büyük olan kişi ",yas2," Dir ")    
elif(yas3>yas2 and yas3>yas1):
    print("Yaşı en büyük olan kişi ",yas3," Dir ")    
if(yas1>yas2 and yas1>yas3):
    if(yas2>yas3):
        print(" Kişilerin yaş sıralaması ",yas1," >",yas2," >",yas3," şeklindedir")    
    else :
        print(" Kişilerin yaş sıralaması ",yas1," >",yas3," >",yas2," şeklindedir")    
elif(yas2>yas1 and yas2>yas3):
    if(yas1>yas3):
        print(" Kişilerin yaş sıralaması ",yas2," >",yas1," >",yas3," şeklindedir")    
    else:
        print(" Kişilerin yaş sıralaması ",yas2," >",yas3," >",yas1," şeklindedir")     
elif(yas3>yas1 and yas3>yas2):
    if(yas2>yas1):
        print(" Kişilerin yaş sıralaması ",yas3," >",yas2," >",yas1," şeklindedir")    
    else:
        print(" Kişilerin yaş sıralaması ",yas3," >",yas1," >",yas2," şeklindedir") 
"""
#Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.
"""
sayi1=int(input("Birinci sayının değerini giriniz "))
sayi2=int(input("İkinci sayının değerini giriniz "))
#toplama 
print("iki sayının toplamı ",(sayi1+sayi2))
print("iki sayının çarpımı ",(sayi1*sayi2))
if(sayi1>sayi2):
    cikartma=sayi1-sayi2
else:
    cikartma=sayi2-sayi1
print("iki sayı arasındaki fark ",cikartma)
#bölme 
if(sayi2==0):
    if(sayi1==0):
        print(" 0/0 tanımsızlığa sebep olur ")
    else :
        print("sayi2/sayi1 in değeri ",sayi2/sayi1)
elif(sayi1==0):
        if(sayi2==0):
            print("0/0 tanımsızlığa sebep olur")
        else:
            print("Sayı1 'in sayı2' e bölümünden sonuç ",sayi1/sayi2)
else:
    print("Sayı1 'in sayı2 ' e bölümünden sonuç ",sayi1/sayi2," Sayı2 'nin sayı1' e bölümünden sonuç",sayi2/sayi1)          

"""

#Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.
"""isim=input("Lütfen isminizi giriniz ")
yas=int(input("Lütfen yaşınızı giriniz  "))
sehir=input("Hangi şehirde yaşadığınızı giriniz ")
meslek=input("Meslek bilginizi giriniz ")
print("Girmiş olduğunuz bilgileriniz :  Adınız " ,isim," Yaşınız ",yas," Yaşadığınız şehir ",sehir," Mesleğiniz ",meslek)"""

""" 
 "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.


 İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir. 
 İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ") 
 İfadeyi hepsini büyük harf olacak hale çevrilir.("hi-kod veri bilimi atölyesi") 

"0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")

"""
Hi_Code="Hi-Kod Veri Bilimi Atölyesi"
Buyuk_harf=Hi_Code.upper()
print(Buyuk_harf)
Kucuk_harf=Hi_Code.lower()
print(Kucuk_harf)
Kelimeler=Hi_Code.split()
print(Kelimeler)
sayilar = "0123456789"

cift_sayilar = " "
tek_sayilar = " "
for sayi in sayilar:
  if int(sayi) % 2 == 0:
    cift_sayilar += sayi
  else:
    tek_sayilar += sayi

print(f"Çift sayılar:",cift_sayilar)
print(f"Tek sayılar: ",tek_sayilar)

















