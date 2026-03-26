# Function-ma'lum vazifani bajaruvchi kod blokidir. 
# Funksiya yaratish uchun "def" kalit so'zidan foydalaniladi, undan keyin funksiya nomi va qavslar ichida parametrlar (agar kerak bo'lsa) yoziladi.
# Pythondagi tayyor funksiyalar-print(), input(), len() va boshqalar mavjud. Shuningdek, foydalanuvchi o'zining maxsus funksiyalarini ham yaratishi mumkin.
print("Hello, World!")  # Bu oddiy bir funksiya bo'lib, ekranga "Hello, World!" matnini chiqaradi.
# Funksiyani e'lon qilish(declaration) va chaqirish(call) qilish mumkin. E'lon qilish - bu funksiya qanday ishlashini belgilash, chaqirish esa funksiya nomini yozib, uning bajarilishini boshlashdir.
# def salom_ber():
#     print("Salom, dunyo!")
    
#       # Bu funksiya ekranga "Salom, dunyo!" matnini chiqaradi.
# # Funksiyani chaqirish(call)
# salom_ber()  # Bu yerda biz "salom_ber" funksiyasini chaqiramiz, va u ekranga "Salom, dunyo!" matnini chiqaradi.
# salom_ber()  # Funksiyani bir necha marta chaqirish mumkin, har safar u o'z vazifasini bajaradi.

# Funksiyada parametrlar,argumentlar
def salom_ber(ism):
    print(f"Assalomu alaykum, {ism}!")

salom_ber("Ali")  
salom_ber("Vali")
salom_ber("Olim")

def yigindi(a, b):
    print(a+b)

yigindi(5, 10)  # Bu yerda 5 va 10 argumentlar bo'lib, a va b parametrlariga mos keladi. Funksiya ularni qo'shadi va natijani ekranga chiqaradi.
yigindi(20, 30)  # Bu yerda 20 va 30 argumentlar bo'lib, a va b parametrlariga mos keladi. Funksiya ularni qo'shadi va natijani ekranga chiqaradi.

def calculate_age(birth_year=1000,name="Olim"):
    age = 2026 - birth_year
    print(f"{name}ning yoshi: {age}")

calculate_age(89,"Ali")  # Bu yerda 1990 va "Ali" argumentlar bo'lib, birth_year va name parametrlariga mos keladi. Funksiya yoshni hisoblaydi va natijani ekranga chiqaradi.
calculate_age(15,"Vali")  # Bu yerda 1985 va "              
calculate_age()  # Bu yerda hech qanday argument berilmagan, shuning uchun default qiymatlar ishlatiladi: birth_year=1995 va name="olim". Funksiya yoshni hisoblaydi va natijani ekranga chiqaradi.

def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1990,2020)  # Bu yerda 1990 argumenti tugilgan_yil parametriga mos keladi, joriy_yil uchun esa default qiymat 2020 ishlatiladi. Funksiya yoshni hisoblaydi va natijani ekranga chiqaradi.    
    # 5gacha

def solishtirish(a, b):
    if a > b:
        print(f"{a} katta {b} dan")
    elif a < b:
        print(f"{a} kichik {b} dan")
    else:
        print(f"{a} va {b} teng")   
solishtirish(10, 5)  # Bu yerda 10 va 5 argumentlar bo'lib, a va b parametrlariga mos keladi. Funksiya ularni solishtiradi va natijani ekranga chiqaradi.
solishtirish(3, 7)  # Bu yerda 3 va 7 argumentlar bo'lib, a va b parametrlariga mos keladi. Funksiya ularni solishtiradi va natijani ekranga chiqaradi.
solishtirish(4, 4)  # Bu yerda 4 va 4