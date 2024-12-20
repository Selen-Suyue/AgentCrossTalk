import tkinter as tk
import time
import pyttsx3
from tkinter import scrolledtext, END, ttk, filedialog, messagebox, font
from crosstalk import perform_crosstalk
from crosstalk_utils import extract_topic_from_image, extract_topic_from_audio
from ui_elements import create_main_window, create_chat_area, create_input_frame
from tts_speech import text_to_speech
from Vtuber_speech import Lian, XingTong
# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 237)  # Speed
engine.setProperty('volume', 1)   # Volume


def append_message(speaker, message, tag=""):
    """Appends a message to the chat area and triggers text-to-speech.

      Args:
          speaker: The name of the speaker (e.g., "逗哏", "捧哏", "系统").
          message: The message to append.
          tag: An optional tag for styling the message in the chat area.
      """
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(END, speaker + ": " + message + "\n", tag)
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(END)
    root.update()
    time.sleep(0.2)
    if special_voice_var.get() == True:
        if speaker == "逗哏":
            Lian(message)
        elif speaker == "捧哏":
            XingTong(message)
    else:
        if speaker != "系统":  # Don't speak system messages
            text_to_speech(message)


def start_crosstalk():
    """Starts the crosstalk performance."""
    topic = user_entry.get()
    if topic:
        user_entry.delete(0, END)
        perform_crosstalk(topic, append_message)


def upload_image():
    """Handles image upload and topic extraction."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        try:
            topic = extract_topic_from_image(file_path)
            if topic:
                user_entry.delete(0, tk.END)
                user_entry.insert(0, topic)
                messagebox.showinfo("主题提取成功", f"从图片中提取的主题: {topic}")
            else:
                messagebox.showwarning("未提取到主题", "无法从图片中提取主题，请重试。")
        except Exception as e:
            messagebox.showerror("图片处理失败", f"图片处理时出错: {e}")


# --- Main application setup ---
if __name__ == "__main__":
    root = create_main_window()
    main_frame, chat_frame, chat_area = create_chat_area(root)
    input_frame, user_entry, upload_button, start_button, special_voice_var = create_input_frame(main_frame, upload_image, start_crosstalk)  # Pass functions

    root.mainloop()

