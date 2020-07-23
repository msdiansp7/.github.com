for i in range(1,100):
    n=int(input(f"{i}).Enter no. of observasions : "))
    DP=int(input("Set precision to decimal points : "))
    x=[]
    y=[]
    X2=[]
    Y2=[]
    XY=[]
    for i in range(0,n):
        x.append(int(input(f"Enter the value of X{i+1} : ")))
        y.append(int(input(f"Enter the value of Y{i+1} : ")))
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
#Average values
        XYavg= XYT/n
        Xavg=xT/n
        Yavg=yT/n
        X2avg=X2T/n
        Y2avg=Y2T/n
#Values required in formula
        R1=Xavg * Yavg
        r1=round(R1,DP)
        R2=X2avg - (Xavg**2)
        r2=round(R2,DP)
        R3=Y2avg - (Yavg**2)
        r3=round(R3,DP)
        Bxy1=(XYavg-r1)/r3
        Byx1=(XYavg-r1)/r2
        Bxy=round(Bxy1,DP)
        Byx=round(Byx1,DP)
        C1=Bxy*(-Yavg)
        C2=C1+Xavg
        C=round(C2,DP)
        LineEqX=str(C)+" + ("+str(Bxy)+"Y)"
        print("Equation of line of regression of X on Y is : ")
        print(f"X = {LineEqX}")
        D1=Byx*(-Xavg)
        D2=D1+Yavg
        D=round(D2,DP)
        LineEqY=str(D)+" + ("+str(Byx)+"X)"
        print("Equation of line of regression of Y on X is : ")
        print(f"Y = {LineEqY}")
    T(x,y,X2,Y2,XY)