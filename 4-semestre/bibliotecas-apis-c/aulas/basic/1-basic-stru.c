// diretivas
#include <stdio.h>

const float PI = 3.14159;

void incrementa()
{
    static int contador = 0;

    contador++;
    printf("contador %d\n", contador);
}

int main()
{

    printf("Bem vindo ao programa de cálculo de area de circulo!\n");

    int raio = 10;
    float area = PI * raio * raio;

    printf("A area do circulo com raio %d e: %.2f\n", raio, area);

    incrementa();
    incrementa();
    incrementa();

    return 0;
}