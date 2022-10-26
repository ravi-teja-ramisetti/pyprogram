#program for generating  while in for loop statement
#whileinforloopex3.py
for i in range(6,0,-1):
    print("="*50)
    print("value of i----outer loop: {}".format(i))
    print("="*50)
    j=3
    while(j>=1):
        print("value of j-----inner loop : {}".format(j))
        j=j-1
        i=i+1
    else:
        print("other program statement")
else:
    print("="*50)
    print("PROGRAM EXECUTED SUCCESFULLY!!!")