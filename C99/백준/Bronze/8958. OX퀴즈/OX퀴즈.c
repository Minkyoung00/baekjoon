#include <stdio.h> 

int main(){
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++){
        char str[80];
        scanf("%s", str);

        char *cur = &str[0];
        int score = 0, pre = 0;

        while (*cur){
            if (*cur == 'O'){
                if (pre){
                    score += pre;
                }
                score++;
                pre++;
            }
            else pre = 0;
            
            cur++;
        }
        
        printf("%d\n",score);
    }

    return 0;
}