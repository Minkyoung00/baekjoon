#include <stdio.h>

int main(void){
    int A, B, V, cnt;
    scanf("%d %d %d", &A, &B, &V);

    cnt = (V - A) / (A - B);

    if ((V - (A - B)*cnt - A) <= 0) cnt += 1;
    else cnt += 2;

    printf("%d", cnt);

    return 0;
}