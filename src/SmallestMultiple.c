#include "stdio.h"

int main(){
  int check;
  for(int i=21 ; i>0 ; i++){
    check=0;
    for(int j=1 ; j<=20 ; j++)
      if(i%j!=0)
        check=1;
    if(check==0){
      printf("%d\n",i);
      break;
    }
  }
}
