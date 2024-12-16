import tkinter as tk
from tkinter import scrolledtext, END
from tkinter import ttk
from tkinter.font import Font
from crosstalk import perform_crosstalk
import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Speech rate (words per minute)
engine.setProperty('rate', 237)

# Volume (0.0 to 1.0)
engine.setProperty('volume', 1)


##########新增
from tkinter import filedialog, messagebox
from crosstalk import extract_topic_from_image, perform_crosstalk

def upload_image():
    # 弹出文件选择窗口，允许选择图片文件
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        try:
            # 提取图像主题
            topic = extract_topic_from_image(file_path)
            if topic:
                user_entry.delete(0, tk.END)
                user_entry.insert(0, topic)  # 将识别到的主题填入输入框
                messagebox.showinfo("主题提取成功", f"从图片中提取的主题: {topic}")
            else:
                messagebox.showwarning("未提取到主题", "无法从图片中提取主题，请重试。")
        except Exception as e:
            messagebox.showerror("图片处理失败", f"图片处理时出错: {e}")


'''
################新增2：语音
import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from crosstalk import perform_crosstalk

def upload_audio():
    # 弹出文件选择对话框，允许用户选择音频文件
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        try:
            # 调用函数提取语音中的文本
            topic = extract_topic_from_audio(file_path)
            if topic:
                user_entry.delete(0, tk.END)
                user_entry.insert(0, topic)  # 将提取的文本填入输入框
                messagebox.showinfo("主题提取成功", f"从语音中提取的主题: {topic}")
            else:
                messagebox.showwarning("未提取到主题", "无法从语音中提取主题，请重试。")
        except Exception as e:
            messagebox.showerror("语音处理失败", f"语音处理时出错: {e}")
'''




def append_message(speaker, message, tag=""):
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(END, speaker + ": " + message + "\n", tag)
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(END)
    root.update()
    time.sleep(0.2)
    # Convert text to speech, excluding system messages
    if speaker != "系统":
        text_to_speech(message)

def start_crosstalk():
    topic = user_entry.get()
    if topic:
        user_entry.delete(0, END)
        perform_crosstalk(topic, append_message)

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.title("Agent_Crosstalk")
root.geometry("800x600")  # Added a fixed window size

modern_font = Font(family="Helvetica Neue", size=12)
bg_color = "#f8f8f8"
chat_bg_color = "#ffffff"
button_color = "#4CAF50"
button_hover_color = "#45a049"
text_color = "#333333"
entry_border_color = "#cccccc"

# --- ttk Style ---
style = ttk.Style()
style.theme_use("clam")
style.configure(".", font=modern_font, background=bg_color, foreground=text_color)
style.configure("TButton", padding=8, foreground="white", background=button_color, borderwidth=0, bordercolor=button_color)
style.map("TButton", background=[('active', button_hover_color), ('disabled', '#9E9E9E')])
style.configure("TEntry", padding=8, fieldbackground="white", borderwidth=1, relief="solid", highlightcolor=entry_border_color, highlightbackground=entry_border_color)
style.configure("TFrame", background=bg_color)
style.configure("Chat.TFrame", background=chat_bg_color, borderwidth=1, relief="solid", highlightbackground=entry_border_color)

main_frame = ttk.Frame(root, style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

chat_frame = ttk.Frame(main_frame, style="Chat.TFrame")
chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(20, 10))
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=70, height=25,
                                      state=tk.DISABLED, font=modern_font, bg=chat_bg_color,
                                      fg=text_color, insertbackground=text_color,
                                      highlightthickness=0, padx=10, pady=10)
chat_area.pack(fill=tk.BOTH, expand=True)
chat_area.tag_configure("system", foreground="gray", font=modern_font)
chat_area.tag_configure("dougen", foreground="darkblue", font=modern_font)
chat_area.tag_configure("penggen", foreground="darkgreen", font=modern_font)
chat_area.tag_configure("error", foreground="red", font=modern_font)

input_frame = ttk.Frame(main_frame, style="TFrame")
input_frame.pack(fill=tk.X, padx=20, pady=(10, 20))

user_entry = ttk.Entry(input_frame)
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# 新增上传图片按钮
upload_button = ttk.Button(input_frame, text="上传图片", command=upload_image)
upload_button.pack(side=tk.RIGHT, padx=(0, 10))
#新增上传语音按钮
#audio_button = ttk.Button(input_frame, text="上传语音", command=upload_audio)
#audio_button.pack(side=tk.RIGHT, padx=(0, 10))  # 添加到界面右侧

start_button = ttk.Button(input_frame, text="Start Show", command=start_crosstalk)
start_button.pack(side=tk.RIGHT)

root.mainloop()
