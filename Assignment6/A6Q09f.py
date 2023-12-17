str1=input("Enter the string:")
str1=str1.lower()
vowel_count=0
consonant_count=0

for ch in str1:
    if ch.isalpha()==True:
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            vowel_count+=1
        else:
            consonant_count+=1

print('Number of vowels=',vowel_count)
print('Number of consonants=',consonant_count)
