# while(toki) loop
# 1 dan 10 gacha sonlarni sanash
# for son in range(1,10):
#     print(son)

# son=1
# while son<10:
#     print(son)
#     son+=1


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat=input(savol)
#     if qiymat !='exit':
#         print(float(qiymat)**2)
#     else:
#         print("Dastur ishlashdan to'xtadi.✅")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


# break(sindirish) operatori
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son==5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

# continue(davom etish) operatori
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# Abadiy sikl tuzog'i
## infinite loop
# son = 1
# while son<100:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# Amaliyot
# print("Yoqtirgan kitoblarni ko'rsatuvchi dastur.")
# savol = "Yoqtirgan kitobingiz nomini kiriting "
# savol += "(dasturni to'xtatish uchun 'stop' deb yozing): "
# qiymat = ''
# while qiymat != 'stop':
#     qiymat=input(savol)
#     if qiymat !='stop':
#         print(qiymat)
#     else:
#         print("Dastur ishlashdan to'xtadi.✅")