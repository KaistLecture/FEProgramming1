
a = [1,2,3,4]
b = []

for i in a:
    b.append(i*2)

print(a)
print(b)

c = [3*i for i in a]
print(c)


for i in range(90,100,3):
    print(i)
    

for i in range(len(a)):
    print(a[i])
    
for i, x in enumerate(a):
    print(i,x)



#while
p = 0
while p<10:
    print(p)
    p = p+1

while True:
    if p>20:
        break
    p += 1
    print(p)

#누적합계
print("="*30)
s=0
for i in a:
    s += i
print(s)


for i in range(100):
    if i%3!=0:
        print("Not")
        continue
    elif i%9!=0:
        print("NOT 9")
    else:
        print(i)
    
print("="*30)
for i in range(100):
    if i%2==0 or i%3==0:
        print(i)

print("="*30)
t = [3,5,2,7,8]
for i in range(10):
    if i not in t:
        print(i)


for i in range(10):
    print("*"*i)



