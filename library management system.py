def book(a):
    def booka(b):
        nonlocal a
        
        if b>0:
            a=a+b
            print("the added books",b)
            
        else:
            print("error")
        return a
    ppt=booka((2))
    print(" total books",ppt)
    def ink(c):
        nonlocal a
        if c>0 and a>=c:
            a=a-c
        
        else:
            print("invalid")
        return a
    svd = ink(45)
    print("the reaming books" ,svd)
    def back(d):
        nonlocal a
        if d>0:
            print("the returned books",d)
            a=a+d
            
        else:
            print("error")
        return a
    avd=back(2)
    print(" total books",avd)
    return a
book(100)

