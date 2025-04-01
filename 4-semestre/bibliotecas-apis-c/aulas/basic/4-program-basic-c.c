#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *array;
    int size, i;

    printf("Quantos números você deseja inserir? ");
    scanf("%d", &size);

    // Alocação dinâmica de memória
    array = (int *)malloc(size * sizeof(int));

    // Verificação de alocação bem-sucedida
    if (array == NULL)
    {
        printf("Erro de alocação de memória.\n");
        return -1; // Encerra o programa com erro
    }

    // Inserção de números no array
    for (i = 0; i < size; i++)
    {
        printf("Digite o número %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    // Exibição dos números
    printf("Você inseriu: ");
    for (i = 0; i < size; i++)
    {
        printf("%d ", array[i]);
    }

    // Liberação da memória alocada
    free(array);

    return 0;
}

#include <stdio.h>

int isPrime(int num)
{
    if (num <= 1)
        return 0;
    for (int i = 2; i * i <= num; i++)
    {
        if (num % i == 0)
            return 0;
    }
    return 1;
}

int main()
{
    int count = 0;
    int num = 2;

    while (count < 100)
    {
        if (isPrime(num))
        {
            count++;
        }
        if (count < 100)
            num++;
    }

    printf("O 100º número primo é: %d\n", num);
    return 0;
}