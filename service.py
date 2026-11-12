class TicketService:
    """Règles métier : validation et transitions de statut."""

    def __init__(self, depot):
        self.depot = depot

    def creer(self, titre):
        titre = titre.strip()
        if not 3 <= len(titre) <= 120:
            raise ValueError("Titre : 3 a 120 caracteres")
        return self.depot.creer(titre)

    def lister(self):
        return self.depot.lister()

    def avancer(self, identifiant):
        ticket = self.depot.obtenir(identifiant)
        if ticket is None:
            raise LookupError("Ticket introuvable")
        transitions = {"OUVERT": "EN_COURS",
                       "EN_COURS": "CLOS"}
        statut = transitions.get(ticket[2])
        if statut is None:
            raise ValueError("Ticket deja clos")
        self.depot.changer_statut(identifiant, statut)
        return statut
