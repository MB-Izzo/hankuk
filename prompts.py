def get_korean_to_french_prompt(word: str) -> str:
    return f"""
    Réponds **uniquement en JSON**, sans préambule.
    Toutes les chaînes doivent être **échapées correctement** :
    - remplace les retours à la ligne par "\\n",
    - échappe toutes les guillemets internes avec \\
    Réponds **uniquement en JSON, sans texte supplémentaire.
    Ne MET PAS de format avec ```json pour le markdown!

    Tu es un dictionnaire coréen→français.
    Pour le mot ou expression coréenne '{word}', réponds en JSON structuré :

    1) traduction française correcte
    2) explication courte du sens / contexte / nuance
    3) forme actives et passives/causatif
    4) un exemple simple en coréen, et sa traduction en français
    5) l'utilisation grammaticale comme "1이 2에 3을..."

    {{
      "traduction": "...",
      "explication": "...",
      "passive_form": "...",
      "active_form": "...",
      "grammar_use": "...",
      "exemple": {{
         "korean": "...",
         "french": "..."
      }}
    }}
    """
