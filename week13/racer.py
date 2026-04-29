import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
RED = (200, 0, 0)
YELLOW = (255, 215, 0)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Игрок
player = pygame.Rect(WIDTH // 2 - 20, HEIGHT - 80, 40, 60)
player_speed = 6

# Монеты
coins = []
coin_size = 20
coin_speed = 5
coin_spawn_delay = 40
coin_timer = 0

# Счёт
score = 0
font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill(WHITE)

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # CONTROL
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # границы
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - player.width:
        player.x = WIDTH - player.width

    # SPAWN COINS
    coin_timer += 1
    if coin_timer >= coin_spawn_delay:
        coin_timer = 0

        x = random.randint(0, WIDTH - coin_size)

        coin = {
            "rect": pygame.Rect(x, 0, coin_size, coin_size),
            "homing": random.random() < 0.3  # 30% тянутся к игроку
        }

        coins.append(coin)

    # UPDATE COINS
    for coin in coins[:]:
        rect = coin["rect"]

        # вниз
        rect.y += coin_speed

        # лёгкое притяжение к игроку
        if coin["homing"]:
            if rect.centerx < player.centerx:
                rect.x += 1
            elif rect.centerx > player.centerx:
                rect.x -= 1

        # столкновение
        if player.colliderect(rect):
            coins.remove(coin)
            score += 1

        # выход за экран
        elif rect.y > HEIGHT:
            coins.remove(coin)

    # DRAW PLAYER
    pygame.draw.rect(screen, RED, player)

    # DRAW COINS
    for coin in coins:
        pygame.draw.rect(screen, YELLOW, coin["rect"])

    # SCORE
    score_text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()