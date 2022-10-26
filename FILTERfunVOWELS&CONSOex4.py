#Program for getting vowels and consonant from the inputing the name
line=input("enter the line of text:")
vowels=list(filter(lambda n:n.lower() in ['a','e','i','o','u'],line))
conso=list(filter(lambda n:n.lower() not in ['a','e','i','o','u'] and n.isalpha(),line))
print("Vowels=",vowels)
print("conso=",conso)#Program for getting vowels and consonant from the inputing the name
line=input("enter the line of text:")
vowels=list(filter(lambda n:n.lower() in ['a','e','i','o','u'],line))
conso=list(filter(lambda n:n.lower() not in ['a','e','i','o','u'] and n.isalpha(),line))
print("Vowels=",vowels)
print("conso=",conso)