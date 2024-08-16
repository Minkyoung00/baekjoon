#include <stdio.h>

int main(void){
    char A[3], B[3];
    int reverse_A = 0, reverse_B = 0;
    
    scanf("%s %s", A, B);

    reverse_A = (A[2] - '0')*100 + (A[1] - '0')*10 + (A[0] - '0') ;
    reverse_B = (B[2] - '0')*100 + (B[1] - '0')*10 + (B[0] - '0');

    
    printf("%d", (reverse_A > reverse_B ? reverse_A : reverse_B));

    return 0;
}