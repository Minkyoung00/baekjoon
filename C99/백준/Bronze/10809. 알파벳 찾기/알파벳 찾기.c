#include <stdio.h>

int main(void){
    char word[100];
    int alphabet[26][2] = {{0,0},};
    scanf("%s", word);

    for (int i = 0; word[i] != '\0'; i++){
        if (!alphabet[word[i] - 97][1]){
            alphabet[word[i] - 97][0] = i;
            alphabet[word[i] - 97][1] = 1;
        }
    }

    for (int j = 0; j < 26; j ++)
        if (alphabet[j][1]) printf("%d ", alphabet[j][0]);
        else printf("%d ", -1);

    return 0;
}