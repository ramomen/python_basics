#Degiskenler

alininMaasi = 3000
ahmetinMaasi = 5000
vergi=0.20
print(alininMaasi - (alininMaasi * vergi))
print(ahmetinMaasi - (ahmetinMaasi * vergi))

#Degiskenler Kurallari

#Degidkenler rakam ile baslayamaz.

#Buyuk kucuk harf duyarliligi vardir.

age = 20
AGE = 20 

# Bu ikisi farkli degerlerdir.
# Turkce karakter kullanilabilir.


x = 1 #int
y = 2.3 #float
name = "Cinar" #string
isStudent= True # boolean


print(type(x))
print(type(y))
print(type(name))
print(type(isStudent))

x, y, name, isStudent = 60, 4.2, 'Ali', False  # Bu sekilde toplu degerler verilebilir.

print(type(x))
print(type(y))
print(type(name))
print(type(isStudent))

# type() methodu verinin turunu gosterir.

a = 10
b = 20

print(a + b) #Cevap 30 cikar


a = "10"
b = "20"

print(a + b) # degerler string oldugu icin matematiksel islem gormez sonuc 1020 olarak cikar.


a = "ramo"
b = "men"

print(a+b) # :)
