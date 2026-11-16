#!/usr/bin/python3
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
folder = Path('/var/www/botd-report')
db = sqlite3.connect('/var/lib/botd-stats/counts.db')
db.execute('CREATE TABLE IF NOT EXISTS visits(day TEXT PRIMARY KEY, total INTEGER)')
rows = db.execute('SELECT day,total FROM visits ORDER BY day DESC LIMIT 30')
body = ''.join(f'<tr><td>{day}</td><td>{total:,}</td></tr>' for day,total in rows)
page = folder / 'next.html'
page.write_text(f"""<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width, initial-scale=1"><title>Burger of the Day analytics</title><style>body{{font:18px system-ui;max-width:42rem;margin:8vh auto;padding:1rem;color:#29251e}}td,th{{text-align:left;padding:.6em 2em .6em 0}}</style><h1>Burger of the Day analytics</h1><p>Daily successful board page requests, including reloads and bots. Offline opens and in-page navigation are excluded.</p><table><tr><th>Date (UTC)</th><th>Page requests</th></tr>{body}</table><p>Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC · refreshes every minute</p>""")
page.chmod(0o644)
page.replace(folder / 'index.html')
