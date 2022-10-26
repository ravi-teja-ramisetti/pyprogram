kvrcon=cx_Oracle.connect("scott/tiger@localhost/orcl")
print("Python program got connection from Oracle DB")
print("type of kvrcon=",type(kvrcon)) # <class, cx_Oracle.Connection>