# and  与（并且） a and b
# or   或（或者） a or b
# not  非（取反） not a

a = True
b = False
print(a and b)  # false
print(a or b)  # true
print(not b)  # true
print(not a)  # false

print(True and True)  # true
print(True or True)  # true
print(not True)  # false

print(1 > 2 or 8 == 8)  # true
print(1 > 2 and 8 == 8)  # false
print(not (1 > 2 and 8 == 8))  # true
