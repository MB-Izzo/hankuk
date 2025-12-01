from translation import Translation
from colors import Colors

def display_data(data: Translation) -> None:
    print(f"{Colors.BOLD}{Colors.HEADER}{'━' * 60}{Colors.END}")
    print(f"{Colors.BOLD}📖 Traduction :{Colors.END} {Colors.GREEN}{data.translation}{Colors.END}\n")

    print(f"{Colors.BOLD}📝 Explication :{Colors.END}\n{Colors.CYAN}{data.explaination}{Colors.END}\n")

    print(f"{Colors.BOLD}🔧 Formes grammaticales :{Colors.END}")
    print(f"  🟡 Forme passive : {Colors.YELLOW}{data.passive_form}{Colors.END}")
    print(f"  🟢 Forme active  : {Colors.YELLOW}{data.active_form}{Colors.END}")
    print(f"  ⚙  Grammaire  : {Colors.YELLOW}{data.grammar_use}{Colors.END}\n")

    print(f"{Colors.BOLD}💡 Exemple :{Colors.END}")
    print(f"Korean : {Colors.BLUE}{data.example.korean}{Colors.END}")
    print(f"French : {Colors.BLUE}{data.example.french}{Colors.END}")

    print(f"{Colors.BOLD}{Colors.HEADER}{'━' * 60}{Colors.END}")
    print("\n")  # un petit espace après chaque mot
