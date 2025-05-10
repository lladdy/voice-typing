# Voice Typer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A lightweight, open-source voice typing application that converts speech to text using local inference with Whisper models. Record and transcribe audio with a simple keyboard shortcut for seamless integration with any application.

## Features

- **Keyboard-Driven**: Toggle recording with a configurable hotkey (default: `Cmd+Alt`)
- **Local Inference**: Uses [whisper.cpp](https://github.com/ggerganov/whisper.cpp) via the PyWhisperCPP wrapper for offline, private speech recognition
- **Universal Compatibility**: Works with any application that accepts pasted text
- **Simple Interface**: No GUI required - just press the hotkey, speak, and release to insert text
- **Customizable**: Configure your preferred language model and hotkey

## Installation

### Prerequisites

- Python 3.8 or higher
- A working microphone
- Linux, macOS, or Windows

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/lladdy/voice-typing.git
   cd voice-typing
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python run.py
   ```

2. Press and hold your configured hotkey (default: `Cmd+Alt`) to start recording.
3. Speak clearly into your microphone.
4. Release the hotkey to stop recording and transcribe.
5. The text will be automatically pasted at your cursor position.

## Configuration

You can customize the application by modifying the `VoiceTyperConfig` in `run.py`:

```python
config = VoiceTyperConfig(
    recording_hotkey="<cmd>+<alt>",  # Change to your preferred hotkey
    model_name="base.en"             # Change to use different Whisper models
)
```

Available model options:
- `tiny.en`: Fastest but less accurate (English only)
- `base.en`: Good balance of speed and accuracy (English only)
- `small.en`: More accurate but slower (English only)
- `medium.en`: Most accurate but requires more resources (English only)
- `tiny`, `base`, `small`, `medium`: Multilingual versions

## Project Structure

- `run.py`: Entry point for the application
- `voice_typer.py`: Core application logic
- `audio.py`: Audio recording and processing
- `speech_to_text.py`: Speech recognition using Whisper.cpp
- `keyboard.py`: Keyboard interaction and hotkey handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Whisper](https://github.com/openai/whisper) by OpenAI
- [whisper.cpp](https://github.com/ggerganov/whisper.cpp) for efficient local inference
- [PyWhisperCPP](https://github.com/aarnphm/pywhispercpp) for Python bindings to whisper.cpp