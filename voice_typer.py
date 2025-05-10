import logging
import threading
from dataclasses import dataclass
from queue import Queue

from audio import AudioManager
from keyboard import Keyboard
from speech_to_text import SpeechToTextModel

logger = logging.getLogger(__name__)


@dataclass
class VoiceTyperConfig:
    """
    Encapsulates configuration settings for the application.
    """
    recording_hotkey: str
    model_name: str


class VoiceTyper:
    """
    Handles the core voice typing functionality.
    """

    def __init__(self, config: VoiceTyperConfig):
        self.speech_to_text_model = SpeechToTextModel(config.model_name)
        self.audio_manager = AudioManager()
        self.keyboard = Keyboard(config.recording_hotkey, self._handle_hotkey_action)

        """
        This queue is used to store audio chunks for transcription.
        It allows for thread-safe communication between the audio recording thread
        and the transcription process.
        """
        self.audio_queue = Queue()

    def _transcribe_audio(self, audio_chunks):
        """Transcribes the audio file and copies the text to the clipboard."""
        try:
            logger.info("Beginning transcription...")
            transcription_segments = self.speech_to_text_model.transcribe(audio_chunks)
            transcription_text = " ".join(segment.text for segment in transcription_segments)
            logger.info(transcription_text)

            self.keyboard.copy_to_clipboard(transcription_text)
            self.keyboard.simulate_paste_action()

        except Exception as error:
            logger.info(f"Error: {str(error)}")

    def _start_audio_recording(self):
        """Starts recording audio."""

        # Start recording in a separate thread
        def record_audio():
            audio_chunks = self.audio_manager.start_recording()
            self.audio_queue.put(audio_chunks)

        recording_thread = threading.Thread(target=record_audio, daemon=True)
        recording_thread.start()

    def _stop_recording_and_transcribe(self):
        """Stops recording and starts transcription."""
        if self.audio_manager.is_recording_active:
            self.audio_manager.stop_recording()
            audio_chunks = self.audio_queue.get()

            if audio_chunks is not None:
                self._transcribe_audio(audio_chunks)
            else:
                logger.info("Skipping transcription: No audio data to transcribe.")

    def _handle_hotkey_action(self):
        """Handles the hotkey press."""
        if not self.audio_manager.is_recording_active:
            self._start_audio_recording()
        else:
            self._stop_recording_and_transcribe()

    def run(self):
        """Main function to start the program."""
        try:
            listener = self.keyboard.start_listener()
            if listener:
                listener.join()
        except Exception as error:
            logger.info(f"Error in the voice typer: {str(error)}")
