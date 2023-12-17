str1=input('Enter 1st string: ')
str2=input('Enter 2nd string: ')
str1=str1.lower()
str2=str2.lower()

if len(str1)!=len(str2):
    print('two strings are not anagram to each other')
else:
    str1=sorted(str1)
    str2=sorted(str2)
    if str1==str2:
        print('two strings are anagram to each other')
    else:
        print('two strings are not anagram to each other')
