s1 = 'pemrograman python'
s2 = "pemrograman python 2"
s3 = '''pemrograman
.   .   . python 3'''

print(s1)
print(s2)
print(s3)
print(s1[0])
print(s1[1])
print(s1[2])

data = 'p001\tspidol\t\t9000\np002\tpensil\t\t6000'
print(data)

data = '\tharga\n' + data
print(data)

# membandingkan string
s1 = 'python'
s2 = 'PYTHON'

print(s1 == s1)
print(s1 != s2)
print(s1 < s2)

# Ekstrak substring
s = "Pemrograman Python dan PyQt"

s1 = s[0:11]
print(s1)

print(len(s1))

s = s[:11]
print(s)

s = s[:8]
print(s)

s = s[8:]
print(s)

s = s[0:11:12]
print(s)

s = s[0:11:1]
print(s)

s = s[0:11:3]
print(s)

# Membuat String dengan format tertentu
s = 'balonku ada %d, kempes %d tinggal %f' % (5,1,4.5)
print(s)
