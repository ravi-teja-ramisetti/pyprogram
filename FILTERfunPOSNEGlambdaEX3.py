#Program for generating positive and negitive numbers from created list by lambda function
positive=lambda n:n>0
negitive=lambda n:n<0
print("Enter the values in list:")
lst=[int(val) for val in input().split()]
positive=list(filter(positive,lst))
negitive=list(filter(negitive,lst))
print("="*100)
print("ORIGINAL NUMBERS IN LIST=",lst)
print("POSITIVE NUMBERS IN LIST=",positive)
print("NEGITIVE NUMBERS IN LIST=",negitive)
print("="*100)