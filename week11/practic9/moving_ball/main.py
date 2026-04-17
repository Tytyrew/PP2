"""
Moving Ball Game
=================
Control a red ball around the screen using the arrow keys.

Controls
--------
  ↑  →  Move up    (20 px)
  ↓  →  Move down  (20 px)
  ←  →  Move left  (20 px)
  →  →  Move right (20 px)
  ESC / close window  →  quit

Rules
-----
* The ball (radius = 25 px) cannot leave the screen.
* Moves that would go out-of-bounds are silently ignored.
"""

import pygame
import sys
from ball import Ball

# ── Constants ──────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 800, 600
FPS = 60

BG_COLOR   = (245, 245, 245)   # White-ish background
GRID_COLOR = (220, 220, 220)   # Light grid
TEXT_COLOR = ( 80,  80,  80)


def draw_grid(surface: pygame.Surface, spacing: int = 40):
    for x in range(0, WIDTH, spacing):
        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, spacing):
        pygame.draw.line(surface, GRID_COLOR, (0, y), (WIDTH, y), 1)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()

    ball = Ball(WIDTH, HEIGHT)

    font = pygame.font.SysFont("segoeui", 18)
    hint = font.render("Arrow keys to move  |  ESC to quit", True, TEXT_COLOR)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        ball.move(0, -Ball.STEP)
                    case pygame.K_DOWN:
                        ball.move(0, Ball.STEP)
                    case pygame.K_LEFT:
                        ball.move(-Ball.STEP, 0)
                    case pygame.K_RIGHT:
                        ball.move(Ball.STEP, 0)
                    case pygame.K_ESCAPE:
                        running = False

        # ── Draw ───────────────────────────────────────────────────────────
        screen.fill(BG_COLOR)
        draw_grid(screen)

        ball.draw(screen)

        # HUD
        pos_text = font.render(
            f"Position: {ball.position}   "
            f"Bounds: {WIDTH}×{HEIGHT}",
            True, TEXT_COLOR,
        )
        screen.blit(pos_text, (10, 10))
        screen.blit(hint, (10, HEIGHT - 30))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
