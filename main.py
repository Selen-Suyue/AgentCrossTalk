import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END, Frame, BOTH
from tkinter import ttk
from tkinter.font import Font
from crosstalk import perform_crosstalk
import time

def append_message(speaker, message, tag=""):
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(END, speaker + ": " + message + "\n", tag)
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(END)
    root.update()  
    time.sleep(0.2)  

def start_crosstalk():
    topic = user_entry.get()
    if topic:
        user_entry.delete(0, END)
        perform_crosstalk(topic, append_message) 



root = tk.Tk()
root.title("Agent_Crosstalk")

modern_font = Font(family="Helvetica Neue", size=12)  
bg_color = "#f8f8f8"  
chat_bg_color = "white"
button_color = "#4CAF50"  
button_hover_color = "#45a049" 
text_color = "#333333"  
entry_border_color = "#cccccc" 

# --- ttk Style ---
style = ttk.Style()
style.theme_use("clam")
style.configure(".", font=modern_font, background=bg_color, foreground=text_color)
style.configure("TButton", padding=8, foreground="white", background=button_color, borderwidth=0, borderradius=8)
style.map("TButton",
    background=[('active', button_hover_color), ('disabled', '#9E9E9E')]
)

style.configure("TEntry", padding=8, fieldbackground="white", borderwidth=1, relief="solid", bordercolor=entry_border_color, borderradius=8)

style.configure("TFrame", background=bg_color)
style.configure("Chat.TFrame", background=chat_bg_color, borderwidth=1, relief="solid", bordercolor=entry_border_color, borderradius=10)

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

start_button = ttk.Button(input_frame, text="Start Show", command=start_crosstalk)  
start_button.pack(side=tk.RIGHT)

root.mainloop()
