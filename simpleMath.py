import tkinter as tk
import random
import time

class MemorizacaoJogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Memorização de Adição e Subtração")
        
        self.parcelas = []
        self.nivel = 2  # Começa com duas parcelas
        self.pontuacao = 0
        self.tempo_inicio = time.time()
        
        self.label_tempo = tk.Label(root, text="Tempo: 0s", font=("Arial", 14))
        self.label_tempo.pack(pady=5)
        
        self.label_pontuacao = tk.Label(root, text="Pontuação: 0", font=("Arial", 14))
        self.label_pontuacao.pack(pady=5)
        
        self.label_expressao = tk.Label(root, text="", font=("Arial", 16))
        self.label_expressao.pack(pady=20)
        
        self.entry_resposta = tk.Entry(root, font=("Arial", 14))
        self.entry_resposta.pack(pady=10)
        self.entry_resposta.bind("<Return>", lambda event: self.verificar_resposta())  # Ativar Enter
        
        self.botao_confirmar = tk.Button(root, text="Confirmar", command=self.verificar_resposta)
        self.botao_confirmar.pack(pady=10)
        
        self.botao_desistir = tk.Button(root, text="Desistir", command=self.finalizar_jogo, fg="red")
        self.botao_desistir.pack(pady=10)
        
        self.label_feedback = tk.Label(root, text="", font=("Arial", 14))
        self.label_feedback.pack(pady=10)
        
        self.atualizar_tempo()
        self.gerar_expressao()
    
    def gerar_expressao(self):
        self.parcelas = [random.randint(-20, 20) for _ in range(self.nivel)]
        expressao = " + ".join(map(str, self.parcelas)).replace("+ -", "- ")
        self.label_expressao.config(text=expressao)
        self.entry_resposta.delete(0, tk.END)
    
    def verificar_resposta(self):
        try:
            resposta_usuario = int(self.entry_resposta.get())
        except ValueError:
            self.label_feedback.config(text="Digite um número válido!", fg="red")
            return
        
        if resposta_usuario == sum(self.parcelas):
            self.label_feedback.config(text="Correto!", fg="green")
            self.nivel += 1  # Aumenta o nível
            self.pontuacao += 10  # Aumenta pontuação
            self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
        else:
            self.label_feedback.config(text=f"Errado! Resposta correta: {sum(self.parcelas)}", fg="red")
            self.nivel = 2  # Reinicia
            self.pontuacao = 0  # Zera pontuação
            self.label_pontuacao.config(text="Pontuação: 0")
        
        self.root.after(1500, self.gerar_expressao)  # Gera nova expressão após 1.5s
    
    def atualizar_tempo(self):
        tempo_decorrido = int(time.time() - self.tempo_inicio)
        self.label_tempo.config(text=f"Tempo: {tempo_decorrido}s")
        self.root.after(1000, self.atualizar_tempo)
    
    def finalizar_jogo(self):
        tempo_total = int(time.time() - self.tempo_inicio)
        self.label_feedback.config(text=f"Jogo finalizado! Pontuação final: {self.pontuacao} em {tempo_total}s", fg="blue")
        self.botao_confirmar.config(state=tk.DISABLED)
        self.botao_desistir.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    jogo = MemorizacaoJogo(root)
    root.mainloop()
