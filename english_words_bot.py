import json, os, random, time
from pathlib import Path
import requests

N = 10
BASE = Path(__file__).parent
WORDS = BASE / 'oxford_words.json'
USED = BASE / 'used_words.json'

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat = os.getenv('TELEGRAM_CHAT_ID')
    if not token or not chat: 
        raise RuntimeError('Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID')

    while True:
        words = json.loads(WORDS.read_text(encoding='utf-8'))
        used = set(json.loads(USED.read_text(encoding='utf-8'))) if USED.exists() else set()
        available = [w for w in words if w['word'].lower() not in used]
        
        if len(available) < N: 
            raise RuntimeError('Not enough unused words.')
            
        selected = random.sample(available, N)
        
        lines = ['📚 OXFORD 3000 — 10 NEW WORDS', '']

        for i, w in enumerate(selected, 1):
            lines.append(f"{i}. {w['word']} ({w.get('pos','')})")

        r = requests.post(
            f'https://api.telegram.org/bot{token}/sendMessage',
            json={'chat_id': chat, 'text': '\n'.join(lines)},
            timeout=30
        )
        r.raise_for_status()
        
        used.update(w['word'].lower() for w in selected)
        USED.write_text(json.dumps(sorted(used), ensure_ascii=False, indent=2), encoding='utf-8')
        
        print('Sent 10 words. Next run in 24 hours.')
        time.sleep(86400)

if __name__ == '__main__': 
    main()
