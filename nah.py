while True:
    def sum(x,y):
        z=x+y
        return z
    def div(x,y):
        if y==0:
            print("can't divide by 0")
        else:
            z=x/y
        return z
    def minus(x,y):
        z=x-y
        return z
    def multi(x,y):
        z=x*y
        return z
    def power(x,y):
        z=x**y
        return z
    use=""
    x=eval(input("Enter x:"))
    while use not in ["+","-","*","/"]:
        use=input("Enter what are u gonna use?: ")
    y=eval(input("Enter y:"))
    if use=="+":
        final=sum(x,y)
    if use=="-":
        final=minus(x,y)
    if use=="*":
        final=multi(x,y)
    if use=="/":
        final=div(x,y)
    if use=="**":
        final=power(x,y)


    print("the result is:",final)
    print(" ")