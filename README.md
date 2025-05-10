# Voice Typing

A Python application that enables voice-to-text functionality using the Whisper.cpp model. This application allows you to record audio using a hotkey and automatically transcribes it to text, which is then pasted at your cursor position.

## Features

- **Hotkey-Based Recording**: Start and stop recording with a customizable keyboard shortcut
- **Real-Time Audio Processing**: Records audio in real-time with automatic normalization
- **Fast Transcription**: Uses Whisper.cpp for efficient speech-to-text conversion
- **Automatic Paste**: Automatically pastes transcribed text at your cursor position

## Requirements

- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`):
  - pywhispercpp (Whisper.cpp Python bindings)
  - sounddevice (for audio recording)
  - pynput (for keyboard control)
  - pyperclip (for clipboard operations)
  - numpy (for audio processing)

## Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:lladdy/voice-typing.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python run.py
   ```

2. The default configuration uses Command+Alt (⌘+⌥) as the recording hotkey and the 'base.en' Whisper model. You can modify these settings in `run.py`:
   ```python
   config = VoiceTyperConfig(recording_hotkey="<cmd>+<alt>",
                            model_name="base.en")
   ```

3. To use:
   - Press the configured hotkey to start recording
   - Speak your text
   - Press the hotkey again to stop recording
   - The transcribed text will automatically be pasted at your cursor position

## Project Structure

- `run.py`: Main entry point of the application
- `voice_typer.py`: Core application logic and coordination between components
- `audio.py`: Handles audio recording functionality using sounddevice
- `keyboard.py`: Manages keyboard interactions and hotkey detection
- `speech_to_text.py`: Wrapper for the Whisper.cpp model and transcription

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
