import os;

with open("Users/nischaya/Documents/project-euler/files/p042_words.txt","r") as fo:
    words = fo.readlines();
words = words[0].split(",");
counter = 0;
isTriangleWord = False;
for word in words:
    sum = 0;
    i = 0;
    for letter in word:
        sum += ord(letter)-64;
    while True:
        num = (i*(i+1))/(2);
        if(sum==num):
            isTriangleWord = True;
            counter += 1;
            break;
        if(num>sum):
            break;
        i+=1;
print counter;
