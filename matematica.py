import random
from time import sleep

class UnidadeMatematica:
    def __init__(self, titulo, nivel):
        self.titulo = titulo
        self.nivel = nivel
        self.concluida = False

    def tutorial(self):
        self._cabecalho()
        self._explicar()
        self._demonstrar()
        self._conceituar()
        self._problema_pratico()
        self._quiz_final()
        self.concluida = True

    def _cabecalho(self):
        print(f"\n{'='*50}")
        print(f"UNIDADE: {self.titulo.upper()} (Nível {self.nivel})")
        print(f"{'='*50}")

    def _explicar(self):
        print("\n💡 EXPLICAR:")
        if "adição" in self.titulo.lower():
            print("Adição é juntar quantidades para formar um total.")
        elif "subtração" in self.titulo.lower():
            print("Subtração é remover uma quantidade de outra.")
        # Adicione outros tópicos aqui...

    def _demonstrar(self):
        print("\n✏️ DEMONSTRAR:")
        a, b = random.randint(1, 10), random.randint(1, 10)
        if "adição" in self.titulo.lower():
            print(f"Exemplo: {a} + {b} = {a + b}")
        elif "subtração" in self.titulo.lower():
            print(f"Exemplo: {a} - {b} = {a - b}")
        sleep(2)

    def _conceituar(self):
        print("\n📚 CONCEITUAR:")
        if "adição" in self.titulo.lower():
            print("Propriedades:\n- Comutativa: a + b = b + a\n- Associativa: (a + b) + c = a + (b + c)")
        elif "subtração" in self.titulo.lower():
            print("Não é comutativa:\na - b ≠ b - a (exceto quando a = b)")
        sleep(2)

    def _problema_pratico(self):
        print("\n🔎 PROBLEMA PRÁTICO:")
        if "adição" in self.titulo.lower():
            print("João tem 5 maçãs. Maria lhe dá 3 mais. Quantas maçãs ele tem agora?")
            resposta = 8
        elif "subtração" in self.titulo.lower():
            print("Uma pizza tem 8 pedaços. Se comermos 3, quantos sobram?")
            resposta = 5
        
        tentativas = 3
        while tentativas > 0:
            try:
                user_resp = int(input("Sua resposta: "))
                if user_resp == resposta:
                    print("✅ Correto!")
                    break
                else:
                    tentativas -= 1
                    print(f"❌ Errado. Tentativas restantes: {tentativas}")
            except ValueError:
                print("Digite um número!")
        
        if tentativas == 0:
            print(f"Resposta correta: {resposta}")

    def _quiz_final(self):
        print("\n🧠 QUIZ FINAL (3 questões):")
        acertos = 0
        perguntas = self._gerar_quiz()
        
        for i, (pergunta, respostas, certa) in enumerate(perguntas, 1):
            print(f"\n{i}. {pergunta}")
            for idx, opcao in enumerate(respostas, 1):
                print(f"{idx}. {opcao}")
            
            while True:
                try:
                    escolha = int(input("Sua escolha (1-3): ")) - 1
                    if 0 <= escolha < 3:
                        break
                except ValueError:
                    print("Digite 1, 2 ou 3!")
            
            if escolha == certa:
                print("✅ Acertou!")
                acertos += 1
            else:
                print(f"❌ Errado. A resposta correta é: {respostas[certa]}")
        
        print(f"\nPontuação final: {acertos}/3")

    def _gerar_quiz(self):
        if "adição" in self.titulo.lower():
            return [
                ("Quanto é 7 + 8?", ["12", "15", "10"], 1),
                ("Qual propriedade permite que 2 + 3 = 3 + 2?", ["Associativa", "Comutativa", "Distributiva"], 1),
                ("Se tenho R$12 e ganho R$5, quanto tenho?", ["R$16", "R$17", "R$15"], 1)
            ]
        elif "subtração" in self.titulo.lower():
            return [
                ("9 - 4 = ?", ["3", "5", "6"], 1),
                ("Subtração é o oposto de:", ["Multiplicação", "Divisão", "Adição"], 2),
                ("Se gasto R$7 de R$10, quanto sobra?", ["R$2", "R$3", "R$4"], 1)
            ]
        # Adicione quizzes para outros tópicos

class JogoMatematica:
    def __init__(self):
        self.unidades = [
            UnidadeMatematica("Introdução à Adição", 1),
            UnidadeMatematica("Introdução à Subtração", 1),
            # Adicione mais unidades:
            # UnidadeMatematica("Multiplicação Básica", 2),
            # UnidadeMatematica("Divisão Simples", 2),
            # UnidadeMatematica("Frações", 3)
        ]
        self.progresso = 0

    def iniciar(self):
        print("🌟 JOGO DE MATEMÁTICA DO ENSINO BÁSICO 🌟")
        print("Selecione uma unidade:")
        
        for i, unidade in enumerate(self.unidades, 1):
            status = "✓" if unidade.concluida else " "
            print(f"{i}. [{status}] {unidade.titulo} (Nível {unidade.nivel})")
        
        while True:
            try:
                escolha = int(input("\nEscolha (0 para sair): "))
                if 0 < escolha <= len(self.unidades):
                    self.unidades[escolha-1].tutorial()
                    self.progresso = sum(1 for u in self.unidades if u.concluida)
                    print(f"\nProgresso geral: {self.progresso}/{len(self.unidades)} unidades")
                    self.iniciar()
                    break
                elif escolha == 0:
                    print("Até logo!")
                    break
            except ValueError:
                print("Digite um número válido!")

# Rodar o jogo
if __name__ == "__main__":
    jogo = JogoMatematica()
    jogo.iniciar()
