import pygame
import math
import sys

# Inicialização
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Funções Trigonométricas")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 22)
big_font = pygame.font.SysFont('Arial', 28, bold=True)

# Cores
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
RED = (255, 80, 80)
BLUE = (100, 100, 255)
ORANGE = (255, 165, 0)
PURPLE = (180, 80, 200)
GREEN = (80, 200, 120)
CYAN = (80, 220, 255)
LIGHT_GRAY = (240, 240, 240)

# Arco-íris (cores do prisma)
RAINBOW_COLORS = [
    (255, 0, 0),     # Vermelho
    (255, 127, 0),   # Laranja
    (255, 255, 0),   # Amarelo
    (0, 255, 0),     # Verde
    (0, 0, 255),     # Azul
    (75, 0, 130),    # Anil
    (148, 0, 211),   # Violeta
]

# Coordenadas do centro e raio
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 250

# Lista de funções e cores
functions = [
    ("sen(θ)", RED),
    ("cos(θ)", BLUE),
    ("tan(θ)", ORANGE),
    ("cotg(θ)", PURPLE),
    ("sec(θ)", GREEN),
    ("cosec(θ)", CYAN),
]

# Frase final
final_quote_lines = [
    "“Matemática é a linguagem com que Deus,",
    "escreveu o universo.”",
    "— Galileu Galilei"
]

def draw_grid():
    spacing = 25
    for x in range(0, WIDTH, spacing):
        pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, spacing):
        pygame.draw.line(screen, LIGHT_GRAY, (0, y), (WIDTH, y))

def draw_cartesian_plane():
    pygame.draw.line(screen, BLACK, (0, CENTER[1]), (WIDTH, CENTER[1]), 2)
    pygame.draw.line(screen, BLACK, (CENTER[0], 0), (CENTER[0], HEIGHT), 2)

def draw_circle_unitario():
    pygame.draw.circle(screen, GRAY, CENTER, RADIUS, 1)

def draw_triangle_and_functions(theta, current_fn):
    x = math.cos(theta)
    y = math.sin(theta)
    px = CENTER[0] + x * RADIUS
    py = CENTER[1] - y * RADIUS

    pygame.draw.line(screen, BLACK, CENTER, (px, py), 2)

    label = None

    if current_fn == 0:
        pygame.draw.line(screen, RED, (px, CENTER[1]), (px, py), 4)
        label = font.render(f"sen(θ) = {round(y, 2)}", True, RED)
    elif current_fn == 1:
        pygame.draw.line(screen, BLUE, (CENTER[0], py), (px, py), 4)
        label = font.render(f"cos(θ) = {round(x, 2)}", True, BLUE)
    elif current_fn == 2:
        try:
            tan = math.tan(theta)
            tx = CENTER[0] + RADIUS
            ty = CENTER[1] - tan * RADIUS
            pygame.draw.line(screen, ORANGE, (CENTER[0] + RADIUS, CENTER[1]), (tx, ty), 4)
            label = font.render(f"tan(θ) = {round(tan, 2)}", True, ORANGE)
        except:
            pass
    elif current_fn == 3:
        try:
            cot = 1 / math.tan(theta)
            tx = CENTER[0] + cot * RADIUS
            pygame.draw.line(screen, PURPLE, (CENTER[0], CENTER[1]), (tx, CENTER[1] - RADIUS), 4)
            label = font.render(f"cotg(θ) = {round(cot, 2)}", True, PURPLE)
        except:
            pass
    elif current_fn == 4:
        try:
            sec = 1 / math.cos(theta)
            sec_x = CENTER[0] + sec * RADIUS
            pygame.draw.line(screen, GREEN, CENTER, (sec_x, CENTER[1]), 4)
            label = font.render(f"sec(θ) = {round(sec, 2)}", True, GREEN)
        except:
            pass
    elif current_fn == 5:
        try:
            cosec = 1 / math.sin(theta)
            cosec_y = CENTER[1] - cosec * RADIUS
            pygame.draw.line(screen, CYAN, CENTER, (CENTER[0], cosec_y), 4)
            label = font.render(f"cosec(θ) = {round(cosec, 2)}", True, CYAN)
        except:
            pass

    if label:
        screen.blit(label, (20, 20))

def draw_quote():
    for i, line in enumerate(final_quote_lines):
        text = big_font.render(line, True, BLACK)
        screen.blit(text, (20, HEIGHT - 100 + i * 30))

# Variáveis de controle
theta = 0
function_index = 0
trail_points = []

# Loop principal
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    draw_grid()
    draw_cartesian_plane()
    draw_circle_unitario()

    # Cálculo do ponto atual
    x = math.cos(theta)
    y = math.sin(theta)
    px = CENTER[0] + x * RADIUS
    py = CENTER[1] - y * RADIUS

    # Atualiza e armazena trilha
    trail_points.append((px, py))
    if len(trail_points) > 1000:
        trail_points.pop(0)

    # Desenha a linha arco-íris
    if len(trail_points) > 1:
        for i in range(1, len(trail_points)):
            color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
            pygame.draw.line(screen, color, trail_points[i - 1], trail_points[i], 2)

    draw_triangle_and_functions(theta, function_index)
    draw_quote()

    theta += 0.01
    if theta > 2 * math.pi:
        theta = 0
        function_index = (function_index + 1) % len(functions)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
