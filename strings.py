name = 'ramo'
lastname = 'men'
age = 23

# My name is ramomen and I'm 23

greetings = "My name is " + name + lastname + " and I'm " + str(age) 

result = len(greetings) # len() methodu karakter sayisini gosterir.


result = greetings[0] #indexlemeye basliyor.

result = greetings[6] 

result = greetings[-1] # en son karakterin index'i

result = greetings[-2] # sondan bir onceki karakterin indexi

result = greetings[3:7] # 3 den basla 7e kadar indexle


result = greetings[:7] # en bastan basla 7e kadar

result = greetings[3:] # 3 den basla sona kadar git

result = greetings[0:10:2] # 0 dan 10'a kadar git 2'ser al 

result = greetings[::-1] # sondan basa dogru alir
print(result) 