import sqlite3

CONN = sqlite3.connect('gym.db')
CURSOR = CONN.cursor()