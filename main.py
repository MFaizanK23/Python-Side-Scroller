# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
v = 10
m = 1

player_pos = pygame.Vector2(40, 460)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.rect(screen, "red", (player_pos[0], player_pos[1], 40, 40))
    pygame.draw.line(screen, "black", (0, 500), (1280, 500))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        F = (1 / 2) * m * (v ** 2)

        # change in the y co-ordinate
        player_pos[1] -= F

        # decreasing velocity while going up and become negative while coming down
        v = v - 1

        # object reached its maximum height
        if v < 0:
            # negative sign is added to counter negative velocity
            m = -1

        # objected reaches its original state
        if v == -6:
            # setting original values to v and m
            v = 10
            m = 1




    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

