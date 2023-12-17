def convert(str1):
    str1=' '+str1.lower()
    str2=''
    for i in range(len(str1)-1):
        if str1[i].isspace():
            str2+=chr(ord(str1[i+1])-32)
        else:
            str2+=str1[i+1]
    return str2

def main():
    str1=input('Enter a string: ')
    result=convert(str1)
    print(result)

if __name__=='__main__':
    main()
