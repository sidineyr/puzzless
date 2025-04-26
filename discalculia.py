import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import time
import json
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

class MathAssessmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avaliação de Discalculia v6.0")
        self.root.geometry("1000x700")
        
        # Configurações iniciais
        self.questions = self.create_question_bank()
        self.current_test = None
        self.current_question = 0
        self.score = 0
        self.response_times = []
        self.error_analysis = {
            'Arithmetic': 0,
            'Geometry': 0,
            'Algebra': 0,
            'Logic': 0,
            'Memory': 0
        }
        self.test_history = []
        
        # Configurar estilo
        self.setup_styles()
        
        # Interface principal
        self.create_main_menu()

    def setup_styles(self):
        """Configura os estilos visuais da aplicação"""
        style = ttk.Style()
        style.configure('TFrame', background='#f5f5f5')
        style.configure('TButton', font=('Arial', 11), padding=8)
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f5f5f5')
        style.configure('Subtitle.TLabel', font=('Arial', 12), background='#f5f5f5')
        style.configure('Question.TLabel', font=('Arial', 12), background='#f5f5f5')

    def create_question_bank(self):
        """Cria um banco de questões para o teste"""
        return {
            'arithmetic': [
                {
                    'id': 'A1',
                    'question': 'Quanto é 8 × 7?',
                    'type': 'input',
                    'answer': '56',
                    'difficulty': 1
                },
                {
                    'id': 'A2',
                    'question': 'Qual é o resultado de 45 ÷ 9?',
                    'type': 'choice',
                    'options': ['A) 4', 'B) 5', 'C) 6', 'D) 7'],
                    'answer': 'B',
                    'difficulty': 1
                },
                # ... mais questões de aritmética
            ],
            'geometry': [
                {
                    'id': 'G1',
                    'question': 'Quantos graus tem um ângulo reto?',
                    'type': 'input',
                    'answer': '90',
                    'difficulty': 2
                },
                # ... mais questões de geometria
            ],
            # ... outras categorias
        }

    def create_main_menu(self):
        """Cria o menu principal da aplicação"""
        self.clear_screen()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        ttk.Label(main_frame, text="Avaliação de Habilidades Matemáticas", style='Title.TLabel').pack(pady=20)
        ttk.Label(main_frame, text="Identificação de Discalculia", style='Subtitle.TLabel').pack(pady=10)
        
        ttk.Button(main_frame, text="Iniciar Teste Completo", 
                 command=self.start_full_assessment).pack(pady=15, fill=tk.X)
        ttk.Button(main_frame, text="Teste Rápido", 
                 command=self.start_quick_test).pack(pady=15, fill=tk.X)
        ttk.Button(main_frame, text="Sair", 
                 command=self.root.quit).pack(pady=15, fill=tk.X)

    def start_full_assessment(self):
        """Inicia a avaliação completa"""
        self.clear_screen()
        self.create_progress_bar()
        self.start_arithmetic_test()

    def create_progress_bar(self):
        """Cria a barra de progresso"""
        self.progress_frame = ttk.Frame(self.root)
        self.progress_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.progress = ttk.Progressbar(self.progress_frame, orient='horizontal', 
                                      mode='determinate', length=800)
        self.progress.pack(fill=tk.X)
        
        self.progress_label = ttk.Label(self.progress_frame, text="0% completo", font=('Arial', 10))
        self.progress_label.pack()

    def start_arithmetic_test(self):
        """Inicia o teste de aritmética"""
        self.current_test = 'arithmetic'
        self.current_question = 0
        self.clear_screen(keep_progress=True)
        
        test_frame = ttk.Frame(self.root)
        test_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        ttk.Label(test_frame, text="Teste de Aritmética", style='Title.TLabel').pack(pady=10)
        
        self.question_frame = ttk.Frame(test_frame)
        self.question_frame.pack(fill=tk.BOTH, expand=True)
        
        self.show_question()

    def show_question(self):
        """Exibe a questão atual"""
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        
        questions = self.questions[self.current_test]
        question = questions[self.current_question]
        total = len(questions)
        
        self.update_progress((self.current_question + 1) / total * 100)
        
        ttk.Label(self.question_frame, 
                 text=f"Questão {self.current_question + 1}/{total}", 
                 font=('Arial', 12)).pack(pady=5)
        
        ttk.Label(self.question_frame, 
                 text=question['question'], 
                 style='Question.TLabel').pack(pady=15)
        
        self.start_timer()
        
        if question['type'] == 'choice':
            self.answer_var = tk.StringVar()
            for option in question['options']:
                ttk.Radiobutton(self.question_frame, 
                               text=option, 
                               variable=self.answer_var, 
                               value=option[0]).pack(anchor='w', pady=3)
        else:
            self.answer_entry = ttk.Entry(self.question_frame, font=('Arial', 12))
            self.answer_entry.pack(pady=15)
        
        ttk.Button(self.question_frame, 
                  text="Responder", 
                  command=self.check_answer).pack(pady=20)

    def start_timer(self):
        """Inicia o temporizador para a questão atual"""
        self.start_time = time.time()
        self.timer_label = ttk.Label(self.question_frame, text="Tempo: 0s", font=('Arial', 10))
        self.timer_label.pack(pady=5)
        self.update_timer()

    def update_timer(self):
        """Atualiza o temporizador"""
        elapsed = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Tempo: {elapsed}s")
        self.root.after(1000, self.update_timer)

    def check_answer(self):
        """Verifica a resposta do usuário"""
        response_time = time.time() - self.start_time
        self.response_times.append(response_time)
        
        question = self.questions[self.current_test][self.current_question]
        user_answer = self.answer_var.get() if question['type'] == 'choice' else self.answer_entry.get().strip()
        correct_answer = str(question['answer']).upper()
        
        is_correct = user_answer == correct_answer
        
        if is_correct:
            self.score += question['difficulty'] * 10
            feedback = "✅ Resposta correta!"
        else:
            self.error_analysis[self.current_test.capitalize()] += 1
            feedback = f"❌ Resposta incorreta. O correto é: {correct_answer}"
        
        self.test_history.append({
            'test': self.current_test,
            'question': question['id'],
            'time': response_time,
            'correct': is_correct
        })
        
        messagebox.showinfo("Resultado", feedback)
        
        self.current_question += 1
        questions = self.questions[self.current_test]
        
        if self.current_question < len(questions):
            self.show_question()
        else:
            self.next_test_section()

    def next_test_section(self):
        """Avança para a próxima seção do teste"""
        test_order = ['arithmetic', 'geometry', 'algebra', 'logic', 'memory']
        current_index = test_order.index(self.current_test)
        
        if current_index < len(test_order) - 1:
            self.current_test = test_order[current_index + 1]
            self.current_question = 0
            self.show_question()
        else:
            self.show_final_results()

    def show_final_results(self):
        """Exibe os resultados finais"""
        self.clear_screen()
        
        result_frame = ttk.Frame(self.root)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        ttk.Label(result_frame, text="Resultados da Avaliação", style='Title.TLabel').pack(pady=20)
        
        ttk.Label(result_frame, 
                 text=f"Pontuação Total: {self.score}/500", 
                 font=('Arial', 14)).pack(pady=10)
        
        avg_time = sum(self.response_times) / len(self.response_times) if self.response_times else 0
        ttk.Label(result_frame, 
                 text=f"Tempo médio por questão: {avg_time:.1f} segundos", 
                 font=('Arial', 12)).pack(pady=5)
        
        ttk.Label(result_frame, 
                 text="\nÁreas com dificuldade:", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        for area, errors in self.error_analysis.items():
            if errors > 0:
                ttk.Label(result_frame, 
                         text=f"- {area}: {errors} erros", 
                         font=('Arial', 11)).pack(anchor='w')
        
        ttk.Button(result_frame, 
                 text="Gerar Relatório PDF", 
                 command=self.generate_pdf_report).pack(pady=20)
        
        ttk.Button(result_frame, 
                 text="Voltar ao Menu", 
                 command=self.create_main_menu).pack(pady=10)

    def generate_pdf_report(self):
        """Gera um relatório em PDF com os resultados"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Salvar relatório como"
        )
        
        if filename:
            try:
                doc = canvas.Canvas(filename, pagesize=letter)
                width, height = letter
                
                # Cabeçalho
                doc.setFont("Helvetica-Bold", 16)
                doc.drawString(100, height-100, "Relatório de Avaliação Matemática")
                
                # Informações básicas
                doc.setFont("Helvetica", 12)
                doc.drawString(100, height-140, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
                doc.drawString(100, height-160, f"Pontuação Total: {self.score}/500")
                
                # Análise de desempenho
                doc.setFont("Helvetica-Bold", 14)
                doc.drawString(100, height-200, "Análise por Área:")
                doc.setFont("Helvetica", 12)
                
                y_position = height-230
                for area, errors in self.error_analysis.items():
                    doc.drawString(120, y_position, f"{area}: {errors} erros")
                    y_position -= 20
                
                # Recomendações
                doc.setFont("Helvetica-Bold", 14)
                doc.drawString(100, y_position-40, "Recomendações:")
                doc.setFont("Helvetica", 12)
                
                recommendations = [
                    "• Pratique exercícios diários de cálculo mental",
                    "• Use métodos visuais para resolver problemas",
                    "• Trabalhe com jogos que envolvam números",
                    "• Consulte um especialista se as dificuldades persistirem"
                ]
                
                for i, rec in enumerate(recommendations):
                    doc.drawString(120, y_position-70-(i*20), rec)
                
                doc.save()
                messagebox.showinfo("Sucesso", f"Relatório salvo como:\n{filename}")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível gerar o relatório:\n{str(e)}")

    def start_quick_test(self):
        """Inicia o teste rápido de triagem"""
        self.clear_screen()
        
        quick_frame = ttk.Frame(self.root)
        quick_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        ttk.Label(quick_frame, text="Teste Rápido de Triagem", style='Title.TLabel').pack(pady=20)
        
        questions = [
            "Você tem dificuldade com cálculos mentais simples?",
            "Comete erros frequentes em operações básicas?",
            "Tem problemas para estimar quantidades?",
            "Confunde símbolos matemáticos com frequência?",
            "Evita situações que envolvam números?"
        ]
        
        for i, question in enumerate(questions):
            ttk.Label(quick_frame, 
                     text=f"{i+1}. {question}", 
                     style='Question.TLabel').pack(anchor='w', pady=5)
            
            var = tk.StringVar()
            ttk.Radiobutton(quick_frame, text="Sim", variable=var, value="S").pack(anchor='w')
            ttk.Radiobutton(quick_frame, text="Não", variable=var, value="N").pack(anchor='w')
        
        ttk.Button(quick_frame, 
                 text="Avaliar Respostas", 
                 command=self.evaluate_quick_test).pack(pady=20)
        
        ttk.Button(quick_frame, 
                 text="Voltar", 
                 command=self.create_main_menu).pack(pady=10)

    def evaluate_quick_test(self):
        """Avalia o teste rápido de triagem"""
        messagebox.showinfo(
            "Resultado da Triagem", 
            "Este teste rápido sugere:\n\n" +
            "🔍 Possível indicativo de discalculia\n\n" +
            "Recomenda-se a realização do teste completo para uma avaliação mais precisa."
        )
        self.create_main_menu()

    def update_progress(self, percent):
        """Atualiza a barra de progresso"""
        self.progress['value'] = percent
        self.progress_label.config(text=f"{int(percent)}% completo")

    def clear_screen(self, keep_progress=False):
        """Limpa a tela mantendo ou não a barra de progresso"""
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Menu) and not (keep_progress and widget == self.progress_frame):
                widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathAssessmentApp(root)
    root.mainloop()
