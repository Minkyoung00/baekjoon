#include <stdio.h>

int main(void){
    int cnt = 0;
    char str[1000002] = {};
    
    for (int j = 0; j < 1000002; j++){
        scanf("%c", &str[j]);

        if (str[j] == ' ') 
            if (j) cnt++;

        if (str[j] == '\n') {
            if (str[j-1] != ' '&& j) cnt++;
            break;  
        }
    }

    printf("%d",cnt);

    return 0;
}