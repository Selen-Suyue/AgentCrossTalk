from gradio_client import Client
import pygame


def XingTong(text):
    client = Client("https://xzjosh-2568-bert-vits2.hf.space/--replicas/08576/")
    result = client.predict(
        text, "星瞳", 0.2, 0.5, 0.9, 1, "ZH", api_name="/tts_fn"
    )
    pygame.mixer.init()
    sound = pygame.mixer.Sound(result[1])
    duration = int(sound.get_length() * 1000)
    sound.play()
    pygame.time.wait(duration)


def Lian(text):
    client = Client("https://xzjosh-lian-bert-vits2-0-2.hf.space/--replicas/cc3pj/")
    result = client.predict(
        text, "东雪莲", 0.2, 0.5, 0.9, 1, "ZH", api_name="/tts_fn"
    )
    pygame.mixer.init()
    sound = pygame.mixer.Sound(result[1])
    duration = int(sound.get_length() * 1000)
    sound.play()
    pygame.time.wait(duration)
