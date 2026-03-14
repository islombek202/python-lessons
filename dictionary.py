# Data types (Ma'lumot turlari)
# 1.integer; 2.float; 3.string;4.boolean;5.list;6.tuple;7.dictionary

# Dictionary(lug'at)
# key-value pair  (kalit-qiymat juftligi)
car={
    'brand':"Ford",
    'name':"Mustang",
    'year':2000,
    'color':"blue"

}
print(car)
print(type(car))  #<class 'dict'>
car=['Audi','Chevrolet','BYD','Tesla']

student = {
    'fullname':"John Doe",
    'age':20,
    'course':3,
    'favourite_books':["Atomic habits","O'tkan kunlar","Jinoyat va jazo"],
    'is_completed': False,
    'is_married':True
}
 
# 1.Qiymatlarniolish (keylar orqali olinadi)
print(student['fullname'])
print(student['age'])
print(student['favourite_books'])

for book in student['favourite_books']:
    print(book)

# 2.Qiymatlarni o'zgartirish
student['age']=21
student['course']=4
print(student)

# 3.Yangi qiymat qo'shish
student['hobbies']=["Reading a book","Watching a football match","Learning knowledges"]
print(student)

# 4. Key-value ni o'chirish 
del student['is_married']
print(student)

# 5.Empty dict(bo'sh lug'at)
talaba_1={}

talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# get() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

print(telefonlar.get('vali'))  # 'galaxy s9'
print(telefonlar.get('akmal')) #None
print('test')

# Amaliyot
# 1-topshiriq
print("                     Oilamiz a'zolarining shaxsiy ma'lumotlari:")
otam={}
otam['ism']="ne'mat"
otam['yil']=1973
otam['viloyat']="xorazm"

onam={}
onam['ism']="ra'no"
onam['yil']=1976
onam['viloyat']="xorazm"

opam={}
opam['ism']="marjona"
opam['yil']=2006
opam['viloyat']="xorazm"

print(f"Otamning ismi {otam['ism'].title()}, {otam['yil']}-yilda tug'ilgan va {otam['viloyat'].title()} viloyatida tug'ilgan.")
print(f"Onamning ismi {onam['ism'].title()}, {onam['yil']}-yilda tug'ilgan va {onam['viloyat'].title()} viloyatida tug'ilgan.")
print(f"Opamning ismi {opam['ism'].title()}, {opam['yil']}-yilda tug'ilgan va {opam['viloyat'].title()} viloyatida tug'ilgan.")

# 2-topshiriq
print("                     Oilamiz a'zolarining sevimli taomlari:")
taomlar ={}
taomlar['otam'] = "palov"
taomlar['onam'] = "manti"
taomlar['opam'] = "shashlik"
taomlar['men'] = "chuchvara"
taomlar['katta_opam'] = "somsa"

print(f"Otamning sevimli taomi {taomlar['otam']}.")
print(f"Onamning sevimli taomi {taomlar['onam']}.")
print(f"Kichik opamning sevimli taomi {taomlar['opam']}.")
print(f"Mening sevimli taomim {taomlar['men']}.")
print(f"Katta opamning sevimli taomi {taomlar['katta_opam']}.")

# 3-topshiriq
print("                     Python dasturlash tilidagi ma'lumot turlari va operatorlar:")
python_lugati = {
    'integer':"Butun son",
    'float':"O'nli son",
    'string':"Matn",
    'boolean':"Mantiqiy",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat",
    'dictionary':"Lug'at",
    'for':"Takrorlash operatori",
    'while':"Davomiy takrorlash operatori",
    'if':"Shart operatori"
}
print(f"Python dasturlash tilida {python_lugati['integer']} integer- ma'lumot turi butun sonlarni ifodalaydi.")
print(f"Python dasturlash tilida {python_lugati['float']} float- ma'lumot turi o'nli sonlarni ifodalaydi.")
print(f"Python dasturlash tilida {python_lugati['string']} string- ma'lumot turi matnlarni ifodalaydi.")
print(f"Python dasturlash tilida {python_lugati['boolean']} boolean- ma'lumot turi mantiqiy qiymatlarni ifodalaydi.")
print(f"Python dasturlash tilida {python_lugati['list']} list- ma'lumot turi ro'yxatlarni ifodalaydi.")
print(f"Python dasturlash tilida {python_lugati['tuple']} tuple- ma'lumot turi o'zgarmas ro'yxatlarni ifodalaydi.")
print(f"Python dasturlash tilida {python_lugati['dictionary']} dictionary- ma'lumot turi lug'atlarni ifodalaydi.")
print(f"Python dasturlash tilida {python_lugati['for']} for- operatori takrorlash operatori.")
print(f"Python dasturlash tilida {python_lugati['while']} while- operatori davomiy takrorlash operatori.")
print(f"Python dasturlash tilida {python_lugati['if']} if- operatori shart operatori bo'lib, berilgan shart bajarilsa kod blokini bajarish imkoni beradi.")

# 4-topshiriq
python_dictionary = {
    'integer':"Butun son",
    'float':"O'nli son",    
    'string':"Matn",
    'boolean':"Mantiqiy",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat",
    'dictionary':"Lug'at",
    'for':"Takrorlash operatori",
    'while':"Davomiy takrorlash operatori",
    'if':"Shart operatori"
}

text=input("Kalit so'zini kiriting: ")

if text in python_dictionary.get(text)==None:
    print("Bunday kalit so'z mavjud emas.") 
else:
    print(python_dictionary.get(text))
print("                                     Aniq izohlar:")
python_dictionary1 = {
    'integer':"Integer so'zi Butun son deb tarjima qilinadi.",
    'float':"Float so'zi O'nli son deb tarjima qilinadi.",
    'string':"String so'zi Matn deb tarjima qilinadi.",
    'boolean':"Boolean so'zi Mantiqiy deb tarjima qilinadi.",
    'list':"List so'zi Ro'yxat deb tarjima qilinadi.",
    'tuple':"Tuple so'zi O'zgarmas ro'yxat deb tarjima qilinadi.",
    'dictionary':"Dictionary so'zi Lug'at deb tarjima qilinadi.",
    'for':"For so'zi Takrorlash operatori deb tarjima qilinadi.",
    'while':"While so'zi Davomiy takrorlash operatori deb tarjima qilinadi.",
    'if':"If so'zi Shart operatori deb tarjima qilinadi."
}
if text in python_dictionary1.get(text)==None:
    print("Bunday kalit so'z mavjud emas.") 
else:
    print(python_dictionary1.get(text))