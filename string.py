# # emoji="👌"
# # print(emoji)

# # string metodlari(methods)

# firstname = "ahad"
# lastname = "qayum"
# fullname = f"{firstname} {lastname}"
# # upper()/lower()
# print(fullname.upper())  
# # natija-AHAD QAYUM 
# print(fullname.lower())
# # natija-ahad qayum
# print("ADMINJON".lower())

# # title() / capitalize()
# print("Welcome to uzbekistan ".title())
# # natija-Welcome To Uzbekistan
# print("Where are you from?".title())
# print("manual tester".capitalize())
# fullname = fullname.capitalize()
# print(fullname)

# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# input()
# nickname1 = 'karimo_f009'
# nickname2 = input("Iltimos Instagramm nicname kiriting!")
# print("1-account:", nickname1)
# print("Foydalanuvchi accounti:", nickname2)

# amailiyot
kocha = input("Iltimos,kochangiz nomini kiriting!")
mahalla = input("Iltimos,mahallangiz nomini kiriting!")
tuman = input("Iltimos,tumaningiz nomini kiriting!")
viloyat = input("Iltimos,viloyatingiz nomini kiriting!")
print(f"{kocha} kochasi, \n {mahalla} mahallasi, \n {tuman} tumani, \n {viloyat} viloyati, \n".upper())
print(f"{kocha} kochasi, \n {mahalla} mahallasi, \n {tuman} tumani, \n {viloyat} viloyati, \n".lower())
print(f"{kocha} kochasi, \n {mahalla} mahallasi, \n {tuman} tumani, \n {viloyat} viloyati, \n".title())
print(f"{kocha} kochasi, \n {mahalla} mahallasi, \n {tuman} tumani, \n {viloyat} viloyati, \n".capitalize())