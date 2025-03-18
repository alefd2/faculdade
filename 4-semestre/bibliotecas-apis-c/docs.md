# Documentação da Linguagem de Programação C

## Sumário
- [Documentação da Linguagem de Programação C](#documentação-da-linguagem-de-programação-c)
  - [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Processo de Compilação](#processo-de-compilação)
  - [Tipos de Dados e Variáveis](#tipos-de-dados-e-variáveis)
    - [Tipos Básicos](#tipos-básicos)
    - [Constantes](#constantes)
    - [Classes de Armazenamento](#classes-de-armazenamento)
  - [Diretivas de Pré-processador](#diretivas-de-pré-processador)
  - [Exemplos](#exemplos)
    - [Estrutura Básica do Programa](#estrutura-básica-do-programa)
    - [Variáveis e Operações](#variáveis-e-operações)
    - [Arrays](#arrays)
    - [Funções](#funções)
  - [Dicas](#dicas)
  - [Flags de Compilação](#flags-de-compilação)
  - [Operadores](#operadores)
    - [Aritméticos](#aritméticos)
    - [Relacionais](#relacionais)
    - [Lógicos](#lógicos)
  - [Modificadores](#modificadores)
    - [Modificadores de Tipo](#modificadores-de-tipo)
    - [Características dos Modificadores](#características-dos-modificadores)

## Introdução
C é uma linguagem de programação de propósito geral criada em 1972 por Dennis Ritchie. É amplamente utilizada para programação de sistemas e sistemas embarcados.

## Processo de Compilação
Para compilar programas em C, siga estas etapas:

1. **Pré-processamento**: Processa diretivas como #include e #define
2. **Compilação**: Converte código-fonte em assembly
3. **Montagem**: Converte assembly em código objeto
4. **Ligação**: Liga arquivos objeto e bibliotecas

Comando básico de compilação:
```bash
gcc programa.c -o programa
```

## Tipos de Dados e Variáveis

### Tipos Básicos
```c
int numero = 42;            // Inteiro
float decimal = 3.14;       // Ponto flutuante
char letra = 'A';          // Caractere
double decimalGrande = 3.14159; // Ponto flutuante de dupla precisão
```

### Constantes
```c
#define PI 3.14159         // Constante do pré-processador
const int TAMANHO_MAXIMO = 100;  // Variável constante
```

### Classes de Armazenamento
```c
auto int x;        // Variável automática (padrão)
register int y;    // Sugere armazenamento em registrador
static int z;      // Mantém valor entre chamadas de função
extern int w;      // Declara variável definida em outro arquivo
```

Características principais:
- **auto**: Classe padrão para variáveis locais
- **register**: Solicita armazenamento em registrador do CPU
- **static**: 
  - Em variáveis locais: preserva valor entre chamadas
  - Em variáveis globais: limita escopo ao arquivo atual
- **extern**: Permite usar variáveis definidas em outros arquivos

## Diretivas de Pré-processador
Diretivas comuns:
```c
#include <stdio.h>    // Inclui biblioteca padrão
#include "meuarquivo.h"   // Inclui arquivo local
#define TAMANHO 100      // Define constante
#ifdef DEBUG         // Compilação condicional
#ifndef HEADER_H    // Proteção de cabeçalho
```

## Exemplos

### Estrutura Básica do Programa
```c
#include <stdio.h>

int main() {
        printf("Olá, Mundo!\n");
        return 0;
}
```

### Variáveis e Operações
```c
int a = 5;
int b = 10;
int soma = a + b;
float media = (float)(a + b) / 2;
```

### Arrays
```c
int numeros[5] = {1, 2, 3, 4, 5};
char texto[] = "Olá";
```

### Funções
```c
int soma(int x, int y) {
        return x + y;
}
```

## Dicas
- Sempre inicialize variáveis
- Use nomes significativos para variáveis
- Comente seu código
- Verifique vazamentos de memória
- Trate erros adequadamente

## Flags de Compilação
Flags comuns do GCC:
```bash
gcc -Wall          # Habilita todos os avisos
gcc -g             # Adiciona informações de depuração
gcc -O2           # Otimiza o código
gcc -std=c99      # Usa o padrão C99
```
## Operadores

### Aritméticos
```c
int a = 10, b = 3;
int soma = a + b;      // Adição
int sub = a - b;       // Subtração
int mult = a * b;      // Multiplicação
int div = a / b;       // Divisão
int resto = a % b;     // Resto
```

### Relacionais
```c
int x = 5, y = 8;
bool igual = x == y;    // Igualdade
bool diferente = x != y; // Diferença
bool maior = x > y;     // Maior que
bool menor = x < y;     // Menor que
bool maiorIgual = x >= y; // Maior ou igual
bool menorIgual = x <= y; // Menor ou igual
```

### Lógicos
```c
bool p = true, q = false;
bool e = p && q;     // AND lógico
bool ou = p || q;    // OR lógico
bool nao = !p;       // NOT lógico
```

## Modificadores

### Modificadores de Tipo
```c
long int numero_longo = 1234567890L;     // Inteiro longo
short int numero_curto = 123;            // Inteiro curto
unsigned int positivo = 100;             // Apenas números positivos
signed int com_sinal = -100;             // Com sinal (padrão)
long double precisao_alta = 3.14159L;    // Ponto flutuante de alta precisão
```

### Características dos Modificadores
- **long**: Aumenta o tamanho do tipo
- **short**: Reduz o tamanho do tipo
- **signed**: Permite valores negativos (padrão)
- **unsigned**: Apenas valores positivos
- **const**: Torna o valor imutável
- **volatile**: Indica que o valor pode mudar externamente