const ROWS = 10; // Número de linhas da grade
const COLS = 20; // Número de colunas da grade
const BALL = 'O'; // Caractere que representa a bola
const EMPTY = ' '; // Caractere que representa espaço vazio

let ballPosition = { x: 0, y: 0 }; // Posição da bola
let grid; // Grade do jogo
let gameInterval; // Intervalo do jogo

// Função para criar a grade
function createGrid() {
    const grid = [];
    for (let i = 0; i < ROWS; i++) {
        grid.push(Array(COLS).fill(EMPTY));
    }
    return grid;
}

// Função para exibir a grade no console
function renderGrid() {
    const gameBoard = document.getElementById('game-board');
    gameBoard.textContent = grid.map(row => row.join('')).join('\n');
}

// Função para mover a bola aleatoriamente
function moveBall() {
    // Remove a bola da posição atual
    grid[ballPosition.y][ballPosition.x] = EMPTY;

    // Escolhe uma direção aleatória
    const direction = Math.floor(Math.random() * 4); // 0: cima, 1: baixo, 2: esquerda, 3: direita
    switch (direction) {
        case 0: // Cima
            ballPosition.y = Math.max(0, ballPosition.y - 1);
            break;
        case 1: // Baixo
            ballPosition.y = Math.min(ROWS - 1, ballPosition.y + 1);
            break;
        case 2: // Esquerda
            ballPosition.x = Math.max(0, ballPosition.x - 1);
            break;
        case 3: // Direita
            ballPosition.x = Math.min(COLS - 1, ballPosition.x + 1);
            break;
    }

    // Coloca a bola na nova posição
    grid[ballPosition.y][ballPosition.x] = BALL;
}

// Função para iniciar o jogo
function startGame() {
    // Cria a grade e posiciona a bola aleatoriamente
    grid = createGrid();
    ballPosition = { x: Math.floor(Math.random() * COLS), y: Math.floor(Math.random() * ROWS) };
    grid[ballPosition.y][ballPosition.x] = BALL;

    // Renderiza a grade inicial
    renderGrid();

    // Inicia o loop do jogo
    if (gameInterval) clearInterval(gameInterval); // Limpa qualquer intervalo existente
    gameInterval = setInterval(() => {
        moveBall();
        renderGrid();
    }, 500); // Atualiza a cada 500ms (0.5 segundos)
}

// Função para pausar o jogo
function pauseGame() {
    if (gameInterval) {
        clearInterval(gameInterval);
        gameInterval = null;
    }
}

// Função para reiniciar o jogo
function resetGame() {
    pauseGame(); // Pausa o jogo atual
    startGame(); // Reinicia o jogo
}

// Inicializa o jogo ao carregar a página
window.onload = () => {
    // Adiciona os botões e seus eventos
    document.getElementById('start-button').addEventListener('click', startGame);
    document.getElementById('pause-button').addEventListener('click', pauseGame);
    document.getElementById('reset-button').addEventListener('click', resetGame);

    // Inicia o jogo automaticamente
    startGame();
};
