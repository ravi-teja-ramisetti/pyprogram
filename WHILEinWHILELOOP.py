i=1
while(i<=5):
    print("="*50)
    print("value of i----outer value: {}".format(i))
    print("="*50)
    i=i+1
    j=1
    while(j<=4):
        print("value of j----inner value:{}".format(j))
        j=j+1
    else:
        print("out of inner loop")
else:
    print("executed!!!")