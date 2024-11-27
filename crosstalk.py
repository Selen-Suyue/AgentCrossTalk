from config import dougen_model, penggen_model
import time

def perform_crosstalk(topic, append_message, max_length=50):
    """Perform the crosstalk based on the topic with limited sentence length and context adherence."""
    append_message("系统", f"好的，我们现在来根据主题“{topic}”来创作一个相声。", "system")

    # 阶段1：讨论阶段
    append_message("系统", "--- 讨论阶段开始 ---\n", "system")
    discussion_context = ""
    for i in range(3):
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
    append_message("逗哏", "准备好开始表演了！", "dougen")
    append_message("捧哏", "准备好开始表演了！", "penggen")
    append_message("系统", "--- 表演阶段开始 ---\n", "system")

    # 阶段2：表演阶段
    for i in range(7):
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
