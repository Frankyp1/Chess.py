import pygame

# --- Initialize ---
pygame.init()

# Window settings
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
LIGHT = (240, 217, 181)  # beige
DARK = (181, 136, 99)    # brown

# Create window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Load piece images
PIECE_IMAGES = {}
pieces = ["wp", "wr", "wn", "wb", "wq", "wk",
          "bp", "br", "bn", "bb", "bq", "bk"]

for piece in pieces:
    img = pygame.image.load(f"images/{piece}.png")
    PIECE_IMAGES[piece] = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))

# Chessboard setup (uppercase = white, lowercase = black)
def create_board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
    ]

# Draw the board
def draw_board(win, board):
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            piece = board[row][col]
            if piece != ".":
                win.blit(PIECE_IMAGES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Main loop
def main():
    board = create_board()
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board(WIN, board)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

#New helper to get row/col from mouse
def get_square_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

#New function to move pieces (no legality yet)
def move_piece(board, start, end):
    sr, sc = start
    er, ec = end
    board[er][ec] = board[sr][sc] #copy piece
    board[sr][sc] = "." #empty old square

#Main loop
def main():
    board = create_board()
    run = True
    clock = pygame.time.Clock()

    selected_square = None #stores first click(row, col)
    turn = "w" #white starts 

    while run:
        clock.tick(60)  # 60 FPS
       
       #Draw board + pieces
    draw_board(WIN, board)
    if selected_square: #highlight selected piece
        row, col = selected_square
        highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        highlight.set_alpha(120) #transpareny
        highlight.fill((255, 255,0)) #yellow
        WIN.blit(highlight, (col * SQUARE_SIZE, row * SQUARE_SIZE))
pygame.display.update()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        row, col = get_square_from_mouse(event.pos)
        if selected_square is None:
            #First click: select a piece if it matches turn
            piece = board[row][col]
            if piece != "." and piece[0] == turn:
                selected_square = (row, col)
        else:
            # second click: move piece 
            move_piece(board, selected_square, (row, col))
            selected_square = None
            #Switch turn
            turn = "b" if turn == "w" else "w"

    pygame.quit()
