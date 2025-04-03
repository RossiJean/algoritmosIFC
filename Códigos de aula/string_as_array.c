#include <stdio.h>
#include <string.h>

int main()
{
    char frase[100];
    strcpy(frase, "Olá, tudo bem com você");
    int tam = strlen(frase);

    for (int i = 0; i < tam; i++)
    {
        printf("%c ", frase[i]);
    }
    return 0;
}
