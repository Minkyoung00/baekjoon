#include <stdio.h>
#include <string.h>

int main(){
    int M;
    int S = 0;
    int bi[20] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288};

    scanf("%d", &M);

    for (int i = 0; i < M; i++){
        char cal[7];
        int x; 
        scanf("%s %d", cal, &x);

        if (strstr(cal, "add")){
            S = S | bi[x-1];
        }
        else if (strstr(cal, "remove")){
            S = S & ~bi[x-1];
        }
        else if (strstr(cal, "check")){
            printf("%d\n", S & bi[x-1] ? 1 : 0);
        }
        else if (strstr(cal, "toggle")){
            S = S ^ bi[x-1];
        }
        else if (strstr(cal, "all")){
            S = 0B11111111111111111111;
        }
        else { // cal == "empty"
            S = 0;
        }    
    }
    
    return 0;  
}