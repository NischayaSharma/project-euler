#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <string.h>

int numOfDigits(int num1){
	int numOfDig=0;
	while(num1!=0){
        num1=num1/10;
        numOfDig++;
    }
    return numOfDig;
}
void tensDigit(int num, FILE *fptr){
    switch(num){
        case 1:
            fprintf(fptr, " Ten");
            break;
        case 2:
            fprintf(fptr, " Twenty");
            break;
        case 3:
            fprintf(fptr, " Thirty");
            break;
        case 4:
            fprintf(fptr, " Forty");
            break;
        case 5:
            fprintf(fptr, " Fifty");
            break;
        case 6:
            fprintf(fptr, " Sixty");
            break;
        case 7:
            fprintf(fptr, " Seventy");
            break;
        case 8:
            fprintf(fptr, " Eighty");
            break;
        case 9:
            fprintf(fptr, " Ninety");
            break;
    }
}
void singleDigit(int num, FILE *fptr){
    switch(num){
        case 1:
            fprintf(fptr, " One");
            break;
        case 2:
            fprintf(fptr, " Two");
            break;
        case 3:
            fprintf(fptr, " Three");
            break;
        case 4:
            fprintf(fptr, " Four");
            break;
        case 5:
            fprintf(fptr, " Five");
            break;
        case 6:
            fprintf(fptr, " Six");
            break;
        case 7:
            fprintf(fptr, " Seven");
            break;
        case 8:
            fprintf(fptr, " Eight");
            break;
        case 9:
            fprintf(fptr, " Nine");
            break;
    }
}
void teenDigit(int num, FILE *fptr){
    switch(num){
        case 11:
            fprintf(fptr, " Eleven");
            break;
        case 12:
            fprintf(fptr, " Twelve");
            break;
        case 13:
            fprintf(fptr, " Thirteen");
            break;
        case 14:
            fprintf(fptr, " Fourteen");
            break;
        case 15:
            fprintf(fptr, " Fifteen");
            break;
        case 16:
            fprintf(fptr, " Sixteen");
            break;
        case 17:
            fprintf(fptr, " Seventeen");
            break;
        case 18:
            fprintf(fptr, " Eighteen");
            break;
        case 19:
            fprintf(fptr, " Nineteen");
            break;
    }
}
void coreDigits(int num, FILE *fptr){
   	int numOfDig = 0;
    bool isTeen = false;
    char str[100];
    numOfDig=numOfDigits(num);
    if(numOfDig>=2)
        if((num%100) < 20 && (num%100) > 10)
            isTeen=true;
    switch(numOfDig){
        case 1:
            singleDigit(num%10,fptr);
            break;
        case 2:
            if(!isTeen){
                tensDigit(num/10,fptr);
                singleDigit(num%10,fptr);
            }
            else
                teenDigit(num%100,fptr);
            break;
        case 3:
            singleDigit(num/100,fptr);
            fprintf(fptr, " Hundred and");
            if(!isTeen){
                tensDigit((num/10)%10,fptr);
                singleDigit(num%10,fptr);
            }
            else
                teenDigit(num%100,fptr);
            break;
    }
}
void coreFunction(int num, int numOfDig, FILE *fptr){
    if(numOfDig>15){
        coreDigits(num/pow(10,15),fptr);
        fprintf(fptr, " Trillion");
        coreFunction(num%(int)pow(10,15),numOfDigits(num%(int)pow(10,15)),fptr);
    }
    else if(numOfDig>12){
        coreDigits(num/pow(10,12),fptr);
        fprintf(fptr, " Trillion");
        coreFunction(num%(int)pow(10,12),numOfDigits(num%(int)pow(10,12)),fptr);
    }
    else if(numOfDig>9){
        coreDigits(num/pow(10,9),fptr);
        fprintf(fptr, " Billion");
        coreFunction(num%(int)pow(10,9),numOfDigits(num%(int)pow(10,9)),fptr);
    }
    else if(numOfDig>6){
        coreDigits(num/pow(10,6),fptr);
        fprintf(fptr, " Million");
        coreFunction(num%(int)pow(10,6),numOfDigits(num%(int)pow(10,6)),fptr);
    }
    else if(numOfDig>3){
        coreDigits(num/pow(10,3),fptr);
        fprintf(fptr, " Thousand");
        coreDigits(num%(int)pow(10,3),fptr);
    }
    else
    	coreDigits(num,fptr);
}
void numToDig(int num, FILE *fptr){
	int numOfDig;
	numOfDig=numOfDigits(num);
	coreFunction(num,numOfDig,fptr);
}

int main() {
	FILE *fptr;
	int num, counter=0;
	char ch ;
	fptr = fopen("/Users/nischaya/Documents/ProjectEuler/C Programs/demoFile.txt","w");
	for(num=1 ; num<=1000 ; num++)
		numToDig(num,fptr);
	fclose(fptr);
	fptr = fopen("/Users/nischaya/Documents/ProjectEuler/C Programs/demoFile.txt","r");
	while( (ch = getc(fptr)) != EOF ) {
    if(ch!=' '){
			counter++;
			printf("%c",ch);
		}
  }
	printf("\n");
	printf("%d\n",counter);
}
