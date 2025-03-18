import tkinter as tk
import random
from tkinter import messagebox as mb

class BombermanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bomberman")
        
        self.grid_size = 10
        self.cell_size = 50
        self.bombs = []
        self.explosions = []
        self.player_pos = [0, 0]
        self.game_over = False
        self.enemies = []  # Lista de inimigos
        self.enemy_speed = 500  # Velocidade de movimento dos inimigos (quanto menor, mais lento)
        
        # Criar a tela de jogo
        self.canvas = tk.Canvas(self.root, width=self.grid_size * self.cell_size, height=self.grid_size * self.cell_size)
        self.canvas.pack()
        
        # Botão para resetar o mapa
        self.reset_button = tk.Button(self.root, text="Resetar Mapa", command=self.reset_game)
        self.reset_button.pack()
        
        # Criar a grid com obstáculos fixos
        self.grid = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.create_grid()
        self.create_player()
        
        # Criar os inimigos
        self.create_enemies()
        
        # Configurar controles de movimento do jogador
        self.root.bind("<KeyPress>", self.move_player)
        
        # Iniciar o movimento dos inimigos
        self.move_enemies()
        
    def create_grid(self):
        """ Cria a grid com obstáculos aleatórios e não muda ao mover o jogador """
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Adicionar obstáculos aleatórios
                if random.random() < 0.2:
                    self.grid[row][col] = "obstacle"
                    self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size,
                                                 (col + 1) * self.cell_size, (row + 1) * self.cell_size,
                                                 fill="black", outline="gray")
                else:
                    self.grid[row][col] = None
    
    def create_player(self):
        """ Desenha o jogador na tela """
        self.player = self.canvas.create_rectangle(self.player_pos[1] * self.cell_size, self.player_pos[0] * self.cell_size,
                                                  (self.player_pos[1] + 1) * self.cell_size, (self.player_pos[0] + 1) * self.cell_size,
                                                  fill="blue", outline="gray")
    
    def create_enemies(self):
        """ Cria inimigos de forma aleatória no mapa """
        for _ in range(3):  # 3 inimigos
            enemy_pos = [random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)]
            while self.grid[enemy_pos[0]][enemy_pos[1]] == "obstacle" or enemy_pos == self.player_pos:
                # Evita que inimigos se sobreponham a obstáculos ou ao jogador
                enemy_pos = [random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)]
            enemy = self.canvas.create_rectangle(enemy_pos[1] * self.cell_size, enemy_pos[0] * self.cell_size,
                                                 (enemy_pos[1] + 1) * self.cell_size, (enemy_pos[0] + 1) * self.cell_size,
                                                 fill="red", outline="gray")
            self.enemies.append((enemy, enemy_pos))
    
    def move_player(self, event):
        """ Move o jogador com base nas teclas pressionadas """
        if self.game_over:
            return
        
        key = event.keysym
        new_pos = self.player_pos.copy()
        
        if key == "Up" and new_pos[0] > 0:
            new_pos[0] -= 1
        elif key == "Down" and new_pos[0] < self.grid_size - 1:
            new_pos[0] += 1
        elif key == "Left" and new_pos[1] > 0:
            new_pos[1] -= 1
        elif key == "Right" and new_pos[1] < self.grid_size - 1:
            new_pos[1] += 1
        
        # Verificar se a nova posição não é um obstáculo
        if self.grid[new_pos[0]][new_pos[1]] != "obstacle":
            self.player_pos = new_pos
        
        self.update_game()
        
    def update_game(self):
        """ Atualiza a posição do jogador e dos inimigos """
        # Atualiza a posição do jogador
        self.canvas.coords(self.player, self.player_pos[1] * self.cell_size, self.player_pos[0] * self.cell_size,
                           (self.player_pos[1] + 1) * self.cell_size, (self.player_pos[0] + 1) * self.cell_size)
        
        # Verificar se o jogador foi atingido por algum inimigo
        for enemy, enemy_pos in self.enemies:
            if enemy_pos == self.player_pos:
                self.game_over_screen()
                return
        
        # Verificar se o jogador está na mesma posição de uma explosão (mas não na bomba original)
        for exp in self.explosions:
            if exp == tuple(self.player_pos) and exp != tuple(self.bombs[0]):
                self.game_over_screen()
                break
        
    def move_enemies(self):
        """ Move os inimigos em direção ao jogador """
        if self.game_over:
            return
        
        for enemy, enemy_pos in self.enemies:
            # Determinar direção do movimento do inimigo
            row_diff = self.player_pos[0] - enemy_pos[0]
            col_diff = self.player_pos[1] - enemy_pos[1]
            
            if abs(row_diff) > abs(col_diff):
                # Movimento na direção vertical
                if row_diff > 0:
                    enemy_pos[0] += 1  # Move para baixo
                elif row_diff < 0:
                    enemy_pos[0] -= 1  # Move para cima
            else:
                # Movimento na direção horizontal
                if col_diff > 0:
                    enemy_pos[1] += 1  # Move para a direita
                elif col_diff < 0:
                    enemy_pos[1] -= 1  # Move para a esquerda
            
            # Verificar se o inimigo colidiu com o jogador
            if enemy_pos == self.player_pos:
                self.game_over_screen()
                return

            # Atualizar a posição do inimigo na tela
            self.canvas.coords(enemy, enemy_pos[1] * self.cell_size, enemy_pos[0] * self.cell_size,
                               (enemy_pos[1] + 1) * self.cell_size, (enemy_pos[0] + 1) * self.cell_size)
        
        # Atualizar a movimentação a cada 'enemy_speed' ms
        self.root.after(self.enemy_speed, self.move_enemies)
        
    def place_bomb(self, event):
        """ Coloca uma bomba no local do jogador """
        if self.game_over:
            return
        
        row, col = self.player_pos
        self.bombs.append((row, col))
        
        # Criar a bomba visualmente (não afetará o jogador diretamente)
        self.canvas.create_oval(col * self.cell_size + 10, row * self.cell_size + 10,
                                (col + 1) * self.cell_size - 10, (row + 1) * self.cell_size - 10,
                                fill="red", outline="black")
        
        # Explodir após 2 segundos
        self.root.after(2000, self.explode_bomb, row, col)
        
    def explode_bomb(self, row, col):
        """ Explode a bomba, criando uma explosão sem remover obstáculos """
        # Mostrar a explosão (simples círculo)
        self.explosions.append((row, col))
        explosion = self.canvas.create_oval(col * self.cell_size + 5, row * self.cell_size + 5,
                                           (col + 1) * self.cell_size - 5, (row + 1) * self.cell_size - 5,
                                           fill="yellow", outline="black")
        
        # Explosão se espalhando para cima, para baixo, para a esquerda e para a direita
        self.create_explosion_in_direction(row - 1, col)  # Para cima
        self.create_explosion_in_direction(row + 1, col)  # Para baixo
        self.create_explosion_in_direction(row, col - 1)  # Para esquerda
        self.create_explosion_in_direction(row, col + 1)  # Para direita
        
        # Limpar a explosão após 1 segundo
        self.root.after(1000, self.clear_explosion, explosion)
        
    def create_explosion_in_direction(self, row, col):
        """ Cria a explosão em uma direção específica, sem destruir obstáculos """
        if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
            if self.grid[row][col] != "obstacle" and (row, col) != tuple(self.bombs[0]):  # Não matar o jogador na bomba
                self.canvas.create_oval(col * self.cell_size + 5, row * self.cell_size + 5,
                                        (col + 1) * self.cell_size - 5, (row + 1) * self.cell_size - 5,
                                        fill="yellow", outline="black")
        
    def clear_explosion(self, explosion):
        """ Limpar a explosão da tela """
        self.canvas.delete(explosion)
        
    def reset_game(self):
        """ Reinicia o jogo """
        self.canvas.delete("all")
        self.game_over = False
        self.player_pos = [0, 0]
        self.explosions.clear()
        self.bombs.clear()
        self.grid = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.create_grid()
        self.create_player()
        self.create_enemies()
        
    def game_over_screen(self):
        """ Exibe a tela de fim de jogo """
        self.game_over = True
        mb.showinfo("Você perdeu!", "Você foi pego pelos inimigos!")
        restart = mb.askyesno("Reiniciar", "Deseja reiniciar o jogo?")
        
        if restart:
            self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = BombermanGame(root)
    
    # Associar a tecla de espaço para colocar bomba
    root.bind("<space>", game.place_bomb)
    
    root.mainloop()
