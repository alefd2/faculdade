# 📚 Bibliotecas e APIs para Linguagem C  

## Introdução  
A linguagem C é amplamente utilizada para desenvolvimento de sistemas, software embarcado e aplicações de alto desempenho. Para facilitar a programação e otimizar o código, C fornece um conjunto de **bibliotecas padrão** e também permite o uso de **APIs avançadas** para funcionalidades específicas, como interfaces gráficas, manipulação de hardware e programação paralela.

## 📌 Bibliotecas Padrões  

### 1️⃣ `stdio.h` – Entrada e saída padrão  
Essa biblioteca contém funções para manipulação de entrada e saída de dados.  

```c
#include <stdio.h>

int main() {
    char nome[50];
    printf("Digite seu nome: ");
    scanf("%s", nome);
    printf("Olá, %s!\n", nome);
    return 0;
}
```

### 2️⃣ `stdlib.h` – Alocação de memória e conversões
Inclui funções para manipulação de memória dinâmica.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int *) malloc(sizeof(int));
    if (ptr == NULL) {
        printf("Erro ao alocar memória\n");
        return 1;
    }
    *ptr = 42;
    printf("Valor armazenado: %d\n", *ptr);
    free(ptr);
    return 0;
}
```

### 3️⃣ `string.h` – Manipulação de strings
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Olá, ";
    char str2[] = "Mundo!";
    strcat(str1, str2);  
    printf("%s\n", str1);  // "Olá, Mundo!"
    return 0;
}
```

### 4️⃣ `math.h` – Funções matemáticas
```c
#include <stdio.h>
#include <math.h>

int main() {
    double num = 16.0;
    printf("Raiz quadrada de %.2f é %.2f\n", num, sqrt(num));
    return 0;
}
```

### 5️⃣ `time.h` – Manipulação de tempo
```c
#include <stdio.h>
#include <time.h>

int main() {
    time_t agora;
    time(&agora);
    printf("Data e hora atual: %s", ctime(&agora));
    return 0;
}
```

## 🚀 APIs e Bibliotecas Avançadas

### 🎨 GTK – Interface gráfica
```c
#include <gtk/gtk.h>

void hello(GtkWidget *widget, gpointer data) {
    g_print("Botão clicado!\n");
}

int main(int argc, char *argv[]) {
    GtkWidget *window, *button;
    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    button = gtk_button_new_with_label("Clique aqui");

    g_signal_connect(button, "clicked", G_CALLBACK(hello), NULL);
    gtk_container_add(GTK_CONTAINER(window), button);
    gtk_widget_show_all(window);
    
    gtk_main();
    return 0;
}
```

### 🎮 OpenGL – Gráficos 3D
```c
#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutCreateWindow("OpenGL Exemplo");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
```

### ⚙️ Pthreads – Programação multithread
```c
#include <stdio.h>
#include <pthread.h>

void *threadFunc(void *arg) {
    printf("Thread executando!\n");
    return NULL;
}

int main() {
    pthread_t thread;
    pthread_create(&thread, NULL, threadFunc, NULL);
    pthread_join(thread, NULL);
    return 0;
}
```

### 🖥️ WinAPI / POSIX – Chamadas do sistema operacional

POSIX (Linux/macOS):
```c
#include <stdlib.h>

int main() {
    system("ls -l");  // Lista arquivos no Linux
    return 0;
}
```

Windows (WinAPI):
```c
#include <windows.h>

int main() {
    MessageBox(NULL, "Olá, Windows!", "Mensagem", MB_OK);
    return 0;
}
```

## 🎯 Aplicações
- ✔ Desenvolvimento de interfaces gráficas com GTK, OpenGL, Qt
- ✔ Manipulação de arquivos e eventos do sistema com stdio.h, stdlib.h
- ✔ Comunicação via rede e hardware com sockets, termios.h
- ✔ Programação concorrente e paralela com Pthreads e OpenMP

## 📌 Conclusão
- As bibliotecas padrão de C fornecem ferramentas essenciais para entrada/saída, manipulação de memória e operações matemáticas.
- As APIs avançadas permitem o desenvolvimento de interfaces gráficas, computação paralela, renderização gráfica e controle de hardware.
- O domínio dessas ferramentas torna o desenvolvimento em C mais produtivo, eficiente e poderoso.