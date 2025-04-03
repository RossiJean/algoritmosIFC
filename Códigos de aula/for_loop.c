//inclusão da biblioteca de entrada e saída
#include <stdio.h>

//ponto de início do programa
int main(){
	
	//repita 10 vezes
	for (int i=1; i <= 10; i++){
		//mostre o contador de repetições
		printf("i = %d\n", i);
	}
	
	//fim do programa
		return 0;
}
///////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int main(){
    srand(time(NULL));
    int s = 0;
    for (int i=1; i <= 10001; i++){
        int r = rand() % 10001;
        printf("%d ", r);
        s = s + r;
    }    
    int m = s / 10001;

    printf("\n média é %d", m);
}
