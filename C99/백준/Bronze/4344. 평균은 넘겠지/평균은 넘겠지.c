#include <stdio.h> 

int main(){
    int C, N, sum = 0;
    int scores[1000] ={};
    float avg, high_s = 0;

    scanf("%d", &C);

    for (int i = 0; i < C; i++){
        sum = high_s = 0;
        scanf("%d", &N);

        for (int j = 0; j < N; j++){
            scanf("%d", &scores[j]);
            sum += scores[j];
        }

        avg = sum / N;
        
        for (int k = 0; k < N; k++){
            if (scores[k] > avg) high_s++;
        }
        
        printf("%.3f%%\n", 100*(high_s / N));
    }

    return 0;
}