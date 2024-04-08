import pygame
import os
pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption('Music Player')
music_dir = '/Users/ayauka/Downloads/Music'
songs = os.listdir(music_dir)
current_song = 0
pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
def play_song():
    pygame.mixer.music.play()
def stop_song():
    pygame.mixer.music.stop()
def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
    pygame.mixer.music.play()
def prev_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
    pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_song()
                else:
                    play_song()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()

    pygame.display.flip()

pygame.quit()
