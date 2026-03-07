# Takrorlanish operatorlari
# loop- sikl
# 1.for loop
# # 2.while loop
# students=['Elbek','Maftuna','G\'ulomjon','Mahliyo','Dilbek']
# hard ccoding
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])
# for student in students:
#     print(student)

# for guest in students:
#     print(f"Hurmatli{guest}, sizni interviewga taklif qilmoqchiman!")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi!")

    # Sonlar ro'yxati uchun for loop
#     even_numbers =list(range(2,51,2))
#     for number in even_numbers:
#         print(number)
# print("Dastur tugadi")

# 1 ning kvadrati 1ga teng
# 2 ning kvadrati 4ga teng
# 3 ning kvadrati 9ga teng
# 4 ning kvadrati 16ga teng
# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng.")

# 1 dan 100 gacha chiqarish
# 1-usul:
# sonlar2= list(range(1,100))
# for son in sonlar2:
#     print(son)
# # 2-usul:
# for son in range(1,100):
#     print(son)
# # ro'yxat elementlarini index orqali olish:
# for index in range(len(sonlar2)):
#     print(index)

# 1-marta:index = 0 =>sonlar[0]=1
# 2-marta:index = 1 =>sonlar[1]=2
# ...
# 99-marta: index = 98 => sonlar[98]=99

# 1 ning kvadrati 1 ga teng
# 2 ning kvadrati 4 ga teng
# 3 ning kvadrati 9 ga teng
# for number in range(1,21):
#     print(f"{number} ning kvadrati {number**2} ga teng")

# amaliyot
# number_of_friends=int(input("Do'stlaringiz sonini kiriting: "))
# friends=[]
# if (number_of_friends == 0):
#     print("Sizning do'stingiz yo'qmi?")
# else:
#     for n in range(number_of_friends):

#         friend=input(f"{n+1}-do\'stingizni kiriting: ")
#         friends.append(friend)
#         print(friends)

# Amaliyot
# dostlar=['Laziz','Javohir','Arslon','Shohruz','Abror']
# for taklifnoma in dostlar:
#     print(f"Salom {taklifnoma}, ertaga maktabga borasanmi?  ")

# print(f"CODE {len(dostlar)} marta takrorlandi!")

# sonlar=list(range(11,100,2))
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")

# kinolar=[]
# for kinolarsoni in range(5):
#     kinolar1=input(f"{kinolarsoni+1} Sevimli kinongizni kiriting: ")
#     kinolar.append(kinolar1)

# print(kinolar)

# people=int(input("Bugun kimlar bilan ko'rishding?:"))
# ismlar=[]
# for son in range(people):
#     ism=input(f"{son+1}-ko'rishgan insoningni ismini kirit: ")
#     ismlar.append(ism)

# print(ismlar)

# for son in range(11):
#     print(son)
# s = 0
# numbers=[12,5,18,25,23]
# for number in numbers:
#     # print(number) 
#     s += number
# print(s)    

# 1 dan 50 gacha bo'lgan toq sonlar yig'indisi
# summa=0
# for son in range(1,50,2):
#  summa += son
# print(summa)    

# numbers=[12,5,18,25,23,88,2]
# # o'rtacha qiymat = s/length
# summa=0
# for s in numbers:
#     summa+=s
# print(summa/len(numbers))

# 1 dan 20 gacha bo'lgan juft sonlarni o'rta arifmetiki
# summa=0
# for son in range(2,21, 2):
#     summa+=son
# print(summa/len(range(2,21, 2)))
import math
# n! = 1*2*3*...*(n-1)*n
# k=1
# for son in range(1,20):
#     k*=son
# print(k)    
# numbers=[12,5,18,25,23,88]
# k=1
# for son in numbers:
#     k*=son
# print(math.pow(k,1/len(numbers)))

# 1 dan 10 gacha bo'lgan juft sonlar ko'paytmasini yig'indisiga nisbati
# k=1
# s=0
# for son in range(2,11,2):
#     k*=son
#     s+=son
# print(k/s)

# # 1 dan 20 gacha bo'lgan sonlardan juftlarini ko'paytmasini, toqlarini yig'indisiga nisbatini toping

# k=1
# s=0
# for juftlar in range(2,21,2):
#     k*=juftlar
# for toqlar in range(1,21,2):
#     s+=toqlar
# print(k/s)
# s=0
# counter=0
# numbers=[7,97,-58,90]
# for number in numbers:
#     if number % 2==0:
#         s+=number
#         counter+=1

# print(s/counter)
# s=0
# numbers=[97,97,-92,14,22]
# for number in numbers:
#     if number%2==0 or number%3==0 or number%5==0:
#         s+=number
# print(s)

# s=0
# counter=0
# numbers=[23, 87, 77, 4, 14, 57, 91, 16, 80, 7, 45, 78, 46]
# for number in numbers:
#     if number%2==1:
#         s+=number
#         counter+=1
# print(s/counter)

# 122
# s=0
# counter=0
# yig=0
# numbers=[44, 59, -75, 73]
# for number in numbers:
#     s+=number**2
#     counter+=1
#     yig+=number
# print(s,yig/counter)

# 115,114

# 114
# s=1
# numbers=[44,34, 42, 83, 43, 64]
# for number in numbers:
#     if number%2==0 or number%5==0:
#         s*=number
# print("%.2f" % math.sin(s))

# 115
# numbers=[85,15,57,68,18,67,7,45,69,21,1,5,98,34]
# m = int(input("m sonini kiriting: "))
# s=0
# for number in numbers:
#     if number < m:
#         s+=number**2
# print(s)

# 126
# nums=[7,24,-5,23,99,-3,24,51]
# s=0
# for num in nums:
#     s+=num
# length=len(nums)
# average_value = s/len(nums)
# log_value = math.log(average_value)

# for index in range(length):
#     if nums[index]<0:
#         nums[index]=log_value

# print(nums)

# 127-uyda

# 123
# numbers=[3,17,-59]
# # plan:  1.juft o'rinli elementlar 2.juft o'rinlar elementlar yigindisi
# # 3.toq qiymatli elementlar 4.toq qiymatli elementlar juft o'rinli elementlar yigindisiga bo'lish
# s=0
# for index in range(len(numbers)):
#     if (index+1) %2==0:
#         s+=numbers[index]
       
# for number in numbers:
#     if number %2==1:
#         print(number/s," ")
#     else:
#         print(number," ")
        
# 127

# nums=[46 ,23 ,-52 ,34 ,6 ,-18 ,52]
# for num in nums:
#     if num<0:
#         num=min(nums)**2
#     print(num)

# # 110

# k=int(input("K sonini kiriting: "))
# m=int(input("M sonini kiriting: "))
# sonlar=[44 ,64 ,23 ,84 ,13 ,6 ,22]
# for son in sonlar:
#     if son==k or son==m:
#      print(k*m)

# 104 
# plan:
# 1.min qiymatni topish
# 2.oxirgi qiymat =>list[-1]/list[len(list)-1]
# 3.almashtirish=> index orqali almashtiramiz
# numbers=[74,0,1,33]
# min_value=min(numbers)
# last_element=numbers[-1]
# # print(numbers.index(1))
# min_index=numbers.index(min_value)
# numbers[min_index],numbers[-1]=last_element,min_value
# print(*numbers)

# a=5
# b=2
# result:a=2;b=5

# 1-usul
# a,b=b,a

# 2-usul
# c - temporary variable
# c=a
# a=b
# b=c

# 3-usul
# [a,b]=[b,a]
# print(a,b)
# numbers=[29 ,50 ,-14,4,27,-56]
# k=int(input("k ning qiymatini kiriting"))
# max_value=max(numbers)
# max_index=numbers.index(max_value)

# numbers[max_index]=numbers[k-1]
# print(*numbers)





        









































































































































































































































































