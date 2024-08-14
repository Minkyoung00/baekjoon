#include <stdio.h> 

int main(){
    int N, X;

    scanf("%d %d", &N, &X);

    int str;

    for (int i = 0; i < N; i++){
        scanf("%d", &str);
        if (str < X) printf("%d ",str);
    }

    return 0;
}