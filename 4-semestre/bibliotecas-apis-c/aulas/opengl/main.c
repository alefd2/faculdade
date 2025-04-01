#include <GL/glut.h>

float posX = 0.0f, posY = 0.0f; // Posição do quadrado
float speed = 0.05f;            // Velocidade de movimento

// Limites da caixa (em coordenadas normalizadas)
float minX = -1.0f, maxX = 1.0f;
float minY = -1.0f, maxY = 1.0f;

// Função de exibição
void display()
{
    glClear(GL_COLOR_BUFFER_BIT); // Limpa a tela

    glLoadIdentity();               // Reseta a transformação
    glTranslatef(posX, posY, 0.0f); // Aplica a movimentação

    // Desenha o quadrado
    glBegin(GL_QUADS);
    glColor3f(1.0, 0.0, 0.0); // Cor vermelha
    glVertex2f(-0.1, -0.1);   // Ponto inferior esquerdo
    glVertex2f(0.1, -0.1);    // Ponto inferior direito
    glVertex2f(0.1, 0.1);     // Ponto superior direito
    glVertex2f(-0.1, 0.1);    // Ponto superior esquerdo
    glEnd();

    glFlush(); // Força a exibição dos gráficos
};

// Função para mover o quadrado com as teclas de seta
void keyboard(int key, int x, int y)
{
    // Mover o quadrado com limites
    if (key == GLUT_KEY_LEFT)
    {
        if (posX - speed >= minX)
            posX -= speed; // Move para a esquerda, mas não ultrapassa o limite
    }
    else if (key == GLUT_KEY_RIGHT)
    {
        if (posX + speed <= maxX)
            posX += speed; // Move para a direita, mas não ultrapassa o limite
    }
    else if (key == GLUT_KEY_UP)
    {
        if (posY + speed <= maxY)
            posY += speed; // Move para cima, mas não ultrapassa o limite
    }
    else if (key == GLUT_KEY_DOWN)
    {
        if (posY - speed >= minY)
            posY -= speed; // Move para baixo, mas não ultrapassa o limite
    }

    glutPostRedisplay(); // Solicita a atualização da tela após movimentar
}

// Função para inicializar a janela e configurar o OpenGL
void initOpenGL()
{
    glClearColor(0.0, 0.0, 0.0, 1.0);         // Cor de fundo preta
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0); // Definição do sistema de coordenadas 2D
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Jogo de Movimento com OpenGL");

    initOpenGL(); // Configurações do OpenGL

    glutDisplayFunc(display);  // Função de renderização
    glutSpecialFunc(keyboard); // Função para teclas especiais (setas)

    glutMainLoop(); // Inicia o loop principal

    return 0;
}
