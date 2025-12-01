def get_korean_to_french_prompt(word: str) -> str:
    return f"""
    Extrait un objet de traduction grace a ce texte.
    Tu es un dictionnaire coréen→français.
    Pour le mot ou expression coréenne '{word}', réponds en JSON structuré :

    1) traduction française correcte
    2) explication courte du sens / contexte / nuance
    3) forme actives et passives/causatif (si le passif ou causatif n'existe pas, cherche bien et dis le)
    4) un exemple simple en coréen, et sa traduction en français
    5) l'utilisation grammaticale comme "1이 2에 3을..."
    """
