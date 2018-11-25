#include <stdio.h>

int main(){
  long int initNum=2, maxNumOfTerms=0, numOfTerms=1, i, maxInitNum;
  for(i=2;i<=1000000;i++){
    numOfTerms=1;
    initNum=i;
    while(initNum!=1){
      if(initNum%2==0)
        initNum=initNum/2;
      else
        initNum=(initNum*3)+1;
      numOfTerms++;
    }
    if(numOfTerms>maxNumOfTerms){
      maxInitNum=i;
      maxNumOfTerms=numOfTerms;
    }
  }
  printf("%ld\t%ld\n", maxNumOfTerms, maxInitNum);
}
