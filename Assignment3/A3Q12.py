#a)
n=5
for i in range(1,n+1):
   for j in range(1,i+1):
      print(j,end=' ')
   print()

print()
#b)
n=4
for i in range(1,n+1):
   for s in range(1,n-i+1):
      print(' ',end=' ')
   for k in range(i,0,-1):
      print(k,end=' ')
   for j in range(2,i+1):
      print(j,end=' ')
   print()
   
print()
#c)
n=5
for i in range(n,0,-1):
   for j in range(i,0,-1):
      print(j,end=' ')
   print()

print()
#d)
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print()
    
print()
#e)
n=5
for i in range(1,n+1):
   for s in range(i-1):
        print(' ', end=' ')
   for j in range(i,n+1):
      print(j,end=' ')
   print()
   
print()
#f)
n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()

print()
#g)
n= 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()
    
print()
#h)
n = 4
for i in range(1, n + 1):
    for s in range(1, n - i + 1):
        print(' ', end=' ')
    for j in range(1, i + 1):
        print('*', end=' ')
    for k in range(i-1,0,-1):
        print('*', end=' ')
    print()

print()
#i)
n = 4
for i in range(n):
    for s in range(i):
        print(' ', end=' ')
    for j in range(2 * (n - i) - 1):
        if i == 0:
            print('*', end=' ')
        elif j == 0 or j == 2 * (n - i) - 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print()
#j)
n = 4
for i in range(n,0,-1):
    for s in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(i-1,0,-1):
        print('*', end=' ')
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

print()
#k)
n = 4
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end=' ')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(2*(n - i - 1) - 1):
        if j == 0 or j == 2*(n - i - 1) - 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print()
#l)
n=4
for i in range(1, n + 1):
    for s in range(1, n - i + 1):
        print(' ', end=' ')
    for j in range(1, i + 1):
        print('*', end=' ')
    for k in range(i-1,0,-1):
        print('*', end=' ')
    print()
for i in range(n-1,0,-1):
    for s in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(i-1,0,-1):
        print('*', end=' ')
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

print()
#m)
n=5
for i in range(1,n+1):
   for s in range(i-1):
        print(' ', end=' ')
   for j in range(i,n+1):
      print('$',end=' ')
   print()

print()
#n)
n=5
for i in range(n,0,-1):
   for s in range(i-1):
        print(' ', end=' ')
   for j in range(i,n+1):
      print('#',end=' ')
   print()

