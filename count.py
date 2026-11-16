#!/usr/bin/python3
import sqlite3
import sys
import time

db = sqlite3.connect('/var/lib/botd-stats/counts.db', timeout=30)
db.execute('CREATE TABLE IF NOT EXISTS visits(day TEXT PRIMARY KEY, total INTEGER)')
for line in sys.stdin:
    try:
        epoch = int(line.strip())
        day = time.strftime('%Y-%m-%d', time.gmtime(epoch))
    except (ValueError, OverflowError):
        continue
    with db:
        db.execute('INSERT INTO visits VALUES (?,1) ON CONFLICT(day) DO UPDATE SET total=total+1', (day,))
