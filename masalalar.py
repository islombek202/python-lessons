# # 1-misol
# x=3
# V=x**3
# print(V)
# # 2-misol
# s=6
# h=1
# a=(2 * s) / h
# print(a)
# # 3-misol
# A=6
# B=6
# C=9
# P=(A + B + C) / 2
# print(P)
# 4-misol
# g=9.8
# H=2
# t=((2 * H) / g) ** (1 / 2)
# print(t)

# 5-misol
# m=6
# g=9.8
# P=m * g
# print(P)

# 6-misol

# m=8
# a=2
# F= m * a
# print(F)

# 7-misol

# R1=1
# R2=7
# R3=3
# R=( R1 * R2 * R3) / ((R1 * R2) + (R2 * R3) + (R3 * R1))
# print(R)

# 8-misol

# t=63072000
# v=0.001
# y=v * t
# print(y)

# 9-misol

# r1=3
# r2=7
# r3=1
# pi=3.14
# S1=pi * ((r1) ** 2)
# S2=pi * ((r2) ** 2)
# S3=pi * ((r3) ** 2)
# print(S1 , S2 , S3)

# 10-misol

# r=2
# pi=3.14
# s=4 * pi * (r ** 2)
# print(s)

# a=4
# b=8
# c=2
# A=(a  + b + c) / 3
# print(A)
# G=(a * b * c) ** (1/3)
# print(G)

# pi=3.1415
# radius=10
# yuza=pi * radius ** 2
# diametr=2 * radius
# print(diametr)
# print(yuza)

# print(50 / 10)

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) 
# print(a*b)
# print(a**b)
# print(2*(a+b))

# aholi_soni = 7594000000 # o'zmizga qulay bo'lishi uchun shinday yozdik
# print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

# PI=3.1415
# G=9.81
# print(PI, G)

# x, y, z = 10, -3, 35 
# print(x + y -z)
# type()-data type checking
# text = "lorem ipsum"
# age= 28
# is_student = True
# print(type(text)) #str
# print(type(-78)) #int
# print(type(30.4567)) #float
# print(type(is_student)) #bool

# kv_tomon=input('Kvadrat tomonini kiriting:') # 5=> "50"; True=> "True"
# print(type(kv_tomon))
 # int()
# x= int(kv_tomon)
# print(type(x))
# print(x ** 2)

# kv_tomon = int(input("Kvadrat tomoni kiriting: "))
# print(kv_tomon ** 2)
# Jobir 36 yoshda
# typecasting - bir turdagi ma'lumotni boshqa turga o'zgartirish
# ism = "Jobir"
# yosh = 36
# xabar = ism + " " + str(yosh) +  "yoshda"
# print(xabar)

# print(int(5.76)) # natija-5

# print(float('8.87'))
# print(float(6))

# t_yil=int(input("Tug'ilgan yilingizni kiriting: "))
# t_yosh= 2025 - t_yil
# print(t_yosh)

# amaliyot
# x=int(input("Istalgan son kiriting: \n=>"))
# xabar1=str(x)+" "+ "ning kvadrati"+" " +str(x ** 2)+" "+"ga teng"
# xabar2=str(x)+" "+ "ning kubi"+" " +str(x ** 3)+" "+"ga teng"
# print(xabar1)
# print(xabar2)

# yosh=int(input("Yoshingiz nechada? \n=>"))
# yil=2025 -yosh
# print(yil,"yilda tug\'ilgansiz")

a=int(input("Birinchi sonni kiriting:"))

b=int(input("Ikkinchi sonni kiriting:"))
# print(f"{a} + {b}=",a+b)
# print(f"{a} - {b}=",a-b)
# print(f"{a} * {b}=",a * b)
# print(f"{a} / {b}=",a / b)
print(str(a)+"+"+str(b)+"="+str(a+b))
print(str(a)+"-"+str(b)+"="+str(a-b))
print(str(a)+"*"+str(b)+"="+str(a * b))
print(str(a)+"/"+str(b)+"="+str(a / b))
print(str(a)+" va "+str(b)+" ning o'rta arifmetigi"+str((a + b) / 2))
print(str(a)+" va "+str(b)+" ning o'rta geometrigi"+str((a * b) ** 1/2))