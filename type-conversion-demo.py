'''
Daire Alanı= πr²
Daire Çevresi= 2πr

*Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r=3.14)

'''

pi=3.14

r= float(input("yarı çap: "))

alan= pi*(r**2)
cevre=2*pi*r

print('Alan:', alan)
print('Çevre:', cevre)

#print('Alan:' +alan+ 'Çevre:' + cevre) #bu sadece string ifadelerde olur

print('Alan:' + str(alan) + ' Çevre:' + str(cevre))
