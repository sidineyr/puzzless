const ROWS = 10; // Número de linhas da grade
const COLS = 20; // Número de colunas da grade
const BALL = 'O'; // Caractere que representa a bola
const EMPTY = ' '; // Caractere que representa espaço vazio

let ballPosition = { x: 0, y: 0 }; // Posição inicial da bola
let gameInterval;

// Função para criar a grade
function createGrid() {
    const grid = [];
    for (let i = 0; i < ROWS; i++) {
        grid.push(Array(COLS).fill(EMPTY));
    }
    return grid;
}

// Função para exibir a grade no console
function renderGrid(grid) {
    const gameBoard = document.getElementById('game-board');
    gameBoard.textContent = grid.map(row => row.join('')).join('\n');
}

// Função para mover a bola aleatoriamente
function moveBall(grid) {
    // Remove a bola da posição atual
    grid[ballPosition.y][ballPosition.x] = EMPTY;

    // Move a bola em uma direção aleatória
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

// Função principal do jogo
function startGame() {
    const grid = createGrid();
    ballPosition = { x: Math.floor(COLS / 2), y: Math.floor(ROWS / 2) }; // Posição inicial da bola no centro
    grid[ballPosition.y][ballPosition.x] = BALL;

    // Renderiza a grade inicial
    renderGrid(grid);

    // Inicia o loop do jogo
    if (gameInterval) clearInterval(gameInterval);
    gameInterval = setInterval(() => {
        moveBall(grid);
        renderGrid(grid);
    }, 500); // Atualiza a cada 500ms
}
