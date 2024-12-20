# AgentCrossTalk
This project uses the Google Gemini to create a simple chatbot application simulating two crosstalk performers (Dougen and Penggen) performing based on user-provided topics with text,image (audio coming soon) input.

## Project Details

This project consists of three Python files:
- **`main.py`:** The main program file responsible for handling user interactions with multimodal input.
- **`crosstalk.py`:** Contains the logic for the crosstalk performance, including interactions with the Gemini and generating dialogues for Dougen and Penggen.
- **`config.py`:** Contains API key and other configuration details.
- **`crosstalk_utils.py:`** The ultis helps **Blip Model** extract topic from image as well as audio assistance.
- **`dianatalk.py:`** A sample for vtuber talk. You can try to interact with diana.
- **`tts_speech.py:`** For standard audio output.
- **`ui_elements.py`** For UI windows embark design.
- **`Vtuber_speech.py:`** Implement for vtuber audio. You can change with your preferd vtuber on huggingface through [link](https://huggingface.co/spaces/XzJosh/Diana-Bert-VITS2).

## How to Run

1. **Install required libraries:**

    ```bash
    conda create -n crosstalk python==3.11
    pip install -r requirements.txt 
    ```

2. **Obtain the Google Gemini API key:**

    You need to register a Google account, enable the Gemini API, and obtain an API key. Refer to the official Google AI documentation for details: [Google aistudio api docs](https://aistudio.google.com/apikey)


    Copy your API key into the `api_key.txt` file's first line. **Do not commit the `api_key.txt` file to version control!**

4. **Run the application:**

    ```bash
    conda activate crosstalk
    python main.py
    ```

    This will start a GUI window where you can input a topic and click the "Start Performance" button. The program will simulate two crosstalk performers discussing and performing based on your topic, displaying the conversation in the chat area. You can also add Image input or launch Vtuber voice via the GUI buttons.

## Example

Enter "Artificial Intelligence" in the input box and click the "Start Performance" button. You will see two crosstalk performers discussing and performing around the topic of artificial intelligence.

## Notes

- Ensure that you have Python 3.7 or later installed.
- The quality and coherence of the crosstalk performance may vary due to limitations of the Gemini API.
- This project is for demonstration and educational purposes only. Please adhere to the Google Cloud Platform's terms of service and usage limitations.

## File Structure

```plaintext
├── main.py         # Main program, handles GUI logic
├── crosstalk.py    # Logic for crosstalk performance
├── config.py       # Configuration (API Key and model initialization)
└── api_key.txt     # File containing the Gemini API key (handle securely)
└── ... (Core files are above)

