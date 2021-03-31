age = 15

print('kid' if age < 18 else 'adult')
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')

#line 4 is equivalent to:if age < 18:
if age < 18:
    if age < 13:
        print('kid')
    else:
        print('teenager')
else:
    print('adult')
