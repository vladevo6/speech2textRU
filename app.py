from huggingsound import SpeechRecognitionModel
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="jonatasgrosman/wav2vec2-large-xlsr-53-russian")

audio_paths = ["/path/to/file.mp3"]

transcriptions = pipe(audio_paths)
print(transcriptions)
