class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename


class MP3(AudioFile):
    ext = 'mp3'

    def play(self):
        print("playing {} as mp3".format(self.filename))


class Matroska(AudioFile):
    ext = "mkv"

    def play(self):
        print("playing {} as mka".format(self.filename))


class Opus(AudioFile):
    ext = "opus"

    def play(self):
        print("playing {} as opus".format(self.filename))
