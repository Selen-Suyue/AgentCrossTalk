# Gemini Crosstalk Performance

This project uses the Google Gemini API to create a simple chatbot application simulating two crosstalk performers (Dougen and Penggen) performing based on user-provided topics.

## Project Details

This project consists of three Python files:

- **`main.py`:** The main program file responsible for creating the GUI and handling user interactions.
- **`crosstalk.py`:** Contains the logic for the crosstalk performance, including interactions with the Gemini API and generating dialogues for Dougen and Penggen.
- **`config.py`:** Contains API key and other configuration details.

## How to Run

1. **Install required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Obtain the Google Gemini API key:**

    You need to register a Google Cloud account, enable the Gemini API, and obtain an API key. Refer to the official Google Cloud documentation for details: [https://cloud.google.com/generative-ai/docs/setup](https://cloud.google.com/generative-ai/docs/setup)

3. **Configure the API key:**

    Copy your API key into the `api_key.txt` file's first line. **Do not commit the `api_key.txt` file to version control!**

4. **Run the application:**

    ```bash
    python main.py
    ```

    This will start a GUI window where you can input a topic and click the "Start Performance" button. The program will simulate two crosstalk performers discussing and performing based on your topic, displaying the conversation in the chat area.

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

