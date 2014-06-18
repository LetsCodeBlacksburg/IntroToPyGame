import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()

#### Game Pieces ############################
box = pygame.Rect(10, 200, 200, 100)
box_color = pygame.Color("yellow")
box_speed = 0

wall = pygame.Rect(700, 50, 25, 500)
wall_color = pygame.Color("blue")

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
    elif event.type == pygame.KEYDOWN:
        box_speed = 3
    elif event.type == pygame.KEYUP:
        box_speed = 0

    ##### Game Rules ########################
    box.centerx += box_speed
    if box.colliderect(wall):
        box.right = wall.left

    ##### Draw the Screen ###################
    # Start with a blank screen
    screen.fill(pygame.Color("black"))

    # Draw game graphics here...
    pygame.draw.rect(screen, box_color, box)
    pygame.draw.rect(screen, wall_color, wall)

    # Show the screen. This must come last.
    pygame.display.flip()

pygame.quit()

