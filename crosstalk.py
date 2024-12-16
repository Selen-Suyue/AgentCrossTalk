from config import dougen_model, penggen_model



#####################新增1,图片
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
def extract_topic_from_image(image_path):
    """
    使用图像分类模型提取图像内容标签，作为相声对话的主题
    :param image_path: 图片文件路径
    :return: 提取的主题（如动物、物体等）
    """
    try:
        # 加载BLIP模型和处理器（可以换成其他模型）
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

        # 打开图片
        image = Image.open(image_path)

        # 处理图像并生成文本描述
        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs)
        description = processor.decode(out[0], skip_special_tokens=True)

        # 返回生成的主题（例如："a cat"）
        return description.strip()

    except Exception as e:
        return f"图片处理出错: {str(e)}"



#####################新增2：语音

import speech_recognition as sr
from pydub import AudioSegment


def extract_topic_from_audio(audio_path):
    """
    将上传的音频文件转化为文本，作为对话的主题
    :param audio_path: 音频文件路径
    :return: 转化后的文本内容
    """
    recognizer = sr.Recognizer()
    try:
        # 将非 WAV 格式的音频转换为 WAV 格式
        if not audio_path.endswith(".wav"):
            audio = AudioSegment.from_file(audio_path)
            audio_path = audio_path.replace(audio_path.split('.')[-1], 'wav')
            audio.export(audio_path, format="wav")

        # 读取音频文件
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        # 使用 Google 的语音识别 API 识别语音内容
        text = recognizer.recognize_google(audio_data, language="zh-CN")  # 中文识别
        return text
    except Exception as e:
        return f"语音处理出错: {str(e)}"






def perform_crosstalk(topic, append_message, max_length=50):
    """Perform the crosstalk based on the topic with limited sentence length and context adherence."""
    append_message("系统", f"好的，我们现在来根据主题“{topic}”来创作一个相声。", "system")

    # 阶段1：讨论阶段
    append_message("系统", "--- 讨论阶段开始 ---\n", "system")
    discussion_context = ""
    for i in range(5):
        if i == 0:
            prompt_dou = f"你是一个相声演员中的逗哏，现在要和捧哏一起根据主题“{topic}”创作相声，这是第{i+1}轮讨论，你想说什么？请用不超过{max_length}个字讨论。"
        else:
            prompt_dou = f"你是一个相声演员中的逗哏，现在要和捧哏一起根据主题“{topic}”创作相声，你的捧哏搭档说了{peng_text},这是第{i+1}轮讨论，你想说什么？请用不超过{max_length}个字讨论。"
        response_dou = dougen_model.generate_content(prompt_dou)
        if response_dou and hasattr(response_dou, 'text'):
            dou_text = response_dou.text
            append_message("逗哏", dou_text, "dougen")
            discussion_context += f"逗哏：{dou_text}\n"
            prompt_peng = f"你是一个相声演员中的捧哏，你的逗哏搭档针对主题“{topic}”说了“{dou_text}”，这是第{i+1}轮讨论，你想回应什么？请用不超过{max_length}个字讨论。"
            response_peng = penggen_model.generate_content(prompt_peng)
            if response_peng and hasattr(response_peng, 'text'):
                peng_text = response_peng.text
                append_message("捧哏", peng_text, "penggen")
                discussion_context += f"捧哏：{peng_text}\n"

    append_message("系统", "--- 讨论阶段结束 ---\n", "system")
    append_message("逗哏", "准备好开始表演了！\n", "dougen")
    append_message("捧哏", "准备好开始表演了！\n", "penggen")
    append_message("系统", "--- 表演阶段开始 ---\n", "system")

    # 阶段2：表演阶段
    for i in range(15):
        if i == 0:
            prompt_dou = f"你是一个相声演员中的逗哏，现在正在和捧哏一起表演关于主题“{topic}”的相声，这是第1句台词，请根据前面讨论的内容，你想说什么？请用不超过{max_length*8}个字表达。\n讨论内容回顾：\n{discussion_context}"
        else:
            prompt_dou = f"你是一个相声演员中的逗哏，现在正在和捧哏一起表演关于主题“{topic}”的相声，你的捧哏搭档说了{peng_text},这是第{i+1}句台词，请根据前面讨论的内容，你想说什么？请用不超过{max_length*8}个字表达。\n讨论内容回顾：\n{discussion_context}"
        response_dou = dougen_model.generate_content(prompt_dou)
        if response_dou and hasattr(response_dou, 'text'):
            dou_text = response_dou.text
            append_message("逗哏", dou_text, "dougen")
            prompt_peng = f"你是一个相声演员中的捧哏，你的逗哏搭档说了“{dou_text}”，请根据前面讨论的内容和逗哏的台词，这是第{i+1}句台词，你想回应什么？请用不超过{max_length*2}个字表达。\n讨论内容回顾：\n{discussion_context}"
            response_peng = penggen_model.generate_content(prompt_peng)
            if response_peng and hasattr(response_peng, 'text'):
                peng_text = response_peng.text
                append_message("捧哏", peng_text, "penggen")

    append_message("系统", "--- 表演阶段结束 ---\n", "system")