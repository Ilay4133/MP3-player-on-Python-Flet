import librosa
import librosa.display
import matplotlib.pyplot as plt
import sklearn
import numpy as np

audio_path = 'C:/Users/Unicum_Student/Desktop/pythonProject1/【Ado】彗星列車のベルが鳴る 歌いました.mp3'
x, sr = librosa.load(audio_path)
print(type(x), type(sr))
print(x.shape, sr)

# Исправленные строки: используем именованные параметры
spectral_centroids = librosa.feature.spectral_centroid(y=x, sr=sr)[0]
spectral_rolloff = librosa.feature.spectral_rolloff(y=x+0.01, sr=sr)[0]

print(f"Spectral centroids shape: {spectral_centroids.shape}")
print(f"Spectral rolloff shape: {spectral_rolloff.shape}")

# Вычисление времени для визуализации
frames = range(len(spectral_centroids))
t = librosa.frames_to_time(frames)

# Нормализация спектрального центроида и rolloff
def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)

# Построение графика
plt.figure(figsize=(14, 5))

# Отображаем форму волны
librosa.display.waveshow(x, sr=sr, alpha=0.4)

# Отображаем spectral rolloff и spectral centroid разными цветами
plt.plot(t, normalize(spectral_rolloff), color='g', label='Spectral Rolloff')
plt.plot(t, normalize(spectral_centroids), color='r', label='Spectral Centroid')

plt.title('Форма волны, спектральный центроид и спектральный rolloff')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда / Нормализованные значения')
plt.legend()
plt.show()
