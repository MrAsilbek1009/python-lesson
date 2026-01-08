# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# print('"Nexia", "Tico", \'Damas\' ko\'rganlar qilar havas')
# print("5 ning 4-darajasi", 5**4 )
# print("22 ni 4 ga bo'lgandagi qoldiq", 22%4, "ga teng")
# print("Tomonlari 125 ga teng kvadratning yuzi va perimetrini natijasi",) 
# print((12**2)*3.14/4)
# phone = "📱"
# print("men\toldim")

# kocha = "Asl"
# mahalla = "Do'stlik"
# tuman = "Bodomzor"
# viloyat = "Gulistan"
# # print(kocha, "ko\'chasi", mahalla, "mahallasi", tuman, "tumani", viloyat "viloyati")
# print(kocha, "ko\'chasi,", mahalla, "mahallasi,", tuman, "tumani,",  viloyat, "viloyati")

# user = int(input("Istalgan son kiriting:\n>>>"))
# # misol = user, "ning kvadrati", user**2,"ga teng"
# misol = user**2
# misol2 = user**3
# print(user,"ning kvadrati", misol, "ga teng") 
# print(user,"ning kubi", misol2, "ga teng") 

# countries = ['usa', 'canada', 'braziliya', 'italiya', 'argentina', 'portugaliya']
# print(f"1) {len(countries)}")
# print(f"2) {sorted(countries)}")
# print(f"3) {sorted(countries, reverse=True)}")
# print(f"4) countries ning asl ko\'rinishi:\n{countries}")

"""
f-string,sort(),reeverse(),range(),len(),sum,max,min shu metodlar foydlanish
"""
# countries2 = countries
# countries['0','1','2','3','4','5'] = countries['0','1','2','3','4','5'].title()
# print(countries)
# countries.reverse()
# print(f"5) {countries}")
# countries.sort()
# print(f"6) {countries}")
# juft_sonlar = list(range(120,1200,2))
# toq_sonlar = list(range(121,1200,2))
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)
# sonlar = list(range(120,1200))
# print(sonlar)
# print(f"Sonlar yig'indisi: {sum(sonlar)}")
# print(f"Sonlar ayirmasi: {max(sonlar)-min(sonlar)}")
# print(len(sonlar))
# print(sonlar[:20])
# print(sonlar[-20:])
# taomlar = ["Kozon kabob","Dumg\'aza","Bifshteks","Bistrogon","Lag\'mon"]
# nonushta = taomlar[:]
# print(f"Taomlar:{taomlar} \nNonushta:{nonushta}")

"""
For metodidan foydalanish
"""
# ismlar = ["Asilbek", "Islom", "Muhammad", "OLimjon", "Umar"]
# for ism in ismlar:
#     print(f"Salom, {ism}")
# print(len(ismlar))

# toq_sonlar = list(range(11,100,2))
# sonlar_kubi = []
# for son in toq_sonlar:
#     sonlar_kubi.append(son**3)

# print(f"Toq sonlar:\n{toq_sonlar}")
# print(f"Sonlar kubi:\n{sonlar_kubi}")
# sonlar_kubi.append()

""" 
For va range metodlaridan foydalanish
"""
# kinolar = []
# print("5 ta sevimli kinolaringizni qaysi? (*_*)")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-sevimli kinoingizni nomini kiriting:"))
# print(kinolar)

"""
Amaliyot,2 xil usulda
"""
# odamlar = [] 
# inson = (int(input("Bugun nechta odamn bilan suxbatlashdingiz?\n>>>")))
# for odam in range(inson):
#     odamlar.append(input(f"{odam+1}-suxbatlashgan odamingiz:"))
# print("Rahmat,salomat bo\'ling!")

# odamlar = (int(input("Bugun nechta odamn bilan suxbatlashdingiz?\n>>>")))
# for odam in range(odamlar):
#     input(f"{odam+1}-suxbatlashgan odamingiz:")
# print("Rahmat,salomat bo\'ling!")

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if cars != 'gm':
#         print(car.title())
#     else: 
#         print(car.upper())

# ismlar = input("Login ismingizni kiriting\n>>>")
# print(input("Login ismingizni kiriting\n>>>"))
# if ismlar == 'Admin' or ismlar == 'admin':
#         print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#         print(f"Xush kelibsiz, {ismlar}!")
 
# sonlar = []
# print("2 ta son kiriting")
# for n in range(2):
#     # input(f"{n+1}-sonni kiriting:")
#     # if n == n:
#     #     print("Sonlar teng")     
#     sonlar.append(int(input(f"{n+1}-sonni kiriting:")))
# if sonlar[0] == sonlar[1]:
#     print("Sonlar teng")
# else:
#     print(f"Sonlar yig\'indisi:{sonlar[0]+sonlar[1]} ga teng")

# print("2 ta son kiriting!")
# son1 = int(input("Sonni kiriting:"))
# son2 = int(input("Sonni kiriting:"))
# if son1 == son2:
#     print("Sonlar teng")
# else:
#     print(f"Sonlar yig\'indisi:{son1+son2} ga teng.")

# sonlar = []
# print("2 ta son kiriting!")
# for n in range(2):
#     sonlar.append(input(f"{n+1}-sonni kiriting:"))
#     if sonlar[0] == sonlar[1]:
#         print("Sonlar teng")
#     else:
#         print(f"Sonlar yig\'indisi:{sonlar[0]+sonlar[1]} ga teng")


# numbers = int(input("Istalgan sonni kiriting:"))
# if numbers >= 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")
    

# numbers = int(input("Istalgan sonni kiriting:"))
# for n in numbers:
#     if n > 0:
#         print(numbers**(1/2))
#     else:
#         print("Musbat son kiriting:")

# sonlar = []
# son = int(input("Son kiriting:"))
# for n in sonlar:
#     sonlar.append(son)
# if n > 0:
#     print(f"{n} bu son 0 dan kichik")
# else:
#     print(f"{n} bu son o dan katta")

# sonlar = []
# son = int(input("son kiriting:"))
# sonlar.append(son)
# if sonlar:
#     for s in sonlar:
#         if s < 0:
#             print(f"{s} bu son 0 dan kichik")
#         else:
#            print(f"{s} bu son 0 dan katta")
# else:
#     print("son kiriting")    
    
# son = int(input("Juft son kiriting\n>>>"))
# if son % 2 == 0:
#     print("rahmat")
# else:
#     print("bu juft son emas")    
"""
elif ni ishlatish
"""
# yosh = int(input("Yoshingizni kiriting:\n>>>"))
# if yosh<=4 or yosh>=60:
#     print("Kirish bepul")
# elif yosh < 18:
#     print("10.000")
# elif yosh > 18:
#     print("20.000")

# sonlar = []
# print("Ikkita son kiriting!")
# for n in range(2):
#     sonlar.append(input(f"{n+1}-kiriting:"))
#     if n == n:
#         print("sonlar teng")
#     elif n > n:
#         print(f"{n} bu son {n} dan katta")
#     elif n < n:
#         print(f"{n} bu son {n} dan kichik")
#     print(sonlar)

# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['sut','qatiq', 'makaron','olma','behi','orbit',"go\'sht", 'maloko','non','choy']
# savat = []
# print("5 ta nahsulot kiriting")
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulot:"))
# for mahsulot in savat:    
#     if mahsulot in mahsulotlar:
#         print("Mahsulot do'konimizda bor")
#     else:
#         print("Mahsulot do'konimizda yo'q")


# mahsulotlar = ['sut','qatiq', 'makaron','olma','behi','orbit',"go\'sht", 'maloko','non','choy']
# savat = []
# print("5 ta nahsulot kiriting")
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulot:"))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:    
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.apppend(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# print(bor_mahsulotlar and mavjud_emas)


import turtle
t= turtle.Turtle()
t.color("purple")
t.forward(100)
t.right(90)
t.forward(100)



























