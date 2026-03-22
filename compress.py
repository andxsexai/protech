import os
from moviepy import VideoFileClip

def compress_video(file_path):
    try:
        print(f"--- Обработка: {file_path}")
        clip = VideoFileClip(file_path)
        
        # Уменьшаем до 480p (идеально для превью на телефоне)
        target_width = 854
        if clip.w > target_width:
            clip = clip.resized(width=target_width)
        
        temp_output = file_path.replace(".mp4", "_compressed.mp4")
        
        # Сжимаем: низкий битрейт, без звука, кодек libx264 для совместимости
        clip.write_videofile(
            temp_output, 
            bitrate="800k", 
            audio=False, 
            codec="libx264",
            preset="faster"
        )
        clip.close()
        
        # Заменяем оригинал
        os.remove(file_path)
        os.rename(temp_output, file_path)
        print(f"✅ Готово: {file_path}")
        
    except Exception as e:
        print(f"❌ Ошибка в файле {file_path}: {e}")

# Поиск всех mp4 в папках ПроТехСервис
for root, dirs, files in os.walk("."):
    for file in files:
        if file.lower().endswith(".mp4"):
            compress_video(os.path.join(root, file))

print("\n🚀 Все видео оптимизированы!")