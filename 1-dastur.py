name = input("Ismingizni kiriting: ")
day = input("Tavallud kun.oy.yilingizni kiriting: ")
#day = 0
#day = day.split()
#for d in int(sorted(day)):
    #print(d)
#year = 2025 - int(day.split(",")[-1])
year = int(day.split(".")[-1])
age = 2025 - int(day.split(".")[-1])
if age >= 18:
    print(f"Salom, {name}.\nSiz voyaga yetgansiz")
elif age ==18:
    print(f"Salom, {name}.\nSiz voyaga yetgansiz")
else:
    print(f"Salom, {name}.\nSiz voyga yetmagansiz")

javob = input("Muchalingizni bilishni hohlaysizmi? (Ha/Yo'q): ") 

      #if javob == "Yo'q":
      # print("Xayr,Salomat bo'ling!") 

#if javob.lower() == "yo'q":
    #print("Xayr,Salomat bo'ling!")
if javob.lower() == "ha":
   muchal = year % 12 
    
   if muchal == 0:
       print("Sizning muchalingiz -> (Maymun)")
   elif muchal == 1:      
       print("Sizning muchalingiz -> (Tovuq)")
   elif muchal == 2:
       print("Sizning muchalingiz -> (It)")
   elif muchal == 3:
       print("Sizning muchalingiz -> (Cho'chqa)")
   elif muchal == 4:
       print("Sizning muchalingiz -> (Sichqon)")
   elif muchal == 5:
       print("Sizning muchalingiz -> (Sigir)")
   elif muchal == 6:   
       print("Sizning muchalingiz -> (Yo'lbars)")
   elif muchal == 7:
       print("Sizning muchalingiz -> (Quyon)")
   elif muchal == 8:
       print("Sizning muchalingiz -> (Ajdar)")
   elif muchal == 9:
       print("Sizning muchalingiz -> (Ilon)")
   elif muchal == 10:
       print("Sizning muchalingiz -> (Ot)")
   elif muchal == 11:
       print("Sizning muchalingiz -> (Qo'y)")


elif javob.lower() == "yo'q":
    print("Xayr,Salomat bo'ling!")

else:
    print("Faqat 'Ha' yoki Yo\'q deb yozing!")
    
    
