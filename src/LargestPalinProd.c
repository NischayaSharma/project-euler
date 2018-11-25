#include "stdio.h"
#include "math.h"
#include "stdbool.h"

bool isPalindrome(int num)
{
  int paliNum=0, n=num;
  while (n) {
    paliNum = (10*paliNum) + (n%10);
    n/=10;
  }
  return paliNum==num;
}

int main(){
  for(int i=999 ; i>99 ; i--){
    for(int j=i ; j>99 ; j--){
      if(isPalindrome(i*j)){
        printf("%d = %d * %d\n", i*j, i, j);
      }
    }
  }
}
