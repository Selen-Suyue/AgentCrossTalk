import tkinter as tk
from tkinter import scrolledtext, ttk, font


def create_main_window():
    """Creates the main window."""
    root = tk.Tk()
    root.title("Agent_Crosstalk")
    root.geometry("800x600")
    return root


def create_chat_area(root):
    """Creates the chat area."""
    modern_font = font.Font(family="Helvetica Neue", size=12)
    style = configure_style(modern_font)
    main_frame = ttk.Frame(root, style="TFrame")
    main_frame.pack(fill=tk.BOTH, expand=True)

    chat_frame = ttk.Frame(main_frame, style="Chat.TFrame")
    chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(20, 10))

    chat_area = scrolledtext.ScrolledText(
        chat_frame, wrap=tk.WORD, width=70, height=25, state=tk.DISABLED,
        font=modern_font, bg="#ffffff", fg="#333333", insertbackground="#333333",
        highlightthickness=0, padx=10, pady=10
    )
    chat_area.pack(fill=tk.BOTH, expand=True)
    configure_tags(chat_area, modern_font)  # Configure tags after creating chat_area
    return main_frame, chat_frame, chat_area


def configure_style(modern_font):
    bg_color = "#f8f8f8"
    chat_bg_color = "#ffffff"
    button_color = "#4CAF50"
    button_hover_color = "#45a049"
    text_color = "#333333"
    entry_border_color = "#cccccc"

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(".", font=modern_font, background=bg_color, foreground=text_color)
    style.configure("TButton", padding=8, foreground="white", background=button_color, borderwidth=0, bordercolor=button_color)
    style.map("TButton", background=[('active', button_hover_color), ('disabled', '#9E9E9E')])
    style.configure("TEntry", padding=8, fieldbackground="white", borderwidth=1, relief="solid", highlightcolor=entry_border_color, highlightbackground=entry_border_color)
    style.configure("TFrame", background=bg_color)
    style.configure("Chat.TFrame", background=chat_bg_color, borderwidth=1, relief="solid", highlightbackground=entry_border_color)

    return style  # Return the style


def configure_tags(chat_area, modern_font):
    """Configures tags for chat area text styling."""
    chat_area.tag_configure("system", foreground="gray", font=modern_font)
    chat_area.tag_configure("dougen", foreground="darkblue", font=modern_font)
    chat_area.tag_configure("penggen", foreground="darkgreen", font=modern_font)
    chat_area.tag_configure("error", foreground="red", font=modern_font)

def create_input_frame(main_frame, upload_image_command, start_crosstalk_command): # Add parameters for commands
    """Creates the input frame with entry, buttons, and checkbutton."""
    input_frame = ttk.Frame(main_frame, style="TFrame")
    input_frame.pack(fill=tk.X, padx=20, pady=(10, 20))

    user_entry = ttk.Entry(input_frame)
    user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

    upload_button = ttk.Button(input_frame, text="上传图片", command=upload_image_command)
    upload_button.pack(side=tk.RIGHT, padx=(0, 10))


    start_button = ttk.Button(input_frame, text="Start Show", command=start_crosstalk_command)
    start_button.pack(side=tk.RIGHT)

    special_voice_var = tk.BooleanVar()
    special_voice_label = ttk.Label(input_frame, text="特殊语音")
    special_voice_label.pack(side=tk.LEFT, padx=(0, 10))
    special_voice_checkbutton = ttk.Checkbutton(input_frame, text="", variable=special_voice_var)
    special_voice_checkbutton.pack(side=tk.LEFT, padx=(0, 10))
    return input_frame, user_entry, upload_button, start_button, special_voice_var  # Return newly created widgets