import matplotlib.pyplot as plt
import librosa
audio_path = 'C:/Users/Unicum_Student/Desktop/pythonProject1/【Ado】彗星列車のベルが鳴る 歌いました.mp3'
x , sr = librosa.load(audio_path)
print(type(x), type(sr))
print(x.shape, sr)


plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)
plt.show()
