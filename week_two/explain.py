import os
import sys
import textwrap
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def main():
    user_input = " ".join(sys.argv[1:])

    if user_input == "":
        return print("Please enter some commands!")
    
    try:
        response = get_response(user_input)
    except Exception:
        return print("The was an issue with the Gemini API, please try again later")

    print(response)

def get_response(prompt: str) -> str:
    SYSTEM_PROMPT = """\
        Explain the purpose of a provided command or command sequence in one clear, concise sentence.
        Respond only to command explanations—ignore all other inputs. 
        Use the format: 'This command[s]...' and avoid technical jargon unless necessary.
        Example prompt: 'grep -ri 'error' /var/log'
        Example response: 'This command recursively searches for the term 'error' within all files in the /var/log directory, ignoring case sensitivity.'""" 

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=textwrap.dedent(SYSTEM_PROMPT)),
        contents=[prompt])

    if response.text is None:
        raise Exception

    return response.text.strip()

if __name__ == "__main__":
    main()
