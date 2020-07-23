for i in range(1,100):    
    n=int(input(f"{i}).Enter no. of observasions : "))
    x=[]
    y=[]
    X2=[]
    Y2=[]
    XY=[]
    for i in range(0,n):
        x.append(int(input("Enter the value of X : ")))
        y.append(int(input("Enter the value of Y : ")))
        x2=x[i]**2
        y2=y[i]**2
        xy=x[i] * y[i]
        X2.append(x2)
        Y2.append(y2)
        XY.append(xy)
        print(f"x2 = {x2} ")
        print(f"y2 = {y2} ")
        print(f"xy = {xy} ")
        i=i+1
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"X2 = {X2}")
    print(f"Y2 = {Y2}")
    print(f"XY = {XY}")
    def T(x,y,X2,Y2,XY):
        xT=0
        yT=0
        X2T=0
        Y2T=0
        XYT=0
        for i in x:
            xT+=i
        print(f"Sum of x is = {xT}")
        for i in y:
            yT+=i
        print(f"Sum of y is = {yT}")
        for i in X2:
            X2T+=i
        print(f"Sum of X2 is = {X2T}")
        for i in Y2:
            Y2T+=i
        print(f"Sum of Y2 is = {Y2T}")
        for i in XY:
            XYT+=i
        print(f"Sum of XY is = {XYT}")
        i=i+1
        rXY= XYT/n
        rx=xT/n
        ry=yT/n
        rX2=X2T/n
        rY2=Y2T/n
    #    print(rXY)
    #    print(rx)
    #    print(ry)
    #    print(rX2)
    #    print(rY2)
        r1=rx * ry
        r2=rX2 - (rx**2)
        r3=rY2 - (ry**2)
    #    print(r1)
    #    print(r2)
    #    print(r3)
        r4=r2**0.5
        r5=r3**0.5
        r=(rXY - r1)/(r4*r5)
        print(r)
    T(x,y,X2,Y2,XY)