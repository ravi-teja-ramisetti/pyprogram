import random
passlen=int(input("Enter the length of the password:"))
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print("".join(random.sample(s,passlen)))

