# tp-tickets

Mini-gestionnaire de tickets d'assistance informatique (application en ligne de commande).
Projet de TP - Atelier de génie logiciel, Licence 3 SIL.

## Prérequis
- Python 3 et Git (aucune bibliothèque externe).
- Sur certains systèmes, utiliser `python3` au lieu de `python`.

## Architecture
| Fichier | Rôle |
|---|---|
| `main.py` | Présentation (menu console) |
| `service.py` | Règles métier (validation, transitions) |
| `repository.py` | Persistance SQLite (`tickets.db`, créé automatiquement) |
| `tests/test_service.py` | Tests automatiques |

## Lancement
```
python main.py
```
Menu : `1` créer, `2` lister, `3` avancer (OUVERT → EN_COURS → CLOS), `0` quitter.

## Règles métier
- EF-01 : titre de 3 à 120 caractères (espaces de bord ignorés).
- EF-02 : liste des tickets.
- EF-03 : OUVERT → EN_COURS → CLOS, sans saut d'étape.

## Tests
```
python -m unittest discover -s tests -v
```
Les tests utilisent SQLite en mémoire et ne touchent pas `tickets.db`.
