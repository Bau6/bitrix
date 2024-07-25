from django.shortcuts import render
from PIL import ImageFont, ImageDraw, Image
from moviepy.editor import ImageSequenceClip
import numpy as np
import os
from django.conf import settings
def generate_video(request):
    # Размеры видео
    width = 100
    height = 100

    # Цвет фона
    background_color = (255, 255, 255)

    # Параметры видео
    fps = 30
    duration = 3  # В секундах

    # Параметры текста
    text = " 3 секунды 30 фпс видео"
    font_path = os.path.join(os.path.dirname(__file__), 'font', 'jaro-cyrillic.otf')
    font_size = 50
    text_color = (0, 0, 0)

    # Создание директории для кадров
    os.makedirs("frames", exist_ok=True)

    # Создание объекта шрифта
    font = ImageFont.truetype(font_path, font_size)

    # Вычисление ширины текста
    text_width, text_height = font.getmask(text).size

    # Создание списка изображений с бегущей строкой
    images = []
    for i in range(int(duration * fps)):
        # Создаем новое изображение для каждого кадра
        image = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Рассчитываем координату X для бегущего текста
        x = -i * (text_width // (duration * fps))  # Сдвиг влево на каждом кадре

        # Отрисовка текста
        draw.text((x, (image.height - text_height) // 2), text, font=font, fill=text_color)

        # Сохранение кадра
        image.save(f"frames/frame_{i}.png")
        images.append(np.array(image))  # Преобразование Image в numpy.ndarray

    # Создание видео из списка изображений
    clip = ImageSequenceClip(images, fps=fps)
    video_path = os.path.join(settings.MEDIA_ROOT, 'test.mp4')
    clip.write_videofile(video_path)
    return render(request, 'index.html')

