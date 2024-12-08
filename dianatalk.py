from gradio_client import Client
from playsound import playsound
import os
import google.generativeai as genai

try:
    with open("api_key.txt", "r") as f:
        genai.configure(api_key=f.readline().strip())
except FileNotFoundError:
    print("Error: File 'api_key.txt' not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the API key: {e}")
    exit()

Diana_model = genai.GenerativeModel('gemini-1.5-pro')
client = Client("https://xzjosh-diana-bert-vits2.hf.space/--replicas/2lwqc/")
context = []  


USER_COLOR = "\033[94m"
DIANA_COLOR = "\033[95m"  
RESET_COLOR = "\033[0m" 

while True:
    try:
        user_input = input("You want to tell Diana that: ")
        if user_input.lower() in ["exit", "quit"]:
            print("对话结束，再见！")
            break

        context.append(f"用户：{user_input}")
        formatted_context = "\n".join(context)

        prompt = (
            f"现在你是虚拟偶像嘉然，请扮演她和我对话。你每次只能用中文（不可以用英文字母和单词）回答不超过3到4句话。\n"
            f"以下是我们当前的对话：\n{formatted_context}\n"
            f"现在我说：{user_input}"
        )
        
        response = Diana_model.generate_content(prompt).text.strip()
        context.append(f"嘉然：{response}")
        
        print(f"{USER_COLOR}用户：{user_input}{RESET_COLOR}")
        print(f"{DIANA_COLOR}嘉然：{response}{RESET_COLOR}")
        
        result = client.predict(response, "Diana", 0.2, 0.5, 0.9, 1, fn_index=0)
        audio_path = result[1]

        if isinstance(audio_path, str):
            print("Playing audio...")
            audio_path = os.path.normpath(audio_path)
            playsound(audio_path)
        else:
            print("Unexpected result format:", result)
    except Exception as e:
        print(f"An error occurred: {e}")
