import pygame

from components.Tetris import Tetris
from constants.Colors import brick_colors, primary_colors
from constants.GameStates import START, GAME_OVER


pygame.init()

screen = pygame.display.set_mode((380, 670))
pygame.display.set_caption("Tetrieus")

done = False
fps = 2
clock = pygame.time.Clock()
counter = 0
zoom = 30

game = Tetris(20, 10)
pressing_down = False
pressing_left = False
pressing_right = False

while not done:
    if game.state == START:
        game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and not game.state == GAME_OVER:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                pressing_left = True
            if event.key == pygame.K_RIGHT:
                pressing_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False
            if event.key == pygame.K_LEFT:
                pressing_left = False
            if event.key == pygame.K_RIGHT:
                pressing_right = False

        if pressing_down:
            game.down()
        if pressing_left:
            game.left()
        if pressing_right:
            game.right()

    screen.fill(color=primary_colors["WHITE"])
    for i in range(game.height):
        for j in range(game.width):
            if game.field[i][j] == 0:
                color = primary_colors["GRAY"]
                just_border = 1
            else:
                color = brick_colors[game.field[i][j]]
                just_border = 0
            pygame.draw.rect(
                screen,
                color,
                [30 + j * zoom, 30 + i * zoom, zoom, zoom],
                just_border,
            )

    if game.Figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.Figure.image():
                    pygame.draw.rect(
                        screen,
                        game.Figure.color,
                        [
                            30 + (j + game.Figure.x) * zoom,
                            30 + (i + game.Figure.y) * zoom,
                            zoom,
                            zoom,
                        ],
                    )

    gameover_font = pygame.font.SysFont("Calibri", 65, True, False)
    text_gameover = gameover_font.render("Game Over!\n Press Esc", True, (255, 215, 0))

    if game.state == GAME_OVER:
        screen.blit(text_gameover, [30, 250])

    score_font = pygame.font.SysFont("Calibri", 25, True, False)
    text_score = gameover_font.render("Score: " + str(game.score), True, (0, 0, 0))
    screen.blit(text_score, [0, 0])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()