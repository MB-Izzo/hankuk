from google import genai
import sys
from spinner import Spinner
from prompts import get_korean_to_french_prompt
from translation import Translation
from display import display_data

def korean_to_french(word: str) -> Translation:
    prompt = get_korean_to_french_prompt(word)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt,
        config ={
            "response_mime_type": "application/json",
            "response_json_schema": Translation.model_json_schema(),
        },
    )
    assert response.text is not None
    return Translation.model_validate_json(response.text)

if __name__ == "__main__":
    client = genai.Client()
    if len(sys.argv) < 2:
        print("Usage: python main.py <korean_word>")
        sys.exit(1)

    word = sys.argv[1]

    spinner = Spinner("Fetching AI response")
    spinner.start()
    try:
        translation = korean_to_french(word)
    finally:
        spinner.stop()

    display_data(translation)
