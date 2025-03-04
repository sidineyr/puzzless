import tkinter as tk
import random
import time
from tkinter import messagebox
from PIL import Image, ImageTk

class CasinoHackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino Hack Game")
        
        self.level = 0
        self.patterns = []
        self.selected = {}
        
        self.create_widgets()
        self.new_round()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Memorize o padrão das estrelas", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()
        
        self.stars = []
        for i in range(6):
            row = []
            for j in range(6):
                x, y = j * 60 + 30, i * 60 + 30
                star = self.canvas.create_text(x, y, text="★", font=("Arial", 48), fill="gray")
                row.append(star)
                self.canvas.tag_bind(star, "<Button-1>", lambda event, r=i, c=j: self.select_star(r, c))
            self.stars.append(row)
        
        self.check_button = tk.Button(self.root, text="Conferir", command=self.check_pattern)
        self.check_button.pack(pady=5)
        
        self.retry_button = tk.Button(self.root, text="Tentar Novamente", command=self.retry_pattern)
        self.retry_button.pack(pady=5)
    
    def generate_pattern(self):
        pattern = set()
        used_columns = set()
        used_rows = set()
        
        while len(pattern) < 6:
            row = random.choice([r for r in range(6) if r not in used_rows])
            col = random.choice([c for c in range(6) if c not in used_columns])
            pattern.add((row, col))
            used_rows.add(row)
            used_columns.add(col)
        
        return pattern
    
    def display_pattern(self):
        self.clear_board()
        pattern = self.patterns[self.level]
        for _ in range(3):
            for i, j in pattern:
                self.canvas.itemconfig(self.stars[i][j], fill="yellow")
            self.root.update()
            time.sleep(2)
            for i, j in pattern:
                self.canvas.itemconfig(self.stars[i][j], fill="gray")
            self.root.update()
            time.sleep(0.5)
        self.selected.clear()
    
    def retry_pattern(self):
        self.display_pattern()
    
    def new_round(self):
        if self.level == 3:
            self.show_reward()
            return
        
        self.clear_board()
        
        if len(self.patterns) > self.level:
            self.patterns.pop(self.level)
        
        self.patterns.append(self.generate_pattern())
        self.display_pattern()
        self.start_timer()
    
    def clear_board(self):
        for row in self.stars:
            for star in row:
                self.canvas.itemconfig(star, fill="gray")
    
    def select_star(self, row, col):
        if row in self.selected or col in self.selected.values():
            return
        self.selected[row] = col
        self.canvas.itemconfig(self.stars[row][col], fill="yellow")
    
    def check_pattern(self):
        if set(self.selected.items()) == self.patterns[self.level]:
            messagebox.showinfo("Sucesso!", "Padrão correto! Avançando...")
            self.level += 1
            self.new_round()
        else:
            messagebox.showerror("Erro!", "Padrão incorreto! Tente novamente.")
        self.selected.clear()
        self.clear_board()
    
    def start_timer(self):
        self.time_remaining = 120000  # 120 segundos em milissegundos
        self.update_timer()
    
    def update_timer(self):
        if self.time_remaining > 0:
            minutes = self.time_remaining // 60000
            seconds = (self.time_remaining % 60000) // 1000
            milliseconds = self.time_remaining % 1000
            self.label.config(text=f"Tempo restante: {minutes}m {seconds}s {milliseconds}ms")
            self.time_remaining -= 100
            self.root.after(100, self.update_timer)
        else:
            messagebox.showerror("Tempo esgotado!", "Você não conseguiu preencher o padrão a tempo.")
            self.level = 0
            self.patterns.clear()
            self.new_round()
    
    def show_reward(self):
        self.canvas.delete("all")
        img = Image.open("pineapple.png")
        img = img.resize((200, 200), Image.LANCZOS)
        self.pineapple_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(200, 200, image=self.pineapple_img)
        messagebox.showinfo("Parabéns!", "Você venceu!")

if __name__ == "__main__":
    root = tk.Tk()
    game = CasinoHackGame(root)
    root.mainloop()
