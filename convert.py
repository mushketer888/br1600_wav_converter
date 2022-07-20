import os
import wave

for file in os.listdir():
    if file.endswith(".VR8"):
        print('Converting file %s' % file)
        with open(file, "rb") as inp_f:
            data = inp_f.read()
            new_filename = file + ".wav"
            out_f = wave.open(new_filename, "wb")
            out_f.setnchannels(1)
            out_f.setsampwidth(2) # number of bytes
            out_f.setframerate(44100)
            out_f.writeframesraw(data)
            out_f.close()
            print('Succesfully created WAV file %s' % new_filename)

print('Press Enter to exit...')
input()
