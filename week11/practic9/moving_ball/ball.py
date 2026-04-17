"""
Ball module – encapsulates ball state and movement logic.
"""

import pygame


class Ball:
    RADIUS = 25
    DIAMETER = RADIUS * 2
    COLOR = (220, 50, 50)       # Red
    OUTLINE_COLOR = (255, 120, 120)
    STEP = 20                   # pixels per key press

    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Start in the centre
        self.x = screen_width // 2
        self.y = screen_height // 2

    # ── Movement ───────────────────────────────────────────────────────────
    def move(self, dx: int, dy: int):
        """
        Attempt to move the ball by (dx, dy).
        The move is silently ignored if it would place any part of the ball
        outside the screen boundaries.
        """
        new_x = self.x + dx
        new_y = self.y + dy

        # Boundary check: centre must stay within [RADIUS, dimension - RADIUS]
        if self.RADIUS <= new_x <= self.screen_width - self.RADIUS:
            self.x = new_x
        if self.RADIUS <= new_y <= self.screen_height - self.RADIUS:
            self.y = new_y

    # ── Drawing ────────────────────────────────────────────────────────────
    def draw(self, surface: pygame.Surface):
        # Shadow
        pygame.draw.circle(surface, (180, 40, 40),
                           (self.x + 4, self.y + 4), self.RADIUS)
        # Main body
        pygame.draw.circle(surface, self.COLOR, (self.x, self.y), self.RADIUS)
        # Highlight
        pygame.draw.circle(surface, self.OUTLINE_COLOR,
                           (self.x - 7, self.y - 7), self.RADIUS // 3)

    # ── Info ───────────────────────────────────────────────────────────────
    @property
    def position(self) -> tuple[int, int]:
        return (self.x, self.y)
