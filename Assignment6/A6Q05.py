import re
def count_words(str1):
    count=0
    for i in re.finditer(r'\b\w+\b',str1):
        print (i.group())
        count = count+1
    return count

def main ():
    str1=input("enter the string ")
    result= count_words(str1)
    print ('number of words=', result)

if __name__=='__main__':
    main()
