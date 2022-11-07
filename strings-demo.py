website = "http://www.aybukesaglam.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

print(len(course))

# 2- 'website' içinden www karakterlerini alın.

print(website[7:10])

# 3-'website' içinden com karakterini alın

print(len(website))
print(website[24:27])

# 4- 'course' içinden ilk 15 ve son 15 karakteri alın.

print(course[:15])
print(course[-15:])


# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result= course[::-1]

# 6- name, surname, age, job = 'Bora','Yılmaz',32, 'mühendis' değişkenleri ile
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'  ifadesini yazdır.

name= 'Bora'
surname= 'Yılmaz'
age= '32'
job= 'mühendis'

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")

# 7- 'Hello world' ifadesindeki w harfini W ile değiştirin.

s= 'Hello world'
result = s[6]
s = s[0:6] + 'W'+s[-4:]
print(s)

s.replace('w','W')

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

result = 'abc '*3
print(result)