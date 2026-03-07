# 1
import math
# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: "))
# a = x + y
# b = math.pow(y, 2)
# c = b + 2
# d = x + math.pow(x, 3) / 5
# e = math.exp(y + 2)
# c1 = a / (b + math.fabs(c / d)) + e
# print("%.2f" % c1)

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# T = math.pow(a, 1/5) + math.pow((b * (a + b) / (2 * b + a * b)), 1/4) * ((a ** 2) + (b ** 2) + 2)
# print("%.2f" % T)
# 24

# a =int(input("1-sonni kiriting(a): "))
# b=int(input("2-sonni kiriting(b): "))
# c=int(input("3-sonni kiriting(c): "))
# x=float(input("4-sonni kiriting(x): "))
# A=8.2 * math.pow(x, 2)
# B=math.pow((math.fabs(math.pow(x, 3) + 3 * x)+math.cos(x - 2)), 1/2)
# C= a / 4 + b / 3 + c / 2 + 1
# W1=0.75 + (A + B) / C
# print("%.2f" % W1)


#23
# a =int(input("1-sonni kiriting(a): "))
# b =int(input("2-sonni kiriting(b): "))
# c =int(input("3-sonni kiriting(c): "))
# d =int(input("4-sonni kiriting(d): "))
# x =float(input("5-sonni kiriting(x): "))
# A = (a * math.pow(x, 2)) + (b * x) +c
# B = x * math.pow(a, 3) + math.pow(a, 2) + math.pow(a, (b-c))
# C = math.cos(math.fabs((a * x + b)/(c * x + d + math.pow(2, c))))
# y2 = (A/B) + C
# print("%.2f" % y2)

# a=a =int(input("1-sonni kiriting(a): "))
# x =float(input("2-sonni kiriting(x): "))
# b = math.sqrt(x - 1)
# c = math.sqrt(x + 2)
# d = math.log10(math.sqrt(a * math.pow(x, 2)) + 2)
# e = math.sqrt(c + math.sqrt(x + 24) + math.pow(x,5))
# TT=(b + c + d) / e
# print("%.2f" % TT)
# 26

# a =int(input("1-sonni kiriting(a): "))
# x =float(input("2-sonni kiriting(x): "))
# y =float(input("3-sonni kiriting(y): "))
# A = math.pow((math.exp(x * y)-(x * math.sin(a * x))-((x ** 2 + 2)/(math.fabs(x) + 5))),1/2)
# B = math.pow((math.log((x ** 2) + 2) +5),1/2)
# W2 = A + B
# print("%.2f" % W2)

# 27

# x =float(input("1-sonni kiriting(x): "))
# A = 2 * math.tan(x + 2) - math.cos(x+math.pow(2,x))
# B = 1 + math.pow(math.cos(x + 2),2)
# C = math.sin(x ** 2)
# D = (x **2) + 3
# AA =math.pow((A/B),1/2) +((C)/(D))
# print("%.2f" % AA)

# 28
# a =int(input("1-sonni kiriting(a): "))
# x =float(input("2-sonni kiriting(x): "))
# A = x * math.sin(x/2 + x/3 + x/4)
# B = math.log10(x ** 2 -2) + math.pow(3,a)
# C = (math.cos(x + 3) * math.sin(x +3)) + 8
# BB1 = A + (B / C)
# print("%.2f" % BB1)

# 29

# a =int(input("1-sonni kiriting(a): "))
# x =float(input("2-sonni kiriting(x): "))
# y =float(input("3-sonni kiriting(y): "))
# A = math.pow(y,2) + math.exp(x)
# B = math.pow((math.exp(x)+(a/(x**2 + 2))),1/2)
# C = math.pow(math.cos(x),2)/math.sin(x ** 2)
# TT=math.pow((A + B + C),1/2) + math.pow(math.cos(x),3)
# print("%.2f" % TT)

# 30

# x =int(input("1-sonni kiriting(x): "))
# y =float(input("2-sonni kiriting(y): "))
# z =float(input("3-sonni kiriting(z): "))
# A = 2**(-x) * math.pow((x + math.pow((math.fabs(y)+2),1/4)),1/2)
# B = math.pow((math.exp(x - 1)/(math.sin(z +2))+2),1/3)
# af= A * B
# print("%.2f" % af )

# 20
x =float(input("1-sonni kiriting(x): "))
y =float(input("2-sonni kiriting(y): "))
A = math.pow(y,2)+(y + x * y)/(math.fabs(x * y)+5)
B= x * y + math.pow(y,2)
C=math.pow(x,2)+1
a = C/(math.pow(x,2)+ (B/A))
b = 1/(1+math.cos(x)+(1/math.sin(math.fabs(x))))
T11=a + b
print("%.2f" % T11)