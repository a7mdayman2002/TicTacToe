from grid import *

pygame.init()

bg()
player = 1
fps = 90
clock = pygame.time.Clock()
run = True
game_over = False
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_ESCAPE:
                run = False
            if key == pygame.K_r:
                restart()
                player = 1
                game_over = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            click_row = int(mouseY // 250)
            click_col = int(mouseX // 300)

            if available_square(click_row, click_col):
                if player == 1:
                    mark_square(click_row, click_col, 1)
                    if check_win(player) == True:
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(click_row, click_col, 2)
                    if check_win(player) == True:
                        game_over = True
                    player = 1
    Xo()
    pygame.display.update()

pygame.quit()