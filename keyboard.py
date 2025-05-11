import logging
import pyperclip
from pynput import keyboard
from pynput.keyboard import Controller, Key

logger = logging.getLogger(__name__)

class Keyboard:
    """
    Handles keyboard interactions such as hotkey detection and simulated key presses.
    """
    def __init__(self, hotkey, hotkey_callback):
        self.hotkey = hotkey
        self.hotkey_callback = hotkey_callback
        self.keyboard_controller = Controller()
        self.hotkey_listener = None
        
    def simulate_paste_action(self):
        """Simulates a Ctrl+V paste operation."""
        self.keyboard_controller.press(Key.ctrl)
        self.keyboard_controller.press('v')
        self.keyboard_controller.release('v')
        self.keyboard_controller.release(Key.ctrl)
        logger.info("Control + v pressed.")
    
    def copy_to_clipboard(self, text):
        """Copies text to clipboard."""
        pyperclip.copy(text)
    
    def _wrapped_hotkey_callback(self):
        """Wrapper around the hotkey callback with logging."""
        logger.info(f"Hotkey {self.hotkey} pressed")
        self.hotkey_callback()
    
    def start_listener(self):
        """Start listening for the configured hotkey."""
        try:
            self.hotkey_listener = keyboard.GlobalHotKeys({self.hotkey: self._wrapped_hotkey_callback})
            self.hotkey_listener.start()
            return self.hotkey_listener
        except Exception as error:
            logger.info(f"Error in the keyboard listener: {str(error)}")
            return None
    
    def stop_listener(self):
        """Stop the hotkey listener."""
        if self.hotkey_listener:
            self.hotkey_listener.stop()
