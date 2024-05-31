import tempfile
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
from pydub import AudioSegment
from pathlib import Path

class ModelOutput:
    def __init__(self, vocals, accompaniment):
        self.vocals = vocals
        self.accompaniment = accompaniment

class Predictor:
    def setup(self):
        self.separator = Separator('spleeter:2stems')
        self.audio_loader = AudioAdapter.default()  # Initialize audio_loader here

    def predict(
            self,
            audio
        ) -> ModelOutput:
        """Separate the vocals from the accompaniment of an audio file"""
        
        # Convert MP3 to WAV
        audio_wav = AudioSegment.from_mp3(str(audio))
        _, audio_wav_path = tempfile.mkstemp(suffix=".wav")
        audio_wav_path = Path(audio_wav_path)
        audio_wav.export(audio_wav_path, format="wav")
        
        waveform, sample_rate = self.audio_loader.load(str(audio_wav_path))
        prediction = self.separator.separate(waveform)

        out_path = Path(tempfile.mkdtemp())

        out_path_vocals = out_path / "vocals.wav"
        out_path_accompaniment = out_path / "accompaniment.wav"

        self.audio_loader.save(str(out_path_vocals), prediction['vocals'], sample_rate)
        self.audio_loader.save(str(out_path_accompaniment), prediction['accompaniment'], sample_rate)

        return ModelOutput(
            vocals=out_path_vocals,
            accompaniment=out_path_accompaniment
        )

if __name__ == "__main__":
    predictor = Predictor()

    predictor.setup()

    audio_mp3_path = r"C:\Users\kgyan\OneDrive\Documents\1Gen\spleeter-fork\audio_example.mp3"

    output = predictor.predict(audio=audio_mp3_path)
    print(output.vocals)

    separated_vocals_path = output.vocals
    separated_accompaniment_path = output.accompaniment
