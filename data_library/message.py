class Message:
    def __init__(self, information: str, photo: str = None, audio: str = None, video: str = None):
        self.information = information
        self.photo = photo
        self.audio = audio
        self.video = video
