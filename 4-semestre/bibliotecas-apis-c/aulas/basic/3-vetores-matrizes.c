#include <stdio.h>

void demonstraVetores(int vetor[], int tamanho);
void demonstraMatriz(int matriz[][3], int linhas);
void demonstraPonteiros(int *ptr);

int main()
{
    // Exemplo de vetor
    int vetor[5] = {1, 2, 3, 4, 5};

    // Exemplo de matriz
    int matriz[2][3] = {
        {1, 2, 3},
        {4, 5, 6}};

    // Exemplo de ponteiro
    int numero = 10;
    int *ponteiro = &numero;

    printf("=== Demonstração de Vetores ===\n");
    demonstraVetores(vetor, 5);

    printf("\n=== Demonstração de Matriz ===\n");
    demonstraMatriz(matriz, 2);

    printf("\n=== Demonstração de Ponteiros ===\n");
    demonstraPonteiros(ponteiro);

    return 0;
}

void demonstraVetores(int vetor[], int tamanho)
{
    printf("Elementos do vetor:\n");
    for (int i = 0; i < tamanho; i++)
    {
        printf("vetor[%d] = %d\n", i, vetor[i]);
    }
}

void demonstraMatriz(int matriz[][3], int linhas)
{
    printf("Elementos da matriz:\n");
    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("matriz[%d][%d] = %d\n", i, j, matriz[i][j]);
        }
    }
}

void demonstraPonteiros(int *ptr)
{
    printf("Valor apontado pelo ponteiro: %d\n", *ptr);
    printf("Endereço armazenado no ponteiro: %p\n", (void *)ptr);

    int idade = 30;
    ptr = &idade;
    printf("Novo valor apontado pelo ponteiro: %d\n", *ptr);

    // Modificando o valor através do ponteiro
    *ptr = 20;
    printf("Novo valor após modificação: %d\n", *ptr);
}