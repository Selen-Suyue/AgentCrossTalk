import speech_recognition as sr
from pydub import AudioSegment
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def extract_topic_from_image(image_path: str) -> str:
    """Extracts the topic from an image."""
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        image = Image.open(image_path)
        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs)
        description = processor.decode(out[0], skip_special_tokens=True)
        return description.strip()
    except Exception as e:
        return f"Error processing image: {str(e)}"


def extract_topic_from_audio(audio_path: str) -> str:
    """Extracts the topic from an audio file."""
    recognizer = sr.Recognizer()
    try:
        if not audio_path.endswith(".wav"):
            audio = AudioSegment.from_file(audio_path)
            audio_path = audio_path.replace(audio_path.split('.')[-1], 'wav')
            audio.export(audio_path, format="wav")

        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="zh-CN")
        return text
    except Exception as e:
        return f"Error processing audio: {str(e)}"