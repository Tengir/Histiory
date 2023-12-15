class Message:
    def __init__(self, question_text, information: str,  first_photo: str = None, output_photo: str = None, audio: str = None, video: str = None):
        self.question_text = question_text
        self.information = information
        self.first_photo = first_photo
        self.output_photo = output_photo
        self.audio = audio
        self.video = video
