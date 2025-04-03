#include <stdio.h>

int main()
{
    int i = 0;
    while (i < 10)
    {
        printf("i %i\n", i);
            i = i + 1;
    }
    return 0;
}
//////////////////////////////////////////////////////////////
#include <stdio.h>

int main(void)
{
    int i = 0;
    do
    {
        printf("i = %i\n", i);
        i++;
    } while (i < 10);
    return(0);
}
