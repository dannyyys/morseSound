import math
import wave
import struct
import os


class sound:

    sample_rate = 44100.0
    duration_milliseconds = 50

    def __init__(self, txt):
        self.audio = []
        self.morseText = txt

    def append_silence(self):
        """
        Adding silence is easy - we add zeros to the end of our array
        """
        num_samples = self.duration_milliseconds * (self.sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.audio.append(0.0)

        return

    def append_silence_space(self):
        """
        Adding silence is easy - we add zeros to the end of our array
        """
        num_samples = (self.duration_milliseconds * 7) * (self.sample_rate /
                                                          1000.0)

        for x in range(int(num_samples)):
            self.audio.append(0.0)

        return

    def append_dotWave(self, freq=440.0, volume=1.0):

        num_samples = self.duration_milliseconds * (self.sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.audio.append(volume * math.sin(2 * math.pi * freq *
                                                (x / self.sample_rate)))

        return

    def append_dashWave(self, freq=440.0, volume=1.0):

        num_samples = (self.duration_milliseconds * 3) * (self.sample_rate /
                                                          1000.0)

        for x in range(int(num_samples)):
            self.audio.append(volume * math.sin(2 * math.pi * freq *
                                                (x / self.sample_rate)))

        return

    def save_wav(self, file_name):
        # By default, output.wav will be saved on Desktop
        default_folder_path = os.path.expanduser('~/Desktop')
        default_file_path = f'{default_folder_path}/{file_name}'

        # Open up a wav file
        wav_file = wave.open(default_file_path, "w")

        # wav params
        nchannels = 1

        sampwidth = 2

        # 44100 is the industry standard sample rate - CD quality.  If you need to
        # save on file size you can adjust it downwards. The stanard for low quality
        # is 8000 or 8kHz.
        nframes = len(self.audio)
        comptype = "NONE"
        compname = "not compressed"
        wav_file.setparams((nchannels, sampwidth, self.sample_rate, nframes,
                            comptype, compname))

        # WAV files here are using short, 16 bit, signed integers for the
        # sample size.  So we multiply the floating point data we have by 32767, the
        # maximum value for a short integer.  NOTE: It is theortically possible to
        # use the floating point -1.0 to 1.0 data directly in a WAV file but not
        # obvious how to do that using the wave module in python.
        for sample in self.audio:
            wav_file.writeframes(struct.pack('h', int(sample * 3000)))

        wav_file.close()

        return default_file_path

    def toSound(self):
        for m in self.morseText:
            if m == '.':
                self.append_dotWave(volume=5.0)
                self.append_silence()
            elif m == '-':
                self.append_dashWave(volume=5.0)
                self.append_silence()
            else:
                self.append_silence_space()

        return self.save_wav("output.wav")