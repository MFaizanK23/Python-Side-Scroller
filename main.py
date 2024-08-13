# Example file showing a circle moving on screen
import pygame


# pygame setup
pygame.init()
WIDTH, HEIGHT = 1280, 900
FPS = 60
player_velocity = 5
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Silly-Side-Scroller")
player_pos = pygame.Vector2(40, 0)


class Player(pygame.sprite.Sprite):
    colour = (0, 255, 0)
    mass = 1
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.falling = 0

    def move(self, displacement_x, displacement_y):
        self.rect.x += displacement_x
        self.rect.y += displacement_y

    def move_left(self, velocity):
        self.x_velocity = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, velocity):
        self.x_velocity = velocity
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def gravity(self, fps):
        if self.rect.y < 800:
            self.y_velocity += min(1, (self.falling / fps) * self.mass)
            self.move(self.x_velocity, self.y_velocity)
            self.falling += .25
        elif self.rect.y > 800:
            self.move(self.x_velocity, 0)

    def obstacle(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        pygame.draw.line(SCREEN, "black", (0, 845), (1280, 845))


def get_background(name):
    image = pygame.image.load(name)
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            position = [i * width, j * height]
            tiles.append(position)

    return tiles, image


def draw(SCREEN, background, bg_image, player):
    for tile in background:
        SCREEN.blit(bg_image, tile)

    player.obstacle(SCREEN)
    pygame.display.update()


def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_velocity = 0  # so when u let go u stop moving
    if keys[pygame.K_a]:
        player.move_left(player_velocity)
    if keys[pygame.K_d]:
        player.move_right(player_velocity)


def main(SCREEN):
    clock = pygame.time.Clock()
    background, bg_image = get_background("appleguy.jpg")

    player = Player(player_pos[0], player_pos[1], 40, 40)
    running = True
    while running:
        clock.tick(FPS)

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        player.gravity(FPS)
        handle_move(player)

        draw(SCREEN, background, bg_image, player)


    pygame.quit()


if __name__ == "__main__":
    main(SCREEN)
