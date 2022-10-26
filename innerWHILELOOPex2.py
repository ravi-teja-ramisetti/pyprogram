#program for generating the inner whileloop statement
#innerWHILELOOPex.py
i=1
while(i<=6):
    print("="*50)
    print("val of i-----outer loop : {}".format(i))
    print("="*50)
    j=1
    while(j<=4):
        print("val of j----inner loop : {}".format(j))
        j=j+1
    else:
        print("=" * 50)
        print("out of inner loop")
        i=i+1
else:
    print("="*50)
