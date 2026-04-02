# def add_numbers(a, b):
#     print(a + b)
# add_numbers(5, 10)  #15
# add_numbers(20, 30)  #50

# Qiymat qaytaruvchi funksiya
# return-funksiya ichida natija qaytarish uchun ishlatiladi.
# def add_numbers(a, b):
#     return a + b 

# print(add_numbers(5, 10))  
# result = add_numbers(20, 30)  
# print(result)

# def isEven (num):
#     if num % 2 == 0:
#         return "Juft son"
#     else:
#         return "Toq son"
# print(isEven(4))  # Juft son
# print(isEven(7))  # Toq son

# Ternary operator yordamida qisqaroq yozish 
def isEven(num):
   return "Juft son" if num % 2 == 0 else "Toq son"

print(isEven(4))  # Juft son
print(isEven(7))  # Toq son