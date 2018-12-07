numOfWays = 0;
for numOf1p in range(201):
    for numOf2p in range(101):
        for numOf5p in range(41):
            for numOf10p in range(21):
                for numOf20p in range(11):
                    for numOf50p in range(5):
                        for numOf100p in range(3):
                            for numOf200p in range(2):
                                print numOf1p,numOf2p,numOf5p,numOf10p,numOf20p,numOf50p,numOf100p,numOf200p;
                                print numOfWays;
                                if(((numOf1p*1)+(numOf2p*2)+(numOf5p*5)+(numOf10p*10)+(numOf20p*20)+(numOf50p*50)+(numOf100p*100)+(numOf200p*200))==200):
                                    numOfWays+=1;
