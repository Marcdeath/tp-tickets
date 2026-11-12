import sqlite3


class TicketRepository:
    """Couche de persistance SQLite."""

    def __init__(self, chemin="tickets.db"):
        self.conn = sqlite3.connect(chemin)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS ticket (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            statut TEXT NOT NULL DEFAULT 'OUVERT'
        )""")
        self.conn.commit()

    def creer(self, titre):
        cur = self.conn.execute(
            "INSERT INTO ticket(titre) VALUES (?)", (titre,))
        self.conn.commit()
        return cur.lastrowid

    def lister(self):
        return self.conn.execute(
            "SELECT id, titre, statut FROM ticket ORDER BY id"
        ).fetchall()

    def obtenir(self, identifiant):
        return self.conn.execute(
            "SELECT id, titre, statut FROM ticket WHERE id=?",
            (identifiant,)).fetchone()

    def changer_statut(self, identifiant, statut):
        self.conn.execute(
            "UPDATE ticket SET statut=? WHERE id=?",
            (statut, identifiant))
        self.conn.commit()
