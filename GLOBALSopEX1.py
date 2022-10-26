#Program for demonstarting globals()
#globalsEx2.py
a=100
b=200
def operation():
    d=globals()
    for k,l in d.items():
        print("\t{}---->{}".format(k,l))
    print("programmer defined global variables")
    print("value of a in global var=",d.get('a'))
    print("value of b in global var=",d.get('b'))
    print("programmer defined global variables")
    print("val of a in global var=",d['a'])
    print("val of b in global var=",d['b'])

operation()