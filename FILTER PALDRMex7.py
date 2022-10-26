#FilterEx7.py
#main program
lst=["abbA","121","abcd","KVK","python","AA"]
pallist=list(filter(lambda word:word[0].lower()==word[-1].lower() and len(word)>2, lst))
print("Given Words=",lst)
print("Palindrome Words=",pallist)