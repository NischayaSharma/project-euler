def thTriangularNum(n):
    return (n*(n+1))/2;

def thPentagonalNum(n):
    return (n*((3*n)-1))/2;

def thHexagonalNum(n):
    return n*((2*n)-1);

for i in range(1,100000):
    triNum = thTriangularNum(i);
    for j in range(1,100000):
        pentNum = thPentagonalNum(j);
        if(triNum==pentNum):
            for k in range(1,100000):
                hexNum = thHexagonalNum(k);
                if(hexNum==triNum):
                    print triNum,i,j,k;
