# Casino Hack Game

## Descrição

Casino Hack Game é um jogo inspirado no minigame de hack das portas do golpe do cassino no GTA V. O objetivo é memorizar um padrão de estrelas que piscam na tela e depois reproduzi-lo corretamente. Após três rodadas bem-sucedidas, o jogador vence e recebe uma imagem de um abacaxi como recompensa.

## Regras do Jogo

1. Um padrão de 6 estrelas é exibido piscando por 2 segundos.
2. O jogador deve memorizar e depois selecionar as estrelas corretamente.
3. O padrão deve conter exatamente uma estrela por linha e coluna.
4. O jogador tem 2 minutos para concluir cada padrão.
5. Se acertar, avança para a próxima fase com um novo padrão.
6. Após três padrões corretos, o jogo é concluído com sucesso e Abre as portas.

## Como Jogar

1. Execute o script `CasinoHackGame.py`.
2. Memorize o padrão que pisca na tela.
3. Clique nas estrelas correspondentes.
4. Utilize os botões:
   - **Conferir**: Verifica se o padrão está correto.
   - **Tentar Novamente**: Exibe novamente o padrão para memória.
5. Complete 3 padrões corretamente para vencer!

## Requisitos

- Python 3.x
- Bibliotecas:
  - `tkinter`
  - `Pillow`

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/casino-hack-game.git
   ```
2. Instale as dependências:
   ```sh
   pip install pillow
   ```
3. Execute o jogo:
   ```sh
   python CasinoHackGame.py
   ```

## Problemas Conhecidos

- Certifique-se de que o arquivo `pineapple.png` está no mesmo diretório do script para exibir corretamente a recompensa.

## Contribuição

Pull requests são bem-vindos! Caso encontre bugs ou tenha sugestões, abra uma issue.

## Licença

Este projeto está sob a licença MIT. Consulte `LICENSE` para mais detalhes.

