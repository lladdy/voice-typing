import logging

from voice_typer import VoiceTyper, VoiceTyperConfig

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

if __name__ == "__main__":
    config = VoiceTyperConfig(recording_hotkey="<cmd>+<alt>",
                              model_name="base.en")
    voice_typing_app = VoiceTyper(config=config)
    voice_typing_app.run()
