#include <GL/glut.h>
#include <stdio.h>

// Função para renderizar a tela
void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

// Função para capturar eventos de mouse
void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        printf("Clique esquerdo detectado!\n");
    }
    else if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        printf("Clique direito detectado!\n");
    }
}

// Função para capturar eventos de teclado
void keyboard(unsigned char key, int x, int y)
{
    if (key == 27)
    { // Tecla ESC
        printf("Tecla ESC pressionada. Fechando a aplicação...\n");
        exit(0); // Fecha a aplicação
    }
    else
    {
        printf("Tecla '%c' pressionada\n", key);
    }
}

int main(int argc, char *argv[])
{
    // Inicializa o GLUT
    glutInit(&argc, argv);

    // Define o modo de exibição e o tamanho da janela
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(640, 480);
    glutCreateWindow("Clique do Mouse e Teclado Detector");

    // Define as funções de callback
    glutDisplayFunc(display);
    glutMouseFunc(mouse);
    glutKeyboardFunc(keyboard); // Função para capturar teclado

    // Inicializa o OpenGL
    glClearColor(1.0, 1.0, 1.0, 1.0); // Cor de fundo (branco)

    // Entra no loop principal do GLUT
    glutMainLoop();

    return 0;
}
