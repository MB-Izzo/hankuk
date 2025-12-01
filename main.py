# pyright: reportUnknownVariableType=false
# pyright: reportImplicitRelativeImport=false
from google import genai
import json
import sys
from colors import Colors
from spinner import Spinner
from prompts import get_korean_to_french_prompt

def korean_to_french(word: str) -> str:
    prompt = get_korean_to_french_prompt(word)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    text: str = response.candidates[0].content.parts[0].text # type: ignore[attr-defined]

    if text.startswith("```json") and text.endswith("```"):
        text = text[7:-3].strip()

    return text

def display_data(data: dict[str, object] | None) -> None:
    if data is None:
        print(f"{Colors.RED}❌ Pas de données à afficher.{Colors.END}")
        return

    print(f"{Colors.BOLD}{Colors.HEADER}{'━' * 60}{Colors.END}")
    print(f"{Colors.BOLD}📖 Traduction :{Colors.END} {Colors.GREEN}{data.get('traduction', '')}{Colors.END}\n")

    print(f"{Colors.BOLD}📝 Explication :{Colors.END}\n{Colors.CYAN}{data.get('explication', '')}{Colors.END}\n")

    print(f"{Colors.BOLD}🔧 Formes grammaticales :{Colors.END}")
    print(f"  🟡 Forme passive : {Colors.YELLOW}{data.get('passive_form', '')}{Colors.END}")
    print(f"  🟢 Forme active  : {Colors.YELLOW}{data.get('active_form', '')}{Colors.END}")
    print(f"  ⚙  Grammaire  : {Colors.YELLOW}{data.get('grammar_use', '')}{Colors.END}\n")

    exemple = data.get("exemple", {})
    print(f"{Colors.BOLD}💡 Exemple :{Colors.END}")
    print(f"Korean : {Colors.BLUE}{exemple.get('korean', '')}{Colors.END}")
    print(f"French : {Colors.BLUE}{exemple.get('french', '')}{Colors.END}")

    print(f"{Colors.BOLD}{Colors.HEADER}{'━' * 60}{Colors.END}")
    print("\n")  # un petit espace après chaque mot

if __name__ == "__main__":
    client = genai.Client()

    if len(sys.argv) < 2:
        print("Usage: python main.py <korean_word>")
        sys.exit(1)

    word = sys.argv[1]
    spinner = Spinner("Fetching AI response")
    spinner.start()

    try:
        res_text = korean_to_french(word)
    finally:
        spinner.stop()

    try:
        res_data = json.loads(res_text)
    except json.JSONDecodeError:
        print("❌ Le modèle n'a pas renvoyé un JSON valide :")
        print(res_text)
        res_data = None

    display_data(res_data)
