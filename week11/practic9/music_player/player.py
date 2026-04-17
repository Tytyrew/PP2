"""
Player module – manages the playlist and pygame.mixer playback.
"""

import os
import pygame


SUPPORTED = (".wav", ".mp3", ".ogg", ".flac")


class MusicPlayer:
    def __init__(self, music_dir: str = "music\sample_tracks"):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

        self.playlist: list[str] = []
        self.current_index: int = 0
        self.is_playing: bool = False
        self.volume: float = 0.8

        self._load_playlist(music_dir)
        pygame.mixer.music.set_volume(self.volume)

    # ── Playlist ───────────────────────────────────────────────────────────
    def _load_playlist(self, directory: str):
        if not os.path.isdir(directory):
            return
        for fname in sorted(os.listdir(directory)):
            if fname.lower().endswith(SUPPORTED):
                self.playlist.append(os.path.join(directory, fname))

    @property
    def current_track(self) -> str | None:
        if not self.playlist:
            return None
        return self.playlist[self.current_index]

    @property
    def current_track_name(self) -> str:
        if self.current_track is None:
            return "No tracks found"
        return os.path.splitext(os.path.basename(self.current_track))[0]

    @property
    def track_count(self) -> int:
        return len(self.playlist)

    # ── Playback controls ─────────────────────────────────────────────────
    def play(self):
        if not self.playlist:
            return
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def toggle_pause(self):
        if not self.is_playing:
            return
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_playing = False
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % self.track_count
        if self.is_playing:
            self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % self.track_count
        if self.is_playing:
            self.play()

    # ── Volume ────────────────────────────────────────────────────────────
    def volume_up(self):
        self.volume = min(1.0, self.volume + 0.05)
        pygame.mixer.music.set_volume(self.volume)

    def volume_down(self):
        self.volume = max(0.0, self.volume - 0.05)
        pygame.mixer.music.set_volume(self.volume)

    # ── Status ────────────────────────────────────────────────────────────
    def get_position_ms(self) -> int:
        """Returns playback position in milliseconds."""
        return pygame.mixer.music.get_pos()

    def is_track_finished(self) -> bool:
        return self.is_playing and not pygame.mixer.music.get_busy()
