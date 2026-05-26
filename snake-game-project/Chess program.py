#Setup Pygame
import pygame as pg
pg.init()
WIDTH, HEIGHT = 1000, 900
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Chess Program")
font = pg.font.Font('freesansbold.ttf', 20)
big_font = pg.font.Font('freesansbold.ttf', 50)
timer = pg.time.Clock()
fps = 60



# Game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',''
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
captured_pieces_white = []
captured_pieces_black = []

turn_step = 0  #Current turn: 0 for white, 1 for black
selection = 100
valid_moves = []
# Load images
black_queen = pg.image.load('images/black_queen.png')
black_queen = pg.image.scale(black_queen, (80, 80))
black_queen_small = pg.image.scale(black_queen, (40, 40))
black_king = pg.image.load('images/black_king.png')
black_king = pg.image.scale(black_king, (80, 80))
black_king_small = pg.image.scale(black_king, (40, 40))
black_bishop = pg.image.load('images/black_bishop.png')
black_bishop = pg.image.scale(black_bishop, (80, 80))
black_bishop_small = pg.image.scale(black_bishop, (40, 40))
black_knight = pg.image.load('images/black_knight.png')
black_knight = pg.image.scale(black_knight, (80, 80))
black_knight_small = pg.image.scale(black_knight, (40, 40))
black_rook = pg.image.load('images/black_rook.png')
black_rook = pg.image.scale(black_rook, (80, 80))
black_rook_small = pg.image.scale(black_rook, (40, 40))
black_pawn = pg.image.load('images/black_pawn.png')
black_pawn = pg.image.scale(black_pawn, (80, 80))
black_pawn_small = pg.image.scale(black_pawn, (40, 40))
white_queen = pg.image.load('images/white_queen.png')
white_queen = pg.image.scale(white_queen, (80, 80))
white_queen_small = pg.image.scale(white_queen, (40, 40))
white_king = pg.image.load('images/white_king.png')
white_king = pg.image.scale(white_king, (80, 80))
white_king_small = pg.image.scale(white_king, (40, 40))
white_bishop = pg.image.load('images/white_bishop.png')
white_bishop = pg.image.scale(white_bishop, (80, 80))
white_bishop_small = pg.image.scale(white_bishop, (40, 40))
white_knight = pg.image.load('images/white_knight.png')
white_knight = pg.image.scale(white_knight, (80, 80))
white_knight_small = pg.image.scale(white_knight, (40, 40))
white_rook = pg.image.load('images/white_rook.png')
white_rook = pg.image.scale(white_rook, (80, 80))
white_rook_small = pg.image.scale(white_rook, (40, 40))
white_pawn = pg.image.load('images/white_pawn.png')
white_pawn = pg.image.scale(white_pawn, (80, 80))
white_pawn_small = pg.image.scale(white_pawn, (40, 40))
white_images = [white_rook, white_knight, white_bishop, white_king, white_queen, white_pawn]
white_images_small = [white_rook_small, white_knight_small, white_bishop_small,
                      white_king_small, white_queen_small, white_pawn_small]
black_images = [black_rook, black_knight, black_bishop, black_king, black_queen, black_pawn]
black_images_small = [black_rook_small, black_knight_small, black_bishop_small,
                      black_king_small, black_queen_small, black_pawn_small]
piece_list = ['rook', 'knight', 'bishop', 'king', 'queen', 'pawn']
#Check variables/flashing counters


#Draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pg.draw.rect(screen, 'light gray',[600 - (column * 200), row * 100, 100, 100])
# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()

# Event handling
for event in pg.event.get():
    if event.type == pg.QUIT:
        run = False

pg.display.flip()  
pg.quit()      