#program for creating list and getting positive and negitive values from the list
def positive(n):
    if(n>0):
        return True
    else:
        return False
def negitive(n):
    if(n<0):
        return True
    else:
        return False
print("Enter the values in list:")
lst=[int(val) for val in input().split()]
positive=list(filter(positive,lst))
negitive=list(filter(negitive,lst))
print("="*100)
print("ORIGINAL VALUES IN LIST=",lst)
print("POSITIVE VALUES IN LIST=",positive)
print("NEGITIVE VALUES IN LIST=",negitive)
print("="*100)