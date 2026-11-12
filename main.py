from repository import TicketRepository
from service import TicketService


def main():
    service = TicketService(TicketRepository())
    while True:
        print("\n1. Creer 2. Lister 3. Avancer 0. Quitter")
        choix = input("Choix : ").strip()
        try:
            if choix == "1":
                identifiant = service.creer(input("Titre : "))
                print("Ticket cree :", identifiant)
            elif choix == "2":
                for ticket in service.lister():
                    print(ticket)
            elif choix == "3":
                numero = int(input("ID : "))
                print("Nouveau statut :", service.avancer(numero))
            elif choix == "0":
                break
            else:
                print("Choix inconnu")
        except (ValueError, LookupError) as erreur:
            print("Erreur :", erreur)


if __name__ == "__main__":
    main()
