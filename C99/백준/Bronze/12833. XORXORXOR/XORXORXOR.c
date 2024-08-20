#include <stdio.h>

int main(){
    int A, B, C;

    scanf("%d %d %d", &A, &B, &C);

    if ( C % 2 == 0) 
        printf("%d", A);
    else 
        printf("%d", A^B);
    
    return 0;
}