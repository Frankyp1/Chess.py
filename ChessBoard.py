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
#I have a big PPp