name = 'Çınar'
surname = 'Turan'
age = 36

#print('My name is {} {}'.format(name, surname))

print('My name is {1} {0}'.format(name, surname)) #ilk indeks 0. sırayla yazman önemli

print('My name is {s} {n}'.format(n=name, s=surname))

print("My name is {} {} and I'm {} years old." .format(name, surname, age))

print(f"My name is {name} {surname} and I'm {age} years old.")

result= 200/700

print('The result is {}' .format(result))   #sayı kaç basamaklı ise hepsini gösterir

print('The result is {r:7.4}' .format(r=result))    #sayının 4 basamağı gösterilir. kendisiyle beraber 7 karakter boşluk var

