import whisper

model = whisper.load_model("base")
result = model.transcribe("C:\Users\LENOVO\Documents\GPT-3\test.mp3")
print(result["text"])