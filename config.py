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

dougen_model = genai.GenerativeModel('gemini-1.5-flash')
penggen_model = genai.GenerativeModel('gemini-1.5-flash')
