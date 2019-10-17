 #key - value turunde veri saklama

 
# 06 => Ankara 
# 34 => istanbul 

sehirler = 'Ankara' , 'istanbul'
plakalar = "06" , "34"

print(sehirler[0] + "="  + plakalar[0])

#kullanissiz bir yontemdir

plakalar = {
    'Ankara' : "06",
    'istanbul' : "34"

}

print(plakalar['Ankara'])
print(plakalar['istanbul'])

users ={
    'ramomen':{
        'e-mail': 'ramazandegirmenci@hacettepe.edu.tr',
        'address' : 'cehennemin dibi',
        'isStudent' : True,
        'age' : 23
    },
     'laptoprecai' :{
        'e-mail': 'recai@laptop.com',
        'address' : 'unknown',
        'isStudent' : False,
        'age' : 48
    }
}

print(users['laptoprecai'])
print(users['laptoprecai']['e-mail'])
print(users['ramomen'])
print(users['ramomen']['address'])