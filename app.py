!pip install huggingsound
from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-russian")
audio_paths = ["/var/tmp/voice.mp3"]

transcriptions = model.transcribe(audio_paths)
print(transcriptions)
