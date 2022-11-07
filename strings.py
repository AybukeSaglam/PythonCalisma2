name = 'Sadık'
surname = 'Turan'
age = '36' #string olmazsa aşağıda hata verir. veya aşağıda str(age) yap

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + age + ' years old.'

print(greeting)

print(greeting[0])  #greeting'de karakterleri tek tek gösterir
print(greeting[1])
print(greeting[2])
print(greeting[3])
print(greeting[4])
print(greeting[5])
print(greeting[6])

print(len(greeting)) #greeting kaç karakterli?

print(greeting[len(greeting)-1])

print(greeting[-1]) #en son karakter

print(greeting[3:7])  #3 ile 7 arasındaki değerler. 2'yi almaz 

print(greeting[3:])   #3'den sonsuza

print(greeting[:16])    #en baştan 16'ya kadar

print(greeting[2:40:3]) #2'den 40'a kadar, 3'er 3'er git


