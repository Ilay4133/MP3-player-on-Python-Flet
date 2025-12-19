import librosa
import matplotlib.pyplot as plt
import librosa
audio_path = 'C:/Users/Unicum_Student/Desktop/pythonProject1/【Ado】彗星列車のベルが鳴る 歌いました.mp3'
x , sr = librosa.load(audio_path)
print(type(x), type(sr))
print(x.shape, sr)


n0 = 9000
n1 = 9100
plt.figure(figsize=(14, 5))
plt.plot(x[n0:n1])
plt.grid()
plt.show()

zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
print(sum(zero_crossings))
