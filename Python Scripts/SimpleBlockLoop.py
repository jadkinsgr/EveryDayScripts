i = 0
while i <= 20:
    ##i2=str(i)
    s = '''\
    This is a stanard {length} example.
    Here is a doubled {doubledlength} example.\
    '''.format(length=i, doubledlength=i*2)
    print(s)
    i = i+1
