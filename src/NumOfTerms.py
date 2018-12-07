nums = [];
for i in range(2,101):
    for j in range(2,101):
        nums.append(i**j);
length = len(nums);
print length;
for i in range(length):
    j=i+1;
    while j<length:
        # print i,nums[i]
        # print j,nums[j];
        # print length;
        if(nums[i]==nums[j]):
            nums.pop(i);
            length-=1;
        # print length;
        j+=1;
print len(nums);
