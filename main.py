from  grid import  *

pygame.init()

bg()
boundaries()
XO()
fps = 90
clock = pygame.time.Clock()
run = True
player =1

while run:

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            click_row = int(mouseY // 300)
            click_col = int(mouseX // 250)

            if available_square(click_row, click_col):
                if player == 1:
                    mark_square(click_row, click_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(click_row, click_col, 2)
                    player = 1

                print(board)




    pygame.display.update()




pygame.quit()