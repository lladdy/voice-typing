import logging

import numpy as np
import sounddevice as sd

logger = logging.getLogger(__name__)

class AudioManager:
    """
    Handles audio recording functionality.
    """
    AUDIO_SAMPLE_RATE = 16000  # This is the only supported sample rate for the model

    def __init__(self):
        sd.default.samplerate = self.AUDIO_SAMPLE_RATE
        sd.default.channels = 1
        self.is_recording_active = False
        self.sleep_time_while_recording = 50

    def configure_audio_stream(self, audio_callback):
        """Configures and returns an audio input stream."""
        return sd.InputStream(callback=audio_callback, channels=1, samplerate=self.AUDIO_SAMPLE_RATE)

    def start_recording(self):
        """Starts recording audio and returns the recorded audio chunks."""
        self.is_recording_active = True
        logger.info("Starting recording...")

        audio_chunks = []

        def audio_callback(indata, frames, time, status):
            if self.is_recording_active:
                audio_chunks.append(indata.copy())

        with self.configure_audio_stream(audio_callback):
            while self.is_recording_active:
                sd.sleep(self.sleep_time_while_recording)

        if audio_chunks:
            audio_chunks = np.concatenate(audio_chunks, axis=0)
            audio_chunks = audio_chunks / np.max(np.abs(audio_chunks))  # Normalize audio
            logger.info(f"Recording stopped. Audio data length: {len(audio_chunks)} samples.")
            return audio_chunks
        else:
            logger.info("No audio recorded.")
            return None

    def stop_recording(self):
        """Stops the current recording session."""
        self.is_recording_active = False
        logger.info("Stopping recording...")
