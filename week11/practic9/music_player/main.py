"""
Music Player with Keyboard Controller
======================================
An interactive music player built with Pygame.

Controls
--------
  P   →  Play current track
  S   →  Stop playback
  SPACE → Pause / Resume
  N   →  Next track
  B   →  Back (previous track)
  ↑   →  Volume up
  ↓   →  Volume down
  Q / ESC →  Quit
"""

import pygame
import sys
from player import MusicPlayer

# ── Constants ──────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 700, 480
FPS = 60

# Colour palette
BG        = (18,  18,  30)
PANEL     = (30,  30,  50)
ACCENT    = (100, 200, 255)
TEXT_PRI  = (240, 240, 255)
TEXT_SEC  = (140, 140, 170)
GREEN     = ( 80, 220, 120)
RED       = (220,  80,  80)
YELLOW    = (255, 210,  60)
BAR_BG    = ( 50,  50,  70)
BAR_FG    = (100, 200, 255)


def draw_rounded_rect(surface, color, rect, radius=12):
    pygame.draw.rect(surface, color, rect, border_radius=radius)


def format_ms(ms: int) -> str:
    if ms < 0:
        return "0:00"
    total_s = ms // 1000
    m, s = divmod(total_s, 60)
    return f"{m}:{s:02d}"


def draw_ui(screen, player: MusicPlayer, fonts: dict):
    screen.fill(BG)
    W, H = screen.get_size()

    # ── Header ─────────────────────────────────────────────────────────────
    pygame.draw.rect(screen, PANEL, (0, 0, W, 80))
    title = fonts["large"].render("🎵  Music Player", True, ACCENT)
    screen.blit(title, title.get_rect(center=(W // 2, 40)))

    # ── Album art placeholder ───────────────────────────────────────────────
    art_rect = pygame.Rect(40, 100, 180, 180)
    draw_rounded_rect(screen, PANEL, art_rect, 16)
    note = fonts["huge"].render("♪", True, ACCENT)
    screen.blit(note, note.get_rect(center=art_rect.center))

    # ── Track info ─────────────────────────────────────────────────────────
    info_x = 250
    track_name = player.current_track_name
    name_surf = fonts["medium"].render(track_name, True, TEXT_PRI)
    screen.blit(name_surf, (info_x, 110))

    idx_text = f"Track {player.current_index + 1} / {player.track_count}" \
               if player.track_count else "No tracks"
    idx_surf = fonts["small"].render(idx_text, True, TEXT_SEC)
    screen.blit(idx_surf, (info_x, 150))

    # Status badge
    status_text = "▶  PLAYING" if player.is_playing else "■  STOPPED"
    status_color = GREEN if player.is_playing else RED
    status_surf = fonts["small"].render(status_text, True, status_color)
    screen.blit(status_surf, (info_x, 185))

    # ── Progress bar ───────────────────────────────────────────────────────
    bar_rect = pygame.Rect(40, 310, W - 80, 12)
    draw_rounded_rect(screen, BAR_BG, bar_rect, 6)

    pos_ms = player.get_position_ms()
    if player.is_playing and pos_ms > 0:
        # We don't know total length from mixer easily, so show scrolling bar
        fill_w = (pos_ms % 30000) / 30000 * bar_rect.width
        fill_rect = pygame.Rect(bar_rect.x, bar_rect.y, int(fill_w), bar_rect.height)
        draw_rounded_rect(screen, BAR_FG, fill_rect, 6)

    pos_surf = fonts["tiny"].render(format_ms(pos_ms), True, TEXT_SEC)
    screen.blit(pos_surf, (bar_rect.right - pos_surf.get_width(), 328))

    # ── Volume bar ─────────────────────────────────────────────────────────
    vol_label = fonts["tiny"].render(f"Volume: {int(player.volume * 100)}%", True, TEXT_SEC)
    screen.blit(vol_label, (40, 348))

    vol_bar = pygame.Rect(40, 365, W - 80, 8)
    draw_rounded_rect(screen, BAR_BG, vol_bar, 4)
    vol_fill = pygame.Rect(40, 365, int((W - 80) * player.volume), 8)
    draw_rounded_rect(screen, YELLOW, vol_fill, 4)

    # ── Key guide ──────────────────────────────────────────────────────────
    controls = [
        ("P", "Play"),   ("S", "Stop"), ("SPACE", "Pause"),
        ("N", "Next"),   ("B", "Back"),
        ("↑↓", "Volume"), ("Q", "Quit"),
    ]
    guide_y = 400
    gap = (W - 80) // len(controls)
    for i, (key, label) in enumerate(controls):
        x = 40 + i * gap
        k_surf = fonts["tiny"].render(f"[{key}]", True, ACCENT)
        l_surf = fonts["tiny"].render(label, True, TEXT_SEC)
        screen.blit(k_surf, (x, guide_y))
        screen.blit(l_surf, (x, guide_y + 18))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    tick = pygame.time.Clock()

    player = MusicPlayer(music_dir="music/sample_tracks")

    fonts = {
        "huge":   pygame.font.SysFont("segoeui", 72),
        "large":  pygame.font.SysFont("segoeui", 36, bold=True),
        "medium": pygame.font.SysFont("segoeui", 26, bold=True),
        "small":  pygame.font.SysFont("segoeui", 20),
        "tiny":   pygame.font.SysFont("segoeui", 16),
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_p:
                        player.play()
                    case pygame.K_s:
                        player.stop()
                    case pygame.K_SPACE:
                        player.toggle_pause()
                    case pygame.K_n:
                        player.next_track()
                    case pygame.K_b:
                        player.prev_track()
                    case pygame.K_UP:
                        player.volume_up()
                    case pygame.K_DOWN:
                        player.volume_down()
                    case pygame.K_q | pygame.K_ESCAPE:
                        running = False

        # Auto-advance when a track ends naturally
        if player.is_track_finished():
            player.next_track()

        draw_ui(screen, player, fonts)
        pygame.display.flip()
        tick.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()