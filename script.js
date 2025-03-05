const ROWS = 6;
const COLS = 6;
const TOTAL_CELLS = ROWS * COLS;
const DISPLAY_TIME = 2000; // 2 segundos

let gameBoard;
let pattern = [];
let userAttempts = 0;
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
    }, DISPLAY_TIME);
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
            if (userAttempts === 3) {
                showTreasure();
            } else {
                startGame();
            }
        }
    } else {
        cell.classList.add('error');
        cell.textContent = '⭐';
        showPattern();
    }
}

// Função para exibir o tesouro
function showTreasure() {
    const message = document.getElementById('message');
    message.innerHTML = '<img src="assets/pineapple.png" alt="Tesouro">';
}

// Função para reiniciar o jogo
function restartGame() {
    userAttempts = 0;
    createGameBoard();
    generatePattern();
    showPattern();
}

// Função para iniciar um novo padrão
function newPattern() {
    userAttempts = 0;
    createGameBoard();
    generatePattern();
    showPattern();
}

// Eventos dos botões
document.getElementById('restart-button').addEventListener('click', restartGame);
document.getElementById('new-pattern-button').addEventListener('click', newPattern);

// Iniciar o jogo ao carregar a página
window.onload = restartGame;
