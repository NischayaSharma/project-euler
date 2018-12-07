import os;

triangleNums = [];
for i in range(2000):
    triangleNums.append((i*(i+1))/(2));
with open(os.path.dirname(os.path.realpath(__file__))+"/p042_words.txt","r") as fo:
    words = fo.readlines();
words = words[0].split(",");
print words;
