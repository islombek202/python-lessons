# Listdan element sug'irib olish
# list.pop(index?)
# gadgets=['telefon','planshet','laptop','pc']
# deletedElement = gadgets.pop(3)
# print(deletedElement)
# print(gadgets)

# lastElement = gadgets.pop(-1)
# print(lastElement)
# print(gadgets)
# gadgets=['telefon','planshet','laptop','pc']
# gadgets.append("airpods")
# print(gadgets)
# gadgets=[]
# gadgets.append('pc')
# gadgets.append('laptop')
# gadgets.append('airpods')
# gadgets.insert(1,'telefon')
# gadgets.insert(3,'playstation')
# print(gadgets)
# gadgets=['telefon','planshet','laptop','pc']
# del gadgets[0]
# print(gadgets)
# gadgets=['telefon','planshet','laptop','pc']
# gadgets.remove('planshet')
# print(gadgets)

# amaliyot
# dostlar=['Laziz','Javohir','Arslon']
# print(dostlar[0]+",Nichiksan?")
# print(dostlar[1]+",Nagap")
# print(dostlar[2]+",beda press garakmi?")

# sonlar=[44,66,86,-345,0]
# print(sonlar[0] * sonlar[-1])
# print(sonlar[2] + sonlar[3])
# print(sonlar[-1] / sonlar[2])

# t_shaxslar=['Amir-Temur','Bobur','Navoiy']
# z_shaxslar=['Pavel Durov','Mark Zuckerberg','Nedik']
# print("Men "+t_shaxslar.pop(0)+" bilan ko\'rishgan bo\'lardim.")
# print(z_shaxslar.pop(0)+"dan dasturlashni o\'rganardim.")

# friends=[]
# friends.append('Laziz')
# friends.append('Javohir')
# friends.append('Arslon')
# friends.append('Shoxruz')
# friends.append('Abror')
# print({friends}, f" mehmonga kelishmoqchi edi.")
# friends.remove('Abror')
# friends.remove('Javohir')
# print({friends},  f" aniq kelishadi")

# list sort
# dostlar=['Laziz','Javohir','Arslon','Abror','Shoxruz']
# print(dostlar)
# dostlar.sort(reverse=True)
# print(dostlar)
# # sorted() function 
# print(dostlar)
# sorted_list=sorted(dostlar,reverse=True)
# print(sorted_list)

# nums = [12,45,-56,40]
# nums.sort() #o'sish tartibida
# print(nums)
# print(sorted(nums,reverse=True))

# nums.reverse()
# print(nums)

#range()
# users=['john','alisa','aziz','alex']
# cars=list(('bmw','audi','porsche','ford'))
# print(cars)  
# print(list(range(1,10)))
# even_nums=list(range(2,20,2))
# print(even_nums)
# odd_nums=list(range(1,20,2))
# print(odd_nums)

# sonli ro'yxat ustida sodda amallar
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# eng_arzoni=min(narhlar)
# eng_qimmati=max(narhlar)
# yigindi=sum(narhlar)
# print(eng_arzoni,eng_qimmati,yigindi)

# ro'yhatni kesib olish
# students=['Akmal','Jasur','Asal','Kumush','Maftuna','Elbek']
# new list=list[start_index:end_index]
# students1=students[2:5]
# students2=students[0:2]
# 2-case
# students3=students[1:] # start_index dan boshlab oxirigacha kesib oladi 
# 3-case
# students4=students[ :4] # boshidan boshlab 4-index(end_index) gacha
# print(students1,students2,students3,students4)

#  manfiy index (-1,-2,-3...)
# 0 dan boshlab index lanadi
# print(students[-1])
# print(students[-2])
# print(students[-5])
# print(students[-4:-2])

# ro'yxatdan nusxa(copy) olish
# 1.Shallow(sayoz) copy
# sonlar=[1,5,-5,12]
# sonlar2=sonlar
# sonlar2.append(77)
# sonlar.insert(2,-8)
# print(sonlar2)
# print(sonlar)
# 2.Deep(chuqur) copy
# sonlar3=sonlar[:]
# sonlar3.append(3)
# print(sonlar3)
# print(sonlar)
# deep copy using copy library
import copy
# orginal_list=[1,2,[3,4],5]
# deep_copy=copy.deepcopy(orginal_list)

# deep_copy[2].append(99)
# print(deep_copy)
# print(orginal_list)

# Tuple-o'zgarmas ro'yxat 
# toys=('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
# toys[1]='dragon'  Error!
# print(toys)  Error!


# toys=list(toys)
# toys[1]='dragon'
# toys.remove('dino')
# toys.append('mcqueen')
# toys=tuple(toys)
# print(toys)

# Amaliyot
# 1-topshiriq
davlatlar=['O\'zbekiston','Rossiya','Korea','Germaniya']
print(davlatlar)

# 2-topshiriq
print("Davlatlar soni:",len(davlatlar))

# 3-topshiriq
print(sorted(davlatlar))

# 4-topshiriq
print(sorted(davlatlar,reverse=True))

# 5-topshiriq
print(davlatlar)

# 6-topshiriq
davlatlar.reverse()
print(davlatlar)

# 7-topshiriq
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 8-topshiriq
nums = list(range(120,1200,2))
print(sum(nums))

# 9-topshiriq
eng_katta=max(nums)
eng_kichik=min(nums)
print(eng_katta - eng_kichik)

# 10-topshiriq
print("Elementlarsoni: ",len(nums))

# 11-topshiriq
print("oldingi 20 ta son-",nums[:20])
print("oxirgi 20 ta son-",nums[-20:])
print("o'rtadagi 20 ta son-",nums[len(nums)//2-10:len(nums)//2+10])

# 12-topshiriq
taomlar=['Osh','Somsa','Kabob','Chuchvara','Shirin kulcha']

# 13-topshiriq 
nonushta=taomlar[:]

# 14-topshiriq
nonushta.remove('Osh')
nonushta.remove('Somsa')
nonushta.remove('Kabob')
nonushta.remove('Chuchvara')
nonushta.append('Holva')
nonushta.append('Murabbo')

# 15-topshiriq
print("Milliy taomlar: ",taomlar)
print("Nonushtaga yeyiladigan taomlar: ",nonushta)

# 16-topshiriq
nonushta = tuple(nonushta)
nonushta=list(nonushta)
nonushta[0] = "qaymoq va non"
nonushta=tuple(nonushta)
print(nonushta)

print("Dastur tugadi")