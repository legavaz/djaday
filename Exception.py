
print ('hello world')
try:
    print (10/0)
except (ZeroDivisionError,SyntaxError):
    print("чет не получилось, походу деление на ноль")
