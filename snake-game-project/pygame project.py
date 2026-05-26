import pygame as pg
import random

pg.init()

# Constants
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 30, 30
PIPE_WIDTH = 60
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_SPEED = 3
BIRD_X = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Flappy Bird")
clock = pg.time.Clock()
font = pg.font.SysFont("comicsans", 30)

class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = HEIGHT // 2
        self.vel = 0

    def jump(self):
        self.vel = JUMP_STRENGTH

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

    def draw(self, win):
        pg.draw.rect(win, BLUE, (self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT))

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.top = self.height
        self.bottom = self.height + PIPE_GAP
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, win):
        pg.draw.rect(win, GREEN, (self.x, 0, PIPE_WIDTH, self.top))
        pg.draw.rect(win, GREEN, (self.x, self.bottom, PIPE_WIDTH, HEIGHT - self.bottom))

    def collide(self, bird):
        bird_rect = pg.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
        top_rect = pg.Rect(self.x, 0, PIPE_WIDTH, self.top)
        bottom_rect = pg.Rect(self.x, self.bottom, PIPE_WIDTH, HEIGHT - self.bottom)
        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

def draw_window(win, bird, pipes, score):
    win.fill(WHITE)
    bird.draw(win)
    for pipe in pipes:
        pipe.draw(win)
    score_text = font.render(f"Score: {score}", 1, BLACK)
    win.blit(score_text, (10, 10))
    pg.display.update()

def main():
    bird = Bird()
    pipes = [Pipe(WIDTH)]
    score = 0
    run = True

    while run:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bird.jump()
            if event.type == pg.MOUSEBUTTONDOWN:
                bird.jump()

        bird.update()

        # Add new pipes
        if pipes[-1].x < WIDTH - 200:
            pipes.append(Pipe(WIDTH))

        # Update pipes and check collisions
        for pipe in pipes[:]:
            pipe.update()
            if pipe.collide(bird):
                run = False
            if pipe.x + PIPE_WIDTH < bird.x and not pipe.passed:
                pipe.passed = True
                score += 1
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)

        # Check boundaries
        if bird.y < 0 or bird.y + BIRD_HEIGHT > HEIGHT:
            run = False

        draw_window(win, bird, pipes, score)

    # Game over screen
    win.fill(BLACK)
    game_over_text = font.render("Game Over", 1, RED)
    final_score_text = font.render(f"Final Score: {score}", 1, WHITE)
    win.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 50))
    win.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2 + 10))
    pg.display.update()
    pg.time.wait(2000)

    pg.quit()

if __name__ == "__main__":
    main()