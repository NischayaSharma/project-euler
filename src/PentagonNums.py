def mod(num):
    return -num if(num<0) else num;
def pentagonNums(num):
    pentNums = [];
    for i in range(1,num+1):
        pentNums.append((i*((3*i)-1))/2);
    return pentNums;

pentNums = pentagonNums(50000);
minDif = mod(pentNums[0]-pentNums[1])
for i in range(len(pentNums)):
    for j in range(i,len(pentNums)):
        for num in pentNums:
            sum = pentNums[i] + pentNums[j];
            dif = mod(pentNums[i] - pentNums[j]);
            if(sum == num and dif == num):
                minDif = minDif if(minDif<dif) else dif;
print minDif;
