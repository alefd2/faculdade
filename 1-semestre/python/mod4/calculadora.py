import tkinter as tk

def clicar(botao):
    if botao == "=":
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    elif botao == "C":
        entrada.delete(0, tk.END)
    else:
        entrada.insert(tk.END, botao)

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Bonita")
janela.configure(bg="#222")  # Fundo da janela
janela.resizable(False, False)

# Caixa de entrada
entrada = tk.Entry(janela, font=("Arial", 20), bg="#333", fg="white", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Botões
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

linha = 1
coluna = 0
for botao in botoes:
    cor_fundo = "#555" if botao not in ["C", "="] else "#FF5733"
    cor_texto = "white"
    tk.Button(
        janela, text=botao, font=("Arial", 18), bg=cor_fundo, fg=cor_texto,
        width=5, height=2, command=lambda b=botao: clicar(b)
    ).grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Iniciar a interface
janela.mainloop()
