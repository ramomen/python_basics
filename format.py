name = 'ramo'
lastname = 'men'
age = 23

# My name is ramomen and I'm 23

print("My name is " + name + lastname + " and I'm " + str(age) )


#bu kisimda suslu parantezlere deger atamayi format() methoduyla gerceklestiriyoruz. sirasiyla name lastname ve age degiskenleri 
# suslu parantezlerin sirasina gore yerlestirildi.

print("My name is {}{} and I'm {}".format(name,lastname,age))


#suslu parantezlerin arasina eklenen sayilara gore indexleme yapar

print("My name is {1} {0} and I'm {2}".format(name,lastname,age)) # men ve ramo nun yerini degistirdik mesela suan

# ! indexleme 0 dan baslar!



print("My name is {n} {l} and I'm {a}  {n} {l}" .format(n=name,l=lastname,a=age)) 
#burada suslu parantazlerin icerisine verdigimiz karakterleri n=name,l=lastname,a=age olarak degiskenlere esitledik.


## print(f"My name is {name} {lastname} and I'm {age} ")

#burada f string teknigini kullanarak ayni islemi yapabiliriz.

