# array
array = [1,2,3,4]

for i in array :
    print(i, end = '')

print('\n')

# param 1 : maksimal
print('param 1')
angka = 10
for i in range(angka):
     print("Angka ke : ")
     print(i)
print('\n')

# param 2 : minim, maksimum
print('param 2')
for i in range(angka, 20):
     print("Angka ke : ")
     print(i)
print('\n')
# param 3 : minim, maks, lompatan (increment + / decrement -)
print('param 3 increment')
for i in range(angka, 20, 2):
     print("Angka ke : ")
     print(i)
print('\n')

print('param 3 decrement')
for i in range(20, angka, -2):
     print("Angka ke : ")
     print(i)