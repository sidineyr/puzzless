document.addEventListener("DOMContentLoaded", () => {
    const matrixContainer = document.getElementById("matrix-container");
    const message = document.getElementById("message");
    const prize = document.getElementById("prize");
    let correctCells = [];
    let userAttempts = 0;
    let correctAttempts = 0;

    // Função para criar a matriz 6x6
    function createMatrix() {
        matrixContainer.innerHTML = "";
        correctCells = [];
        let usedColumns = new Set();

        for (let row = 0; row < 6; row++) {
            let col;
            do {
                col = Math.floor(Math.random() * 6);
            } while (usedColumns.has(col));
            usedColumns.add(col);
            correctCells.push({ row, col });
        }

        for (let row = 0; row < 6; row++) {
            for (let col = 0; col < 6; col++) {
                const cell = document.createElement("div");
                cell.classList.add("cell");
                cell.dataset.row = row;
                cell.dataset.col = col;
                matrixContainer.appendChild(cell);
            }
        }
    }

    // Função para exibir os círculos nas células corretas
    function showCircles() {
        correctCells.forEach(({ row, col }) => {
            const cell = document.querySelector(`.cell[data-row="${row}"][data-col="${col}"]`);
            cell.classList.add("circle");
        });
    }

    // Função para ocultar os círculos
    function hideCircles() {
        correctCells.forEach(({ row, col }) => {
            const cell = document.querySelector(`.cell[data-row="${row}"][data-col="${col}"]`);
            cell.classList.remove("circle");
        });
    }

    // Função para piscar os círculos
    function blinkCircles() {
        let blinkCount = 0;
        const interval = setInterval(() => {
            if (blinkCount % 2 === 0) {
                showCircles();
            } else {
                hideCircles();
            }
            blinkCount++;
            if (blinkCount >= 6) {
                clearInterval(interval);
                hideCircles();
                startUserInput();
            }
        }, 500); // Pisca a cada 500ms (3 vezes em 2 segundos)
    }

    // Função para iniciar a entrada do usuário
    function startUserInput() {
        message.textContent = "Marque as células com círculos!";
        let selectedCells = [];

        matrixContainer.querySelectorAll(".cell").forEach(cell => {
            cell.addEventListener("click", handleCellClick);
        });

        setTimeout(() => {
            if (selectedCells.length === 0) {
                message.textContent = "Tempo esgotado! Tente novamente.";
                resetGame();
            }
        }, 30000); // 30 segundos para marcar as células

        function handleCellClick(event) {
            const cell = event.target;
            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);

            if (selectedCells.some(c => c.row === row && c.col === col)) {
                cell.style.backgroundColor = "white"; // Desmarca a célula
                selectedCells = selectedCells.filter(c => c.row !== row || c.col !== col);
            } else {
                cell.style.backgroundColor = "yellow"; // Marca a célula
                selectedCells.push({ row, col });
            }

            if (selectedCells.length === 6) {
                checkUserInput(selectedCells);
            }
        }
    }

    // Função para verificar a entrada do usuário
    function checkUserInput(selectedCells) {
        const isCorrect = selectedCells.every(cell =>
            correctCells.some(c => c.row === cell.row && c.col === cell.col)
        );

        if (isCorrect) {
            correctAttempts++;
            if (correctAttempts === 2) {
                message.textContent = "Parabéns! Você acertou duas vezes!";
                prize.style.display = "block";
            } else {
                message.textContent = "Correto! Vamos para a próxima rodada.";
                startGame();
            }
        } else {
            message.textContent = "Errado! Tente novamente.";
            resetGame();
        }
    }

    // Função para reiniciar o jogo
    function resetGame() {
        correctAttempts = 0;
        startGame();
    }

    // Função principal para iniciar o jogo
    function startGame() {
        createMatrix();
        setTimeout(blinkCircles, 1000); // Espera 1 segundo antes de piscar
    }

    // Inicia o jogo
    startGame();
});
