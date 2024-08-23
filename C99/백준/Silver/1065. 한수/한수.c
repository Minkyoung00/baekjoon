#include <stdio.h>

int main(){
    int N, N_100, N_10, N_1, cnt;

    scanf("%d", &N);

    if (N < 100) cnt = N;
    else{
        cnt = 99;
        for (int i = 100; i <= N; i++){
            N_100 = (i / 100);
            N_10 = (i % 100) / 10;
            N_1 = (i % 10);
            if ((N_100 - N_10) == (N_10 - N_1)) 
                    cnt++;
        }
    }
    
    printf("%d", cnt);
    
    return 0;  
}