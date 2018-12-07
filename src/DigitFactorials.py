def factorial(num):
    if(num==1):
        return 1;
    if(num==0):
        return 1;
    return factorial(num-1)*num;

def sumOfFactorials(num):
    initNum = num;
    sum = 0;
    while num:
        fact = factorial(num%10);
        sum+=fact;
        num = num/10;
    # print sum,initNum;
    return sum==initNum;

sum=0;
for i in range(9,100001):
    if(sumOfFactorials(i)):
        sum+=i;
print sum;
