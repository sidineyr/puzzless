const ROWS = 6;
const COLS = 6;
const TOTAL_CELLS = ROWS * COLS;
const MAX_ATTEMPTS = 3;
const DISPLAY_TIME = 2000; // 2 segundos
const GAME_TIME = 120000; // 2 minutos

let gameBoard;
let pattern = [];
let userAttempts = 0;
let gameInterval;
let isShowingPattern = false;

// Função para criar a grade do jogo
function createGameBoard() {
    gameBoard = document.getElementById('game-board');
    gameBoard.innerHTML = '';
    for (let i = 0; i < TOTAL_CELLS; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.index = i;
        cell.addEventListener('click', () => selectCell(i));
        gameBoard.appendChild(cell);
    }
}

// Função para gerar um padrão aleatório
function generatePattern() {
    pattern = [];
    const usedRows = new Set();
    const usedCols = new Set();

    while (pattern.length < ROWS) {
        const row = Math.floor(Math.random() * ROWS);
        const col = Math.floor(Math.random() * COLS);

        if (!usedRows.has(row) && !usedCols.has(col)) {
            pattern.push({ row, col });
            usedRows.add(row);
            usedCols.add(col);
        }
    }
}

// Função para exibir o padrão
function showPattern() {
    isShowingPattern = true;
    pattern.forEach(({ row, col }) => {
        const index = row * COLS + col;
        const cell = gameBoard.children[index];
        cell.textContent = '⭐';
    });

    setTimeout(() => {
        pattern.forEach(({ row, col }) => {
            const index = row * COLS + col;
            const cell = gameBoard.children[index];
            cell.textContent = '';
        });
        isShowingPattern = false;
        startGame();
    }, DISPLAY_TIME);
}

// Função para iniciar o jogo
function startGame() {
    userAttempts = 0;
    createGameBoard();
    generatePattern();
    showPattern();

    setTimeout(() => {
        endGame();
    }, GAME_TIME);
}

// Função para selecionar uma célula
function selectCell(index) {
    if (isShowingPattern) return;

    const cell = gameBoard.children[index];
    const row = Math.floor(index / COLS);
    const col = index % COLS;

    const isCorrect = pattern.some(({ row: pRow, col: pCol }) => pRow === row && pCol === col);

    if (isCorrect) {
        cell.classList.add('selected');
        cell.textContent = '⭐';
        userAttempts++;

        if (userAttempts === pattern.length) {
            if (userAttempts === MAX_ATTEMPTS) {
                showTreasure();
            } else {
                startGame();
            }
        }
    } else {
        endGame();
    }
}

// Função para exibir o tesouro
function showTreasure() {
    const message = document.getElementById('message');
    message.innerHTML = '<img src="pineapple.png" alt="Tesouro">';
}

// Função para finalizar o jogo
function endGame() {
    clearInterval(gameInterval);
    const message = document.getElementById('message');
    message.textContent = 'Fim do jogo! Tente novamente.';
}

// Eventos dos botões
document.getElementById('restart-button').addEventListener('click', startGame);
document.getElementById('show-pattern-button').addEventListener('click', showPattern);
document.getElementById('exit-button').addEventListener('click', () => {
    alert('Recomendamos que você faça mais exercícios para melhorar sua capacidade de memorização!');
    window.close();
});

// Iniciar o jogo ao carregar a página
window.onload = startGame;
