# # return function
# def sum_list(lst):
#     s=o
#     for number in lst:
#         s+=number

#     return s
# print(sum_list([15,-5,0,8,7]))
                                             
# flexible(moslashuvchan) function            
# *args, **kwargs     
# *args usuli                       
# def summa(*sonlar):                         
#     #                                         
#     # print(sonlar) -------> (8, 9, 12, -5, 89, 100)
#     # print(type(sonlar)) --------> <class 'tuple'>
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son

#     return yigindi

# print(summa(8,9,12,-5,89,100))
# print(summa(7,-2,-5))

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")



# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello", "Emil", "Tobias", "Linus")

# def summa(x,y=7,*sonlar):
#    return x+y + sum(sonlar)

# print(summa(1,7,1,-5,-2))
# print(summa(2,12))

# # **kwargs usuli
# def avto_info(kompaniya,model,**malumotlar):
#     # print(malumotlar) ---> {'rang': 'qora', 'yil': 2025}  --->  {'key':value}
#     # print(type(malumotlar)) ---> <class 'dict'>
#      malumotlar['kompaniya']=kompaniya
#      malumotlar['model']=model
#      return malumotlar
# print(avto_info("GM Uzbekistan","Onix",rang='qora',yil=2025))
# print()
# print(avto_info("GM", "malibu", rang='qora', yil=2018))
# print(avto_info("Kia", "K5", rang='qizil', narh=35000))


# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# AMALIYOT
# 1.Sonlar ko'paytmasi
def kopaytma(*sonlar):
    k=1
    for son in sonlar:
        k*=son
    return k
print(kopaytma(1,2,3,4,5,6,7,8,9))

# 2.Talaba haqida ma'lumot
def talaba_info(ism,familiya,**malumotlar):
       malumotlar['ism']=ism
       malumotlar['familiya']=familiya
       return malumotlar
print(talaba_info("Anvar", "Quronboyev", millati='O\'zbek', yoshi=22))

      

