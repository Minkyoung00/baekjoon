#include <stdio.h> 

int main(){
    int A, B, C, result;
    int count[10] = {0,};
    int num[9] = {0,};

    scanf("%d\n%d\n%d", &A, &B, &C);

    result = A*B*C;
    
    int cnt = 0;

    for (int i = 1000000000; i > 1; i /= 10){ 
        num[cnt] = result % i / (i / 10);
        cnt ++;
    }

    int k = 0;

    while(!num[k]) k ++;

    for (k ; k < 9; k++){
        count[num[k]]++;
    }

    for (int j = 0; j < 10; j++) printf("%d\n", count[j]);

    return 0;
}