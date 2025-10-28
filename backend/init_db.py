import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS eventi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    descrizione TEXT,
    data TEXT NOT NULL,
    ora TEXT
)
""")

# Eventi di prova
eventi_demo = [
    ("Cena di Club", "Incontro mensile con tutti i soci del Rotaract Trento.", "2025-10-12", "20:00"),
    ("Giornata Ambientale", "Attività di volontariato per la pulizia del Parco delle Albere.", "2025-10-23", "09:30"),
    ("Assemblea Distrettuale", "Evento del Distretto Rotaract con aggiornamenti e workshop.", "2025-11-02", "10:00")
]

c.executemany("INSERT INTO eventi (titolo, descrizione, data, ora) VALUES (?, ?, ?, ?)", eventi_demo)

conn.commit()
conn.close()
print("✅ Database inizializzato con eventi di prova.")
