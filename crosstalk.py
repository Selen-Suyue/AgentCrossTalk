from config import dougen_model, penggen_model

def perform_crosstalk(topic, append_message, max_length=50):
    """Perform the crosstalk based on the topic."""
    append_message("系统", f"好的，我们现在来根据主题“{topic}”来创作一个相声。", "system")

    # 阶段1：讨论阶段
    append_message("系统", "--- 讨论阶段开始 ---\n", "system")
    discussion_context = ""
    for i in range(5):
        dou_prompt = generate_dou_prompt(topic, i, peng_text if i > 0 else None, max_length)
        dou_text = generate_response(dougen_model, dou_prompt)
        append_message("逗哏", dou_text, "dougen")
        discussion_context += f"逗哏：{dou_text}\n"

        peng_prompt = generate_peng_prompt(topic, dou_text, i, max_length)
        peng_text = generate_response(penggen_model, peng_prompt)
        append_message("捧哏", peng_text, "penggen")
        discussion_context += f"捧哏：{peng_text}\n"

    append_message("系统", "--- 讨论阶段结束 ---\n", "system")
    append_message("逗哏", "准备好开始表演了！\n", "dougen")
    append_message("捧哏", "准备好开始表演了！\n", "penggen")
    append_message("系统", "--- 表演阶段开始 ---\n", "system")

    # 阶段2：表演阶段
    for i in range(15):
        dou_prompt = generate_dou_prompt(topic, i, peng_text if i > 0 else None, max_length * 8, discussion_context)
        dou_text = generate_response(dougen_model, dou_prompt)
        append_message("逗哏", dou_text, "dougen")

        peng_prompt = generate_peng_prompt(topic, dou_text, i, max_length * 2, discussion_context)
        peng_text = generate_response(penggen_model, peng_prompt)
        append_message("捧哏", peng_text, "penggen")

    append_message("系统", "--- 表演阶段结束 ---\n", "system")


def generate_dou_prompt(topic, i, previous_peng_text=None, max_length=50, discussion_context=None):
    prefix = f"你是一个相声演员中的逗哏，现在{'正在和捧哏一起表演' if discussion_context else '要和捧哏一起创作'}关于主题“{topic}”的相声，"
    if previous_peng_text:
        prefix += f"你的捧哏搭档说了{previous_peng_text}，"
    prefix += f"这是第{i + 1}句{'台词' if discussion_context else '轮讨论'}，"
    if discussion_context:
        prefix += f"请根据前面讨论的内容，"
    prefix += f"你想说什么？请用不超过{max_length}个字表达。"
    if discussion_context:
        prefix += f"\n讨论内容回顾：\n{discussion_context}"
    return prefix


def generate_peng_prompt(topic, previous_dou_text, i, max_length=50, discussion_context=None):
    prefix = f"你是一个相声演员中的捧哏，你的逗哏搭档说了“{previous_dou_text}”，"
    if discussion_context:
      prefix += f"请根据前面讨论的内容和逗哏的台词，"
    prefix += f"这是第{i+1}句{'台词' if discussion_context else '轮讨论'}，你想回应什么？请用不超过{max_length}个字表达。"

    if discussion_context:
        prefix += f"\n讨论内容回顾：\n{discussion_context}"

    return prefix

def generate_response(model, prompt):
    response = model.generate_content(prompt)
    return response.text if response and hasattr(response, 'text') else ""