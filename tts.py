import argparse
from gtts import gTTS
from pydub import AudioSegment
import os
from playsound import playsound

class TextToSpeech:
    def __init__(self, language='en', voice='male', rate=1.0, pitch=1.0):
        self.language = language
        self.voice = voice
        self.rate = rate
        self.pitch = pitch
        self.audio_file = "output.mp3"

    def speak(self, text):
        """
        Convert the text to speech and play it.
        """
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save(self.audio_file)
        self._play_audio()

    def save(self, filename):
        """
        Save the generated speech as an audio file.
        """
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save(filename)
        print(f"Audio saved as {filename}")

    def _play_audio(self):
        """
        Play the generated audio file.
        """
        print(f"Playing audio: {self.audio_file}")
        playsound(self.audio_file)

def main():
    parser = argparse.ArgumentParser(description="Text-to-Speech Conversion")
    parser.add_argument("text", help="Text to convert into speech")
    parser.add_argument("--language", default="en", help="Language for speech (default: 'en')")
    parser.add_argument("--voice", choices=["male", "female"], default="male", help="Voice type (default: 'male')")
    parser.add_argument("--rate", type=float, default=1.0, help="Speech rate (default: 1.0)")
    parser.add_argument("--pitch", type=float, default=1.0, help="Speech pitch (default: 1.0)")
    parser.add_argument("--save", action="store_true", help="Save the audio to a file instead of playing it")

    args = parser.parse_args()

    # Create a Text-to-Speech instance
    tts = TextToSpeech(language=args.language, voice=args.voice, rate=args.rate, pitch=args.pitch)
    
    # Convert text to speech
    if args.save:
        filename = "output.mp3"
        tts.save(filename)
    else:
        tts.speak(args.text)

if __name__ == "__main__":
    main()
