import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio_path = 'C:/Users/Unicum_Student/Desktop/pythonProject1/【Ado】彗星列車のベルが鳴る 歌いました.mp3'

try:
    x, sr = librosa.load(audio_path)
    print(f"Audio loaded: shape={x.shape}, sr={sr}")

    hop_length = 512

    # Способ 1: Прямой вызов с y=
    try:
        chromagram = librosa.feature.chroma_stft(y=x, sr=sr, hop_length=hop_length)
        print(f"Chromagram shape: {chromagram.shape}")
    except Exception as e1:
        print(f"Method 1 failed: {e1}")

        # Способ 2: Через спектрограмму
        try:
            S = np.abs(librosa.stft(x, hop_length=hop_length))
            chromagram = librosa.feature.chroma_stft(S=S, sr=sr, hop_length=hop_length)
            print(f"Chromagram shape (via STFT): {chromagram.shape}")
        except Exception as e2:
            print(f"Method 2 failed: {e2}")
            raise

    # Визуализация
    plt.figure(figsize=(15, 5))
    librosa.display.specshow(chromagram,
                             x_axis='time',
                             y_axis='chroma',
                             hop_length=hop_length,
                             cmap='coolwarm')
    plt.colorbar(label='Intensity')
    plt.title('Chromagram')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")
    print(f"Librosa version: {librosa.__version__}")
