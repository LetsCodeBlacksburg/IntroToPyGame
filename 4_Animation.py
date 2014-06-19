import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()

#### Game Pieces ############################
box = pygame.Rect(10, 200, 200, 100)
box_color = pygame.Color("yellow")
box_speed = 3

##### Play Loop #############################
running = True
while running:

    # Run 60 frames per second
    clock.tick(60)

    ##### User Input ########################
    # End the game when player closes the window.
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    ##### Game Rules ########################
    box.centerx += box_speed

    ##### Draw the Screen ###################
    # Start with a blank screen
    screen.fill(pygame.Color("black"))

    # Draw game graphics here...
    pygame.draw.rect(screen, box_color, box)

    # Show the screen. This must come last.
    pygame.display.flip()

pygame.quit()

