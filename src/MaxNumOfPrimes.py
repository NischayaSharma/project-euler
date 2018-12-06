
def isPrime(num):
  if(num==2 or num==3):
    return True;
  for i in range(num-1,1,-1):
    if(num%i==0):
      return False;
  return True;

maxNumOfPrimes=0;
a,b = 0,0;
for i in range(-999,1000):
    for j in range(-1000,1001):
        n=0;
        numOfPrimes=0;
        while True:
            primeQuad = n**2 + i*n + j;
            if(primeQuad<0):
                break;
            if(not isPrime(primeQuad)):
                break;
            numOfPrimes += 1;
            if(maxNumOfPrimes>numOfPrimes):
                maxNumOfPrimes = maxNumOfPrimes;
            else:
                maxNumOfPrimes = numOfPrimes;
                a=i;
                b=j;
            n+=1;
print a*b;
