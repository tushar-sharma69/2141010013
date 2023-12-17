str1=input('Enter a string: ')
str2=''
for ch in str1:
    if ch not in str2:
        str2+=ch
    else:
        str2+='*'

print(str2)
