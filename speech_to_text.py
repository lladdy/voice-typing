import logging

from pywhispercpp.model import Model

logger = logging.getLogger(__name__)

class SpeechToTextModel:
    """
    A wrapper around the Whisper.cpp model for speech-to-text transcription.
    """

    def __init__(self, model_name):
        self.model = Model(model_name)

    def transcribe(self, audio_chunks):
        """Transcribes the audio chunks into text."""
        logger.info("Transcribing audio...")
        return self.model.transcribe(audio_chunks)
