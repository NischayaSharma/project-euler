maxNumOfSol = 0;
maxNumOfSolAt = 0;
for i in range(1001):
    numOfSolutions = 0;
    for a in range(i):
        for b in range(i):
            for c in range(i):
                isTriangle = (a+b>c)and(a+c>b)and(b+c>a);
                isRightTriangle = ((a**2)+(b**2)==(c**2)) or ((a**2)+(c**2)==(b**2)) or ((c**2)+(b**2)==(a**2))
                isSum = (a+b+c==i);
                print a,b,c;
                if(isTriangle and isRightTriangle and isSum):
                    numOfSolutions+=1;
    numOfSolutions = numOfSolutions/6;
    if(numOfSolutions>maxNumOfSol):
        maxNumOfSol = numOfSolutions;
        maxNumOfSolAt = i;
    else:
        maxNumOfSol = maxNumOfSol;
    print i;
print maxNumOfSolAt, numOfSolutions;
