
# import sys

# -------------1
# def test():
#     print('test none')

# rez =   test()
# print(rez)

# --------------2
# fo      =  print()
# if fo   ==  None:
#     print(1)
# else:
#     print(2)

# ----------------3
# test    =   {
#     "key":"volume1",
#     "key1":"volume2",   
#     "key2":"volume3"
#     }

# for target_list in test:
#     print(target_list,test[target_list])

# try:
#     print(test["jjdl"])
# except KeyError:
#     pass

# if "key" in test:
#     print('yes')
# else:
#     print('no')
fib  = {
    1:1,
    2:1,
    3:2,
    4:3,
    }

print(fib.get(4,0))
print(fib.get(4,0) + fib.get(7,5))