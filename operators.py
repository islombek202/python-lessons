# # Python operators
# # 1.Arifmetik operatorlar(+,-,*,/,%,**,//)
# x=8
# y=2
# # modules(%)-qoldiqli bo'lish
# print(x % y)
# print(x//y)

# # Comparison(solishtirish) operators => boolean values(true,false)
# # == -equal
# print(3 == 4) # false
# print(5.5 == 5.5) #true
# # != -no equal
# print(3 != 4) #true
# print(5.5 != 5.5) #false
# # > -	Greater than
# print(x > y)#true
# # < -	Less than
# print(x < y)#false
# # >= -Greater than or equal to
# print(5 >= 3,5>=5)#true
# # <= -Less than or equal to
# print(5 <= 3,5<=5)#false ,true

# # Logical(mantiqiy) Operators
# # and(va) operator
# score=55
# print(score > 69 and score < 86)#FALSE
# score2=72
# print(score2 > 69 and score2 < 86)#true
# print(8 == 8 and 8 < 7)#false

# # or(yoki) operatori
# print(8 == 8 or 8 < 7)#true
# print(score > 69 or score < 86)#true

# # not(emas) operatori*(true=>false,false=>true)
# print(not(8 == 8 or 8 < 7))#false
# print(not(12 > 18))#true
z=12
print(z > 10 and z < 5 or z > 8) # true and false or true => false or true => true 
print(z > 10 and z < 5 or not( z > 8))  # true and false or true => false or true =>false

# Assignment(tayinlash) Operators
# =
y =5

# +=
z +=3 # z = z + 3
print(z)
y +=5 #y = y + 5
print(y)
z -=2 #z=z-2
print(z)

y *=2 # y=y*2
print(y)
y /=2 # y =y / 2
print(y)#y=10

y %=2 # y=y % 2 (qoldiq) => 0.0
print(y) 