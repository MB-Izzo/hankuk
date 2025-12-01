# Korean to French dictionary

Translate Korean to French using Google's Gemini AI.

## Usage

```bash
python main.py <korean_word>
```

Output:
```
📝 Explication :
Désigne l'action de réunir plusieurs éléments distincts ou divers pour en faire un tout cohérent, ou de les inclure dans un ensemble plus vaste. Implique souvent une notion d'intégration ou de synthèse.

🔧 Formes grammaticales :
  🟡 Forme passive : Aucune
  🟢 Forme active  : 아우르다
  ⚙  Grammaire  : 1이 2를 아우르다 (1 rassemble/englobe 2)

💡 Exemple :
Korean : 그의 연설은 다양한 관점을 아우르는 내용으로 청중의 공감을 얻었다.
French : Son discours, qui englobait diverses perspectives, a gagné l'empathie du public.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Requirements

- Python 3.10+
- Google GenAI library

## Notes

This is mostly a personal script. In korean, causative/passive form is often a difficult point for me so this small script helps with that.

Sometimes, it invents passive forms though: if I input 아우르다, it often says 아울리다 is the passive form but this form does not exist.
