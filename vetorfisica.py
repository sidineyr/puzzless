import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import ipywidgets as widgets
from IPython.display import display, clear_output
import time

class AventuraVetorial:
    def __init__(self):
        # Configurações iniciais
        self.nivel_atual = 1
        self.pontuacao = 0
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        plt.close()  # Evita exibição duplicada no Jupyter Notebook
        
    def iniciar_jogo(self):
        """Roda a introdução e inicia o jogo."""
        print("===== AVENTURA VETORIAL =====")
        print("\nVocê está em uma missão para dominar os vetores na Física!")
        print("Complete desafios, responda quizzes e avance de nível.\n")
        self.mostrar_explicacao_inicial()
    
    def mostrar_explicacao_inicial(self):
        """Introdução conceitual com visualização."""
        print("\n💡 **O que é um vetor?**")
        print("Um vetor é uma grandeza que possui:")
        print("- Módulo (tamanho)")
        print("- Direção (linha de ação)")
        print("- Sentido (para onde aponta)")
        
        # Visualização gráfica de um vetor
        self.fig, self.ax = plt.subplots()
        self.ax.quiver(0, 0, 3, 2, angles='xy', scale_units='xy', scale=1, color='r', label='Vetor A (3,2)')
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.grid(True)
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        self.ax.set_title("Visualização de um Vetor no Plano XY")
        self.ax.legend()
        plt.show()
        
        input("\nPressione Enter para continuar...")
        self.quiz_nivel_1()
    
    def quiz_nivel_1(self):
        """Quiz básico sobre conceitos iniciais."""
        print("\n=== QUIZ NÍVEL 1 (BÁSICO) ===")
        perguntas = [
            {
                "pergunta": "Um vetor tem:",
                "opcoes": ["A) Apenas módulo", "B) Módulo e direção", "C) Módulo, direção e sentido", "D) Apenas direção"],
                "resposta": "C"
            },
            {
                "pergunta": "Se um vetor tem componentes (4, 3), seu módulo é:",
                "opcoes": ["A) 5", "B) 7", "C) 12", "D) 1"],
                "resposta": "A"
            }
        ]
        
        for p in perguntas:
            print(f"\n{p['pergunta']}")
            for opcao in p["opcoes"]:
                print(opcao)
            resposta = input("Resposta (A/B/C/D): ").upper()
            
            if resposta == p["resposta"]:
                print("✅ Correto! +10 pontos")
                self.pontuacao += 10
            else:
                print(f"❌ Errado! A resposta correta era {p['resposta']}")
        
        self.avancar_nivel()
    
    def avancar_nivel(self):
        """Passa para o próximo nível ou finaliza o jogo."""
        self.nivel_atual += 1
        
        if self.nivel_atual == 2:
            print("\n🌟 Parabéns! Você avançou para o Nível 2 (Intermediário)!")
            self.mostrar_explicacao_soma_vetores()
        elif self.nivel_atual == 3:
            print("\n🚀 Incrível! Agora você está no Nível 3 (Avançado)!")
            self.mostrar_explicacao_produto_escalar()
        else:
            self.finalizar_jogo()
    
    def mostrar_explicacao_soma_vetores(self):
        """Demonstra a soma vetorial graficamente."""
        print("\n📐 **Soma de Vetores**")
        print("A soma de vetores segue a regra do paralelogramo ou do polígono.")
        
        # Visualização da soma
        A = np.array([2, 3])
        B = np.array([3, -1])
        C = A + B
        
        self.fig, self.ax = plt.subplots()
        self.ax.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vetor A')
        self.ax.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vetor B')
        self.ax.quiver(0, 0, C[0], C[1], angles='xy', scale_units='xy', scale=1, color='g', label='A + B')
        self.ax.set_xlim(-1, 6)
        self.ax.set_ylim(-2, 4)
        self.ax.grid(True)
        self.ax.legend()
        plt.show()
        
        input("\nPressione Enter para continuar...")
        self.quiz_nivel_2()
    
    def quiz_nivel_2(self):
        """Quiz intermediário sobre soma vetorial."""
        print("\n=== QUIZ NÍVEL 2 (INTERMEDIÁRIO) ===")
        perguntas = [
            {
                "pergunta": "Se A = (1, 2) e B = (3, -1), qual é A + B?",
                "opcoes": ["A) (4, 1)", "B) (3, 2)", "C) (2, 3)", "D) (1, -1)"],
                "resposta": "A"
            },
            {
                "pergunta": "A subtração de vetores é equivalente a:",
                "opcoes": ["A) Somar o oposto", "B) Multiplicar os módulos", "C) Dividir os vetores", "D) Nenhuma das anteriores"],
                "resposta": "A"
            }
        ]
        
        for p in perguntas:
            print(f"\n{p['pergunta']}")
            for opcao in p["opcoes"]:
                print(opcao)
            resposta = input("Resposta (A/B/C/D): ").upper()
            
            if resposta == p["resposta"]:
                print("✅ Correto! +20 pontos")
                self.pontuacao += 20
            else:
                print(f"❌ Errado! A resposta correta era {p['resposta']}")
        
        self.avancar_nivel()
    
    def finalizar_jogo(self):
        """Encerra o jogo e mostra a pontuação."""
        print("\n=== FIM DO JOGO ===")
        print(f"Pontuação final: {self.pontuacao} pontos")
        if self.pontuacao >= 50:
            print("🎉 Excelente! Você domina os vetores!")
        elif self.pontuacao >= 30:
            print("👍 Bom trabalho! Continue praticando!")
        else:
            print("📚 Revise os conceitos e tente novamente!")

# Inicia o jogo
if __name__ == "__main__":
    jogo = AventuraVetorial()
    jogo.iniciar_jogo()
