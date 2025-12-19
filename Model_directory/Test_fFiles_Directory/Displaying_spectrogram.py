import matplotlib.pyplot as plt
import librosa
audio_path = 'C:/Users/Unicum_Student/Desktop/pythonProject1/【Ado】彗星列車のベルが鳴る 歌いました.mp3'
x , sr = librosa.load(audio_path)
print(type(x), type(sr))
print(x.shape, sr)

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
plt.show()
