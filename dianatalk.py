from gradio_client import Client
from playsound import playsound
import os
import google.generativeai as genai

#   This file is for the future diverse audio extension for AgentCrosstalk 

# Configure the generative AI model using the API key from a file
try:
    with open("api_key.txt", "r") as f:
        genai.configure(api_key=f.readline().strip())
except FileNotFoundError:
    print("Error: File 'api_key.txt' not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the API key: {e}")
    exit()

# Initialize the AI model and client for interaction
Diana_model = genai.GenerativeModel('gemini-1.5-pro')
client = Client("https://xzjosh-diana-bert-vits2.hf.space/--replicas/2lwqc/")
context = []  

# Define terminal text colors
USER_COLOR = "\033[94m"
DIANA_COLOR = "\033[95m"  
RESET_COLOR = "\033[0m"

# Main interaction loop
while True:
    try:
        # Get user input
        user_input = input("You want to tell Diana that: ")
        if user_input.lower() in ["exit", "quit"]:
            print("对话结束，再见！")
            break

        # Append user input to context
        context.append(f"用户：{user_input}")
        formatted_context = "\n".join(context)

        # Create a prompt for the generative model
        prompt = ("")  # Define your prompt here
        
        # Generate response from AI model
        response = Diana_model.generate_content(prompt).text.strip()
        
        # Get audio prediction from the client
        result = client.predict(response, "Diana", 0.2, 0.5, 0.9, 1, fn_index=0)
        audio_path = result[1]

        # Play audio if the path is valid
        if isinstance(audio_path, str):
            print("Playing audio...")
            audio_path = os.path.normpath(audio_path)
            playsound(audio_path)
        else:
            print("Unexpected result format:", result)
    except Exception as e:
        print(f"An error occurred: {e}")
